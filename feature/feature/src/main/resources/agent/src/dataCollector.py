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
import os
import subprocess

import multiprocessing

from ctypes import *

class PowerClass(Structure):
    _fields_ = [('ACLineStatus', c_byte),
            ('BatteryFlag', c_byte),
            ('BatteryLifePercent', c_byte),
            ('Reserved1',c_byte),
            ('BatteryLifeTime',c_ulong),
            ('BatteryFullLifeTime',c_ulong)]


def getBatteryLevel():

    powerclass = PowerClass()
    result = windll.kernel32.GetSystemPowerStatus(byref(powerclass))
    # print "BATTRY LEVEL"
    battery_level =  (powerclass.BatteryLifePercent)
    # print "BATTERY STATUS"
    # print (powerclass.ACLineStatus)

    return int(battery_level)


def getBatteryStatus():

    powerclass = PowerClass()
    result = windll.kernel32.GetSystemPowerStatus(byref(powerclass))

    # print "BATTERY STATUS"
    battery_status =  (powerclass.ACLineStatus)

    return battery_status

def getCPUUsage():

    """ Returns a list CPU Loads"""
    result = []
    cmd = "WMIC CPU GET LoadPercentage "
    response = os.popen(cmd + ' 2>&1', 'r').read().strip().split("\r\n")
    for load in response[1:]:
        result.append(int(load))

    result = str(result)
    temp = result.split('[')[1]
    cpuusage = temp.split(']')[0]

    return int(cpuusage)
