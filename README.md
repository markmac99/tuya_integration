# README for anker_integration

This folder contains configuration and other files for running the anker-mqtt gateway to capture data from your Solarbank E5000 to an MQTT broker.

## Setup

First clone required software `anker-mqtt-gateway` and this repo `anker_integration`

``` bash
cd $HOME/src
git clone https://github.com/netwdev/anker-mqtt-gateway.git
git clone https://github.com/markmac99/anker_integration.git
```

In this repo, configure the `.env` file with your settings.

Now copy the below files from this repo to `$HOME/src/anker-mqtt-gateway`:

``` bash
getdata.sh
ankermq.service
installservice.sh
.env
```

Create a conda runtime environment called `anker`

``` bash
conda create -n anker
```

Install the requirements in the environment

``` bash
conda activate anker
pip install -r $HOME/src/anker-mqtt-gateway/requirements.txt

Finally, install and start the service

``` bash
bash ./installservice.sh
```
