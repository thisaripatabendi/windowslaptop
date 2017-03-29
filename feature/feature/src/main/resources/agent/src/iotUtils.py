#!/usr/bin/env python

"""
/**
* Copyright (c) 2015, WSO2 Inc. (http://www.wso2.org) All Rights Reserved.
*
* WSO2 Inc. licenses this file to you under the Apache License,
* Version 2.0 (the "License"); you may not use this file except
* in compliance with the License.
* You may obtain a copy of the License at
*
* http://www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing,
* software distributed under the License is distributed on an
* "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
* KIND, either express or implied. See the License for the
* specific language governing permissions and limitations
* under the License.
**/
"""

import time
import ConfigParser, os
import random
import running_mode

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#           HOST_NAME(IP) of the Device
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
global HOST_NAME
HOST_NAME = "0.0.0.0"
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
HTTP_SERVER_PORT = 5678 # http server port which is listening on

# global LAST_TEMP
# LAST_TEMP = 25  # The Last read temperature value from the DHT sensor. Kept globally

# laptop statistics
global BATTERY_LEVEL
BATTERY_LEVEL = 0
global BATTERY_STATUS
BATTERY_STATUS = 0
global CPU_USAGE
CPU_USAGE = 0

# Windows Agent
DATA_READING_INTERVAL_REAL_MODE = 3
DATA_READING_INTERVAL_VIRTUAL_MODE = 60


global GPIO

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#       Device specific info when pushing data to server
#       Read from a file "deviceConfig.properties" in the same folder level
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
configParser = ConfigParser.RawConfigParser()
configFilePath = os.path.join(os.path.dirname(__file__), './deviceConfig.properties')
configParser.read(configFilePath)

SERVER_NAME = "carbon.super"
DEVICE_OWNER = configParser.get('Device-Configurations', 'owner')
DEVICE_ID = configParser.get('Device-Configurations', 'deviceId')
MQTT_EP = configParser.get('Device-Configurations', 'mqtt-ep')
XMPP_EP = "http://204.232.188.215:5222"
AUTH_TOKEN = configParser.get('Device-Configurations', 'auth-token')
CONTROLLER_CONTEXT = configParser.get('Device-Configurations', 'controller-context')
# MQTT_SUB_TOPIC = configParser.get('Device-Configurations', 'mqtt-sub-topic').format(owner = DEVICE_OWNER, deviceId = DEVICE_ID)
# MQTT_PUB_TOPIC = configParser.get('Device-Configurations', 'mqtt-pub-topic').format(owner = DEVICE_OWNER, deviceId = DEVICE_ID)
DEVICE_INFO = '{{"event":{{"metaData":{{"owner":"' + DEVICE_OWNER + '","type":"windowslaptop","deviceId":"' + DEVICE_ID + '","time":{}}},"payloadData":{{"windowsbatterylevel":{:.2f}, "windowsbatterystatus":{:.2f}, "windowscpuusage":{:.2f}}}}}}}'

HTTPS_EP = configParser.get('Device-Configurations', 'https-ep')
# HTTP_EP = configParser.get('Device-Configurations', 'http-ep')
# APIM_EP = configParser.get('Device-Configurations', 'apim-ep')
# DEVICE_IP = '"{ip}","value":'
# DEVICE_DATA = '"{temperature}"'  # '"{temperature}:{load}:OFF"'



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#       This method generate a random temperature value
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def generateRandomTemperatureAndHumidityValues():
    return [random.randint(15, 40),random.randint(15, 40)]
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#      If an agent runs on a real setup GPIO needs to be imported
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def initGPIOModule():
    if running_mode.RUNNING_MODE == 'N':
        import RPi.GPIO as GPIO
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#       Get the IP-Address of the interface via which the RPi is connected
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def getDeviceIP():
    return "4.0.9.8"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#       Get the port which http server is listening on
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def getHTTPServerPort():
    return HTTP_SERVER_PORT
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#       The Main method of the server script
#           This method is invoked from RaspberryStats.py on a new thread
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
    global HOST_NAME
    # HOST_NAME = getDeviceIP()
    # if running_mode.RUNNING_MODE == 'N':
        # setUpGPIOPins()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == '__main__':
    main()
