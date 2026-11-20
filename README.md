# README for tuya_integration

Copyright Mark McIntyre, 2025

This folder contains configuration and other files for running the tuya-mqtt gateway to capture data from Tuya SmartLife compatible devices and publish it to an MQTT broker.

## Setup

First, on the machine where you intend to run the MQTT gateway, clone required software `tuya-mqtt` and `tuya-local-key`, and this repo `tuya_integration`.

``` bash
cd $HOME/src
git clone  https://github.com/TheAgentK/tuya-mqtt
git clone https://github.com/vineetchoudhary/tuya-local-key.git 
git clone https://github.com/markmac99/tuya_integration.git
```

## Getting Device IDs and Keys

Follow the `CLI` section of the README in `tuya-local-key` to install the software and obtain your Client ID from SmartLife.

Now run the tuya-local-key command:

```bash
cd  $HOME/src/tuya-local-key
.venv/bin/python tuya_devices.py
```

The first time you run this you'll be promted for your Client ID and will then have to scan a QR code. After a few seconds, the device list will be printed on the screen.

Now run the script again, but this time send output to a file `../tuya-mqtt/device_data.txt`.

```bash
cd  $HOME/src/tuya-local-key
.venv/bin/python tuya_devices.py > ../tuya-mqtt/device_data.txt

```

Now run this script to convert the data:

``` bash
cd $HOME/src/tuya-mqtt
python ../tuya_integration/convertDevData.py
```

This will create a `devices.conf` file which lists your discovered devices and their keys and is used by `tuya-mqtt`.

## Installing the MQ gateway

Follow the instructions in `tuya-mqtt`'s README to install the software.

Copy `installservice.sh` and `tuya-mqtt.service` from this repo to the `tuya-mqtt` folder.

Finally, install and start the service

``` bash
bash $HOME/src/tuya-mqtt/installservice.sh
```

The service should start up, and a few seconds later a new Tuya topic should appear in MQTT Explorer.

If the topics don't appear, check you configured the MQ broker details correctly in `config.json`.
