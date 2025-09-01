## Asignment week 3 - git_asset-publisher_drive

import hou
import os
from googledrive_uploader import Uploader ## Imports a method to upload files to google drive. Imports google´s custom libraries. Doesnt work with houdini by default.

class Publisher:
    def __init__(self):

        self.name = None
        self.version = None
        self.path = None
        self.user = None
        self.check_asset = False
    
    def set_publish_path(self): # 1) method to get al the inputs from the user and save the asset on disk
    
        my_hda = hou.pwd()
        geo_type = ".abc" 
        
        self.user = str(os.environ["USER"])
        self.name = str(my_hda.parm("basename").eval())
        self.version = str(my_hda.parm("version").eval())
        
        constructed_path = "$HIP/houdini/geo/" + self.name +  "/v" + self.version + "/" + self.name + "_geo" + geo_type 
        
        my_hda.parm("file").set(constructed_path) #Sets the file path output in the HDA
        
        self.path = str(my_hda.parm("file").eval())
        my_hda.parm("execute").pressButton()
                
        print("asset saved to disk!: ", self.path)
        
        return self.path 
        
                
    def upload_to_drive(self): # 2) method to call the class Uploader from my custom "googledrive_uploader" library
        
        asset_path = self.set_publish_path()
 
        Up = Uploader()
        Up.driveUploader(asset_path)
        
        print("published on drive!")
           

Pu = Publisher()
