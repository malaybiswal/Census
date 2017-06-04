import requests
url='https://maps.googleapis.com/maps/api/geocode/json?address='
#add='Nucleus+1+Pune+Maharashtra+411001+India'
add="Dhabalagiri+jajpur+Road+Orissa+India"
url=url+add
response = requests.get(url)
resp_json_payload = response.json()
#print(resp_json_payload['results'][0]['geometry']['location'])
lat=resp_json_payload['results'][0]['geometry']['location']['lat']
lng=resp_json_payload['results'][0]['geometry']['location']['lng']
print(lat,lng)
