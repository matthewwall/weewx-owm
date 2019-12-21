# $Id: install.py 1788 2018-12-30 16:47:23Z mwall $
# installer for OpenWeatherMap
# Copyright 2014 Matthew Wall

from setup import ExtensionInstaller

def loader():
    return OWMInstaller()

class OWMInstaller(ExtensionInstaller):
    def __init__(self):
        super(OWMInstaller, self).__init__(
            version="0.8",
            name='owm',
            description='Upload weather data to OpenWeatherMap.',
            author="Matthew Wall",
            author_email="mwall@users.sourceforge.net",
            restful_services='user.owm.OpenWeatherMap',
            config={
                'StdRESTful': {
                    'OpenWeatherMap': {
                        'appid': 'INSERT_APPID_HERE',
                        'station_id': 'INSERT_STATION_ID_HERE'}}},
            files=[('bin/user', ['bin/user/owm.py'])]
            )
