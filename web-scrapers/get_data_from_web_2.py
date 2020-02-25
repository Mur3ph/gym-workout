#Python version 2 for reading data from a web page 
#import lidrary
import urllib

#open url page for reading various pages
htmlFile = urllib.urlopen("http://www.rte.ie/news/")

#store data in variable
htmltext = htmlFile.read()

#find the html tag <title>
start_title = htmltext.find('<title>')

#find the ending html tag </title>
end_title = htmltext.find('</title>', start_title)

# Start tag plus 7 or 8 characters of the html tag
title_text = htmltext[start_title + 7:end_title]

print(title_text)