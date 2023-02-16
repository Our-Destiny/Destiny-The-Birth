<a href="#"><img width="100%" height="auto" src="https://github.com/Our-Destiny/Destiny-The-Birth/blob/main/Assets/Destiny-The-Birth.png" height="175px"/></a>


<p align="center">
    <img src="https://img.shields.io/badge/Build%20Date-2019%20Mar%2021-blue?style=social&logo=jabber">
    <img alt="Build" src="https://img.shields.io/badge/build-passed-success">
    <img alt="Contributors" src="https://img.shields.io/badge/contributors-2-blue">
    <img alt="Status" src="https://img.shields.io/badge/status-working-success">
    <img alt="Status" src="https://img.shields.io/badge/current%20release-v0.0.1-informational">
    <img alt="Status" src="https://img.shields.io/badge/progress-discontinued-important">
</p>




# The Birth Of Destiny `[This Repo is Incomplete. Stay Tuned For Updates]`
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
usage: [-h] [-c] [-s] [-j] [-v] [-g] [--server API_KEY] [-p PORT]
                  [--version]

optional arguments:
  -h, --help            show this help message and exit
  -c, --cli             Command-line interface mode. Give commands to
                        Destiny via command-line inputs (keyboard) instead
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
  --version             Display the version number of Destiny
```
#### Built-in Commands

```
DESTINY | WAKE UP | HEY
GO TO SLEEP
ENOUGH | SHUT UP
WHO AM I | SAY MY NAME
MY TITLE IS LADY | I'M A LADY | I'M A WOMAN | I'M A GIRL
MY TITLE IS SIR | I'M A MAN | I'M A BOY | CALL ME *
WHAT IS YOUR NAME
WHAT IS YOUR GENDER
FILE MANAGER | OPEN FILES
OPEN (BROWSER | CHROME | FIREFOX)
PHOTOSHOP | PHOTO EDITOR
INKSCAPE | VECTOR GRAPHICS
VIDEO EDITOR
OPEN [CAMERA, CALENDAR, CALCULATOR, STEAM, BLENDER, WRITER, MATH, IMPRESS, DRAW, TERMINAL]
SOFTWARE CENTER
OFFICE SUITE
KEYBOARD *
ENTER | NEW TAB | SWITCH TAB | CLOSE | GO BACK | GO FORWARD
SCROLL LEFT | SCROLL RIGHT | SCROLL UP | SCROLL DOWN
PLAY | PAUSE | SPACEBAR
SHUT DOWN THE COMPUTER
GOODBYE | BYE BYE | SEE YOU LATER
(SEARCH|FIND) * (IN|ON|AT|USING) WIKIPEDIA
(SEARCH|FIND) * (IN|ON|AT|USING) YOUTUBE
(SEARCH|FIND) * (IN|ON|AT|USING) (GOOGLE|WEB)
(SEARCH IMAGES OF|FIND IMAGES OF|SEARCH|FIND) * (IN|ON|AT|USING) (GOOGLE|WEB|GOOGLE IMAGES|WEB IMAGES)
WHAT'S THE TEMPERATURE IN *
WHAT TIME IS IT
```


