import os

from util import XML
reload( XML )

class Project():
    '''
    Core project methods.
    '''

    def __init__(self):
        self.openPipeline_projectFilePath = ""
        self.openPipeline_projList = ""
    
    def create():
        pass
    
    def remove():
        pass
        
    def list():
        pass
    
    def set():
        # app specific?
        pass
    
    def validateProject(self):
        pass
    
    def validateProjectFile(self):
        pass
        
    def path(self):
        '''
        Description: 	Returns the full path of the Project File
        Input: 		none
        Returns: 	The full path of the Project File (string)
        '''
        
        projectFilePath = os.path.join(self.openPipeline_projectFilePath, self.openPipeline_projList)
        return projectFilePath
