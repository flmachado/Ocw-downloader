import urllib.request
import sys
import os.path

folder_path = ''
ocw_path = ''

if len(sys.argv) == 2 and (sys.argv[1] == '-h' or sys.argv[1] == '--help'):
    print("help")
    
if len(sys.argv) < 3:
    sys.exit("A path to ocw and to a folder is needed")

ocw_path = sys.argv[1]
folder_path = sys.argv[2]

#if os.path.isdir(folder_path):
#    os.makedirs(folder_path)

# Open the video lecture url provided and get the links to each lecture
base_url = "ocw.mit.edu/"
beg = ocw_path.fing(base_url) + len(base_url)
path = path[beg:end]
if path[-1]!="/":
    path += "/"
lecture_url = []

response = urllib.request.urlopen(ocw_path)
html = str(response.read())
index = html.find(path)
while (index != -1):
    print(index)
    end = html.find('"', index)
    print(end)
    print(html[index:end])
    lecture_url.append(html[index:end])
    index = html.find(path, index+1)

print(lecture_url)

for i,url in enumerate(lecture_url):
    response = urllib.request.urlopen("http://ocw.mit.edu/" + url)
    html = str(response.read())
    start = html.find('http://www.archive.org/download')
    end = html.find('"', start)
    
    download_link = html[start:end]

    print("Downloading "+download_link) 
    urllib.request.urlretrieve(download_link, folder_path + "/Lecture" + str(i)+ ".mp4")


    
