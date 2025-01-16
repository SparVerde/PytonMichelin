import requests
from pprint import pp, pprint
import json

#requests.get('https://icanhazdadjoke.com')#add the link wit get function
BASE_UL ="https://icanhazdadjoke.com"
API_PAGE ='' #'/api' if no json
URL = BASE_UL + API_PAGE

header_dict = {
    "Accept":"application/json"
}

response = requests.get(URL, headers=header_dict)
print(response.status_code)
print(response.text)

json_response = json.loads(response.text)
print(type(json_response))
pprint(json_response)


pp(response.text)

#file_handler = open('joke.html','w') #need a name of file for open function, in opening mode: in write mode it is "w" ('joke.html','w') if html
with open('joke.json','w') as file_handler:
    file_handler.write(response.text)
#file_handler.close() with html we should close it
# we need to translate the file, format: text (headers) + json / plain text