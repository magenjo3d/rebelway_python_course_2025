## Asignment week 3 - git_asset-publisher_drive

import hou
import os

class Publisher:
    def __init__(self):

        self.name = None
        self.version = None
        self.path = None
        self.user = None
    
    def set_publish_path(self): # 2) Func to get the string from the search field
    
        my_hda = hou.pwd()
        
        self.user = str(os.environ["USER"])
        self.name = str(my_hda.parm("basename").eval())
        self.version = str(my_hda.parm("version").eval())
        
        constructed_path = "$HIP/houdini/geo" + "/v" + self.version + "/" + self.user + "/" + self.name 
        
        my_hda.parm("file").set(constructed_path)
        
        self.path = str(my_hda.parm("file").eval())
        my_hda.parm("execute").pressButton()
        
        print(self.path)
        
        
