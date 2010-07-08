import maya.cmds as cmds

class window():
    
    def __init__(self):
        '''
        Name: window.py
        Description: Base-class for OpenPipeline Maya Windows. The purpose of this class is to avoid writing redundant Maya UI functionality into every Maya GUI. For example, deleting a duplicate UI before building a new one. 
        Directions: This class functions through inheritance, so that a given class inherits the functionality of this class. In creating a new class that inherits from this window class, you must have a procedure called 'content' in your inheriting class.
        
        example: def content(self):
        
        This procedure entitled 'content' must return one or more Maya 'formLayout' elements as a list. Additionally, you must instantiate and define the following class attributes in order for the 'showWindow method' to work properly:
        
        self.width = (integer) example: 450
        self.height = (integer) example: 450
        self.prettyName = (string) example: 'OpenPipeline 2.0'
        self.name = (string containing only integers and numbers AKA no funky stuff) example: 'openPipelineUI'
        self.dockable = (boolean) example: 0
        
        Attributes such as self.width stupilate the width of a given window. self.dockable enables a given window as a floating dockable window (if using Maya2011). A future TODO might be to further develop and refine this dock functionality. This could be done by creating a simple drop down for each window that docks the window left, right, up or down, which might create a more desirable outcome than the somewhat still buggy 'floating but dockable' mode that is currently offered in Maya2011, which often ends up in uncontrollable window sizes.
        
        '''
    
    def showWindow(self, dockableDropdownOption=None):
        
        try: self.prettyName
        except: self.prettyName = self.name
        self.uiName = self.name.replace(" ", "")
        self.dockControl = self.uiName
        self.window = str(self.uiName)+"_window"
        self.m2011 = None
        
        self.m2011 = ( cmds.about(version=1) == "2011 x64")
        # check if a version of this dock/window is already open, clear it
        if ( self.m2011 and self.dockable ): # if in Maya 2011+ and dockable,
            
            if cmds.dockControl(self.dockControl, exists=1):
                cmds.deleteUI(self.uiName)
            if cmds.window(self.window, q=True, ex=True):
                cmds.deleteUI(self.window)
            self.window = cmds.window(self.window, title=self.prettyName, sizeable=1)
            
        else: # older version of Maya
            
            self.window = self.uiName
            if cmds.window(self.window, q=True, ex=True): cmds.deleteUI(self.window)
            self.window = cmds.window(self.window, title=self.prettyName, sizeable=1)
        
        # Content command that changes depending on the instance of this class
        windowElements = self.content()
        for element in windowElements:
            cmds.formLayout( element, e=1, parent = self.window )
        
        # docking (if available) and show window
        if ( self.m2011 and self.dockable ): # if in Maya 2011+ and dockable,
            cmds.dockControl( self.dockControl, area='left', content=self.window, floating=1, label=self.prettyName )
            cmds.dockControl( self.dockControl, e=1, height=self.height, width=self.width)
            self.UIObjects.addDockControl(self.dockControl)
        else:
            cmds.showWindow(self.window)
            cmds.window(self.window, e=1, width=self.width, height=self.height)
            self.UIObjects.addWindow(self.window)
  
    def deleteWindow(self):
        if ( self.m2011 and self.dockable ): cmds.deleteUI(self.dockControl)
        else: cmds.deleteUI(self.window)