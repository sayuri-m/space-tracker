import requests
from .launchEntity import LaunchEntity

class GetLaunches:
# curl --location --request GET 'https://api.spacexdata.com/v4/launches/latest'
    def getLastLaunch():
        URL = 'https://api.spacexdata.com/v4/launches/latest'
        request = requests.get(URL)
        response = request.json()
        return LaunchEntity(response)

# curl --location --request GET 'https://api.spacexdata.com/v4/launches/next'
    def getNextLaunch():
        URL = 'https://api.spacexdata.com/v4/launches/next'
        request = requests.get(URL)
        response = request.json()
        return LaunchEntity(response)

# curl --location --request GET 'https://api.spacexdata.com/v4/launches/upcoming'
    def getUpcomingLaunch():
        URL = 'https://api.spacexdata.com/v4/launches/upcoming'
        request = requests.get(URL)
        response = request.json()
        display_launches = []
        for entry in response[0:5]:
            display_launches.append(LaunchEntity(entry))
        return display_launches;


# curl --location --request GET 'https://api.spacexdata.com/v4/launches/past'
    def getPastLaunch():
        URL = 'https://api.spacexdata.com/v4/launches/past'
        request = requests.get(URL)
        response = request.json()
        display_launches = []
        for entry in response[0:5]:
            display_launches.append(LaunchEntity(entry))
        return display_launches;
