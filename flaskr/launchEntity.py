import urllib
from os.path import exists

class LaunchEntity:
    def __init__(self, data):
        self.date = data['date_utc']
        self.id = data['id']
        self.icon = data['id'] + '.png'
        self.model = data['name']
        self.success = data['success']
        
        if data['links']['webcast']:
            self.webcast = data['links']['webcast']
            pass

        if data['links']['patch']['large'] :
            icon_path = 'flaskr/static/'+ data['id']+'.png'
            if not exists(icon_path):
                urllib.request.urlretrieve(data['links']['patch']['large'], icon_path)
                pass
            pass
