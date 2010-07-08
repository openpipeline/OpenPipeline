import os

class Inventory:
    def __init__(self, elements):
        self.elements = elements
        pass
    
    def getPath(self):
        # project, module, type, asset
        
        # 1 = project
        # 2 = module: lib, scenes, comp, etc
        # 3 = asset type or sequence
        # 4 = asset or shot (returns components)
        # 5 = component
        
        depth = len(self.elements)
        path = ""
        count = 0
        
        print depth
        
        for item in self.elements:
            print path
            if depth == 5 and count == 3:
                path = os.path.join(path, item, "components")
                print "hererere!"
            else:
                path = os.path.join(path, item)
            count = count + 1
        
        return path    
    
    def list(self, path=""):
        if path == "":
            path = self.getPath()

        # create list remove files that start with a "."            
        inventory = [f for f in os.listdir(path) if f[0] != '.']
        print inventory
        return inventory
    
    def count(self):
        file_count = len([f for f in os.listdir(path) if os.path.isfile(f)])
        return file_count
    
    