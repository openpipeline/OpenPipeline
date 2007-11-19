import fnmatch
import os
import re
import datetime

#returns a list of all MEL files under the given folder
def getMelFiles(folder):
    return [folder+"/"+filename for filename in os.listdir(folder) if fnmatch.fnmatch ( filename, '*.mel' )]

#returns whether the given folder is a valid openPipeline folder (contains "openPipeline.mel" file and "openPipeline" folder)
def isValidOpFolder(folder):
    return os.path.exists(folder) and os.path.exists(folder+"/openPipeline")

#returns a dictionary of all the scripts and their comments
#keys = script filenames (string), data = procedures and info for that file (dictionary)
def getAllComments(scriptPath):
    allComments = {}
    if (isValidOpFolder(scriptPath)):
        opPath = scriptPath+"/openPipeline"
        scriptFiles = [scriptPath+"/openPipeline.mel"]
        scriptFiles.extend(getMelFiles(opPath))
        for script in scriptFiles:
            allComments[os.path.basename(script)] = getComments(script)
    else:
        print scriptPath+" is not a valid openPipeline script path.  Please manually set the script path at the bottom of the openPipelineCreateProcDoc.py file."
    return allComments

#returns a dictionary of all procedures and their info for the given script file
#keys = procedure names (string), data = comments (string)
def getComments(filename):
    p = re.compile('//#+')
    p2 = re.compile('//')
    p3 = re.compile('[ ]*//[ ]*[Nn][Aa][Mm][Ee][ ]*:')
    try:
        f = open(filename, "r")
        comments = {}
        currProc=""
        currComments=""
        write = 0
        for line in f.readlines():
            if (write):
                m = p3.match(line)
                if (m):
                    currProc = line[m.end():(len(line)-1)]
                elif p2.match(line) and not (p.match(line)):
                    currComments += line[2:len(line)]
            if (p.match(line)):
                if (write):
                    comments[currProc] = currComments
                    currComments=""
                    write = 0
                else:
                    write = 1
        return comments
        f.close()
    except IOError:
        print("Warning: " + filename+ " could not be opened for reading!")


#given a dictionary of all relevant info, writes the info to the given html file in a readable format
def htmlWriter(comments, filename):
    files = comments.keys()
    try:
        f = open(filename, 'w')
        f.write('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN""http://www.w3.org/TR/html4/loose.dtd">\n<html>\n<head>\n<title>openPipeline for Maya Procedure Overview</title>\n<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">\n</head>\n<body>\n')
        f.write('<a name="top"><h1>openPipeline for Maya Procedure Documentation ('+datetime.date.today().strftime("%b. %d, %Y")+')</h1></a>\n')
        i = 0
        for script in files:
            f.write('<a href="#' + script + '">' + script + '<a><br>\n')
            i+=1
        i = 0
        for script in files:
            
            f.write('<a name="'+script+'"><h2>'+script+'</h2></a>\n')
            procDictionary = comments[script]
            procs = procDictionary.keys()
            for proc in procs:
                f.write('<h4>'+proc+'</h4>\n')
                f.write(re.sub("\n","<br>",(procDictionary[proc])))
                
            f.write('<a href="#top">back to top</a>\n')
            i+=1
        f.write('<br><br><br><i>This file was created by the openPipelineCreateProcDoc.py script.</i>\n')
        f.write('</body>\n</html>\n')
        f.close()
    except IOError:
        print(filename+" could not be opened/created for writing. Please make sure the script path you specified contains an 'openPipeline' folder.")

#given the maya scriptPath and an html filename, retrieves the openPipeline procedure info and writes it to the html file
def openPipelineCreateProcDoc(scriptPath, htmlFile):
    htmlWriter(getAllComments(scriptPath),htmlFile)
               
if __name__ == "__main__":
    #edit the path and filename below before using this script:
    #the maya script path that contains your openPipeline.mel file and openPipeline folder:
    scriptPath = "[insert path here]"
    htmlFile = scriptPath+"/openPipeline/openPipelineProcedures.html"
    openPipelineCreateProcDoc(scriptPath, htmlFile)

