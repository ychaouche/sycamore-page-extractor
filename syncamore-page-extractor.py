import BeautifulSoup as bs
import sys
import os.path
reload(sys)
sys.setdefaultencoding("utf-8")


#####################################
#                                   #
#      ##### CONFIGURE ME #####     #
#                                   #
#####################################


DIRECTORY         = "./PAGES/"    
SLASH_REPLACEMENT = "_slash_"     
IMPORT_FILE       = "wikispot"    
if len(sys.argv) > 1:
    IMPORT_FILE = sys.argv[1]

print "preparing the soup for",IMPORT_FILE,"..."
soup = bs.BeautifulSoup(open(IMPORT_FILE).read())
print "soup is ready !"
for page in soup.findAll("page"):
    page_name = page.get("name")
    page_path = DIRECTORY + page_name.replace("/",SLASH_REPLACEMENT)
    print "getting page",page_name
    if os.path.exists(page_path):
        print "this page already exists, nothing else to do..."
        continue
    text = page.find("text")
    if text:
        page_file = open(page_path,"w")
        print "writing the content to",page_path
        page_file.write(text.text)
        page_file.close()
    else:
        print "no content found"




