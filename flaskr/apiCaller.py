import requests

def parseResponse(response):
    if len(response) == 1:
        return displayableLaunch(response[0])
    display_launches = []
    for value in response:
        display_launches.append(displayableLaunch(value))
    return display_launches

def request(action):
    URL =  "http://127.0.0.1:5000/" + action
    request = requests.get(URL)
    return parseResponse(request.json())

class displayableLaunch:
    def __init__(self, data):
        self.id = data['id']
        self.model = data['model']
        self.date = data['date']
        self.success = data['success']
        self.icon = data['icon']
        if 'webcast' in data:
            self.webcast = data['webcast']
