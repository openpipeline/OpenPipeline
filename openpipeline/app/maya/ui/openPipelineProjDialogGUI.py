###########################################
# Name: openPipelineprojDialogGUI (formerly openPipelineprojDialogWindow)
# Description: Opens the Project Dialog Window. This is used either for creating a new project or editing an existing project.
# Input: $mode - 0 for creating a new project, 1 for editing an existing project (int)
# Returns: none
############################################

import maya.cmds as cmds

import window as window

import UIObjects as UIObjects

class openPipelineProjDialogGUI(window.window):

#    def __init__(self, mode):
    def __init__(self):
        
        self.UIObjects = UIObjects.UIObjects()
        
        #self.mode = mode
        self.width=380
        self.height=700
        self.name = "Create New Project"
        self.dockable=0
        
        self.lfMargin = 5
        self.rtMargin = 5
        
        self.projDialogueCreationDate = 'dd/mm/year'
        self.projDialogueDeadline = 'dd/mm/year'
        self.projDialogMasterFilesName = 'master'
        self.projDialogWorkshopFilesName = 'workshop'
        self.projDialogAssetLibrary = 'lib'
        self.projDialogScripts = 'scripts'
        self.projDialogShotLibrary = 'scenes'
        self.projDialogTextures = 'textures'
        self.projDialogRenders = 'renders'
        self.projDialogParticles = 'particles'
        self.projDialogArchive = 'archive'
        self.projDialogDeleted = 'deleted'
    
    def content(self):
        
        self.form1 = cmds.formLayout( 'openPipelineprojDialogGUI_form', numberOfDivisions=100 )
        
        # Project Name Section
        self.projDialogProjName_txt =  cmds.text('ProjDialogProjName_txt', parent=self.form1, fn="boldLabelFont", label="Project  Name (max length: 22):", align="left", width=220)
        self.projDialogProjName_txtField = cmds.textField('projDialogProjName_txtField', parent=self.form1, h=20)
        self.projDialogSeperator1 = cmds.separator(h=5, st="out")
        
        # Project Path Section
        self.projDialogProjPath_txt =  cmds.text('projDialogProjPath_txt', parent=self.form1, fn="boldLabelFont", label="Project Path:", align="left", width=90)
        self.projDialogProjPathParens_txt =  cmds.text('projDialogProjPathParens_txt', parent=self.form1, label="(folders which don't already exist will be created)", align="left", width=250)
        self.projDialogPathField_txtField = cmds.textField('projDialogPathField_txtField', parent=self.form1, h=20)
        self.projDialogPathBrowse_btn = cmds.button('projDialogPathBrowse_btn', parent=self.form1, w=60, l="Browse...", c="fileBrowser \"openPipelineSetprojDialogPath\" \"OK\" \"\" 4")
        self.projDialogSeperator2 = cmds.separator(parent=self.form1, h=5, st="out")
        
        # Description Section
        self.projDialogDescription_txt =  cmds.text('projDialogDescription_txt', parent=self.form1, fn="boldLabelFont", label="Description:", align="left", width=80)
        self.projDialogDescription_txtField = cmds.textField('projDialogDescription_txtField', parent=self.form1, h=20)
        self.projDialogSeperator3 = cmds.separator(parent=self.form1, h=5, st="out")
        
        # Project Status Section
        self.projDialogStatus_txt =  cmds.text('projDialogStatus_txt', parent=self.form1, fn="boldLabelFont", label="Project Status:", align="left", width=100)
        self.projDialogStatus_optMenu = cmds.optionMenu('projDialogStatus_optMenu', parent=self.form1)
        cmds.menuItem(label="active", parent=self.projDialogStatus_optMenu)
        cmds.menuItem(label="inactive", parent=self.projDialogStatus_optMenu)
        self.projDialogStatusParens_txt = cmds.text('projDialogStatusParens_txt', parent=self.form1, fn="smallPlainLabelFont", label="(inactive projects won't appear in main openPipeline window)", align="left", width=340)
        self.projDialogSeperator4 = cmds.separator(parent=self.form1, h=5, st="out")
        
        # Custom Users Section
        self.projDialogueCustomUsers_checkBox = cmds.checkBox('projDialogueCustomUsers_checkBox', parent=self.form1, label="")
        self.projDialogueEnableCustomUsers_txt = cmds.text('projDialogueEnableCustomUsers_txt', parent=self.form1, fn="boldLabelFont", label="Enable Custom Users", align="left", width=320)
        self.projDialogueCustomUsers_txt = cmds.text('projDialogueCustomUsers_txt', parent=self.form1, fn="boldLabelFont", label="Users:", align="left", width=80)
        self.projDialogueCustomUsers_txtField = cmds.textField('projDialogueCustomUsers_txtField', parent=self.form1, enable=0, h=20)
        self.projDialogueCustomUsers_btn = cmds.button('projDialogueCustomUsers_btn', parent=self.form1, l="...")
        self.projDialogSeperator5 = cmds.separator(parent=self.form1, h=5, st="out")
        
        # Creation Date & Deadline Section
        self.projDialogueCreationDate_txt = cmds.text('projDialogueCreationDate_txt', parent=self.form1, fn="boldLabelFont", label="Creation Date:", align="left", width=100)
        self.projDialogueCreationDate_txtField = cmds.textField('projDialogueCreationDate_txtField', text=self.projDialogueCreationDate, parent=self.form1, h=20)
        self.projDialogueDeadline_txt = cmds.text('projDialogueDeadline_txt', parent=self.form1, fn="boldLabelFont", label="Deadline:", align="center", width=70)
        self.projDialogueDeadline_txtField = cmds.textField('projDialogueDeadline_txtField', text=self.projDialogueDeadline, parent=self.form1, h=20)
        self.projDialogSeperator6 = cmds.separator(parent=self.form1, h=5, st="out")
        
        # Master Files Section
        self.projDialogMasterFiles_txt = cmds.text('projDialogMasterFiles_txt', parent=self.form1, fn="boldLabelFont", label="Master Files:", align="left", width=100)
        self.projDialogMasterFilesParens_txt = cmds.text('projDialogMasterFilesParens_txt', parent=self.form1, fn="smallPlainLabelFont", label="(finalized versions with flattened references)", align="left", width=240)
        self.projDialogMasterFilesName_txt = cmds.text('projDialogMasterFilesName_txt', parent=self.form1, fn="smallPlainLabelFont", label="Name:", align="left", width=50)
        self.projDialogMasterFilesName_txtField = cmds.textField('projDialogMasterFilesName_txtField', text=self.projDialogMasterFilesName, parent=self.form1, h=20,)
        self.projDialogMasterFileFormat_txt = cmds.text('projDialogMasterFileFormat_txt', parent=self.form1, fn="smallPlainLabelFont", label="File Format:", align="center")
        self.projDialogMasterFileFormat_optMenu = cmds.optionMenu('projDialogMasterFileFormat_optMenu', parent=self.form1,)
        cmds.menuItem(label="mb", parent=self.projDialogMasterFileFormat_optMenu)
        cmds.menuItem(label="ma", parent=self.projDialogMasterFileFormat_optMenu)
        self.projDialogSeperator7 = cmds.separator(parent=self.form1, h=5, st="out")
        
        # Workshop Files Section
        self.projDialogWorkshopFiles_txt = cmds.text('projDialogWorkshopFiles_txt', parent=self.form1, fn="boldLabelFont", label="Workshop Files:", align="left", width=100)
        self.projDialogWorkshopFilesParens_txt = cmds.text('projDialogWorkshopFilesParens_txt', parent=self.form1, fn="smallPlainLabelFont", label="(preliminary and test versions)", align="left", width=240)
        self.projDialogWorkshopFilesName_txt = cmds.text('projDialogWorkshopFilesName_txt', parent=self.form1, fn="smallPlainLabelFont", label="Name:", align="left", width=50)
        self.projDialogWorkshopFilesName_txtField = cmds.textField('projDialogWorkshopFilesName_txtField', parent=self.form1, text=self.projDialogWorkshopFilesName, h=20,)
        self.projDialogWorkshopFileFormat_txt = cmds.text('projDialogWorkshopFileFormat_txt', parent=self.form1, fn="smallPlainLabelFont", label="File Format:", align="center")
        self.projDialogWorkshopFileFormat_optMenu = cmds.optionMenu('projDialogWorkshopFileFormat_optMenu', parent=self.form1,)
        cmds.menuItem(label="mb", parent=self.projDialogWorkshopFileFormat_optMenu)
        cmds.menuItem(label="ma", parent=self.projDialogWorkshopFileFormat_optMenu)
        self.projDialogSeperator8 = cmds.separator(parent=self.form1, h=5, st="out")
        
        # Sub-Folder Section
        self.projDialogSubFolderNames_txt = cmds.text('projDialogSubFolderNames_txt', parent=self.form1, fn="boldLabelFont", label="Sub-Folder Names:", align="left", width=200)
        self.projDialogAssetLibrary_txt = cmds.text('projDialogAssetLibrary_txt', fn="smallPlainLabelFont", parent=self.form1, label="Asset Library:", align="left", width=70)
        self.projDialogAssetLibrary_txtField = cmds.textField('projDialogAssetLibrary_txtField', parent=self.form1, text=self.projDialogAssetLibrary, h=20)
        self.projDialogScripts_txt = cmds.text('projDialogScripts_txt', parent=self.form1, fn="smallPlainLabelFont", label="Scripts:", align="center", width=50)
        self.projDialogScripts_txtField = cmds.textField('projDialogScripts_txtField', parent=self.form1, text=self.projDialogScripts, h=20)
        
        self.projDialogShotLibrary_txt = cmds.text('projDialogShotLibrary_txt', fn="smallPlainLabelFont", parent=self.form1, label="Shot Library:", align="left", width=70)
        self.projDialogShotLibrary_txtField = cmds.textField('projDialogShotLibrary_txtField', parent=self.form1, text=self.projDialogShotLibrary, h=20)
        self.projDialogTextures_txt = cmds.text('projDialogTextures_txt', parent=self.form1, fn="smallPlainLabelFont", label="Textures:", align="center", width=50)
        self.projDialogTextures_txtField = cmds.textField('projDialogTextures_txtField', parent=self.form1, text=self.projDialogTextures, h=20)
        
        self.projDialogRenders_txt = cmds.text('projDialogRenders_txt', fn="smallPlainLabelFont", parent=self.form1, label="Renders:", align="left", width=70)
        self.projDialogRenders_txtField = cmds.textField('projDialogRenders_txtField', parent=self.form1, text=self.projDialogRenders, h=20)
        self.projDialogParticles_txt = cmds.text('projDialogParticles_txt', parent=self.form1, fn="smallPlainLabelFont", label="Particles:", align="center", width=50)
        self.projDialogParticles_txtField = cmds.textField('projDialogParticles_txtField', parent=self.form1, text=self.projDialogParticles, h=20)
        
        # Archived and Deleted Items
        self.projDialogArchiveDeletedItems_txt = cmds.text('projDialogArchiveDeletedItems_txt', fn="boldLabelFont", label="Archived and Deleted Items Locations:", align="left", width=70)
        self.projDialogArchive_txt = cmds.text('projDialogArchive_txt', fn="smallPlainLabelFont", parent=self.form1, label="Archive:", align="left", width=70)
        self.projDialogArchive_txtField = cmds.textField('projDialogArchive_txtField', parent=self.form1, text=self.projDialogArchive, h=20)
        self.projDialogueArchiveBrowse_btn = cmds.button('projDialogueArchiveBrowse_btn', parent=self.form1, width=70, l="Browse...")
        self.projDialogDeletedItems_txt = cmds.text('projDialogDeletedItems_txt', fn="smallPlainLabelFont", parent=self.form1, label="Deleted Items:", align="left", width=70)
        self.projDialogDeletedItems_txtField = cmds.textField('projDialogDeletedItems_txtField', parent=self.form1, text=self.projDialogDeleted, h=20)
        self.projDialogDeletedItems_btn = cmds.button('projDialogDeletedItems_btn', parent=self.form1, width=70, l="Browse...")
        self.projDialogSeperator9 = cmds.separator(parent=self.form1, h=5, st="out")
        
        # Accept & Cancel Buttons
        self.projDialogAccept_btn = cmds.button('projDialogAccept_btn', parent=self.form1, l="Accept")
        self.projDialogCancel_btn = cmds.button('projDialogCancel_btn', parent=self.form1, l="Cancel")
        
    #Attach elements to form
        cmds.formLayout(
            self.form1,
            edit=True,
            attachPosition=[
                
                # Project Name Section
                (self.projDialogProjName_txt, 'top', 6, 0),
                (self.projDialogProjName_txtField, 'top', 6, 0),
                (self.projDialogProjName_txt, 'left', self.lfMargin, 0),
                (self.projDialogProjName_txtField, 'right', self.rtMargin, 100),
                (self.projDialogSeperator1, 'left', self.lfMargin, 0),
                (self.projDialogSeperator1, 'right', self.rtMargin, 100),
                
                # Project Path Section
                (self.projDialogProjPath_txt, 'left', self.lfMargin, 0),
                (self.projDialogPathField_txtField, 'left', self.lfMargin, 0),
                (self.projDialogPathField_txtField, 'right', 70, 100),
                (self.projDialogPathBrowse_btn, 'right', self.rtMargin, 100),
                (self.projDialogSeperator2, 'left', self.lfMargin, 0),
                (self.projDialogSeperator2, 'right', self.rtMargin, 100),
                
                # Description Section
                (self.projDialogDescription_txt, 'left', self.lfMargin, 0),
                (self.projDialogDescription_txtField, 'right', self.rtMargin, 100),
                (self.projDialogSeperator3, 'left', self.lfMargin, 0),
                (self.projDialogSeperator3, 'right', self.rtMargin, 100),
                
                # Project Status Section
                (self.projDialogStatus_txt, 'left', self.lfMargin, 0),
                (self.projDialogStatusParens_txt, 'left', self.lfMargin, 0),
                (self.projDialogSeperator4, 'left', self.lfMargin, 0),
                (self.projDialogSeperator4, 'right', self.rtMargin, 100),
                
                # Custom Users Section
                (self.projDialogueCustomUsers_checkBox, 'left', self.lfMargin, 0),
                (self.projDialogueCustomUsers_txt, 'left', self.lfMargin, 0),
                (self.projDialogueCustomUsers_txtField, 'right', 50, 100),
                (self.projDialogueCustomUsers_btn, 'right', self.rtMargin, 100),
                (self.projDialogSeperator5, 'left', self.lfMargin, 0),
                (self.projDialogSeperator5, 'right', self.rtMargin, 100),
                
                # Creation Date & Deadline Section
                (self.projDialogueCreationDate_txt, 'left', self.lfMargin, 0),
                (self.projDialogueCreationDate_txtField, 'right', 0, 50),
                (self.projDialogueDeadline_txtField, 'right', self.rtMargin, 100),
                (self.projDialogSeperator6, 'left', self.lfMargin, 0),
                (self.projDialogSeperator6, 'right', self.rtMargin, 100),
                
                # Master Files Section
                (self.projDialogMasterFiles_txt, 'left', self.lfMargin, 0),
                (self.projDialogMasterFilesName_txt, 'left', self.lfMargin, 0),
                (self.projDialogMasterFileFormat_optMenu, 'right', self.rtMargin, 100),
                (self.projDialogSeperator7, 'left', self.lfMargin, 0),
                (self.projDialogSeperator7, 'right', self.rtMargin, 100),
                
                # Workshop Files Section
                (self.projDialogWorkshopFiles_txt, 'left', self.lfMargin, 0),
                (self.projDialogWorkshopFilesName_txt, 'left', self.lfMargin, 0),
                (self.projDialogWorkshopFileFormat_optMenu, 'right', self.rtMargin, 100),
                (self.projDialogSeperator8, 'left', self.lfMargin, 0),
                (self.projDialogSeperator8, 'right', self.rtMargin, 100),
                
                # Sub-Folder Section
                (self.projDialogSubFolderNames_txt, 'left', self.lfMargin, 0),
                (self.projDialogAssetLibrary_txt, 'left', self.lfMargin, 0),
                (self.projDialogAssetLibrary_txtField, 'right', 0, 50),
                (self.projDialogScripts_txtField, 'right', self.rtMargin, 100),
                
                (self.projDialogShotLibrary_txt, 'left', self.lfMargin, 0),
                (self.projDialogShotLibrary_txtField, 'right', 0, 50),
                (self.projDialogTextures_txtField, 'right', self.rtMargin, 100),
                
                (self.projDialogRenders_txt, 'left', self.lfMargin, 0),
                (self.projDialogRenders_txtField, 'right', 0, 50),
                (self.projDialogParticles_txtField, 'right', self.rtMargin, 100),
                
                # Archived and Deleted Items
                (self.projDialogArchiveDeletedItems_txt, 'left', self.lfMargin, 0),
                (self.projDialogArchive_txt, 'left', self.lfMargin, 0),
                (self.projDialogueArchiveBrowse_btn, 'right', self.rtMargin, 100),
                (self.projDialogDeletedItems_txt, 'left', self.lfMargin, 0),
                (self.projDialogDeletedItems_btn, 'right', self.rtMargin, 100),
                (self.projDialogSeperator9, 'left', self.lfMargin, 0),
                (self.projDialogSeperator9, 'right', self.rtMargin, 100),
                
                # Accept & Cancel Buttons
                (self.projDialogAccept_btn, 'left', self.lfMargin, 0),
                (self.projDialogAccept_btn, 'right', 0, 50),
                (self.projDialogCancel_btn, 'right', self.rtMargin, 100),
                (self.projDialogCancel_btn, 'left', 0, 50),
                (self.projDialogAccept_btn, 'bottom', 2, 100),
                (self.projDialogCancel_btn, 'bottom', 2, 100),
                
            ],
            attachForm=[
            ],
            attachControl=[
                
                # Project Name Section
                (self.projDialogProjName_txtField, 'left', 2, self.projDialogProjName_txt),
                (self.projDialogSeperator1, 'top', 6, self.projDialogProjName_txtField),
                
                # Project Path Section
                (self.projDialogProjPath_txt, 'top', 5, self.projDialogSeperator1),
                (self.projDialogProjPathParens_txt, 'top', 5, self.projDialogSeperator1),
                (self.projDialogProjPathParens_txt, 'left', 6, self.projDialogProjPath_txt),
                (self.projDialogPathField_txtField, 'top', 6, self.projDialogProjPath_txt),
                (self.projDialogPathBrowse_btn, 'top', 6, self.projDialogProjPath_txt),
                (self.projDialogPathBrowse_btn, 'left', 2, self.projDialogPathField_txtField),
                (self.projDialogSeperator2, 'top', 6, self.projDialogPathField_txtField),
                
                # Description Section
                (self.projDialogDescription_txt, 'top', 6, self.projDialogSeperator2),
                (self.projDialogDescription_txtField, 'top', 6, self.projDialogSeperator2),
                (self.projDialogDescription_txtField, 'left', 6, self.projDialogDescription_txt),
                (self.projDialogSeperator3, 'top', 6, self.projDialogDescription_txtField),
                
                # Project Status Section
                (self.projDialogStatus_txt, 'top', 6, self.projDialogSeperator3),
                (self.projDialogStatus_optMenu, 'top', 6, self.projDialogSeperator3),
                (self.projDialogStatus_optMenu, 'left', 2, self.projDialogStatus_txt),
                (self.projDialogStatusParens_txt, 'top', 6, self.projDialogStatus_txt),
                (self.projDialogSeperator4, 'top', 6, self.projDialogStatusParens_txt),
                
                # Custom Users Section
                (self.projDialogueCustomUsers_checkBox, 'top', 6, self.projDialogSeperator4),
                (self.projDialogueEnableCustomUsers_txt, 'top', 6, self.projDialogSeperator4),
                (self.projDialogueEnableCustomUsers_txt, 'left', 6, self.projDialogueCustomUsers_checkBox),
                (self.projDialogueCustomUsers_txt, 'top', 6, self.projDialogueEnableCustomUsers_txt),
                (self.projDialogueCustomUsers_txtField, 'left', 6, self.projDialogueCustomUsers_txt),
                (self.projDialogueCustomUsers_txtField, 'top', 6, self.projDialogueEnableCustomUsers_txt),
                (self.projDialogueCustomUsers_btn, 'top', 6, self.projDialogueEnableCustomUsers_txt),
                (self.projDialogueCustomUsers_btn, 'left', 6, self.projDialogueCustomUsers_txtField),
                (self.projDialogSeperator5, 'top', 6, self.projDialogueCustomUsers_btn),
                
                # Creation Date & Deadline Section
                (self.projDialogueCreationDate_txt, 'top', 6, self.projDialogSeperator5),
                (self.projDialogueCreationDate_txtField, 'top', 6, self.projDialogSeperator5),
                (self.projDialogueCreationDate_txtField, 'left', 6, self.projDialogueCreationDate_txt),
                (self.projDialogueDeadline_txt, 'top', 6, self.projDialogSeperator5),
                (self.projDialogueDeadline_txt, 'left', 6, self.projDialogueCreationDate_txtField),
                (self.projDialogueDeadline_txtField, 'top', 6, self.projDialogSeperator5),
                (self.projDialogueDeadline_txtField, 'left', 6, self.projDialogueDeadline_txt),
                (self.projDialogSeperator6, 'top', 6, self.projDialogueDeadline_txtField),
                
                # Master Files Section
                (self.projDialogMasterFiles_txt, 'top', 6, self.projDialogSeperator6),
                (self.projDialogMasterFilesParens_txt, 'top', 6, self.projDialogSeperator6),
                (self.projDialogMasterFilesParens_txt, 'left', 6, self.projDialogMasterFiles_txt),
                (self.projDialogMasterFilesName_txt, 'top', 10, self.projDialogMasterFiles_txt),
                (self.projDialogMasterFilesName_txtField, 'top', 10, self.projDialogMasterFiles_txt),
                (self.projDialogMasterFilesName_txtField, 'left', 6, self.projDialogMasterFilesName_txt),
                (self.projDialogMasterFilesName_txtField, 'right', 6, self.projDialogMasterFileFormat_txt),
                (self.projDialogMasterFileFormat_txt, 'top', 10, self.projDialogMasterFiles_txt),
                (self.projDialogMasterFileFormat_txt, 'right', 6, self.projDialogMasterFileFormat_optMenu),
                (self.projDialogMasterFileFormat_optMenu, 'top', 10, self.projDialogMasterFiles_txt),
                (self.projDialogSeperator7, 'top', 6, self.projDialogMasterFilesName_txtField),
                
                # Workshop Files Section
                (self.projDialogWorkshopFiles_txt, 'top', 6, self.projDialogSeperator7),
                (self.projDialogWorkshopFilesParens_txt, 'top', 6, self.projDialogSeperator7),
                (self.projDialogWorkshopFilesParens_txt, 'left', 6, self.projDialogWorkshopFiles_txt),
                (self.projDialogWorkshopFilesName_txt, 'top', 10, self.projDialogWorkshopFiles_txt),
                (self.projDialogWorkshopFilesName_txtField, 'top', 10, self.projDialogWorkshopFiles_txt),
                (self.projDialogWorkshopFilesName_txtField, 'left', 6, self.projDialogWorkshopFilesName_txt),
                (self.projDialogWorkshopFilesName_txtField, 'right', 6, self.projDialogWorkshopFileFormat_txt),
                (self.projDialogWorkshopFileFormat_txt, 'top', 10, self.projDialogWorkshopFiles_txt),
                (self.projDialogWorkshopFileFormat_txt, 'right', 10, self.projDialogWorkshopFileFormat_optMenu),
                (self.projDialogWorkshopFileFormat_optMenu, 'top', 10, self.projDialogWorkshopFiles_txt),
                (self.projDialogSeperator8, 'top', 6, self.projDialogWorkshopFilesName_txtField),
                
                # Sub-Folder Section
                (self.projDialogSubFolderNames_txt, 'top', 6, self.projDialogSeperator8),
                (self.projDialogAssetLibrary_txt, 'top', 10, self.projDialogSubFolderNames_txt),
                (self.projDialogAssetLibrary_txtField, 'left', 6, self.projDialogAssetLibrary_txt),
                (self.projDialogAssetLibrary_txtField, 'top', 10, self.projDialogSubFolderNames_txt),
                (self.projDialogScripts_txt, 'top', 10, self.projDialogSubFolderNames_txt),
                (self.projDialogScripts_txt, 'left', 6, self.projDialogAssetLibrary_txtField),
                (self.projDialogScripts_txtField, 'top', 10, self.projDialogSubFolderNames_txt),
                (self.projDialogScripts_txtField, 'left', 6, self.projDialogScripts_txt),
                
                (self.projDialogShotLibrary_txt, 'top', 6, self.projDialogAssetLibrary_txtField),
                (self.projDialogShotLibrary_txtField, 'left', 6, self.projDialogShotLibrary_txt),
                (self.projDialogShotLibrary_txtField, 'top', 6, self.projDialogAssetLibrary_txtField),
                (self.projDialogTextures_txt, 'top', 6, self.projDialogAssetLibrary_txtField),
                (self.projDialogTextures_txt, 'left', 6, self.projDialogShotLibrary_txtField),
                (self.projDialogTextures_txtField, 'top', 6, self.projDialogAssetLibrary_txtField),
                (self.projDialogTextures_txtField, 'left', 6, self.projDialogTextures_txt),
                
                (self.projDialogRenders_txt, 'top', 6, self.projDialogShotLibrary_txtField),
                (self.projDialogRenders_txtField, 'left', 6, self.projDialogRenders_txt),
                (self.projDialogRenders_txtField, 'top', 6, self.projDialogShotLibrary_txtField),
                (self.projDialogParticles_txt, 'top', 6, self.projDialogShotLibrary_txtField),
                (self.projDialogParticles_txt, 'left', 6, self.projDialogRenders_txtField),
                (self.projDialogParticles_txtField, 'top', 6, self.projDialogShotLibrary_txtField),
                (self.projDialogParticles_txtField, 'left', 6, self.projDialogParticles_txt),
                
                # Archived and Deleted Items
                (self.projDialogArchiveDeletedItems_txt, 'top', 10, self.projDialogRenders_txtField),
                (self.projDialogArchive_txt, 'top', 10, self.projDialogArchiveDeletedItems_txt),
                (self.projDialogArchive_txtField, 'top', 10, self.projDialogArchiveDeletedItems_txt),
                (self.projDialogArchive_txtField, 'left', 10, self.projDialogArchive_txt),
                (self.projDialogArchive_txtField, 'right', 10, self.projDialogueArchiveBrowse_btn),
                (self.projDialogueArchiveBrowse_btn, 'top', 10, self.projDialogArchiveDeletedItems_txt),
                (self.projDialogDeletedItems_txt, 'top', 10, self.projDialogArchive_txtField),
                (self.projDialogDeletedItems_txtField, 'top', 10, self.projDialogArchive_txtField),
                (self.projDialogDeletedItems_txtField, 'left', 10, self.projDialogDeletedItems_txt),
                (self.projDialogDeletedItems_txtField, 'right', 10, self.projDialogDeletedItems_btn),
                (self.projDialogDeletedItems_btn, 'top', 10, self.projDialogArchive_txtField),
                (self.projDialogSeperator9, 'top', 10, self.projDialogDeletedItems_txtField),
                
                # Accept & Cancel Buttons
                (self.projDialogAccept_btn, 'top', 10, self.projDialogSeperator9),
                (self.projDialogCancel_btn, 'top', 10, self.projDialogSeperator9),
        
            ]
            )
        return [self.form1]