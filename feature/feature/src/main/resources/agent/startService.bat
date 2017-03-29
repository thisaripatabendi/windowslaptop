@echo off

REM ------------------------------------------------------------------------

REM Copyright (c) 2016, WSO2 Inc. (http://www.wso2.org) All Rights Reserved.

REM WSO2 Inc. licenses this file to you under the Apache License,
REM Version 2.0 (the "License"); you may not use this file except
REM in compliance with the License.
REM You may obtain a copy of the License at

REM http://www.apache.org/licenses/LICENSE-2.0

REM Unless required by applicable law or agreed to in writing,
REM software distributed under the License is distributed on an
REM "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
REM KIND, either express or implied. See the License for the
REM specific language governing permissions and limitations
REM under the License.

REM -------------------------------------------------------------------------


echo ----------------------------------------------------------------
echo 	                 WSO2 IOT Sample
echo 		              Agent
echo 	                 ----------------
echo                 ....initializing startup-script
echo ----------------------------------------------------------------


REM Check if the glob gets expanded to existing files.
REM If not, f here will be exactly the pattern above
REM and the exists test will evaluate to false.

if exist deviceConfig.properties (
	echo Configuration file found......
) else (
    echo 'deviceConfig.properties' file does not exist in current path. \nExiting installation...
)

REM install mqtt dependency


REM now we are in the windowslapagent folder
REM want to copy the file from the current folder to one folder ahead
copy deviceConfig.properties src

REM run the agent file
python .\src\agent.py

echo --------------------------------------------------------------
echo 	            Successfully Started
echo	                 --------------------------
