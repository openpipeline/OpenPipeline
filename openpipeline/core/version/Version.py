import os
import re

class Version():
    '''
    The Version class contains the functionality for "classic" OpenPipeline
    file version control which is just making copies of files.  Simple but it
    works.  Classes for SVN or CVS can derive from this to take advantage of
    other other revision control schemas.
    
    Default naming:
        [name]_workshop_####.type
    
    Examples:
        testMaster_workshop_0003.mb
    
    '''
    def __init__(self):
        pass
        self.object = object

    def getByIndex(self, index):
        pass
    
    def latest(self, path):
        '''
        Get latest version
        '''
        all = self.all(path)
        if len(all) > 0:
            latest = max(all)
            return latest
        else:
            return None
        
    def verify(self):
        '''
        Verify that version exists
        '''
        if os.path.exists(path):
            return 1
        else:
            return 0
        
    def next(self, input="testMaster_workshop_0003.mb"):
        '''
        Get the next version
        '''     
        basename = os.path.splitext(input)
        elements = basename[0].split("_")
        
        version = int(elements[2])
        next = version + 1
        
        print '%(asset)s has %(#)04d %(type)s.' % {'asset': elements[0], "#": version, "type": elements[1]}     
       
        
    def all(self, path):
        '''
        Get a list of all the versions
        '''
        versions = []
        versionspath = os.path.join(path, "workshop") # workshop is temp
        inventory = [f for f in os.listdir(versionspath) if f[0] != '.']
        for version in inventory:
            basename = os.path.splitext(version)
            elements = basename[0].split("_")
            versions.append(int(elements[2]))
        versions.sort()
        return versions
    
    
class svn(Version):
    pass

class git(Version):
    pass

class cvs(Version):
    pass