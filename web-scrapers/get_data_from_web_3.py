import urllib.request
with urllib.request.urlopen('http://www.rte.ie/news/') as response:

   #get http status code (i.e. 200 http status code = ok) - str is a method to make it a string/text
   print(str(response.getcode()))
   
   #store all html from rte page in variable
   html_data = response.read().decode("utf-8")
   
   #find the html tag <title>
   start_title_tag = html_data.find('<title>')
   
   #find the ending html tag </title>
   end_title_tag = html_data.find('</title>', start_title_tag)
   
   # Start tag plus 7 or 8 characters of the html tag
   title_text = html_data[start_title_tag + 7:end_title_tag]
   
   # Print text in between html title tags
   print(title_text)