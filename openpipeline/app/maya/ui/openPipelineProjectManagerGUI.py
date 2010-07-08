###########################################
# Name: openPipelineProjectManagerGUI
# Description: creates oP Project UI
# Input: none
# Returns: none
############################################

import maya.cmds as cmds

import window as window
reload(window)

import UIObjects as UIObjects

class openPipelineProjectManagerGUI(window.window):

    def __init__(self):
        
        self.UIObjects = UIObjects.UIObjects()
        
        self.width=550
        self.height=460
        self.name = "openPipeline Project Manager"
        self.dockable=0
        self.scriptLocation = "userName/Documents/OpenPipeline"
    
    def content(self):
        
        self.form1 = cmds.formLayout( 'openPipelineProjectManagerGUI_form', numberOfDivisions=100 )
        
        self.projManagerScriptLocation_txt = cmds.text('projManagerScriptLocation_txt', parent=self.form1, align="right", l="Script Location:", w=110)
        self.projManagerScriptLocation_txtField = cmds.textField('projManagerScriptLocation_txtField', parent=self.form1, editable=0, tx=self.scriptLocation)
        self.projManagerProjFileLocation_txt = cmds.text('projManagerProjFileLocation_txt', parent=self.form1, align="right", l="Project File Location:", w=110)
        self.projManagerProjFPath_txtField = cmds.textField('projManagerProjFPath_txtField', parent=self.form1, editable=0, tx="userName/Documents/OpenPipeline/Projects")
        self.projManagerOpenPipelineSetup_btn = cmds.button('projManagerOpenPipelineSetup_btn', parent=self.form1, l="Edit\nLocations...", h=45, c="openPipelineSetup")
        
        self.projManagerEditUsers_btn = cmds.button('projManagerEditUsers_btn', l="Edit Users", parent=self.form1, c="openPipelineProjEditUsers", ann="Add / Remove users to system")
        self.projManagerProjectList_txtScrollList = cmds.textScrollList('projManagerProjectList_txtScrollList', parent=self.form1, sc="openPipelineProjectUISelection", doubleClickCommand="openPipelineProjDialogWindow 1")
        
        #############
        # start sub form
        self.form2 = cmds.formLayout( 'openPipelineProjectManagerGUI_form2', parent=self.form1, numberOfDivisions=100 )
        
        self.projManagerProjNew_btn = cmds.button('projManagerProjNew_btn', parent=self.form2, l="New...", bgc=(.6, .8, .5), c="openPipelineProjDialogWindow 0", ann="") 
        self.projManagerProjRm_btn = cmds.button('projManagerProjRm_btn', parent=self.form2, l="Remove", bgc=(.8, .3, .3), en=0, c="openPipelineRemoveProjectProcess", ann="")
        self.projManagerProjEdit_btn = cmds.button('projManagerProjEdit_btn', parent=self.form2, l="Edit..", bgc=(.5, .7, .7), en=0, c="openPipelineProjDialogWindow 1", ann="")

        #Attach elements to form
        cmds.formLayout(
            self.form2,
            edit=True,
            attachPosition=[
                (self.projManagerProjNew_btn, 'left', 0, 0),
                (self.projManagerProjNew_btn, 'right', 0, 50),
                (self.projManagerProjRm_btn, 'left', 0, 50),
                (self.projManagerProjRm_btn, 'right', 0, 100),
                (self.projManagerProjEdit_btn, 'left', 0, 0),
                (self.projManagerProjEdit_btn, 'right', 0, 100),
                (self.projManagerProjEdit_btn, 'bottom', 0, 100),
            ],
            attachControl=[
                (self.projManagerProjNew_btn, 'bottom', 2, self.projManagerProjEdit_btn),
                (self.projManagerProjRm_btn, 'bottom', 2, self.projManagerProjEdit_btn),
                ]
           )
        
        # end sub form
        #############
        
        self.projManagerProjInfo_txt = cmds.text('projManagerProjInfo_txt', parent=self.form1, l="Project Info", fn="plainLabelFont", al="left")
        self.projManagerProjInfo_scrollField = cmds.scrollField('projManagerProjInfo_scrollField', parent=self.form1, ww=1, editable=0)
        self.projManagerRefresh_btn = cmds.button('projManagerRefresh_btn', parent=self.form1, height=30, l="Refresh List", c="openPipelineProjectUI")
        self.projManagerClose_btn = cmds.button('projManagerClose_btn', parent=self.form1, height=30, l="Close", c="openPipelineCloseProjUI")  
                
        #Attach elements to form
        cmds.formLayout(
            self.form1,
            edit=True,
            attachPosition=[
                (self.projManagerScriptLocation_txtField, 'right', 90, 100),
                (self.projManagerProjFPath_txtField, 'right', 90, 100),
                (self.projManagerProjectList_txtScrollList, 'right', 0, 30),
                (self.projManagerProjInfo_txt, 'right', 2, 100),
                (self.projManagerProjInfo_scrollField, 'right', 5, 100),
                (self.projManagerEditUsers_btn, 'right', 0, 30),
                (self.form2, 'right', 0, 30),
                (self.projManagerRefresh_btn, 'right', 0, 50),
                (self.projManagerClose_btn, 'left', 0, 50),
                (self.projManagerClose_btn, 'right', 5, 100),
                (self.projManagerClose_btn, 'bottom', 5, 100),
                (self.projManagerRefresh_btn, 'bottom', 5, 100),
                (self.projManagerOpenPipelineSetup_btn, 'right', 2, 100),
                (self.projManagerOpenPipelineSetup_btn, 'top', 2, 0),
            ],
            attachForm=[
                (self.projManagerScriptLocation_txt, 'top', 2),
                (self.projManagerScriptLocation_txt, 'left', 2),
                (self.projManagerScriptLocation_txtField, 'top', 2),
                (self.projManagerProjFileLocation_txt, 'left', 2),
                (self.projManagerEditUsers_btn, 'left', 10),
                (self.projManagerProjectList_txtScrollList, 'left', 10),
                (self.form2, 'left', 10),
                (self.projManagerRefresh_btn, 'left', 10),
            ],
            attachControl=[
                (self.projManagerScriptLocation_txtField, 'left', 2, self.projManagerScriptLocation_txt),
                (self.projManagerProjFileLocation_txt, 'top', 2, self.projManagerScriptLocation_txtField),
                (self.projManagerProjFPath_txtField, 'top', 2, self.projManagerScriptLocation_txtField),
                (self.projManagerProjFPath_txtField, 'left', 2, self.projManagerProjFileLocation_txt),
                (self.projManagerOpenPipelineSetup_btn, 'left', 2, self.projManagerScriptLocation_txtField),
                (self.projManagerEditUsers_btn, 'top', 30, self.projManagerProjFileLocation_txt),
                (self.projManagerProjectList_txtScrollList, 'top', 2, self.projManagerEditUsers_btn),
                (self.projManagerProjectList_txtScrollList, 'bottom', 2, self.form2),
                (self.projManagerProjInfo_scrollField, 'top', 30, self.projManagerProjInfo_txt),
                (self.projManagerProjInfo_txt, 'top', 50, self.projManagerProjFileLocation_txt),
                (self.projManagerProjInfo_txt, 'left', 30, self.form2),
                (self.projManagerProjInfo_scrollField, 'top', 2, self.projManagerProjInfo_txt),
                (self.projManagerProjInfo_scrollField, 'left', 30, self.form2),
                (self.form2, 'bottom', 20, self.projManagerRefresh_btn),
                (self.projManagerProjInfo_scrollField, 'bottom', 20, self.projManagerRefresh_btn),
                
            ]
            )
        return [self.form1]