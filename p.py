from textwrap import indent
import urllib.request, urllib.parse, urllib.error
import json

ur = urllib.request.urlopen('http://api.teleport.org/api/urban_areas/')
js = json.loads(ur.read().decode())
idented = json.dumps(js["_links"]["ua:item"], indent=4)

c=0
cities = 'none'
di = dict()

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
while True:
        try:
            cities = json.dumps(js["_links"]["ua:item"][c]["name"])
            di[c] = cities
            c = c + 1
        except:
            break
print(idented, di)
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')






