owm - weewx extension that sends data to OpenWeatherMap
Copyright 2014-2020 Matthew Wall

Installation instructions:

1) run the installer:

wee_extension --install weewx-owm.tgz

2) modify weewx.conf:

[StdRESTful]
    [[OpenWeatherMap]]
        appid = OWM_APPID
        station_id = STATION_ID

3) restart weewx

sudo /etc/init.d/weewx stop
sudo /etc/init.d/weewx start
