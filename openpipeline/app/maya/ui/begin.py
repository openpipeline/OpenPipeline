import maya.cmds as cmds
import sys

class begin():
    
    def __init__(self):
        
        '''
        Name: begin.py
        Input: none
        Returns: none
        Description: This script is an example of a potential entry point for the OpenPipeline Maya GUI
        Use: Initialization of this script will open a dialogue window. Using that window, select the folder that contains the 'openpipeline' directory.
        
        Examples:
        
        openPipeline = begin()
        
        openPipeline.diagnosticUI.showWindow()
        
        '''
        
        self.sourceFilesPath()
        self.appendDir()
        self.diagnostic()
    
    
    def sourceFilesPath(self):
        
        cmds.fileBrowserDialog( m = 4, fc = self.getSrcDir, ft = "directory", an = "Select the folder that contains the 'openpipeline' directory")


    def getSrcDir(self, directoryPathInput, fileType):
        
        self.srcDir = directoryPathInput


    def diagnostic(self):
        
        import openpipeline.app.maya.ui.diagnosticUI as diagnosticUI
        reload(diagnosticUI)
        self.diagnosticUI = diagnosticUI.diagnosticUI(self.srcDir)
        self.diagnosticUI.showWindow()


    def appendDir(self):
            
        sysPath = sys.path
        ks_appendGo = 1
        for aPath in sysPath:
            if (aPath == str(self.srcDir) ):
                ks_appendGo = 0
        
        if ks_appendGo:
            sys.path.insert(0,self.srcDir)