import urllib2
import json
print "give geographic coordinates"
print "(becareful with the coordinates you give)"
x=raw_input("lat: ")
y=raw_input("lon: ")
url='http://api.openweathermap.org/data/2.5/weather?lat='+x+'&lon='+y+'&appid=d89ab85c7700a2ee6e26475397209c20'
json_obj=urllib2.urlopen(url)#για να ανοιξουμε τη σελιδα με τα δεδομενα
data=json.load(json_obj)#για να αποθηκευσουμε τα δεδομενα που παιρνουμε
for i in data['weather']:
    if i['main']=='Rain':
        print 'i am singing in the rain'
K=data['main']['temp']#μετατροπη της θερμοκρασιας Kelvin που μας δινεται σε celsius
celsius=K-273.15
print celsius
if celsius>20:
    print 'nice'
elif celsius<5:
    print 'brrr...'


        

