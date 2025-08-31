## Asignment week 3 - git_asset-publisher_drive

#import hou
import os
from driveUploader import Uploader

class Publisher:
    def __init__(self):

        self.name = None
        self.version = None
        self.path = None
        self.user = None
    
    def set_publish_path(self): # 2) Func to get the string from the search field
    
        """my_hda = hou.pwd()
        geo_type = ".abc"
        
        self.user = str(os.environ["USER"])
        self.name = str(my_hda.parm("basename").eval())
        self.version = str(my_hda.parm("version").eval())
        
        constructed_path = "$HIP/houdini/geo/" + self.name +  "/v" + self.version + "/" + self.name + "_geo" + geo_type
        
        #Sets the file path output
        my_hda.parm("file").set(constructed_path)
        
        self.path = str(my_hda.parm("file").eval())
        my_hda.parm("execute").pressButton()"""
        
        self.path = "C:/Users/Miguel/houdini/geo/myAsset/v1/myAsset_geo.abc"
        print(self.path)
        
        Uploader.driveUploader(self.path)