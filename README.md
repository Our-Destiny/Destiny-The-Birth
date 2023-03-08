<a href="#"><img width="100%" height="auto" src="https://github.com/Our-Destiny/Destiny-The-Birth/blob/main/Assets/Birth-Of-Destiny-Wall.pngo" height="175px"/></a>


<p align="center">
    <img src="https://img.shields.io/badge/Build%20Date-2019%20Mar%2021-blue?style=social&logo=jabber">
    <img alt="Build" src="https://img.shields.io/badge/build-passed-success">
    <img alt="Contributors" src="https://img.shields.io/badge/contributors-2-blue">
    <img alt="Status" src="https://img.shields.io/badge/status-working-success">
    <img alt="Status" src="https://img.shields.io/badge/current%20release-v0.0.1%20to%20v0.0.7-informational">
    <img alt="Status" src="https://img.shields.io/badge/progress-discontinued-important">
</p>




# The Birth Of Destiny

`This repository contains the initial steps taken and [The First 10 Lines of Code Created] by the founders M.S Hariprasad and Ribin Baby as a part of learning to create a basic rule-based skeleton for Destiny.`

---


A python-based text-to-speech engine using the pyttsx3 module integrated into a simple if-else-driven logical skeleton to collect input and provide predefined output for the user input. We have created a minimal console script without any Graphical User Interface(GUI) and limited commands. We have included seven versions in this repository. All the versions are nothing but minor changes to the code as adding typing animations for printing output, etc. These might not be major developments, but was very helpfull at the time of development to keep going.

**The First 10 Lines Of Code [ `This is a reminder that Getting Started will be hard and you don't have to be great to get started.` ]**

 ```python

    import pyttsx3
    
    print('Destiny V.0.0.1 Python Test Sequence')
    
    # Destiny Speech Engine Initialization Statement.
    
    destiny_engine = pyttsx3.init()                                                
    
    destiny_voice = destiny_engine.getProperty('voices')
    
    destiny_engine.setProperty('voice', destiny_voice[0].id)
    
    variable = "hello"
    
    destiny_engine.say(variable)
    
    # Audio Output Of The Initial Text.
    
    destiny_engine.say('Initializing Destiny, Basic Test Sequence!')   
    
    # Audio Output Of The Greeting Statement.
    
    destiny_engine.say('Hello, Boss!')                                             
    
    destiny_engine.runAndWait()
```

---

## Built-in Commands

```
DESTINY | HONEY
WHATS THE TIME
PLAY MUSIC
THANK YOU
BYE | QUIT
```
---

## Features

- `Cross-platform` targeted design configuration.
- Simple speech engine and easy to configure.
- `Sapi5` Voice Support.
- Uses `Ivona Text To Speech Engine` Voices.
- `Works Completely Offline.`
- Threaded Speech with Printing on command line.
- Adaptive Hotword Reply (Greet By Time).

---


## Prerequisite Installation

**Install Python Version 3.7.6 - 64Bit Interpreter**

```bash
https://www.python.org/downloads/release/python-376/

```
**Pip Command to install the Library used for Text-to-Speech**

```bash
pip install pyttsx3==2.7

```
**Download IVONA 2 Salli - US English female voice [22kHz]**
```bash
https://nextup.com/ivona/

```
---

## Supported Environments

|                         |                                         |
|-------------------------|-----------------------------------------|
| **Operating systems**   | Linux & Windows                         |
| **Python versions**     | Python 3.7.6 (64-bit)                   |
| **Distros**             | Ubuntu, Windows 8, 8.1 Pro, 10 (All Distros)         |
| **Package managers**    | APT, pip                                |
| **Languages**           | English                                 |
| **System requirements** | 2GB of free RAM, Intel i3 - Any Higher  |
|                         |                                         |

---

> ***And The Journey Of Our Destiny Begins....***
