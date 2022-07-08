import urllib
from os.path import exists

class LaunchEntity:
    def __init__(self, data):
        self.id = data['id']
        self.model = data['name']
        self.date = data['date_utc']
        self.success = data['success']
        self.icon = data['id'] + '.png'

        if data['links']['webcast']:
            self.webcast = data['links']['webcast']
            pass

        if data['links']['patch']['large'] :
            icon_path = 'flaskr/static/'+ data['id']+'.png'
            if not exists(icon_path):
                urllib.request.urlretrieve(data['links']['patch']['large'], icon_path)
                pass
            pass
