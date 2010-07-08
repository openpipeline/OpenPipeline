'''
import sys
sys.path.append("/Volumes/KICKSTAND/DEV/openPipeline/openpipeline")

import OpenPipeline as op
reload(op)

op.OpenPipeline().ui()
'''

import os

class OpenPipeline:
    def __init__(self):
        # can we tell which app we're using? or set it?
        print "the BIG __init__"
        pass
        
    def ui(self):
        from core.file import inventory
        reload(inventory)

        from core.version import Version
        reload(Version)
        
        from core.file import master
        reload(master)

        from core.file import workshop
        reload(workshop)
        
        from core.notes import notes
        reload(notes)
        
        from app.maya.file import file as mayafile
        reload(mayafile)
        
        project = os.path.join("/Volumes", "KICKSTAND", "PROJECTS", "DEV")
        module = "lib"
        type = "characters"
        asset = "woman"
        component = "model"
        elements = [project, module, type, asset, component]
        
        inv = inventory.Inventory(elements).list()
        print inv
        for item in inv:
            path = inventory.Inventory(elements).getPath()
            fullpath = os.path.join(path, item)
            print fullpath
            
            versions = Version.Version().all(fullpath)
            print ("versions:")
            print versions
            
            hasMaster = master.Master().query(fullpath)
            if hasMaster == 1:
                print(item + ": mastered")
            else:
                print(item + ": not mastered")
            
            hasNotes = notes.Notes().query(fullpath, item)
            if hasNotes == 1:
                print(item + ": has notes")
            else:
                print(item + ": no notes")
                
            getLatestWorkshopNumber = Version.Version().latest(fullpath)
            if getLatestWorkshopNumber != None:
                latestWorkshop = workshop.Workshop().open(fullpath, item, getLatestWorkshopNumber)
                mayafile.open(latestWorkshop)
                