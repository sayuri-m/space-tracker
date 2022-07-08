import requests
from .launchEntity import LaunchEntity

def makeRequest(action):
    URL = 'https://api.spacexdata.com/v4/launches/'+ action
    request = requests.get(URL)
    return request.json()

class GetLaunches:
    def getLastLaunch():
        response = makeRequest('latest')
        return LaunchEntity(response)

    def getNextLaunch():
        response = makeRequest('next')
        return LaunchEntity(response)

    def getUpcomingLaunch():
        response = makeRequest('upcoming')
        display_launches = []
        for entry in response[0:5]:
            display_launches.append(LaunchEntity(entry))
        return display_launches;

    def getPastLaunch():
        response = makeRequest('past')
        display_launches = []
        for entry in response[0:5]:
            display_launches.append(LaunchEntity(entry))
        return display_launches;
