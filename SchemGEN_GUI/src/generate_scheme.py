import mcschematic
import tifffile
import numpy as np

def write_image(schem : mcschematic.MCSchematic, bool_image : np.ndarray, block_data : str):
    """Writes a boolean image to a schematic."""
    assert bool_image.ndim == 3
    for idx, bool_value in np.ndenumerate(bool_image):
        if bool_value:
            schem.setBlock(idx, block_data)
    
def read_npy(path : str):
    """reads a boolean image from a numpy file."""
    img = np.load(path)
    bool_img = img.astype("bool") # ensure boolean
    return bool_img

def read_tiff(path : str):
    """reads a tiff stack (in ImageJ format) and returns a minecraft compatible boolean image."""
    # remove color channel
    img = tifffile.imread(path)
    if img.ndim == 4:
        img = img.sum(axis=-1)
    # rearrange axes to be minecraft (x, y, z)
    img = np.moveaxis(img, 0, 1)
    bool_img = img.astype("bool") # convert to boolean
    return bool_img

def generate_scheme(path: dict, block_type:dict, saving_path:str):
    schem = mcschematic.MCSchematic()
    #loop over the file path and block type over the keys, cuz the key is the same
    for file_name in path:
        bool_img = read_npy(path[file_name])
        block = "minecraft:{}".format(block_type[file_name])
        write_image(schem, bool_img, block)
        
    schem.save('.', "scheme_result", mcschematic.Version.JE_1_20)
    