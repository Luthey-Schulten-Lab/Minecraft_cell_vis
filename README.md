# Visualizing Cell Structures with Minecraft
Authors and Affiliation:
Tianyu Wu<sup>1, 2, 3</sup>, Zane R. Thornburg<sup>4, 5</sup>, Kevin Tan<sup>3, 4, 6</sup>, Seth Kenkel<sup>3, 4</sup>, Stephen A. Boppart<sup>3, 4, 5, 6, 7, 10</sup>, Rohit Bhargava<sup>2, 3, 4, 5, 6, 7, 8, 9</sup>, Zaida Luthey-Schulten<sup>1, 2, 3, *</sup>


<sup>1</sup> Center for Biophysics and Quantitative Biology, University of Illinois at Urbana–Champaign, Urbana, IL, USA
<sup>2</sup> Department of Chemistry, University of Illinois at Urbana–Champaign, Urbana, IL, USA
<sup>3</sup> National Science Foundation Science and Technology Center for Quantitative Cell Biology, Beckman Institute for Advanced Science and Technology, University of Illinois at Urbana–Champaign, Urbana, IL, USA
<sup>4</sup> Beckman Institute for Advanced Science and Technology, University of Illinois at Urbana-Champaign, Urbana, IL, USA
<sup>5</sup> Cancer Center at Illinois, University of Illinois at Urbana-Champaign, Urbana, IL, 61801, USA
<sup>6</sup> Department of Bioengineering, University of Illinois at Urbana-Champaign, Urbana, IL, 61801, USA
<sup>7</sup> Department of Electrical and Computer Engineering, University of Illinois at Urbana–Champaign, Urbana, IL, USA
<sup>8</sup> Department of Chemical and Biomolecular Engineering, University of Illinois at Urbana-Champaign, Urbana, IL, 61801, USA
<sup>9</sup> Department of Mechanical Science and Engineering, University of Illinois at Urbana-Champaign, Urbana, IL, 61801, USA
<sup>10</sup> NIH/NIBIB Center for Label-free Imaging and Multiscale Biophotonics


![minecraft edu](./images/minecraft.svg) ![amulet](./images/amulet.svg)![pyqt6](./images/pyqt6.svg)[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

### **NOT AN OFFICIAL MINECRAFT [PRODUCT/SERVICE/EVENT/etc.]. NOT APPROVED BY OR ASSOCIATED WITH MOJANG OR MICROSOFT.**
## You can watch more demos on QCB youtube channel: 
[![Watch the video](path_to_your_gif.gif)](https://youtube.com/playlist?list=PLR1Fx92RsGfWXiZm-Nqjf_glfWtq4bEVJ&si=EwhHNwTGRBpluElC)
## Quick Start

To quickly load and play with the cells we demonstrated in the paper, you can go to the directoy `/Worlds` and choose the worlds based on your Edition (Education edition please choose Bedrock). Download the entire file, unzip and then put them under certain directories based on your OS and Minecraft Edition. (If you don't know, please check the section: [place to put the world Files](#place-to-put-the-world-files)).

After you put the world in the proper directory, launch/restart Minecraft, you should find the world in Minecraft now.



https://github.com/user-attachments/assets/33ef624d-2ef2-4779-8476-844168eff06e



## Repository Organization

```markdown
/repository-root
├── /Schematics/             # Schematics files for Amulet/MCEdit/WorldEdit
│
├── /Worlds/                 # Minecraft world files
│   ├── /bedrock/            # Bedrock/Education edition worlds
│   ├── /java/               # Java edition worlds
│   └── /Empty/              # Empty worlds for DIY
│
├── /Resources/              # Segmented data and scripts for different cell examples
│   ├── /MinCell/            
│   ├── /Yeast/
│   ├── /Breast Cancer Cells/
│   └── /Human Epithelial Cells/
│
├── /SchemGen_GUI/           # Generate schematics from segmented data with GUI
│   ├── /src/                # source code
│   └── /mcvis.exe/          # GUI
│
├── /images/                 # images for readme.md 
│
├── .gitignore               # Git ignore file to exclude unnecessary files
├── LICENSE                  # License file
└── README.md                # Main README file (Project Overview)
```
## Prerequisite
The entire workflow starting from segmented data (saved as .npys files) requires the users to install:

1. Minecraft (Java/Bedrock/Education)
2. [Optional] GUI or python with numpy, mcschematic
3. [Optional] MC amulet

If you prefer to use use the worlds we already generated for our examples mentioned in the paper, you can directly download those worlds and put them under the Minecraft world directory. 

### 1. Minecraft Installation

Please be aware that there are different versions of Minecraft for different Operating Systemf:
Here's a table comparing the different Minecraft editions and the corresponding operating systems they support:

| **Edition**               | **Supported OS**           | **Description**                                                                                      | **Notes**                                                                                                    |
|---------------------------|----------------------------|------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| **Minecraft: Java Edition**| Windows, macOS, Linux      | The original version of Minecraft designed primarily for personal computers.                         | Supports mods and custom servers. The most flexible edition in terms of customizations and community tools.   |
| **Minecraft: Bedrock Edition** | Windows, Xbox, PlayStation, Nintendo Switch, iOS, Android, Fire OS, Apple TV, Gear VR, Windows 10 (UWP), Windows 11 | Cross-platform edition optimized for performance and compatibility across multiple devices.            | Includes Minecraft for mobile devices and consoles. Less modding support compared to Java Edition.            |
| **Minecraft: Education Edition** | Windows, macOS, iPad, Chromebook | A version of Minecraft designed specifically for educational use, with features tailored for classroom activities. | Built on the Bedrock Edition, but includes educational tools like coding and lesson plans for students.       |

We are aware there are other Minecraft versions for Mobile phones, VR headsets, etc. In such cases, you should be able to start from schematic files and generate the corresponding worlds and put them under appropriate directories.

#### 1.1 Java Edition

Java is the most versatile in terms of mods, custom servers, and community content but is only available on PC platforms (Windows, macOS, Linux). But it is not free, you can purchase and download it from here: 

[Minecraft: Java Edition for PC Standard Edition](https://www.minecraft.net/en-us/store/minecraft-java-bedrock-edition-pc)

#### 1.2 Education Edition

Minecraft Education is free for Educational Purposes. You can download it from the following link:

[Minecraft Education](https://education.minecraft.net/en-us)

## 2. [Optional] Schematics Generation
There are two ways to generate schematics from segemented data (.npy or .tiff files): python script or GUI.
### 2.1 python scripts
If you are familiar with python, we recommend you take a look of the template jupyter notebooks and write your own for your own cell structures.  Templates are under `/Resources/` together with segmented data.

1. intstall miniconda/Anaconda: 

   [Installing Miniconda — Anaconda documentation](https://docs.anaconda.com/free/miniconda/miniconda-install/)

2. install required packages

   ```bash
   conda create -n cellvis python
   conda activate cellvis
   pip install numpy mcschematic jupyterlab
   ```

3. Run corresponding jupyter notebooks saved under `/Resources/*/`

### 2.2 GUI

Alternatively, users might try out the GUI to import the segmented npys and generate schematics files with GUI. Currently, the GUI is only available for Windows and Mac OS. And only support segmented data in `npy` and `tiff` format. 

## 3. [Optional] MC Amulet
**MC Amulet** is a versatile Minecraft world editor for both **Java** and **Bedrock Editions**. It enables users to modify world structures, import/export **schematic files**, and convert worlds between different versions. With features like **chunk management**, **NBT editing**, and a **3D visualization tool**, MC Amulet allows precise customization and efficient world editing. It's ideal for transferring builds, optimizing worlds, and managing cross-platform projects.

Here is the link [Amulet Editor (amuletmc.com)](https://www.amuletmc.com/)

Install if you want to import schematic files into a Minecraft world.


## DIY your own worlds 
If you are not satisfied with the Quick Start and want more freedom to create your own worlds with the segmented cell data provided or even your own segmented data, You should follow this workflow.

1. convert your segmented cell data to binary 3-D matrix npy files. Different regions should have different npys with proper names. 
2. Use python scripts or GUI to generate the schematic files. (For 2D images, you can use webtool: https://herhor.net/minecraft/imager/)
3. Use MC Amulet to import schematic files into a Minecraft world. We include [Empty Minecraft Worlds](#empty-minecraft-worlds) for convenience. 
4. Follow the instruction in [Quick Start](#quick-start) to put the world folder in the proper directory.
5. Launch/ Restart the Minecraft and Open the World.

## Information might be useful


### Place to put the world Files

#### Java Edition

If you didn't change the default directory to install Minecraft, for the **Java Edition**, it should be located in:



| OS      | Location                                         |
| :------ | :----------------------------------------------- |
| Windows | `%APPDATA% \.minecraft\saves`                    |
| macOS   | `~/ Library/Application Support/minecraft/saves` |
| Linux   | `~/.minecraft/saves`                             |

If you're a Windows user and are unfamiliar with how to find your appdata folder, follow these steps:

1. Click Start → Run. If you don't see "Run", press ⊞ Windows + R.
2. Type `%APPDATA%\.minecraft` and click "OK".

If you're a Mac user, you can open the folder through Spotlight:

1. Open Finder and press ⇧ Shift + ⌘ Command + G or open the Spotlight popup through the magnifying glass icon on the right of the Menu Bar.
2. Type `~/Library/Application Support/minecraft` and hit ↵ Enter.

On Linux or macOS, the `~` in the path refers to the home directory. Folders starting with a `.` are hidden by default. In most file managers, hitting Ctrl + H toggles their hidden status. In macOS specifically, since version 10.12 (Sierra), the shortcut ⌘ Command + ⇧ Shift + . toggles the hidden status of files.

[reference from Minecraft Fandom]([.minecraft – Minecraft Wiki (fandom.com)](https://minecraft.fandom.com/wiki/.minecraft))

#### Education Edition

| OS                      | Location                                                     |
| :---------------------- | :----------------------------------------------------------- |
| Windows Desktop Version | `C:\Users\[*USERNAME*]\AppData\Roaming\Minecraft Education Edition\games\com.mojang\minecraftWorlds` |
| Windows Store Version   | `C:\Users\username\AppData\Local\Packages\Microsoft.MinecraftEducationEdition_8wekyb3d8bbwe\LocalState\games\com.mojang\minecraftWorlds` |
| Mac                     | `HD > Users > [*USERNAME*] > Library > Application support > Minecraftpe > Games > com.mojang` |
| IPad                    | `Minecraft Education Edition\games\com.mojang\minecraftWorlds` |
| Chromebook              | `Play files > games > com.mojang > minecraftWorlds`          |

*Note: "*[*USERNAME*]*" refers to the user account used to log in to the device, not the sign in for Minecraft Education.*

+ Reference: [Location of World Files – Minecraft Education](https://educommunity.minecraft.net/hc/en-us/articles/4404785703316-Location-of-World-Files#:~:text=If)

#### Bedrock Edition

| OS      | Location                                                     |
| :------ | :----------------------------------------------------------- |
| Windows | `%localappdata%\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\minecraftWorlds` |

1. Click Start → Run. If you don't see "Run", press ⊞ Windows + R.
2. Type **the location above** and click "OK".

+ Reference: [How to Transfer Your World to Another Device in Minecraft: Bedrock Edition | Minecraft Help](https://help.minecraft.net/hc/en-us/articles/4409165790605-How-to-Transfer-Your-World-to-Another-Device-in-Minecraft-Bedrock-Edition)

## Contribution

WT built the repository and created the GUI and workflow for yeast. ZT created the workflow and data for the minimal cell. KT created the workflow and data for human breast cells. SK provided the data for the human epithelial cells.

## Acknowledgements

We would like to extend our gratitude to the following tools and communities that made this project possible:

+ Minecraft Java Edition, Minecraft Education Edition, and Minecraft Bedrock Edition for providing the platforms to build and explore interactive worlds.

+ MC Amulet for its powerful world editing capabilities, enabling us to modify and transfer Minecraft worlds across different platforms.


+ Chunker for its world edition conversion tools, making it easier to move between different versions of Minecraft.


+ Minecraft Wiki for providing valuable resources, support, and inspiration. 
