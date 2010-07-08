import os

class Notes:
    def __init__(self):
        pass

    def create(self):
        pass
    
    def query(self, path, element):
        note = os.path.join(path, "notes", (element + "_AssetNote.xml"))
        if os.path.exists(note):
            return 1
        else:
            return 0
    
    def read(self):
        pass
    
    def write(self):
        pass