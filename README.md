# README for tuya_integration

Copyright Mark McIntyre, 2025

This folder contains configuration and other files for running the tuya-mqtt gateway to capture data from Tuya SmartLife compatible devices.

## Setup

First clone required software `tuya-mqtt` and `tuya-local-key`, and this repo `tuya_integration`

``` bash
cd $HOME/src
git clone  https://github.com/TheAgentK/tuya-mqtt
git clone https://github.com/vineetchoudhary/tuya-local-key.git 
git clone https://github.com/markmac99/tuya_integration.git
```

## Getting Device IDs and Keys

Follow the README in `tuya-local-key` to get the device IDs and keys for your devices.

Copy `devices.conf.sample` in this repo to `devices.conf`, and update the file with your device IDs and Keys. Use double-quotes if any key contains special characters.

## Installing the MQ gateway

Follow the instructions in `tuya-mqtt`'s README to install the software.

Copy `devices.conf`. `installservice.sh` and `tuya-mqtt.service1` from this repo to `$HOME/src/tuya-mqtt`.

Finally, install and start the service

``` bash
bash $HOME/src/tuya-mqtt/installservice.sh
```
