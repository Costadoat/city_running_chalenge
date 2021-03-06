from html.parser import HTMLParser
from html.entities import name2codepoint
from geolocator.geolocator import geolocator
from settings import FOLDER_COURSES


class MyHTMLParser(HTMLParser):

    def __init__(self):
         #Since Python 3, we need to call the __init__() function 
         #of the parent class
         super().__init__()
         self.info = None
         self.course = {}
         self.course['coordinates']=[]
    
    def handle_starttag(self, tag, attrs):
#        print("Start tag:", tag)
        if tag == 'name':
            self.info = 'name'
        elif tag == 'time':
            self.info = 'time'
        elif tag == 'type':
            self.info = 'type'
        else:
            self.info=None
        lat,lon='',''
        for attr in attrs:
#            print("     attr:", attr)
            if attr[0]=='lat':
                lat=attr[1]
            elif attr[0]=='lon':
                lon=attr[1]
        if lat!='' and lon!='':
#            location = geolocator.reverse("%s,%s" % (lat,lon))
            self.course['coordinates'].append((float(lat),float(lon)))
#            print(lat,lon,location.raw['address']['road'])
           
#	print(attr[1])

    def handle_endtag(self, tag):
#        print("End tag  :", tag)
        self.info=None

    def handle_data(self, data):
#        print("Data     :", data)
        if self.info:
            self.course[self.info]=data
            

    def handle_comment(self, data):
        print("Comment  :", data)

    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        print("Named ent:", c)

    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("Num ent  :", c)

    def handle_decl(self, data):
        print("Decl     :", data)


def read_gpx(gpx_file):
    parser = MyHTMLParser()
    file=open(FOLDER_COURSES+'/'+gpx_file,'r')
    contenu=file.read()
    parser.feed(contenu)
    return parser.course
