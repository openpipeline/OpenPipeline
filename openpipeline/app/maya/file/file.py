import maya.cmds as cmds

def open(path):
    cmds.file(path, f=True, o=True)
