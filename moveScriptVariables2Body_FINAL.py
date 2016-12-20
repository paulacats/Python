import re
import os
import fileinput

'''
This script updates redirection files. 
It moves the scripts inside the body tags, so that when the master pages are applied, 
the redirection scripts continue to work. 

Error checking nor traversing a directory are not yet implemented.
'''

#set the working directory
path = 'C:\\Users\\hodgkinp\\Desktop\\inProcess'
os.chdir(path)


#create the hook
#bodyOldText = "<body onLoad=\"SimpleRedirect(TopicModuleURL)\" />"
bodyOldText = "<body onLoad=\"SimpleRedirect(TopicModuleURL)\">"
#bodyNewText = "<body><script language=\"JavaScript\" src=\"../../../infrastructure/scripts/redirection.js\"></script><script language=\"JavaScript\">/*<![CDATA[*/	window.onload = function(){SimpleRedirect(TopicModuleURL);}; /*]]>*/ </script></body>"
bodyNewText = "<body><script language=\"JavaScript\" src=\"../Resources/scripts/redirection.js\"></script><script language=\"JavaScript\">/*<![CDATA[*/	window.onload = function(){SimpleRedirect(TopicModuleURL);}; /*]]>*/ </script></body>"

for files in os.listdir(path):
	with fileinput.FileInput(files, inplace=True) as file:  
		for line in file:
			print(line.replace(bodyOldText, bodyNewText))

#set up search
searchTextRegex = re.compile(r'var TopicModuleURL=\"(.*)htm\"')

#make a list of the URL variables
myURLList = []
stringSearchText = "var TopicModuleURL="
stringFunctionCall = "window.onload = function(){SimpleRedirect(TopicModuleURL);};"
#get list URL variables from files
for files in os.listdir(path):
	f = open(files,'r')
	filedata = f.readlines()
	searchText = searchTextRegex.findall(str(filedata))
	theSearchText = "".join(searchText) + "htm""\""
	#add the quotes
	theSearchTextQuotes =  "\"" + theSearchText + ";"
	stringSearchText += theSearchTextQuotes
	myURLList.append(stringSearchText)
	stringSearchText ="var TopicModuleURL="
	f.close()

#Add the URL variables to the files
i=0
for files in os.listdir(path):
	with fileinput.FileInput(files, inplace=True) as file:  
		for line in file:
			print(line.replace(stringFunctionCall, ((str(myURLList[i]))+ "  " + stringFunctionCall)), end='')
	i+=1

print("File updates complete")

#http://stackoverflow.com/questions/4205854/python-way-to-recursively-find-and-replace-string-in-text-files
