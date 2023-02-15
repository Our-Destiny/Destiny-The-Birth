<a href="#"><img width="100%" height="auto" src="https://github.com/Our-Destiny/Destiny-The-Birth/blob/main/Assets/Destiny-The-Birth.png" height="175px"/></a>


<p align="center">
    <img src="https://img.shields.io/badge/Build%20Date-2019%20Mar%2021-blue?style=social&logo=jabber">
    <img alt="Build" src="https://img.shields.io/badge/build-passed-success">
    <img alt="Contributors" src="https://img.shields.io/badge/contributors-2-blue">
    <img alt="Status" src="https://img.shields.io/badge/status-working-success">
    <img alt="Status" src="https://img.shields.io/badge/current%20release-v0.0.1-informational">
    <img alt="Status" src="https://img.shields.io/badge/progress-discontinued-important">
</p>




# The Birth Of Destiny
### Destiny-Version-0.0.1 



A Python based simple text to speech engine.
First initiative step taken in the development for Project Destiny.
In theory, Destiny is an Autonomus Artificial Intelligence Based Digital Assistant designed to
enhance human life and ensure privacy to data and security to life.
Version Control For This Project Is Completely Based On Evolution Of The Project.
## Features

- `Cross-platform` targeted design configuration.
- Simple speech engine and easy to configure.
- Sapi5 Voice Support.
- Uses Ivona Text To Speech Engine Voices.
- Works Completely Offline


## Installation

Install python interpreter version

```bash
Python Version 3.7.6

```
Library used for text to speech

```bash
pip install pyttsx3==2.7

```
Ivona Voice Used
```bash
IVONA 2 Salli - US English female voice [22kHz]

```


 ```python
    import time
    #The current epoch time
    current_time = time.time()
    #Set the time for a minute
    event_activation_time = current_time+60
```


#### Supported Environments

|                         |                                         |
|-------------------------|-----------------------------------------|
| **Operating systems**   | Linux                                   |
| **Python versions**     | Python 3.x (64-bit)                     |
| **Distros**             | KDE neon, elementary OS, Ubuntu         |
| **Package managers**    | APT, pip                                |
| **Languages**           | English                                 |
| **System requirements** | preferably a [CUDA supported GPU](https://www.geforce.com/hardware/technology/cuda/supported-gpus), 2GB of free RAM   |
|                         |                                         |

```
usage: dragonfire [-h] [-c] [-s] [-j] [-v] [-g] [--server API_KEY] [-p PORT]
                  [--version]

optional arguments:
  -h, --help            show this help message and exit
  -c, --cli             Command-line interface mode. Give commands to
                        Dragonfire via command-line inputs (keyboard) instead
                        of audio inputs (microphone).
  -s, --silent          Silent mode. Disable Text-to-Speech output. Dragonfire
                        won't generate any audio output.
  -j, --headless        Headless mode. Do not display an avatar animation on
                        the screen. Disable the female head model.
  -v, --verbose         Increase verbosity of log output.
  -g, --gspeech         Instead of using the default speech recognition
                        method(Mozilla DeepSpeech), use Google Speech
                        Recognition service. (more accurate results)
  --server API_KEY      Server mode. Disable any audio functionality, serve a
                        RESTful spaCy API and become a Twitter integrated
                        chatbot.
  -p PORT, --port PORT  Port number for server mode.
  --version             Display the version number of Dragonfire.
```
