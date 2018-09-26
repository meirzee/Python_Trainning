# Meir Zeevi
# Sep 17th 2018
# working with URL pages for testing Jenkins performance.
# Fetching data across the Web


import urllib.request
import webbrowser


# Open URL for reading - will 

with urllib.request.urlopen('http://indlin2201:18080/job/CRM_Upload_HF_To_Sites/graph/') as response:
    html = response.read()
    print (html)



#Open a web URL like selenume
url="http://indlin2201:18080/job/CRM_Upload_HF_To_Sites/graph/";
webbrowser.open(url,3);




#Open Jenkind Consol Log
#Open Jenkins Job Configuration



