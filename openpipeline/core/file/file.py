import os

class File:
    def __init__(self):
        pass
  
    def query(self, path):
        if os.path.exists(path):
            return 1
        else:
            return 0

    def bundle(self):
        pass        
   