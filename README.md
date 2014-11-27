rpi-monitor-dht
===============

The files needed to extend RPi-Monitor and show a DHT sensor data.

## Introduction ##

[RPi-Monitor](http://rpi-experiences.blogspot.com.br/p/rpi-monitor.html) is a nice monitoring tool for your Raspberry Pi. It provides a web view where you can watch things such as memory, CPU and temperature. It also can be easily extended to show the temperature and humidity read by a DHT sensor.

![Stats](https://raw.githubusercontent.com/lzkill/rpi-monitor-dht/master/stats.jpg)

## License ##

These files may be used under the terms of the MIT License, wich a [copy](LICENSE) is included in the download.

## Dependencies ##

- [Python](https://www.python.org) 2.6 or greater
- [Stem](https://stem.torproject.org) 1.2.2 or greater
- [Adafruit DHT library](https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/software-install-updated)
- [Supervisor](http://supervisord.org)

## Configuration ##

- Copy [dht.conf](dht.conf) to `/etc/rpimonitor/template/`
- Add the following line to `/etc/rpimonitor/data.conf`
```
include=/etc/rpimonitor/template/dht.conf
```
- Copy [dht.jpg](dht.png) to `/usr/share/rpimonitor/web/img`
- Copy [__dht.conf](__dht.conf) to `/etc/supervisor/conf.d/dht.conf`
- Modify `/etc/supervisor/conf.d/dht.conf` with your sensor model (11, 22 or 2302) and RPi pin
- Run `sudo groupadd supervisor;sudo usermod -a -G supervisor pi`
- Modify `/etc/supervisor/supervisord.conf` with the following:
```
[unix_http_server]
file=/var/run/supervisor.sock
chmod=0770
chown=root:supervisor
```
- Run `sudo mkdir /usr/local/sbin/rpimonitor/`
- Copy [dht.py](dht.py) to `/usr/local/sbin/rpimonitor`  
- Logout/login and run `sudo service supervisor restart;sudo service rpimonitor restart`

## Your Improvements ##

If you add improvements to these files please send them to me as pull requests on GitHub. I will add them to the next release so that everyone can enjoy your work. You might also benefit from it as others may fix bugs in your files or may continue to enhance them.

## Credits ##

This extension contains code written by the folks at [Adafruit](https://github.com/adafruit/Adafruit_Python_DHT).

## Thanks ##

With regards from

[Luiz Kill](mailto:me@lzkill.com)

