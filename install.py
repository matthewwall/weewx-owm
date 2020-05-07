# installer for OpenWeatherMap
# Copyright 2014 Matthew Wall
# Distributed under the terms of the GNU Public License (GPLv3)

from weecfg.extension import ExtensionInstaller

def loader():
    return OWMInstaller()

class OWMInstaller(ExtensionInstaller):
    def __init__(self):
        super(OWMInstaller, self).__init__(
            version="0.9",
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
