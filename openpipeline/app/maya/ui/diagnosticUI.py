import maya.cmds as cmds
import os

import window as window

import UIObjects as UIObjects

import openpipeline.core.util.XML as XML
reload(XML)

import openPipelineSaveMasterGUI as openPipelineSaveMasterGUI
reload(openPipelineSaveMasterGUI)

import openPipelineProjectManagerGUI as openPipelineProjectManagerGUI
reload(openPipelineProjectManagerGUI)

import openPipelineProjDialogGUI as openPipelineProjDialogGUI
reload(openPipelineProjDialogGUI)

import openPipelineMainUI as openPipelineMainUI
reload(openPipelineMainUI)

class diagnosticUI(window.window):

    def __init__(self, filePath = None):
        
        '''
        Name: diagnosticUI.py
        Input: filePath (a root file path that contains the 'openpipeline' folder)
        Returns: none
        Description:  This script is an example of how a single class can manage and store the data for all Maya OpenPipeline GUIs, and with it's loadPrefs() and savePrefs() procedures, it also demonstrates it's potential ability to save out both session independent & application independent information.
        Use: This script can work in conjunction with the 'begin.py' module or on it's own. If working with the 'begin.py' module (the most basic method), see the 'begin.py' script for further directions. If using the 'diagnosticUI.py' module on it's own, before instantiating this class you must first append/insert the system path that contains the openpipeline folder. Upon initialization, this class inherits functionality from the 'window.py' module, and as a result has the method 'showWindow' available to it. Example - self.showWindow() (or whatever you name the instance of this module) will show the Diagnostic UI. The method entitled 'content' contains the actual UI commands. The 'showWindow' method uses this command to build a dockable or stand-alone window. See the 'window.py' module for more information on this relationship. The loadPrefs() and savePrefs() procedures only work when this 'diagnosticUI' module is instantiated with an incoming 'filePath' string. Part of the purpose of the 'begin.py' module is to allow the user to select this path, which then gets passed to the 'diagnostic.py' module. Attributes such as self.width stupilates the width of the window. self.dockable enables this window as a floating dockable window (if using Maya2011). A future TODO might be to further develop and refine this dock functionality. This could be done in the 'window.py' base class by creating a simple drop down for each window that docks the window left, right, up or down, which might create a more desirable outcome than the somewhat still buggy 'floating but dockable' mode that is currently offered in Maya2011, which often ends up in uncontrollable window sizes.
        '''
        
        self.UIObjects = UIObjects.UIObjects()
        
        self.filePath = filePath
        
        self.width=500
        self.height=300
        self.name = "Diagnostic UI Manager"
        self.dockable=0
        self.UIObjects.openPipelineSaveMasterGUI = openPipelineSaveMasterGUI.openPipelineSaveMasterGUI()
        self.UIObjects.openPipelineProjectManagerGUI = openPipelineProjectManagerGUI.openPipelineProjectManagerGUI()
        self.UIObjects.openPipelineProjDialogGUI = openPipelineProjDialogGUI.openPipelineProjDialogGUI()
        self.UIObjects.openPipelineMainUI = openPipelineMainUI.openPipelineMainUI()
    
    def content(self):
        
        '''
        "content" - see the 'window.py' module for more information about how this "content" method functions
        '''
        
        self.form1 = cmds.formLayout( 'openPipelineProjectManagerGUI_form', numberOfDivisions=100 )
        
        self.menuBarLayout0 = cmds.menuBarLayout()
        self.menu01 = cmds.menu(label='options')
        cmds.menuItem(label="Refresh Objects Field", subMenu=0, parent=self.menu01, command=lambda *args:self.updateTextField() )
        cmds.menuItem(label="Reload", subMenu=0, parent=self.menu01, command=lambda *args:self.reload() )
        cmds.menuItem(label="Save Prefs", subMenu=0, parent=self.menu01, command=lambda *args:self.savePrefs() )
        cmds.menuItem(label="Load Prefs", subMenu=0, parent=self.menu01, command=lambda *args:self.loadPrefs() )
        cmds.setParent(self.menuBarLayout0)
        cmds.setParent(self.form1)
        
        self.diagnosticUI_UIObjects_scrollField = cmds.scrollField('diagnosticUI_UIObjects_scrollField', parent=self.form1, ww=1, editable=0)
        self.diagnosticUImainUI_btn = cmds.button(l="Open Pipeline Main GUI", parent=self.form1, bgc=(.85, .85, .85), c=lambda *args:self.buttonRelease('openPipelineMainUI'))
        self.diagnosticUIProjManager_btn = cmds.button(l="Project Manager GUI", parent=self.form1, bgc=(.8, .8, .8), c=lambda *args:self.buttonRelease('openPipelineProjectManagerGUI'))
        self.diagnosticUISaveMaster_btn = cmds.button(l="Save Master GUI", parent=self.form1, bgc=(.75, .75, .75), c=lambda *args:self.buttonRelease('openPipelineSaveMasterGUI'))
        self.diagnosticUIProjDialog_btn = cmds.button(l="Project Dialogue GUI", parent=self.form1, bgc=(.7, .7, .7), c=lambda *args:self.buttonRelease('openPipelineProjDialogGUI'))

        #Attach elements to form
        cmds.formLayout(
            self.form1,
            edit=True,
            attachPosition=[
                (self.menuBarLayout0, 'top', 0, 0),
                (self.menuBarLayout0, 'left', 0, 0),
                (self.menuBarLayout0, 'right', 0, 100),
                (self.diagnosticUImainUI_btn, 'left', 5, 0),
                (self.diagnosticUImainUI_btn, 'right', 5, 100),
                (self.diagnosticUI_UIObjects_scrollField, 'left', 5, 0),
                (self.diagnosticUI_UIObjects_scrollField, 'right', 5, 100),
                (self.diagnosticUIProjManager_btn, 'left', 5, 0),
                (self.diagnosticUIProjManager_btn, 'right', 5, 100),
                (self.diagnosticUISaveMaster_btn, 'left', 5, 0),
                (self.diagnosticUISaveMaster_btn, 'right', 5, 100),
                (self.diagnosticUIProjDialog_btn, 'left', 5, 0),
                (self.diagnosticUIProjDialog_btn, 'right', 5, 100),
                (self.diagnosticUIProjDialog_btn, 'bottom', 2, 100),
            ],
            attachControl=[
                
                (self.diagnosticUI_UIObjects_scrollField, 'top', 2, self.menuBarLayout0),
                (self.diagnosticUI_UIObjects_scrollField, 'bottom', 2, self.diagnosticUImainUI_btn),
                (self.diagnosticUImainUI_btn, 'bottom', 2, self.diagnosticUIProjManager_btn),
                (self.diagnosticUIProjManager_btn, 'bottom', 2, self.diagnosticUISaveMaster_btn),
                (self.diagnosticUISaveMaster_btn, 'bottom', 2, self.diagnosticUIProjDialog_btn),
            ]
            )
        
        return [self.form1]
    
    
    def reload(self):
        '''
        "reload" resets the diagnosticUI
        '''
        for obj in self.UIObjects.window:
            if cmds.window(obj, q=True, ex=True):
                cmds.deleteUI(obj)
        for obj in self.UIObjects.dockControl:
            if cmds.dockControl(obj, q=1, exists=1):
                cmds.deleteUI(obj)
        self.UIObjects = UIObjects.UIObjects()
        self.showWindow()
        self.updateTextField()
    
    
    def buttonRelease(self, window):
        eval('self.UIObjects.%s.showWindow()' % window)
    
    
    def updateTextField(self):
        '''
        "updateTextField" updates the 'self.diagnosticUI_UIObjects_scrollField' text field to reflect the most current GUI state.
        '''
        textFieldString = '---window objects---\n\n'
        for obj in self.UIObjects.window:
            if cmds.window(obj, q=True, ex=True):
                textFieldString += obj + '\n'
        textFieldString += '\n---dockable objects---\n\n'
        for obj in self.UIObjects.dockControl:
            if cmds.dockControl(obj, q=1, exists=1):
                textFieldString += obj + '\n'
        cmds.scrollField(self.diagnosticUI_UIObjects_scrollField, edit=1, text=textFieldString)
        
    def savePrefs(self):
        
        '''
        "savePrefs" stores xml data using the 'XML.py' module
        '''
        fileName = 'test1.xml'
        prefs = [('hello'),('goodbye'),('idunno')]
        filePath = os.path.join(self.filePath, 'openpipeline', 'app', 'maya', 'ui', 'prefs', fileName)
        xmlFile = XML.xmlfile(filePath)
        xmlFile.save(prefs)
        
    def loadPrefs(self):
        
        '''
        "loadPrefs" loades xml data using the 'XML.py' module
        '''
        
        fileName = 'test1.xml'
        filePath = os.path.join(self.filePath, 'openpipeline', 'app', 'maya', 'ui', 'prefs', fileName)
        xmlFile = XML.xmlfile(filePath)
        prefs = xmlFile.load()
        print "prefs = %s" % prefs