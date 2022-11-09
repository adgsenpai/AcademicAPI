import requests
import pandas as pd
import urllib.parse
 
def SearchForPapersByAuthor(authorname):
    #encode the author name to be used in the url
    try:
        authorname = urllib.parse.quote(authorname)
        url = 'https://api.openaire.eu/search/publications/?author='+authorname+r'&format=xml'
        #download content from url and save it as xml
        r = requests.get(url)
        with open('api.xml', 'wb') as f:
            f.write(r.content)    
        df = pd.read_xml('api.xml', xpath='.//oaf:result', namespaces={'oaf': 'http://namespace.openaire.eu/oaf'})
        return df
    except:
        return None
    

SearchForPapersByAuthor('Ashlin Darius Govindasamy')
