import os

import file
reload(file)

class Workshop(file.File):
    def __init__(self):
        pass
    
    def open(self, path, item, version):
        # break out workshop
        name = '%(item)s_workshop_%(version)04d.mb' % {'item': item, "version": version}     
        workshopPath = os.path.join(path, "workshop", name)
                
        if self.query(workshopPath):
            print workshopPath
            return workshopPath
        else:
            print "error"

    
    def save(self):
        pass

