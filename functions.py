from keys import *
from place import *
import requests
import json
from pprint import pprint

city = "San Francisco"
choice = "Art Museums"

def getPlaces(city , choice):
    print(city)
    print(choice)
    places = []
    ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
    HEADERS = {'Authorization': 'Bearer %s' % API_KEY}
    PARAMETERS = {'term': choice,
                    'limit': 1,
                    'radius': 10000,
                    'location': city,
                    'limit': 10,
                    'offset': 1
                    }
    response = requests.get(url = ENDPOINT , params = PARAMETERS, headers = HEADERS)
    buisness_data = response.json()
    #pprint(buisness_data)
    for biz in buisness_data['businesses']:
        name = biz['name']
        address = biz['location']['display_address']
        number = biz['display_phone']
        photo = biz['image_url']
        #statement ="Name : ", name , "\n" ,"Location: " , address , "\n" ,"Phone Number: " , str(number) , "\n"

        #newplace = Place(name , address , number , photo)
        newplace = {
            'name': name,
            'address': address,
            'number': number,
            'photo' : photo
        }
        places.append(newplace)

    return places
