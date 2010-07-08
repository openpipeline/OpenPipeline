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

class openPipelineMainUI(window.window):

    def __init__(self):
        
        self.UIObjects = UIObjects.UIObjects()
        
        self.width=450
        self.height=780
        self.prettyName = "OpenPipeline 2.0"
        self.name = "openPipelineUI"
        self.dockable=1
        self.scriptLocation = "userName/Documents/OpenPipeline"
        
        self.lfMargin = 5
        self.rtMargin = 5
        
        self.op_icon_filePath='\\\\venkman\KICKSTAND\DEV\openPipeline\openPipeline\\app\maya\ui\openPipelineIcon.jpg'
        self.op_currOpenPreview_filePath='\\\\venkman\KICKSTAND\DEV\openPipeline\openPipeline\\app\maya\ui\\noPreview.jpg'
        self.op_defaultPreview_filePath='\\\\venkman\KICKSTAND\DEV\openPipeline\openPipeline\\app\maya\ui\\defaultPreview.jpg'
        
        
        self.anno_projectList="Select from the available Projects."
        self.anno_projectManager="Open the Project Manager, where you can add or remove Projects."
        self.anno_saveWorkshop="Save a workshop file for the current Asset/Shot/Component."
        self.anno_master="Save a master file for the current Asset/Shot/Component."
        self.anno_revive="Revive an old version of the current Asset/Shot/Component."
        self.anno_closeFile="Close the currently open file."
        self.anno_assetTypeList="Choose an Asset Type."
        self.anno_newAssetType="Create a new Asset Type"
        self.anno_removeAssetType="Remove the selected Asset Type(s) from the inventory."
        self.anno_removeAsset="Remove the selected Asset from the inventory."
        self.anno_editAsset="Open the Asset for editing."
        self.anno_viewAsset="Open the master file for the Asset."
        self.anno_importAssetWorkshop="Import the Asset's latest workshop file into the current scene."
        self.anno_importAssetMaster="Import the Asset's master file into the current scene."
        self.anno_referenceAssetWorkshop="Reference the Asset's latest workshop file into the current scene."
        self.anno_referenceAssetMaster="Reference the Asset's master file into the current scene."
        self.anno_assetList="Double-click to edit Asset. Hold right mouse button for more options."
        self.anno_renameAsset="Rename the selected Asset."
        self.anno_editComponent="Open the Component for editing."
        self.anno_viewComponent="Open the master file for the Component."
        self.anno_importComponentWorkshop="Import the Component's latest workshop file into the current scene."
        self.anno_importComponentMaster="Import the Component's master file into the current scene."
        self.anno_referenceComponentWorkshop="Reference the Component's latest workshop file into the current scene."
        self.anno_referenceComponentMaster="Reference the Component's master file into the current scene."
        self.anno_componentList="Double-click to edit Component. Hold down right mouse button for more options."
        self.anno_newComponent="Create a new Component for the selected Asset."
        self.anno_removeComponent="Remove the selected Component from the inventory."
        self.anno_close="Close openPipeline."
        self.anno_sequenceList="Choose a Sequence."
        self.anno_newSequence="Create a new Sequence"
        self.anno_removeSequence="Remove the selected Sequence from the inventory."
        self.anno_editShotComponent="Open the Component for editing."
        self.anno_viewShot="Open the master file for the Shot."
        self.anno_importShotWorkshop="Import the Shot's latest workshop file into the current scene."
        self.anno_editShot="Open the Shot for editing."
        self.anno_importShotMaster="Import the Shot's master file into the current scene."
        self.anno_referenceShotWorkshop="Reference the Shot's latest workshop file into the current scene."
        self.anno_referenceShotMaster="Reference the Shot's master file into the current scene."
        self.anno_shotList="Double-click to Edit Shot. Hold down right mouse button for more options."
        self.anno_newShot="Create a new Shot."
        self.anno_removeShot="Remove the selected Shot."
        self.anno_viewShotComponent="Open the master file for the Component."
        self.anno_importShotComponentWorkshop="Import the Component's latest workshop file into the current scene."
        self.anno_importShotComponentMaster="Import the Component's master file into the current scene."
        self.anno_referenceShotComponentWorkshop="Reference the Component's latest workshop file into the current scene."
        self.anno_referenceShotComponentMaster="Reference the Component's master file into the current scene."
        self.anno_shotComponentList="Double-click to edit Component. Hold down right mouse button for more options."
        self.anno_newShotComponent="Create a new Component for the selected Asset."
        self.anno_removeShotComponent="Remove the selected Component from the inventory."
    
    def content(self):
        
        #--------------------------------------------
        #   START Main Form
        #--------------------------------------------
        
        self.op_form1 = cmds.formLayout( numberOfDivisions=100 )
        
        #--------------------------------------------
        #   START Drop Down Menu at the Top of the Window
        #--------------------------------------------
        
        self.op_topDropDown_menuBarLayout = cmds.menuBarLayout('op_topDropDown_menuBarLayout', parent=self.op_form1)
        
        # menus (more can go here)
        
        self.op_topDropDownMayaTools_menu = cmds.menu('op_topDropDownMayaTools_menu', parent=self.op_topDropDown_menuBarLayout, label="Maya Tools")
        self.op_topDropDownMayaTools_menuItem1 = cmds.menuItem('op_topDropDownMayaTools_menuItem1', parent=self.op_topDropDownMayaTools_menu, label="Maya Reference Editor", command="ReferenceEditor")
        self.op_topDropDownMayaTools_menuItem2 = cmds.menuItem('op_topDropDownMayaTools_menuItem2', parent=self.op_topDropDownMayaTools_menu, label="Maya Project Manager", command="projectSetup 2")
        
        self.op_topDropDownAddOns_menu = cmds.menu(label="Add-ons", parent=self.op_topDropDown_menuBarLayout)
        
        #--------------------------------------------
        #   START old MEL from openPipeline0.9.1
        #--------------------------------------------
        
        #        for (self.item in self.addons)
        #        {
        #                int self.length = size(self.item);
        #                self.length-=4;
        #                string self.command = `startString self.item self.length`;
        #                menuItem -label self.command -command self.command;
        #        }
        #        
        #        for (self.item in self.pyAddons)
        #        {
        #                int self.length = size(self.item);
        #                self.length-=3;
        #                string self.pyModule = `startString self.item self.length`;
        #                string self.pyCommand = self.pyModule + "." + self.pyModule + "()";
        #                string self.command = "eval(python(\"" + self.pyCommand + "\"))";
        #                menuItem -label self.pyModule -command self.command;
        #        }
        
        #--------------------------------------------
        #   END old MEL from openPipeline0.9.1
        #--------------------------------------------
        
        self.op_topDropDownAddOns_menuItem2 = cmds.menuItem('op_topDropDownAddOns_menuItem2', parent=self.op_topDropDownAddOns_menu, label="How to add to this menu...", c='openPipelineAddonsDialog')
        
        self.op_topDropDownHelp_menu = cmds.menu(label="Help", parent=self.op_topDropDown_menuBarLayout, helpMenu=1)
        self.op_topDropDown_menuItem1 = cmds.menuItem('op_topDropDown_menuItem1', parent=self.op_topDropDownHelp_menu, label="About openPipeline...", command="openPipelineAboutDialog")
        self.op_topDropDown_menuItem2 = cmds.menuItem('op_topDropDown_menuItem2', parent=self.op_topDropDownHelp_menu, label="Help...", command="openPipelineHelpLaunch")
      
        
        #--------------------------------------------
        #   END Drop Down Menu at the Top of the Window
        #
        #   START Section 1.00 - Basic Info
        #   Below the Drop Down Menu on the top of UI
        #   includes Login User, Proj Name, Proj Path
        #
        #   START Section 1.01 - Login User
        #--------------------------------------------
        
        self.op_userName_txt = cmds.text('op_userName_txt', parent=self.op_form1, al="right", label="User Name : ", w=150)
        
        #--------------------------------------------
        #   START old MEL from openPipeline0.9.1
        #--------------------------------------------
        
        #self.op_userName_txt = string self.currProjName = `optionVar -q "op_currProjectName"`;
        #string self.currProjXml = openPipelineGetSingleProjectXml(self.currProjName);
        #int self.currUserNameMode = openPipelineGetXmlData(self.currProjXml,"userMode");
        
        #--------------------------------------------
        #   END old MEL from openPipeline0.9.1
        #--------------------------------------------
        
        self.op_userName_optionMenu = cmds.optionMenu('op_userName_optionMenu', parent=self.op_form1, cc="openPipelineUpdateUser", enable=0)
        
        #--------------------------------------------
        #   END Section 1.01 - Login User
        #
        #   START Section 1.02 - Proj Name
        #--------------------------------------------
        
        self.op_projName_txt = cmds.text('op_projName_txt', parent=self.op_form1, al="right", label="Project Name : ", w=150)
        
        self.op_projManager_btn = cmds.button('op_projManager_btn', parent=self.op_form1, label="Project Manager...", c="openPipelineProjectUI", ann=self.anno_projectManager, h=30)
        
        self.op_projName_optionMenu = cmds.optionMenu('op_projName_optionMenu', parent=self.op_form1, cc="openPipelineProjSelected 1", ann=self.anno_projectList)

        #--------------------------------------------
        #   START old MEL from openPipeline0.9.1
        #--------------------------------------------
        
        #int self.numProjects = size(self.validProjList);
        #string self.currProjName = `optionVar -q "op_currProjectName"`;
        #for(self.i=0; self.i<self.numProjects; self.i++)
        #{
        #        string self.temp_projName = openPipelineGetXmlData(self.validProjList[self.i],"name");
        #        string self.temp_projPath = openPipelineGetXmlData(self.validProjList[self.i],"path");
        #        if (`filetest -d self.temp_projPath`)
        #        {
        #                menuItem -label self.temp_projName;
        #                if (self.currProjName==self.temp_projName)
        #                                optionMenu -e -v self.temp_projName op_projNameMenu;
        #        }
        #}
        
        #--------------------------------------------
        #   END from openPipeline0.9.1
        #
        #   END Section 1.02 - Proj Name
        #
        #   START Section 1.03 - Proj Path
        #--------------------------------------------
        
        self.op_projPath_txt = cmds.text('op_projPath_txt', parent=self.op_form1, al="right", label="Project Path : ", w=150)
        self.op_projPath_txtField = cmds.textField('op_projPath_txtField', parent=self.op_form1, editable=0)
        
        #--------------------------------------------
        #   END Section 1.03 - Proj Path
        #
        #   START Section 1.04 - Project Image
        #--------------------------------------------
        
        self.op_icon_image = cmds.image('op_icon_image', parent=self.op_form1, i=self.op_icon_filePath, h=50, w=415, bgc=(0, 0, 0))
        
        #--------------------------------------------
        #   END Section 1.04 - Project Image
        #
        #   END Section 1.00 - Basic Info
        #
        #   START - Main Tab Layout
        #   Tab layout for switching between
        #   Currently Open, Asset and Shots Inventory
        #--------------------------------------------
        
        #self.op_mainTabs_tabLayout = cmds.tabLayout('op_mainTabs_tabLayout', parent=self.op_form1, scr=0, innerMarginWidth=0, innerMarginHeight=0, sc="openPipelineUpdateWorkingTab")

        self.op_mainTabs_tabLayout = cmds.tabLayout('op_mainTabs_tabLayout', parent=self.op_form1, scr=0, innerMarginWidth=0, innerMarginHeight=0)
        
        #--------------------------------------------
        #   START Section 2.00 - "Currently Open" Tab
        #   This is the first section that will be attached to the tab layout
        #--------------------------------------------
        
        self.op_currOpen_formLayout = cmds.formLayout('op_currOpen_formLayout', parent=self.op_mainTabs_tabLayout, width=410, numberOfDivisions=100)
        
        self.op_currOpenSeperator01 = cmds.separator('op_currOpenSeperator01', parent=self.op_currOpen_formLayout, style="double", w=410)
        self.op_currOpenTitle_txt = cmds.text('op_currOpenTitle_txt', fn="boldLabelFont", parent=self.op_currOpen_formLayout, w=400, label="CURRENTLY OPEN:", al="left")
        self.op_currOpenHeading_txt = cmds.text('op_currOpenHeading_txt', fn="smallBoldLabelFont", w=290, label=" ", al="left")
        
        self.op_currOpenHeadingVersion_txt = cmds.text('op_currOpenHeadingVersion_txt', parent=self.op_currOpen_formLayout, fn="smallBoldLabelFont", w=370, label=" ", al="left")
        
        self.op_currOpenSeperator03 = cmds.separator('op_currOpenSeperator03', parent=self.op_currOpen_formLayout, style="double", w=410)
        self.op_currOpenActions_txt = cmds.text('op_currOpenActions_txt', parent=self.op_currOpen_formLayout, fn="smallBoldLabelFont", label="Actions", w=100, al="left")
        
        self.op_currOpenSaveWorkshop_btn = cmds.button('op_currOpenSaveWorkshop_btn', parent=self.op_currOpen_formLayout, l="Save Workshop...", w=164, bgc=(.8, .6, .5), c="openPipelineSaveWorkshopGUI", ann=self.anno_saveWorkshop)
        self.op_currOpenMaster_btn = cmds.button('op_currOpenMaster_btn', parent=self.op_currOpen_formLayout, l="MASTER...", w=164, bgc=(.9, .7, .4), c="openPipelineSaveMasterFileGUI", ann=self.anno_master)
        self.op_currOpenRevive_btn = cmds.button('op_currOpenRevive_btn', parent=self.op_currOpen_formLayout, l="Revive...", bgc=(.5, .7, .7), w=82, c="openPipelineReviveGUI", ann=self.anno_revive)
        self.op_currOpenClose_btn = cmds.button('op_currOpenClose_btn', parent=self.op_currOpen_formLayout, l="Close", bgc=(.8, .8, .8), c="openPipelineCloseCurrent", ann=self.anno_closeFile)
        
        self.op_currOpenHistory_txt = cmds.text('op_currOpenHistory_txt', parent=self.op_currOpen_formLayout, fn="smallBoldLabelFont", label="History", w=180, al="left")
        self.op_currOpenAssetNote_scrollField = cmds.scrollField('op_currOpenAssetNote_scrollField', parent=self.op_currOpen_formLayout, w=220, h=103, enable=1, editable=0, wordWrap=1, font="smallPlainLabelFont", text="")
        
        self.op_currOpenPreview_txt = cmds.text('op_currOpenPreview_txt', parent=self.op_currOpen_formLayout, fn="smallBoldLabelFont", l="Preview", w=164, al="left")
        
        #--------------------------------------------
        #   START from openPipeline0.9.1
        #--------------------------------------------
        
        #self.op_currOpenPreview_img = `image -h 105 -w 164 -i (self.openPipeline_scriptPath+"openPipeline/"+self.openPipeline_defaultPreviewFilename) -bgc 0 0 0 op_currPreviewImage`;
        
        #--------------------------------------------
        #   END from openPipeline0.9.1
        #--------------------------------------------

        self.op_currOpenPreview_img = cmds.image('op_currOpenPreview_img', parent=self.op_currOpen_formLayout, i=self.op_currOpenPreview_filePath, h=105, w=164, bgc=(0, 0, 0))
        self.op_currOpenSnapshot_btn = cmds.button('op_currOpenSnapshot_btn', parent=self.op_currOpen_formLayout, l="Take Snapshot", w=164, c="openPipelineTakeSnapshot")
        
        self.op_currOpenRecordPlayblast_btn = cmds.button('op_currOpenRecordPlayblast_btn', parent=self.op_currOpen_formLayout, w=82, h=20, l="Rec Playblast", c="openPipelineRecordCurrentPlayblast")
        self.op_currOpenViewPlayblast_btn = cmds.button('op_currOpenViewPlayblast_btn', parent=self.op_currOpen_formLayout, w=82, h=20, l="View Playblast", c="openPipelineViewPlayblastCurrent")
        
        self.op_currOpenNotes_txt = cmds.text('op_currOpenNotes_txt', parent=self.op_currOpen_formLayout, fn="smallBoldLabelFont", l="Notes", w=220, al="left")
        self.op_currOpen_scrollField = cmds.scrollField('op_currOpen_scrollField', parent=self.op_currOpen_formLayout, w=220, h=125, enable=1, editable=0, wordWrap=1, font="smallPlainLabelFont", text="", kpc="button -e -en 1 op_saveNoteButton")
        
        #--------------------------------------------
        #   START Section 2.01 - Subform01
        #--------------------------------------------
        
        self.op_currOpenSubRegion1_formLayout = cmds.formLayout('op_currOpenSubRegion1_formLayout', parent=self.op_currOpen_formLayout, numberOfDivisions=100)
        
        self.op_currOpenClearNote_btn = cmds.button('op_currOpenClearNote_btn', parent=self.op_currOpenSubRegion1_formLayout, w=110, h=20, l="Clear", c="openPipelineClearNote")
        self.op_currOpenSaveNote_btn = cmds.button('op_currOpenSaveNote_btn', parent=self.op_currOpenSubRegion1_formLayout, w=110, h=20, l="Save", c="openPipelineSaveNote", en=0)
        
        cmds.formLayout(self.op_currOpenSubRegion1_formLayout,
            e=1,
            attachPosition=[
            (self.op_currOpenSaveNote_btn, "right", 0, 100),
            (self.op_currOpenSaveNote_btn, "left", 0, 50),
            (self.op_currOpenClearNote_btn, "left", 0, 0),
            (self.op_currOpenClearNote_btn, "right", 0, 50),
            ]
            )
        
        #--------------------------------------------
        #   END Section 2.01 - Subform01
        #--------------------------------------------
        
        self.op_currOpenLocation_txt = cmds.text('op_currOpenLocation_txt', parent=self.op_currOpen_formLayout, fn="smallBoldLabelFont", l="Location", w=395, al="center")
        self.op_currOpenLocation_txtField = cmds.textField('op_currOpenLocation_txtField', parent=self.op_currOpen_formLayout, editable=0, w=345)
        self.op_currOpenExplore_btn = cmds.button('op_currOpenExplore_btn', parent=self.op_currOpen_formLayout, w=50, align="center", label="explore...", c="openPipelineExploreCurrent")
        
        #--------------------------------------------
        #   START Attach elements to op_currOpen_formLayout
        #--------------------------------------------
        
        cmds.formLayout(self.op_currOpen_formLayout,
            edit=1,
            attachPosition=[
                
                (self.op_currOpenSeperator01, "right", 0, 100),
                (self.op_currOpenSeperator03, "right", 0, 100),
                
                (self.op_currOpenAssetNote_scrollField, "right", 0, 100),
                (self.op_currOpen_scrollField, "right", 0, 100),
                (self.op_currOpenExplore_btn, "right", 0, 100),
                (self.op_currOpenExplore_btn, "left", 0, 80),
                
                (self.op_currOpenSubRegion1_formLayout, "right", 0, 100),
                
                ],
            attachForm=[
                
                (self.op_currOpenSeperator01, "top", 5),
                
                (self.op_currOpenSeperator01, "right", 10),
                (self.op_currOpenSeperator01, "left", 0),
                (self.op_currOpenHeadingVersion_txt, "right", 10),
                (self.op_currOpenHeadingVersion_txt, "left", 0),
                (self.op_currOpenSeperator03, "right", 10),
                (self.op_currOpenSeperator03, "left", 0),
                
                (self.op_currOpenLocation_txt, "right", 10),
                (self.op_currOpenLocation_txt, "left", 10),
                
                (self.op_currOpenLocation_txtField, "left", 0),
                
            ],
            attachControl=[
                
                (self.op_currOpenTitle_txt, "top", 5, self.op_currOpenSeperator01),
                (self.op_currOpenHeading_txt, "top", 5, self.op_currOpenTitle_txt),
                (self.op_currOpenHeadingVersion_txt, "top", 5, self.op_currOpenHeading_txt),
                (self.op_currOpenSeperator03, "top", 5,self.op_currOpenHeadingVersion_txt),
            
                (self.op_currOpenActions_txt, "top", 5, self.op_currOpenSeperator03),
                (self.op_currOpenSaveWorkshop_btn, "top", 5, self.op_currOpenActions_txt),
                (self.op_currOpenMaster_btn, "top", 5, self.op_currOpenSaveWorkshop_btn),
                (self.op_currOpenMaster_btn, "top", 5, self.op_currOpenSaveWorkshop_btn),
                (self.op_currOpenRevive_btn, "top", 5, self.op_currOpenMaster_btn),
                (self.op_currOpenClose_btn, "left", 5, self.op_currOpenRevive_btn),
                (self.op_currOpenClose_btn, "right", 20, self.op_currOpenAssetNote_scrollField),
                (self.op_currOpenClose_btn, "top", 5, self.op_currOpenMaster_btn),
                
                (self.op_currOpenHistory_txt, "top", 5, self.op_currOpenSeperator03),
                (self.op_currOpenHistory_txt, "left", 20, self.op_currOpenSaveWorkshop_btn),
                (self.op_currOpenAssetNote_scrollField, "left", 20,self.op_currOpenMaster_btn),
                (self.op_currOpenAssetNote_scrollField, "top", 5, self.op_currOpenHistory_txt),
                
                (self.op_currOpenPreview_txt, "top", 5, self.op_currOpenAssetNote_scrollField),
                (self.op_currOpenPreview_img, "top", 5, self.op_currOpenPreview_txt),
                (self.op_currOpenSnapshot_btn, "top", 0, self.op_currOpenPreview_img),
                (self.op_currOpenRecordPlayblast_btn, "top", 0, self.op_currOpenSnapshot_btn),
                (self.op_currOpenViewPlayblast_btn, "top", 0, self.op_currOpenSnapshot_btn),
                (self.op_currOpenViewPlayblast_btn, "right", 20, self.op_currOpenAssetNote_scrollField),
                (self.op_currOpenViewPlayblast_btn, "left", 5, self.op_currOpenRecordPlayblast_btn),
                
                (self.op_currOpenNotes_txt, "top", 5, self.op_currOpenAssetNote_scrollField),
                (self.op_currOpenNotes_txt, "left", 20, self.op_currOpenPreview_txt),
                (self.op_currOpen_scrollField, "top", 5, self.op_currOpenPreview_txt),
                (self.op_currOpen_scrollField, "left", 20, self.op_currOpenPreview_img),
                
                (self.op_currOpenLocation_txt, "top", 5, self.op_currOpenViewPlayblast_btn),
                (self.op_currOpenLocation_txtField, "top", 5, self.op_currOpenLocation_txt),
                (self.op_currOpenLocation_txtField, "right", 5, self.op_currOpenExplore_btn),
                (self.op_currOpenExplore_btn, "top", 5, self.op_currOpenLocation_txt),

                (self.op_currOpenSubRegion1_formLayout, "top", 0, self.op_currOpen_scrollField),
                (self.op_currOpenSubRegion1_formLayout, "left", 20, self.op_currOpenViewPlayblast_btn),
                
            ],
            )
        
        #--------------------------------------------
        #   END Attach elements to op_currOpen_formLayout
        #
        #   END Section 2.00 - "Currently Open" Tab
        #
        #   START Section 3.00 - "Asset Inventory" Tab
        #   this is the second section that will be attached to the tab layout
        #--------------------------------------------
        
        self.op_assetBrowser_formLayout = cmds.formLayout('op_assetBrowser_formLayout', parent=self.op_mainTabs_tabLayout, width=410, numberOfDivisions=100)
        
        self.op_assetSeperator01 = cmds.separator('op_assetSeperator01', parent=self.op_assetBrowser_formLayout, style="double", w=410)
        self.op_assetAssetBrowser_txt = cmds.text('op_assetAssetBrowser_txt', parent=self.op_assetBrowser_formLayout, fn="boldLabelFont", label="ASSET BROWSER", w=410, al="left")
        self.op_assetSeperator02 = cmds.separator('op_assetSeperator02', parent=self.op_assetBrowser_formLayout, style="double", w=410)
        
        #--------------------------------------------
        #   START Section 3.01 - "Asset Types"
        #   Left Column in the "Assets" Tab
        #--------------------------------------------
        self.op_shotSequence_formLayout = cmds.formLayout('op_shotSequence_formLayout', parent=self.op_assetBrowser_formLayout, numberOfDivisions=100)

        self.op_assetAssetTypes_txt = cmds.text('op_assetAssetTypes_txt', parent=self.op_shotSequence_formLayout, l="Asset Types", w=125, fn="smallBoldLabelFont", al="left")
        self.op_assetType_txtScrollList = cmds.textScrollList('op_assetType_txtScrollList', parent=self.op_shotSequence_formLayout, h=119, ams=0, sc="openPipelineUpdateAssetList 0", fn="smallPlainLabelFont", ann=self.anno_assetTypeList)
        self.op_assetTypeNew_btn = cmds.button('op_assetTypeNew_btn', parent=self.op_shotSequence_formLayout, l="New...", bgc=(.6, .8, .5), c="openPipelineNewAssetTypeUI", ann=self.anno_newAssetType)
        self.op_assetTypeRemove_btn = cmds.button('op_assetTypeRemove_btn', parent=self.op_shotSequence_formLayout, l="Delete", bgc=(.8, .3, .3), c="openPipelineRemoveProcess 2 1", ann=self.anno_removeAssetType)
        
        cmds.formLayout(
            self.op_shotSequence_formLayout,
            e=1,
            attachPosition=[
                (self.op_assetAssetTypes_txt, "left", 0, 0),
                (self.op_assetType_txtScrollList, "right", 0, 100),
                (self.op_assetType_txtScrollList, "left", 0, 0),
                (self.op_assetTypeNew_btn, "left", 0, 0),
                (self.op_assetTypeNew_btn, "right", 0, 50),
                (self.op_assetTypeRemove_btn, "right", 0, 100),
                (self.op_assetTypeRemove_btn, "left", 0, 50),
                (self.op_assetTypeRemove_btn, "left", 0, 50),
            ],
            attachControl=[
                (self.op_assetType_txtScrollList, "top", 5, self.op_assetAssetTypes_txt),
                (self.op_assetTypeNew_btn, "top", 5, self.op_assetType_txtScrollList),
                (self.op_assetTypeRemove_btn, "top", 5, self.op_assetType_txtScrollList),
            ],
            )
        
        
        #--------------------------------------------
        #   END Section 3.01 - "Asset Types"
        #
        #   START Section 3.02 - "Assets"
        #   Center Column in the "Assets" Tab
        #--------------------------------------------
        
        self.op_assetAssets_formLayout = cmds.formLayout('op_assetAssets_formLayout', parent=self.op_assetBrowser_formLayout, numberOfDivisions=100)

        self.op_assetAssetsTxt = cmds.text('op_assetAssetsTxt', parent=self.op_assetAssets_formLayout, fn="smallBoldLabelFont", l="Assets", w=125, al="left")
        
        self.op_assetMenuBarLayout01 = cmds.menuBarLayout('op_assetMenuBarLayout01', parent=self.op_assetAssets_formLayout, w=125, h=175)
        
        self.op_assetActions_menu = cmds.menu('op_assetActions_menu', parent=self.op_assetMenuBarLayout01, label="ACTIONS...", aob=1)
        self.op_assetActions_editAsset_menuItem = cmds.menuItem('op_assetActions_EditAsset_menuItem', parent=self.op_assetActions_menu, label="Edit Asset", subMenu=0, command="openPipelineOpenCurrentlySelected 2 2 workshop 0", ann=self.anno_editAsset)
        self.op_assetActions_openMaster_menuItem = cmds.menuItem('op_assetActions_OpenMaster_menuItem', parent=self.op_assetActions_menu, label="Open Master", subMenu=0, command="openPipelineOpenCurrentlySelected 2 2 master 0", ann=self.anno_viewAsset)
        
        self.op_assetActions_import_menuItem = cmds.menuItem('op_assetActions_import_menuItem', parent=self.op_assetActions_menu, label="Import", aob=1, subMenu=1, ann=" ")
        self.op_assetActions_importWorkshop_menuItem = cmds.menuItem('op_assetActions_workshop_menuItem', parent=self.op_assetActions_import_menuItem, label="Workshop", command="openPipelineImportUI 0 asset workshop", ann=self.anno_importAssetWorkshop)
        self.op_assetActions_importWorkshop_opBox = cmds.menuItem('op_assetActions_workshop_opBox', parent=self.op_assetActions_import_menuItem, ob=1, c="openPipelineImportUI 1 asset workshop")
        self.op_assetActions_importMaster_menuItem = cmds.menuItem('op_assetActions_importMaster_menuItem', parent=self.op_assetActions_import_menuItem, label="Master", command="openPipelineImportUI 0 asset master", ann=self.anno_importAssetMaster)
        self.op_assetActions_importMaster_opBox = cmds.menuItem('op_assetActions_importMaster_opBox', parent=self.op_assetActions_import_menuItem, ob=1, c="openPipelineImportUI 1 asset master")


        self.op_assetActions_reference_menuItem = cmds.menuItem('op_assetActions_reference_menuItem', parent=self.op_assetActions_menu, label="Reference", aob=1, subMenu=1, ann=" ")
        self.op_assetActions_referenceWorkshop_menuItem = cmds.menuItem('op_assetActions_referenceWorkshop_menuItem', parent=self.op_assetActions_reference_menuItem, label="Workshop", command="openPipelineReferenceUI 0 asset workshop", ann=self.anno_referenceAssetWorkshop)
        self.op_assetActions_referenceWorkshop_opBox = cmds.menuItem('op_assetActions_referenceWorkshop_opBox', parent=self.op_assetActions_reference_menuItem, ob=1, c="openPipelineReferenceUI 1 asset workshop")
        self.op_assetActions_referenceMaster_menuItem = cmds.menuItem('op_assetActions_referenceMaster_menuItem', parent=self.op_assetActions_reference_menuItem, label="Master", command="openPipelineReferenceUI 0 asset master", ann=self.anno_referenceAssetMaster)
        self.op_assetActions_referenceMaster_opBox = cmds.menuItem('op_assetActions_referenceMaster_opBox', parent=self.op_assetActions_reference_menuItem, ob=1, c="openPipelineReferenceUI 1 asset master")

        self.op_assetActions_archive_menuItem = cmds.menuItem('op_assetActions_archive_menuItem', parent=self.op_assetActions_menu, label="Archive...", command="openPipelineArchiveDialog 2 2")


        self.op_assetColumnLayout01 = cmds.columnLayout('op_assetColumnLayout01', adj=1)
        self.op_asset_scrollList = cmds.textScrollList(w=125, h=100, dcc="openPipelineOpenCurrentlySelected 2 2 workshop 0", sc="openPipelineAssetSelected 0", fn="smallPlainLabelFont", ann=self.anno_assetList)
        self.op_assetpopUpMenu = cmds.popupMenu(p=self.op_asset_scrollList, b=3, mm=1, pmc="openPipelineAssetSelected 1")
        self.op_assetPopUpMenu_editAsset_menuItem = cmds.menuItem(parent=self.op_assetpopUpMenu, label="Edit Asset", command="openPipelineOpenCurrentlySelected 2 2 workshop 0", ann=self.anno_editAsset)
        
        self.op_assetPopUpMenu_openMaster_menuItem = cmds.menuItem(parent=self.op_assetpopUpMenu, label="Open Master", command="openPipelineOpenCurrentlySelected 2 2 master 0", ann=self.anno_viewAsset)
        self.op_assetPopUpMenu_import_menuItem = cmds.menuItem(parent=self.op_assetpopUpMenu, label="Import", aob=1, subMenu=1, ann=" ")
        self.op_assetPopUpMenu_workshop_menuItem = cmds.menuItem(parent=self.op_assetPopUpMenu_import_menuItem, label="Workshop", command="openPipelineImportUI 0 asset workshop", ann=self.anno_importAssetWorkshop)
        self.op_assetPopUpMenu_workshop_opBox = cmds.menuItem(parent=self.op_assetPopUpMenu_import_menuItem, ob=1, c="openPipelineImportUI 1 asset workshop")
        self.op_assetPopUpMenu_master_menuItem = cmds.menuItem(parent=self.op_assetPopUpMenu_import_menuItem, label="Master", command="openPipelineImportUI 0 asset master", ann=self.anno_importAssetMaster)
        self.op_assetPopUpMenu_master_opBox = cmds.menuItem(parent=self.op_assetPopUpMenu_import_menuItem, ob=1, c="openPipelineImportUI 1 asset master")
        
        self.op_assetPopUpMenu_reference_menuItem = cmds.menuItem(label="Reference", aob=1, subMenu=1, ann=" ")
        self.op_assetPopUpMenu_referenceWorkshop_menuItem = cmds.menuItem(parent=self.op_assetPopUpMenu_reference_menuItem, label="Workshop", command="openPipelineReferenceUI 0 asset workshop", ann=self.anno_referenceAssetWorkshop)
        self.op_assetPopUpMenu_referenceWorkshop_opBox = cmds.menuItem(parent=self.op_assetPopUpMenu_reference_menuItem, ob=1, c="openPipelineReferenceUI 1 asset workshop")
        self.op_assetPopUpMenu_referenceMaster_menuItem = cmds.menuItem(parent=self.op_assetPopUpMenu_reference_menuItem, label="Master", command="openPipelineReferenceUI 0 asset master", ann=self.anno_referenceAssetMaster)
        self.op_assetPopUpMenu_referenceMaster_opBox = cmds.menuItem(parent=self.op_assetPopUpMenu_reference_menuItem, ob=1, c="openPipelineReferenceUI 1 asset master")

        self.op_assetPopUpMenu_archive_menuItem = cmds.menuItem(parent=self.op_assetPopUpMenu_reference_menuItem, label="Archive...", command="openPipelineArchiveDialog 2 2")
        self.op_assetSeparator03 = cmds.separator(style="none", w=125, h=5)
        
        self.op_assetAssetTypes_formLayout = cmds.formLayout(numberOfDivisions=100)
        self.op_assetNew_btn = cmds.button(parent=self.op_assetAssetTypes_formLayout, l="New...", bgc=(.6, .8, .5), w=65, c="openPipelineNewAssetUI", ann=self.anno_editAsset)
        self.op_assetRemove_btn = cmds.button(parent=self.op_assetAssetTypes_formLayout, l="Delete", bgc=(.8, .3, .3), w=60, c="openPipelineRemoveProcess 2 2", ann=self.anno_removeAsset)
        self.op_assetRename_btn = cmds.button(parent=self.op_assetAssetTypes_formLayout, l="Rename...", bgc=(.6, .8, .5), w=65, c="openPipelineRenameAssetUI", ann=self.anno_renameAsset)

        cmds.formLayout(
            self.op_assetAssetTypes_formLayout,
            e=1,
            attachPosition=[
                (self.op_assetNew_btn, "left", 0, 0),
                (self.op_assetNew_btn, "right", 0, 50),
                (self.op_assetRemove_btn, "left", 0, 50),
                (self.op_assetRemove_btn, "right", 0, 100),
                (self.op_assetRename_btn, "left", 0, 0),
                (self.op_assetRename_btn, "right", 0, 100),
            ],
            attachControl=[
                (self.op_assetRename_btn, "top", 0, self.op_assetNew_btn),
            ],
            )
        
        cmds.formLayout(
            self.op_assetAssets_formLayout, 
            e=1,
            attachForm=[
                (self.op_assetAssetsTxt, "left", 0),
                (self.op_assetMenuBarLayout01, "left", 0),
            ],
            attachControl=[
                (self.op_assetMenuBarLayout01, "top", 5, self.op_assetAssetsTxt),
            ],
            attachPosition=[
                (self.op_assetMenuBarLayout01, "right", 0, 100),
            ],
        )

        #--------------------------------------------
        #   END Section 3.02 - "Assets"
        #
        #   START Section 3.03 - "Components"
        #   Right Column in the "Assets" Tab
        #--------------------------------------------
        
        self.op_assetsComponents_formLayout = cmds.formLayout(parent=self.op_assetBrowser_formLayout, numberOfDivisions=100)
        
        self.op_assetsComponents_txt = cmds.text(parent=self.op_assetsComponents_formLayout, fn="smallBoldLabelFont", l="Components", w=125, al="left")
        
        self.op_assets_components_menuBarLayout = cmds.menuBarLayout(parent=self.op_assetsComponents_formLayout, w=125, h=175)
        
        self.op_assetComponentMenu = cmds.menu(label="ACTIONS...")
        self.op_compMenuEdit = cmds.menuItem(parent=self.op_assetComponentMenu, label="Edit Component", subMenu=0, command="openPipelineOpenCurrentlySelected 2 3 workshop 0", ann=self.anno_editComponent)
        self.op_compMenuView = cmds.menuItem(parent=self.op_assetComponentMenu, label="View Master", command="openPipelineOpenCurrentlySelected 2 3 master 0" , ann=self.anno_viewComponent)
        
        self.op_compMenuImport = cmds.menuItem(parent=self.op_assetComponentMenu, label="Import", aob=1, subMenu=1, ann=" ")
        self.op_compMenuImportWorkshop = cmds.menuItem(parent=self.op_compMenuImport, label="Workshop",command="openPipelineImportUI 0 component workshop", ann=self.anno_importComponentWorkshop)
        self.op_compMenuImportWorkshopOpBox = cmds.menuItem(ob=1, c="openPipelineImportUI 1 component workshop")
        self.op_compMenuImportMaster = cmds.menuItem( parent=self.op_compMenuImport, label="Master", command="openPipelineImportUI 0 component master", ann=self.anno_importComponentMaster)
        self.op_compMenuImportMasterOpBox = cmds.menuItem(ob=1, c="openPipelineImportUI 1 component master")
        
        self.op_compMenuReference = cmds.menuItem(parent=self.op_assetComponentMenu, label="Reference", aob=1, subMenu=1, ann=" ")
        self.op_compMenuReferenceWorkshop = cmds.menuItem(parent=self.op_compMenuReference, label="Workshop", command="openPipelineReferenceUI 0 component workshop", ann=self.anno_referenceComponentWorkshop)
        self.op_compMenuReferenceWorkshopOpBox = cmds.menuItem(ob=1, c="openPipelineReferenceUI 1 component workshop")
        self.op_compMenuReferenceMaster = cmds.menuItem(parent=self.op_compMenuReference, label="Master", command="openPipelineReferenceUI 0 component master", ann=self.anno_referenceComponentMaster)
        self.op_compMenuReferenceMasterOpBox = cmds.menuItem(ob=1, c="openPipelineReferenceUI 1 component master")
        
        self.op_assetCompMenuArchive = cmds.menuItem(parent=self.op_assetComponentMenu, label="Archive...", command="openPipelineArchiveDialog 2 3")

        self.op_assetColumnLayout02 = cmds.columnLayout(parent=self.op_assets_components_menuBarLayout, adj=1)
        self.op_componentScrollList = cmds.textScrollList(parent=self.op_assetColumnLayout02, w=125, h=100, en=0, dcc="openPipelineOpenCurrentlySelected 2 3 workshop 0", sc="openPipelineComponentSelected", fn="smallPlainLabelFont", ann=self.anno_componentList)
        self.op_assetPopupMenu02 = cmds.popupMenu(parent=self.op_componentScrollList, b=3, mm=1, pmc="openPipelineComponentSelected")
        self.op_compMenuEdit2 = cmds.menuItem(parent=self.op_assetPopupMenu02, label="Edit Component", subMenu=0, command="openPipelineOpenCurrentlySelected 2 3 workshop 0", ann=self.anno_editComponent)
        self.op_compMenuView2 = cmds.menuItem(parent=self.op_assetPopupMenu02, label="View Master", command="openPipelineOpenCurrentlySelected 2 3 master 0", ann=self.anno_viewComponent)
        
        self.op_compMenuImport2 = cmds.menuItem(parent=self.op_assetPopupMenu02, label="Import", aob=1, subMenu=1, ann=" ")
        self.op_compMenuImportWorkshop2 = cmds.menuItem(parent=self.op_compMenuImport2, label="Workshop", command="openPipelineImportUI 0 component workshop", ann=self.anno_importComponentWorkshop)
        self.op_compMenuImportWorkshopOpBox2 = cmds.menuItem(ob=1, c="openPipelineImportUI 1 component workshop")
        self.op_compMenuImportMaster2 = cmds.menuItem(parent=self.op_compMenuImport2, label="Master", command="openPipelineImportUI 0 component master", ann=self.anno_importComponentMaster)
        self.op_compMenuImportMasterOpBox2 = cmds.menuItem(ob=1, c="openPipelineImportUI 1 component master")
        
        self.op_compMenuReference2 = cmds.menuItem(parent=self.op_assetPopupMenu02, label="Reference", aob=1, subMenu=1, ann=" ")
        self.op_compMenuReferenceWorkshop2 = cmds.menuItem(parent=self.op_compMenuReference2, label="Workshop", command="openPipelineReferenceUI 0 component workshop", ann=self.anno_referenceComponentWorkshop)
        self.op_compMenuReferenceWorkshopOpBox2 = cmds.menuItem(ob=1, c="openPipelineReferenceUI 1 component workshop")
        self.op_compMenuReferenceMaster2 = cmds.menuItem(parent=self.op_compMenuReference2, label="Master", command="openPipelineReferenceUI 0 component master", ann=self.anno_referenceComponentMaster)
        self.op_compMenuReferenceMasterOpBox2 = cmds.menuItem(ob=1, c="openPipelineReferenceUI 1 component master")
        
        self.op_assetCompMenuArchive2 = cmds.menuItem(parent=self.op_assetPopupMenu02, label="Archive...", command="openPipelineArchiveDialog 2 3")
        
        self.op_assetSubFormLayout02 = cmds.formLayout(parent=self.op_assetColumnLayout02, numberOfDivisions=100)
        self.op_componentNewButton = cmds.button(parent=self.op_assetSubFormLayout02, l="New...", bgc=(.6, .8, .5), w=65, c="openPipelineNewAssetComponentUI", ann=self.anno_newComponent)
        self.op_componentRemoveButton = cmds.button(parent=self.op_assetSubFormLayout02, l="Delete", bgc=(.8, .3, .3), w=60, c="openPipelineRemoveProcess 2 3", ann=self.anno_removeComponent)

        cmds.formLayout(
            self.op_assetSubFormLayout02,
            e=1,
            attachPosition=[
                (self.op_componentNewButton, "left", 0, 0),
                (self.op_componentNewButton, "right", 0, 50),
                (self.op_componentNewButton, "top", 5, 0),
                (self.op_componentRemoveButton, "left", 0, 50),
                (self.op_componentRemoveButton, "right", 0, 100),
                (self.op_componentRemoveButton, "top", 5, 0),
            ],
            )
        
                        
        cmds.formLayout(
            self.op_assetsComponents_formLayout,
            e=1,
            attachForm=[
                (self.op_assetsComponents_txt, "left", 0),
                ],
            attachControl=[
                (self.op_assets_components_menuBarLayout, "top", 5, self.op_assetsComponents_txt),
            ],
            attachPosition=[
                (self.op_assets_components_menuBarLayout, "right", 0, 100),
                (self.op_assets_components_menuBarLayout, "left", 0, 0),
            ]
        )
        
        #--------------------------------------------
        #   END Section 3.03 - "Components"
        #
        #   START Section 3.04 - Lower Contents of "Asset Inventory" Tab
        #   this includes view playblast, notes, and the explore location 
        #--------------------------------------------       
     
        self.op_assetPreviewTxt = cmds.text(parent=self.op_assetBrowser_formLayout, fn="smallBoldLabelFont", l="Preview", w=164, al="center")
        self.op_assetPreviewImage = cmds.image(parent=self.op_assetBrowser_formLayout, h=105, w=164, i=self.op_currOpenPreview_filePath, bgc=(0, 0, 0))
        self.op_assetViewPlayblastAssetButton = cmds.button(parent=self.op_assetBrowser_formLayout, l="View Playblast", h=30, en=0, w=164, c="openPipelineViewPlayblastSelected 2")
        self.op_assetHistoryTxt = cmds.text(parent=self.op_assetBrowser_formLayout, fn="smallBoldLabelFont", l="History", w=225, al="center")
        self.op_commentField = cmds.scrollField(parent=self.op_assetBrowser_formLayout, w=225, h=80,enable=1, editable=0, wordWrap=1, font="smallPlainLabelFont", text="")
        self.op_assetNotesTxt = cmds.text(parent=self.op_assetBrowser_formLayout, fn="smallBoldLabelFont", l="Notes", w=225, al="center")
        self.op_assetNoteField = cmds.scrollField(parent=self.op_assetBrowser_formLayout, w=225, h=45, enable=1, editable=0, wordWrap=1, font="smallPlainLabelFont", text="")
        self.op_assetLocationTxt = cmds.text(parent=self.op_assetBrowser_formLayout, fn="smallBoldLabelFont", l="Location", w=395, al="center")
        self.op_assetLocationField = cmds.textField(parent=self.op_assetBrowser_formLayout, editable=0, w=345)
        self.op_exploreAssetsButton = cmds.button(parent=self.op_assetBrowser_formLayout, w=50, align="center", label="explore...", c="openPipelineExploreSelected 2")
        
        #--------------------------------------------
        #   END Section 3.04 - Lower Contents of "Asset Inventory" Tab
        #
        #   START Attach elements to op_assetBrowser_formLayout
        #--------------------------------------------
        
        
        cmds.formLayout(
            self.op_assetBrowser_formLayout,
            e=1,
            attachPosition=[
                (self.op_assetSeperator01, "left", 0, 0),
                (self.op_assetSeperator01, "right", 0, 100),
                (self.op_assetSeperator01, "top", 5, 0),
                (self.op_assetAssetBrowser_txt, "left", 0, 0),
                (self.op_assetSeperator02, "left", 0, 0),
                (self.op_assetSeperator02, "right", 0, 100),
                
                (self.op_shotSequence_formLayout, "left", 0, 0),
                (self.op_shotSequence_formLayout, "right", 2, 33),
                
                (self.op_assetAssets_formLayout, "left", 2, 33),
                (self.op_assetAssets_formLayout, "right", 2, 66),
                
                (self.op_assetsComponents_formLayout, "left", 2, 66),
                (self.op_assetsComponents_formLayout, "right", 0, 100),
                
                (self.op_assetPreviewTxt, "left", 0, 0),
                (self.op_assetPreviewImage, "left", 0, 0),
                (self.op_assetHistoryTxt, "right", 0, 100),
                (self.op_commentField, "right", 0, 100),
                (self.op_assetViewPlayblastAssetButton, "left", 0, 0),
                
                (self.op_assetNotesTxt, "right", 0, 100),
                
                (self.op_assetLocationTxt, "left", 5, 0),
                (self.op_assetLocationTxt, "right", 0, 100),
                (self.op_assetNoteField, "right", 0, 100),
                (self.op_assetLocationField, "right", 0, 80),
                (self.op_assetLocationField, "left", 0, 0),
                (self.op_exploreAssetsButton, "right", 0, 100),
            ],
            attachControl=[
                (self.op_assetAssetBrowser_txt, "top", 5, self.op_assetSeperator01),
                (self.op_assetSeperator02, "top", 0, self.op_assetAssetBrowser_txt),
                
                (self.op_assetAssets_formLayout, "top", 5, self.op_assetSeperator02),
                (self.op_shotSequence_formLayout, "top", 5, self.op_assetSeperator02),
                (self.op_assetsComponents_formLayout, "top", 5, self.op_assetSeperator02),
                
                (self.op_assetPreviewTxt, "top", 5, self.op_assetAssets_formLayout),
                (self.op_assetPreviewTxt, "top", 5, self.op_assetAssets_formLayout),
                (self.op_assetPreviewImage, "top", 5, self.op_assetPreviewTxt),
                (self.op_assetHistoryTxt, "left", 5, self.op_assetPreviewImage),
                (self.op_assetHistoryTxt, "top", 5, self.op_assetAssets_formLayout),
                (self.op_commentField, "left", 5, self.op_assetPreviewImage),
                (self.op_commentField, "top", 5, self.op_assetPreviewTxt),
                (self.op_assetViewPlayblastAssetButton, "top", 5, self.op_assetPreviewImage),
                
                (self.op_assetNotesTxt, "top", 5, self.op_commentField),
                (self.op_assetNotesTxt, "left", 5, self.op_assetPreviewImage),
                (self.op_assetNoteField, "left", 5, self.op_assetPreviewImage),
                (self.op_assetNoteField, "top", 5, self.op_assetNotesTxt),
                (self.op_assetLocationTxt, "top", 5, self.op_assetNoteField),
                (self.op_assetLocationField, "top", 5, self.op_assetLocationTxt),
                (self.op_exploreAssetsButton, "left", 5, self.op_assetLocationField),
                (self.op_exploreAssetsButton, "top", 5, self.op_assetLocationTxt),
            ],
            )
        
        #--------------------------------------------
        #   END Attach elements to op_assetBrowser_formLayout
        #
        #   END Section 3.00 - "Asset Inventory" Tab
        #
        #   START Section 4.00 - "Shot Inventory" Tab
        #   this is the third section that will be attached to the tab layout
        #--------------------------------------------
        
        self.op_shotFormLayout = cmds.formLayout('op_shotFormLayout', parent=self.op_mainTabs_tabLayout, width=410, numberOfDivisions=100)
        self.op_shotSeperator01 = cmds.separator(parent=self.op_shotFormLayout, style="double", w=410)
        self.op_shotTabShotBrowserTxt = cmds.text(parent=self.op_shotFormLayout, fn="boldLabelFont", label="SHOT BROWSER", w=410, al="left")
        self.op_shotSeperator02 = cmds.separator(parent=self.op_shotFormLayout, style="double", w=410)
        

        #--------------------------------------------
        #   START Section 4.01 - "Sequence"
        #   Left Column in the "Shot Inventory" Tab
        #--------------------------------------------
        
        
        self.op_shotSequenceFormLayout = cmds.formLayout(parent=self.op_shotFormLayout, numberOfDivisions=100)
        
        self.op_shotSequenceTxt = cmds.text(parent=self.op_shotSequenceFormLayout, l="Sequence", w=125, fn="smallBoldLabelFont", al="left")
        self.op_sequenceScrollList = cmds.textScrollList(parent=self.op_shotSequenceFormLayout, w=125, h=119, ams=0, sc="openPipelineUpdateShotList 0", fn="smallPlainLabelFont", ann=self.anno_sequenceList)
        self.op_assetTypeNewButton = cmds.button(parent=self.op_shotSequenceFormLayout, l="New...", bgc=(.6, .8, .5), w=65, c="openPipelineNewSequenceUI", ann=self.anno_newSequence)
        self.op_sequenceRemoveButton = cmds.button(parent=self.op_shotSequenceFormLayout, l="Delete", bgc=(.8, .3, .3), w=60, c="openPipelineRemoveProcess 3 1", ann=self.anno_removeSequence)


        cmds.formLayout(
            self.op_shotSequenceFormLayout,
            e=1,
            attachPosition=[
                (self.op_shotSequenceTxt, "left", 0, 0),
                (self.op_sequenceScrollList, "left", 0, 0),
                (self.op_sequenceScrollList, "right", 0, 100),
                
                (self.op_assetTypeNewButton, "left", 0, 0),
                (self.op_assetTypeNewButton, "right", 0, 50),
                
                (self.op_sequenceRemoveButton, "left", 0, 50),
                
                (self.op_sequenceRemoveButton, "right", 0, 100),
            ],
            attachControl=[
                (self.op_sequenceScrollList, "top", 5, self.op_shotSequenceTxt),
                
                (self.op_assetTypeNewButton, "top", 5, self.op_sequenceScrollList),
                
                (self.op_sequenceRemoveButton, "top", 5, self.op_sequenceScrollList),
            ],
            )
            
        #--------------------------------------------
        #   END Section 4.01 - "Sequence"
        #
        #   START Section 4.02 - "Shot"
        #   Center Column in the "Shot Inventory" Tab
        #--------------------------------------------
    
        self.op_shotShotFormLayout = cmds.formLayout(parent=self.op_shotFormLayout, numberOfDivisions=100)
        self.op_shotShotTxt = cmds.text(parent=self.op_shotShotFormLayout, fn="smallBoldLabelFont", l="Shot", w=120, al="left")
        self.op_shotMenuBarLayout01 = cmds.menuBarLayout(parent=self.op_shotShotFormLayout, w=125, h=175)
        
        #--------------------------------------------
        #   START Section 4.02.1 - "Actions" dropdown
        #--------------------------------------------
        self.op_shotMenu = cmds.menu(parent=self.op_shotMenuBarLayout01, label="ACTIONS...")
        
        self.op_shotMenuEdit = cmds.menuItem(parent=self.op_shotMenu, label="Edit Shot", subMenu=0, command="openPipelineOpenCurrentlySelected 3 2 workshop 0", ann=self.anno_editShot)
        self.op_shotMenuView = cmds.menuItem(parent=self.op_shotMenu, label="View Master", subMenu=0, command="openPipelineOpenCurrentlySelected 3 2 master 0", ann=self.anno_viewShot)
        
        self.op_shotMenuImport = cmds.menuItem(parent=self.op_shotMenu, label="Import", aob=1, subMenu=1, ann=" ")
        self.op_shotMenuImportWorkshop = cmds.menuItem(parent=self.op_shotMenuImport, label="Workshop", command="openPipelineImportUI 0 shot workshop", ann=self.anno_importShotWorkshop)
        self.op_shotMenuImportWorkshopOpBox = cmds.menuItem(ob=1, c="openPipelineImportUI 1 shot workshop", en=0)
        self.op_shotMenuImportMaster = cmds.menuItem(parent=self.op_shotMenuImport, label="Master", command="openPipelineImportUI 0 shot master", ann=self.anno_importShotMaster)
        self.op_shotMenuImportMasterOpBox = cmds.menuItem(ob=1, c="openPipelineImportUI 1 shot master")
        
        self.op_shotMenuReference = cmds.menuItem(parent=self.op_shotMenu, label="Reference", aob=1, subMenu=1, ann=" ")
        self.op_shotMenuReferenceWorkshop = cmds.menuItem(parent=self.op_shotMenuReference, label="Workshop", command="openPipelineReferenceUI 0 shot workshop", ann=self.anno_referenceShotWorkshop)
        self.op_shotMenuReferenceWorkshopOpBox = cmds.menuItem(ob=1, c="openPipelineReferenceUI 1 shot workshop")
        self.op_shotMenuReferenceMaster = cmds.menuItem(parent=self.op_shotMenuReference, label="Master", command="openPipelineReferenceUI 0 shot master", ann=self.anno_referenceShotMaster)
        self.op_shotMenuReferenceMasterOpBox = cmds.menuItem(ob=1, c="openPipelineReferenceUI 1 shot master")
        
        self.op_shotMenuArchive = cmds.menuItem(parent=self.op_shotMenu, label="Archive...", command="openPipelineArchiveDialog 3 2")
        
        #--------------------------------------------
        #   END Section 4.02.1 - "Actions" dropdown
        #--------------------------------------------
        
        self.op_shotColumnLayout01 = cmds.columnLayout(parent=self.op_shotMenuBarLayout01, adj=1)
        self.op_shotScrollList = cmds.textScrollList(parent=self.op_shotColumnLayout01, w=125, h=100, dcc="openPipelineOpenCurrentlySelected 3 2 workshop 0", sc="openPipelineShotSelected 0", fn="smallPlainLabelFont", ann=self.anno_shotList)
        
        #--------------------------------------------
        #   START Section 4.02.2 - Popup dropdown
        #--------------------------------------------
        
        self.op_shotPopupMenu01 = cmds.popupMenu(p=self.op_shotScrollList, b=3, mm=1, pmc="openPipelineShotSelected 0")
        
        self.op_shotMenuEdit2 = cmds.menuItem(parent=self.op_shotPopupMenu01, label="Edit Shot", command="openPipelineOpenCurrentlySelected 3 2 workshop 0", ann=self.anno_editShot)
        self.op_shotMenuView2 = cmds.menuItem(parent=self.op_shotPopupMenu01, label="View Master", command="openPipelineOpenCurrentlySelected 3 2 master 0", ann=self.anno_viewShot)
        
        self.op_shotMenuImport2 = cmds.menuItem(parent=self.op_shotPopupMenu01, label="Import", aob=1, subMenu=1, ann=" ")
        self.op_shotMenuImportWorkshop2 = cmds.menuItem(parent=self.op_shotMenuImport2, label="Workshop", command="openPipelineImportUI 0 shot workshop", ann=self.anno_importShotWorkshop)
        self.op_shotMenuImportWorkshopOpBox2 = cmds.menuItem(ob=1, c="openPipelineImportUI 1 shot workshop")
        self.op_shotMenuImportMaster2 = cmds.menuItem(parent=self.op_shotMenuImport2, label="Master", command="openPipelineImportUI 0 shot master", ann=self.anno_importShotMaster)
        self.op_shotMenuImportMasterOpBox2 = cmds.menuItem(ob=1, c="openPipelineImportUI 1 shot master")
        
        self.op_shotMenuReference2 = cmds.menuItem(parent=self.op_shotPopupMenu01, label="Reference", aob=1, subMenu=1, ann=" ")
        self.op_shotMenuReferenceWorkshop2 = cmds.menuItem(parent=self.op_shotMenuReference2, label="Workshop", command="openPipelineReferenceUI 0 shot workshop", ann=self.anno_referenceShotWorkshop)
        self.op_shotMenuReferenceWorkshopOpBox2 = cmds.menuItem(ob=1, c="openPipelineReferenceUI 1 shot workshop")
        self.op_shotMenuReferenceMaster2 = cmds.menuItem(parent=self.op_shotMenuReference2, label="Master", command="openPipelineReferenceUI 0 shot master", ann=self.anno_referenceShotMaster)
        self.op_shotMenuReferenceMasterOpBox2 = cmds.menuItem(ob=1, c="openPipelineReferenceUI 1 shot master")
        
        self.op_shotMenuArchive2 = cmds.menuItem(parent=self.op_shotPopupMenu01, label="Archive...", command="openPipelineArchiveDialog 3 2")
        
        #--------------------------------------------
        #   END Section 4.02.2 - Popup dropdown
        #--------------------------------------------
        
        self.op_shotSubFormLayout01 = cmds.formLayout(parent=self.op_shotColumnLayout01, numberOfDivisions=100)
        self.op_shotNewButton = cmds.button(parent=self.op_shotSubFormLayout01, l="New...", bgc=(.6, .8, .5), w=65, c="openPipelineNewShotUI", ann=self.anno_newShot)
        self.op_shotRemoveButton = cmds.button(parent=self.op_shotSubFormLayout01, l="Delete", bgc=(.8, .3, .3), w=60, c="openPipelineRemoveProcess 3 2", ann=self.anno_removeShot)
        cmds.formLayout(
            self.op_shotSubFormLayout01,
            e=1,
            attachPosition=[
                (self.op_shotNewButton, "left", 0, 0),
                (self.op_shotNewButton, "right", 0, 50),
                (self.op_shotNewButton, "top", 5, 0),
                (self.op_shotRemoveButton, "left", 0, 50),
                (self.op_shotRemoveButton, "right", 0, 100),
                (self.op_shotRemoveButton, "top", 5, 0),
            ],
        )
        
        cmds.formLayout(
            self.op_shotShotFormLayout,
            e=1,
            attachForm=[
                (self.op_shotShotTxt, "left", 0),
                (self.op_shotMenuBarLayout01, "left", 0),
            ],
            attachControl=[
                (self.op_shotMenuBarLayout01, "top", 5, self.op_shotShotTxt),
            ],
            attachPosition=[
                (self.op_shotMenuBarLayout01, "right", 0, 100),
            ]
        )
        
        #--------------------------------------------
        #   END Section 4.02 - "Shot"
        #
        #   START Section 4.03 - "Components"
        #   Right Column in the "Shot Inventory" Tab
        #--------------------------------------------
        self.op_shotComponentsFormLayout = cmds.formLayout(parent=self.op_shotFormLayout, numberOfDivisions=100)
        
        self.op_shotComponentsTxt = cmds.text(parent=self.op_shotComponentsFormLayout, fn="smallBoldLabelFont", l="Components", w=125, al="left")
        self.op_shotMenuBarLayout02 = cmds.menuBarLayout(parent=self.op_shotComponentsFormLayout, w=125, h=175)
        
        #--------------------------------------------
        #   START Section 4.03.1 - "Actions" dropdown
        #--------------------------------------------
        
        self.op_shotComponentMenu = cmds.menu(parent=self.op_shotMenuBarLayout02, label="ACTIONS...")
        
        self.op_shotcompMenuEdit = cmds.menuItem(parent=self.op_shotComponentMenu, label="Edit Shot Component", subMenu=0, command="openPipelineOpenCurrentlySelected 3 3 workshop 0", ann=self.anno_editShotComponent)
        self.op_shotcompMenuView = cmds.menuItem(parent=self.op_shotComponentMenu, label="View Master", command="openPipelineOpenCurrentlySelected 3 3 master 0", ann=self.anno_viewShotComponent)
        
        self.op_shotcompMenuImport = cmds.menuItem(parent=self.op_shotComponentMenu, label="Import", aob=1, subMenu=1, ann=" ")
        self.op_shotcompMenuImportWorkshop = cmds.menuItem(parent=self.op_shotcompMenuImport, label="Workshop", command="openPipelineImportUI 0 shotComponent workshop", ann=self.anno_importShotComponentWorkshop)
        self.op_shotcompMenuImportWorkshopOpBox = cmds.menuItem(ob=1, c="openPipelineImportUI 1 shotComponent workshop")
        self.op_shotcompMenuImportMaster = cmds.menuItem(parent=self.op_shotcompMenuImport, label="Master", command="openPipelineImportUI 0 shotComponent master", ann=self.anno_importShotComponentMaster)
        self.op_shotcompMenuImportMasterOpBox = cmds.menuItem(ob=1, c="openPipelineImportUI 1 shotComponent master")
        
        self.op_shotcompMenuReference = cmds.menuItem(parent=self.op_shotComponentMenu, label="Reference", aob=1, subMenu=1, ann=" ")
        self.op_shotcompMenuReferenceWorkshop = cmds.menuItem(parent=self.op_shotcompMenuReference, label="Workshop", command="openPipelineReferenceUI 0 shotComponent workshop", ann=self.anno_referenceShotComponentWorkshop)
        self.op_shotcompMenuReferenceWorkshopOpBox = cmds.menuItem(ob=1, c="openPipelineReferenceUI 1 shotComponent workshop")
        self.op_shotcompMenuReferenceMaster = cmds.menuItem(parent=self.op_shotcompMenuReference, label="Master", command="openPipelineReferenceUI 0 shotComponent master", ann=self.anno_referenceShotComponentMaster)
        self.op_shotcompMenuReferenceMasterOpBox = cmds.menuItem(ob=1, c="openPipelineReferenceUI 1 shotComponent master")
        
        #--------------------------------------------
        #   END Section 4.03.1 - "Actions" dropdown
        #--------------------------------------------
        
        self.op_shotcompMenuArchive = cmds.menuItem(parent=self.op_shotComponentMenu, label="Archive...", command="openPipelineArchiveDialog 3 3")
        
        self.op_shotColumnLayout02 = cmds.columnLayout(parent=self.op_shotMenuBarLayout02, adj=1)
        self.op_shotComponentScrollList = cmds.textScrollList(parent=self.op_shotColumnLayout02, w=125, h=100, en=0, dcc="openPipelineOpenCurrentlySelected 3 3 workshop 0", sc="openPipelineShotComponentSelected", fn="smallPlainLabelFont", ann=self.anno_shotComponentList)
        
        
        #--------------------------------------------
        #   START Section 4.03.2 - Popup dropdown
        #--------------------------------------------
        self.op_shotPopupMenu02 = cmds.popupMenu(p=self.op_shotComponentScrollList, b=3, mm=1, pmc="openPipelineShotComponentSelected")
        
        self.op_shotcompMenuEdit2 = cmds.menuItem(p=self.op_shotPopupMenu02, label="Edit Shot Component", subMenu=0, command="openPipelineOpenCurrentlySelected 3 3 workshop 0", ann=self.anno_editShotComponent)
        self.op_shotcompMenuView2 = cmds.menuItem(p=self.op_shotPopupMenu02, label="View Master", command="openPipelineOpenCurrentlySelected 3 3 master 0", ann=self.anno_viewShotComponent)
        
        self.op_shotcompMenuImport2 = cmds.menuItem(p=self.op_shotPopupMenu02, label="Import", aob=1, subMenu=1, ann=" ")
        self.op_shotcompMenuImportWorkshop2 = cmds.menuItem(parent=self.op_shotcompMenuImport2, label="Workshop", command="openPipelineImportUI 0 shotComponent workshop", ann=self.anno_importShotComponentWorkshop)
        self.op_shotcompMenuImportWorkshopOpBox2 = cmds.menuItem(ob=1, c="openPipelineImportUI 1 shotComponent workshop")
        self.op_shotcompMenuImportMaster2 = cmds.menuItem(parent=self.op_shotcompMenuImport2, label="Master", command="openPipelineImportUI 0 shotComponent master", ann=self.anno_importShotComponentMaster)
        self.op_shotcompMenuImportMasterOpBox2 = cmds.menuItem(ob=1, c="openPipelineImportUI 1 shotComponent master")
        
        self.op_shotcompMenuReference2 = cmds.menuItem(p=self.op_shotPopupMenu02, label="Reference", aob=1, subMenu=1, ann=" ")
        self.op_shotcompMenuReferenceWorkshop2 = cmds.menuItem(parent=self.op_shotcompMenuReference2, label="Workshop", command="openPipelineReferenceUI 0 shotComponent workshop", ann=self.anno_referenceShotComponentWorkshop)
        self.op_shotcompMenuReferenceWorkshopOpBox2 = cmds.menuItem(ob=1, c="openPipelineReferenceUI 1 shotComponent workshop")
        self.op_shotcompMenuReferenceMaster2 = cmds.menuItem(parent=self.op_shotcompMenuReference2, label="Master", command="openPipelineReferenceUI 0 shotComponent master", ann=self.anno_referenceShotComponentMaster)
        self.op_shotcompMenuReferenceMasterOpBox2 = cmds.menuItem(ob=1, c="openPipelineReferenceUI 1 shotComponent master")
        
        self.op_shotcompMenuArchive2 = cmds.menuItem(p=self.op_shotPopupMenu02, label="Archive...", command="openPipelineArchiveDialog 3 3")
        
        #--------------------------------------------
        #   END Section 4.03.2 - Popup dropdown
        #--------------------------------------------
        
        self.op_shotSubFormLayout02 = cmds.formLayout(parent=self.op_shotColumnLayout02, numberOfDivisions=100)
        self.op_shotComponentNewButton = cmds.button(parent=self.op_shotSubFormLayout02, l="New...", bgc=(.6, .8, .5), w=65, c="openPipelineNewShotComponentUI", ann=self.anno_newShotComponent)
        self.op_shotComponentRemoveButton = cmds.button(parent=self.op_shotSubFormLayout02, l="Delete", bgc=(.8, .3, .3), w=60, c="openPipelineRemoveProcess 3 3", ann=self.anno_removeShotComponent)
        
        cmds.formLayout(
            self.op_shotSubFormLayout02,
            e=1,
            attachPosition=[
                (self.op_shotComponentNewButton, "top", 5, 0),
                (self.op_shotComponentNewButton, "left", 0, 0),
                (self.op_shotComponentNewButton, "right", 0, 50),
                (self.op_shotComponentRemoveButton, "top", 5, 0),
                (self.op_shotComponentRemoveButton, "left", 0, 50),
                (self.op_shotComponentRemoveButton, "right", 0, 100),
            ]
        )
        
        cmds.formLayout(
            self.op_shotComponentsFormLayout,
            e=1,
            attachForm=[
                (self.op_shotComponentsTxt, "left", 0),
                (self.op_shotMenuBarLayout02, "left", 0),
            ],
            attachControl=[
                (self.op_shotMenuBarLayout02, "top", 5, self.op_shotComponentsTxt),
            ],
            attachPosition=[
                (self.op_shotMenuBarLayout02, "right", 0, 100),
            ],
        )	
        
        #--------------------------------------------
        #   END Section 4.03 - "Components"
        #
        #   START Section 4.04 - Lower Contents of "Shot" Tab
        #   this includes view playblast, notes, and the explore location
        #--------------------------------------------
        
        self.op_shotPreviewTxt = cmds.text(parent=self.op_shotFormLayout, fn="smallBoldLabelFont", w=164, l="Preview", al="center")
        self.op_shotPreviewImage = cmds.image(parent=self.op_shotFormLayout, h=105, w=164, i=self.op_defaultPreview_filePath, bgc=(0, 0, 0))
        self.op_shotViewPlayblastButton = cmds.button(parent=self.op_shotFormLayout, l="View Playblast", h=30, w=164, c="openPipelineViewPlayblastSelected 3")
        self.op_shotHistoryTxt = cmds.text(parent=self.op_shotFormLayout, fn="smallBoldLabelFont", l="History", al="center")
        self.op_shotCommentField = cmds.scrollField(parent=self.op_shotFormLayout, w=225, h=80, enable=1, editable=0, wordWrap=1, font="smallPlainLabelFont", text="")
        self.op_shotNotesTxt = cmds.text(parent=self.op_shotFormLayout, fn="smallBoldLabelFont", l="Notes", al="center")
        self.op_shotInfoField = cmds.scrollField(parent=self.op_shotFormLayout, w=225, h=45, enable=1, editable=0, wordWrap=1, font="smallPlainLabelFont", text="")
        self.op_shotLocationTxt = cmds.text(parent=self.op_shotFormLayout, fn="smallBoldLabelFont", l="Location", al="center")
        self.op_shotLocationField = cmds.textField(parent=self.op_shotFormLayout, editable=0, w=345)
        self.op_exploreShotsButton = cmds.button(parent=self.op_shotFormLayout, w=50, align="center", label="explore...", c="openPipelineExploreSelected 3")
        
        #--------------------------------------------
        #   END Section 4.03 - Lower Contents of "Shot" Tab
        #
        #   START Attach elements to op_shotFormLayout
        #--------------------------------------------
        
        cmds.formLayout(
            self.op_shotFormLayout,
            e=1,
            attachPosition=[
                (self.op_shotSeperator01, "left", 0, 0),
                (self.op_shotSeperator01, "top", 5, 0),
                (self.op_shotSeperator01, "right", 0, 100),
                (self.op_shotSeperator02, "left", 0, 0),
                (self.op_shotSeperator02, "right", 0, 100),
                
                (self.op_shotSequenceFormLayout, "left", 0, 0),
                (self.op_shotSequenceFormLayout, "right", 2, 33),
                
                (self.op_shotComponentsFormLayout, "right", 0, 100),
                (self.op_shotComponentsFormLayout, "left", 2, 66),
                
                (self.op_shotShotFormLayout, "left", 2, 33),
                (self.op_shotShotFormLayout, "right", 2, 66),
                
                (self.op_shotPreviewTxt, "left", 0, 0),
                (self.op_shotPreviewImage, "left", 0, 0),
                (self.op_shotViewPlayblastButton, "left", 0, 0),
                
                (self.op_shotHistoryTxt, "right", 0, 100),
                (self.op_shotCommentField, "right", 0, 100),
                (self.op_shotNotesTxt, "right", 0, 100),
                (self.op_shotInfoField, "right", 0, 100),
                
                (self.op_shotLocationTxt, "left", 0, 0),
                (self.op_shotLocationTxt, "right", 0, 100),
                (self.op_shotLocationField, "left", 0, 0),
                (self.op_shotLocationField, "right", 0, 100),
                (self.op_shotLocationField, "right", 0, 80),
                (self.op_exploreShotsButton, "right", 0, 100),
                
            ],
            attachControl=[
                (self.op_shotTabShotBrowserTxt, "top", 5, self.op_shotSeperator01),
                (self.op_shotSeperator02, "top", 0, self.op_shotTabShotBrowserTxt),
                
                (self.op_shotSequenceFormLayout, "top", 5, self.op_shotSeperator02),
                
                (self.op_shotShotFormLayout, "top", 5, self.op_shotSeperator02),
                
                (self.op_shotComponentsFormLayout, "top", 5, self.op_shotSeperator02),
                
                (self.op_shotPreviewTxt, "top", 22, self.op_shotSequenceFormLayout),
                (self.op_shotPreviewImage, "top", 5, self.op_shotPreviewTxt),
                (self.op_shotViewPlayblastButton, "top", 5, self.op_shotPreviewImage),
                
                (self.op_shotHistoryTxt, "top", 22, self.op_shotSequenceFormLayout),
                (self.op_shotHistoryTxt, "left", 5, self.op_shotPreviewImage),
                (self.op_shotCommentField, "top", 5, self.op_shotHistoryTxt),
                (self.op_shotCommentField, "left", 5, self.op_shotPreviewImage),
                (self.op_shotNotesTxt, "top", 5, self.op_shotCommentField),
                (self.op_shotNotesTxt, "left", 5, self.op_shotPreviewImage),
                (self.op_shotInfoField, "top", 5, self.op_shotNotesTxt),
                (self.op_shotInfoField, "left", 5, self.op_shotPreviewImage),
                
                (self.op_shotLocationTxt, "top", 5, self.op_shotInfoField),
                (self.op_shotLocationField, "top", 5, self.op_shotLocationTxt),
                (self.op_exploreShotsButton, "left", 5, self.op_shotLocationField),
                (self.op_exploreShotsButton, "top", 5, self.op_shotLocationTxt),
                
            ],
            attachForm=[
                (self.op_shotTabShotBrowserTxt, "left", 0),
                
                
                
            ]
            )
        
        #--------------------------------------------
        #   END Attach elements to op_shotFormLayout
        #
        #   END Section 4.00 - "Shot Inventory" Tab
        #--------------------------------------------
        
        #   tabLayout editing, giving tabs diff names
        
        cmds.tabLayout(self.op_mainTabs_tabLayout, edit=1, tabLabel=[(self.op_assetBrowser_formLayout, "Asset Browser"), (self.op_shotFormLayout, "Shot Browser"), (self.op_currOpen_formLayout, "Currently Open")])
        
        
        #   columnLayout : Refresh UI
        
        self.op_refreshUI_formLayout = cmds.formLayout(parent=self.op_form1, width=410, numberOfDivisions=100)
        
        self.op_refreshUIButton = cmds.button(h=30, label="Refresh UI", command="openPipelineUI")
        self.op_closeUIButton = cmds.button(h=30, label="Close", command="openPipelineCloseUI", ann=self.anno_close)
        cmds.formLayout(
            self.op_refreshUI_formLayout,
            e=1,
            attachPosition=[
                (self.op_refreshUIButton, "right", 0, 50),
                (self.op_closeUIButton, "left", 0, 50),
                (self.op_refreshUIButton, "left", 0, 0),
                (self.op_refreshUIButton, "bottom", 5, 100),
                (self.op_closeUIButton, "right", 0, 100),
                (self.op_closeUIButton, "bottom", 5, 100),
            ],
        )
        
        
        #--------------------------------------------
        #   START Attach elements to Main Form
        #--------------------------------------------
        
        cmds.formLayout(
            self.op_form1,
            edit=True,
            attachPosition=[
                
                #   Top Drop Down Menu
                (self.op_topDropDown_menuBarLayout, 'top', 0, 0),
                (self.op_topDropDown_menuBarLayout, 'right', self.rtMargin, 100),
                (self.op_topDropDown_menuBarLayout, 'left', self.lfMargin, 0),
                
                #   Section 1.01
                #(self.op_userName_optionMenu, 'left', 100, 0),
                #(self.op_projName_optionMenu, 'right', 100, 100),
                (self.op_projPath_txtField, 'right', self.rtMargin, 100),
                (self.op_projPath_txt, 'left', self.lfMargin, 0),
                (self.op_projName_txt, 'left', self.lfMargin, 0),
                (self.op_userName_txt, 'left', self.lfMargin, 0),
                (self.op_icon_image, 'right', self.rtMargin, 100),
                (self.op_icon_image, 'left', self.lfMargin, 0),
                (self.op_mainTabs_tabLayout, 'right', self.rtMargin, 100),
                (self.op_mainTabs_tabLayout, 'left', self.lfMargin, 0),
                (self.op_refreshUI_formLayout, 'right', self.rtMargin, 100),
                (self.op_refreshUI_formLayout, 'left', self.lfMargin, 0),
                (self.op_refreshUI_formLayout, 'bottom', 10, 100)
                
                
            ],
            attachControl=[
                
                #   Section 1.01
                (self.op_userName_txt, 'top', 8, self.op_topDropDown_menuBarLayout),
                (self.op_userName_optionMenu, 'top', 8, self.op_topDropDown_menuBarLayout),
                (self.op_userName_optionMenu, 'left', 2, self.op_userName_txt),
                (self.op_projManager_btn, 'top', 8, self.op_topDropDown_menuBarLayout),
                (self.op_projManager_btn, 'left', 2, self.op_userName_optionMenu),
                (self.op_projName_txt, 'top', 2, self.op_userName_optionMenu),
                (self.op_projName_optionMenu, 'top', 2, self.op_userName_optionMenu),
                (self.op_projName_optionMenu, 'left', 2, self.op_projName_txt),
                (self.op_projPath_txt, 'top', 2, self.op_projName_optionMenu),
                (self.op_projPath_txtField, 'top', 2, self.op_projName_optionMenu),
                (self.op_projPath_txtField, 'left', 2, self.op_projPath_txt),
                (self.op_icon_image, 'top', 2, self.op_projPath_txtField),
                (self.op_mainTabs_tabLayout, 'top', 10, self.op_icon_image),
                (self.op_mainTabs_tabLayout, 'bottom', 10, self.op_refreshUI_formLayout),
            ]
            )
        
        #--------------------------------------------
        #   END Attach elements to Main Form
        #--------------------------------------------
        
        #--------------------------------------------
        #   END Main Form
        #--------------------------------------------
        
        return [self.op_form1]