# This Python file uses the following encoding: utf-8
# import sys
# from PySide6.QtWidgets import QApplication, QWidget


# class mcvis(QWidget):
#     def __init__(self, parent=None):
#         super().__init__(parent)


# if __name__ == "__main__":
#     app = QApplication([])
#     window = mcvis()
#     window.show()
#     sys.exit(app.exec())
# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

"""PySide6 port of the qt3d/simple-cpp example from Qt v5.x"""
import os 
import sys
import csv
from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import (Property, QObject, QPropertyAnimation, Signal)
from PySide6.QtGui import (QIcon, QGuiApplication, QMatrix4x4, QQuaternion, QVector3D)
from PySide6.Qt3DCore import (Qt3DCore)
from PySide6.Qt3DExtras import (Qt3DExtras)
from mainwindow import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWidgets import QMessageBox, QLineEdit,QFileDialog, QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QDialog, QListWidget, QVBoxLayout, QListWidgetItem
import mcschematic
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import tifffile
# Mock function to load icons for demonstration
def resource_path(relative_path):
    """ Get absolute path to resource, works for PyInstaller and development """
    try:
        # When the program is packaged, PyInstaller uses a temporary folder (_MEIPASS)
        base_path = sys._MEIPASS
    except AttributeError:
        # If not packaged, use the current directory
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
class ListDialog(QDialog):
    def __init__(self, items, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Select The Block Type")
        self.setLayout(QVBoxLayout())
        # Search bar
        self.searchBar = QLineEdit(self)
        self.searchBar.setPlaceholderText("Search...")
        self.layout().addWidget(self.searchBar)
        # List widget
        self.listWidget = QListWidget()
        self.layout().addWidget(self.listWidget)
        self.items = items
        for item in items:
            self.listWidget.addItem(item)
        # Connect search bar signal to slot
        self.searchBar.textChanged.connect(self.filterList)  
        self.listWidget.itemDoubleClicked.connect(self.accept)
        
    def filterList(self, text):
        # Clear the list and repopulate based on the filter
        self.listWidget.clear()
        for item in self.items:
            if text.lower() in item.lower():
                QListWidgetItem(item, self.listWidget)
                
    def getSelectedItem(self):
        item = self.listWidget.currentItem()
        return item.text() if item else None

class MplCanvas(FigureCanvas):
    def __init__(self, width=5.51, height=5.81, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111, projection='3d')
        super().__init__(self.fig)
        
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Add this line to set the window icon
        self.setWindowIcon(QIcon(resource_path("icons/software_icon.png")))
        # qlabels for images
        # Add references to your new QLabels
        self.label1 = self.findChild(QtWidgets.QLabel, u"label_2")
        self.label2 = self.findChild(QtWidgets.QLabel, u"label_3")
        # retrive all the buttons from the ui
        self.add_button = self.findChild(QtWidgets.QPushButton, "add_button")
        self.delete_all_button = self.findChild(QtWidgets.QPushButton, "delete_all_button")
        self.delete_selected_button = self.findChild(QtWidgets.QPushButton, "delete_select_button")
        self.generate_button = self.findChild(QtWidgets.QPushButton, "generate_button")
        self.preview_button = self.findChild(QtWidgets.QPushButton, "preview_button")
        # connect the buttons to the functions
        self.add_button.clicked.connect(self.load_file)
        self.delete_all_button.clicked.connect(self.delete_all)
        self.delete_selected_button.clicked.connect(self.delete_selected)
        self.generate_button.clicked.connect(self.generate_scheme)
        self.preview_button.clicked.connect(self.preview)
        # retrieve the list widget from the ui
        self.table_display = self.findChild(QtWidgets.QTableWidget, "tableWidget")
        # connect to double click the table element
        self.table_display.cellDoubleClicked.connect(self.cellDoubleClicked)
        # Disable editing in the table widget
        self.table_display.setEditTriggers(QTableWidget.NoEditTriggers)
        # find the graphics view
        self.graphics_view = self.findChild(QtWidgets.QGraphicsView, "graphicsView")
        self.scene = QtWidgets.QGraphicsScene()
        self.graphics_view.setScene(self.scene)
        # auxillary parameters
        self.current_row = -1
        self.file_path = dict()
        self.file_blocktype = dict()
        self.default_block = "Gray Concrete"
        self.all_blocks = dict()
        self.get_item_list()
    def load_file(self):
        #Open the file dialog
        # file_paths, _ = QFileDialog.getOpenFileNames(self, "Select all the files need to import.", "./", "npy files (*.npy)")
        file_paths, _ = QFileDialog.getOpenFileNames(
            self,
                "Select all the files to import.",
                "./",
                "Supported files (*.npy *.tif *.tiff);;NPY files (*.npy);;TIFF files (*.tif *.tiff)"
            )
       
        if file_paths:
            #get the file name part from the full path
            for file_path in file_paths:
                
                file_name = os.path.basename(file_path)
                # check if the file is already added to the table
                if file_name not in self.file_path:
                    self.file_path[file_name] = file_path
                    self.file_blocktype[file_name] = self.all_blocks[self.default_block]
                    
                    # if not added:
                    self.table_display.insertRow(self.current_row+1)
                    self.current_row += 1
                    item = QtWidgets.QTableWidgetItem(file_name)
                    print(item.text())
                    self.table_display.setItem(self.current_row, 0, item)
                    # get the key for the default block
                    
                    self.table_display.setItem(self.current_row, 1, QTableWidgetItem(self.default_block))
       
    def delete_all(self):
        self.table_display.setRowCount(0)
        #empty the file path and block type dictionary
        self.file_path = dict()
        self.file_blocktype = dict()
        self.current_row = -1
        
    def delete_selected(self):
        
        # for item in self.list_added.selectedItems():
        #     self.list_added.takeItem(self.list_added.row(item))
        for item in self.table_display.selectedItems():
            self.table_display.removeRow(item.row())
            # remove the file path and block type from the dictionary
            file_name = item.text()
            del self.file_path[file_name]
            del self.file_blocktype[file_name]
            self.current_row -= 1
    def preview(self):
        if len(self.file_path) == 0 :
            self.show_warning(msg="No file is added to the table")
            return
        
        canvas = MplCanvas(width=5.51, height=5.81, dpi=100)
        canvas.axes.clear()
        for file_name in self.file_path:
            # bool_img = self.read_npy(self.file_path[file_name])
            file_path = self.file_path[file_name]
            file_extension = os.path.splitext(file_path)[1].lower()

            if file_extension == '.npy':
                bool_img = self.read_npy(file_path)
            elif file_extension in ['.tif', '.tiff']:
                bool_img = self.read_tiff(file_path)
            else:
                self.show_warning(f"Unsupported file type: {file_extension}")
                return
            x, y, z = np.where(bool_img)
            canvas.axes.scatter(x, y, z, marker=',', alpha= 0.05, s=9)
            canvas.axes.set_axis_off()
        self.scene.addWidget(canvas)
        
    def cellDoubleClicked(self, row, column):
        # Example list of items to select from
        items = list(self.all_blocks.keys())
        dialog = ListDialog(items, self)
        if dialog.exec_():
            selectedItem = dialog.getSelectedItem()
            # print("selectedItem", selectedItem) 
            if selectedItem:
                self.table_display.setItem(row, 1, QTableWidgetItem(selectedItem))
                # set the block type to the dictionary
                self.file_blocktype[self.table_display.item(row, 0).text()] = self.all_blocks[selectedItem]
                
    def get_item_list(self):
        csv_file_path = resource_path("java1.20.csv")
        with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                if len(row) >= 2:  # Make sure the row has at least 2 columns
                    key, value = row[0], row[1]
                    self.all_blocks[key] = value
        self.all_blocks = {key: self.all_blocks[key] for key in sorted(self.all_blocks)}
    
    
    # following function is used to generate the scheme
    def write_image(self, schem : mcschematic.MCSchematic, bool_image : np.ndarray, block_data : str):
        """Writes a boolean image to a schematic."""
        assert bool_image.ndim == 3
        for idx, bool_value in np.ndenumerate(bool_image):
            if bool_value:
                schem.setBlock(idx, block_data)
    
    def read_npy(self,path : str):
        """reads a boolean image from a numpy file."""
        img = np.load(path)
        bool_img = img.astype("bool") # ensure boolean
        return bool_img
   
    def read_tiff(self,path : str):
        """reads a tiff stack (in ImageJ format) and returns a minecraft compatible boolean image."""
        # remove color channel
        img = tifffile.imread(path)
        if img.ndim == 4:
            img = img.sum(axis=-1)
        # rearrange axes to be minecraft (x, y, z)
        img = np.moveaxis(img, 0, 1)
        bool_img = img.astype("bool") # convert to boolean
        return bool_img

    def generate_scheme(self):
        # let user decide where to save the file
        options = QFileDialog.Options()
        save_path, _ = QFileDialog.getSaveFileName(self,
                                                    "Choose Save Path",
                                                "",
                                                "Schem (*.schem)",
                                                options=options)
        
        schem = mcschematic.MCSchematic()
        if len(self.file_path) == 0 :
            self.show_warning(msg="No file is added to the table")
            return
        #loop over the file path and block type over the keys, cuz the key is the same
        
        for file_name in self.file_path:
            # bool_img = self.read_npy(self.file_path[file_name])
            file_path = self.file_path[file_name]
            file_extension = os.path.splitext(file_path)[1].lower()

            if file_extension == '.npy':
                bool_img = self.read_npy(file_path)
            elif file_extension in ['.tif', '.tiff']:
                bool_img = self.read_tiff(file_path)
            else:
                self.show_warning(f"Unsupported file type: {file_extension}")
                return
            block = "minecraft:{}".format(self.file_blocktype[file_name])
            self.write_image(schem, bool_img, block)
        
        schem.save(os.path.dirname(save_path), os.path.basename(save_path), mcschematic.Version.JE_1_20)
        print("Scheme generated")

    def show_warning(self,msg: str):
        # Create a QMessageBox
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setWindowTitle("Warning")
        msgBox.setText(msg)
        # msgBox.setInformativeText()
        # msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setDefaultButton(QMessageBox.Ok)
        
        # Display the message box and capture the response
        retval = msgBox.exec_()
        print(f"Message box return value: {retval}")
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())