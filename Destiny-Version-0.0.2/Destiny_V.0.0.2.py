'''DESTINY Autonimous Artificial Intelligence Programme (Python 3).
Copyright (c) 2012 - End Of Times | OUR DESTINY (A.A.I) Research And Development Labs,Inc.
All rights reserved. This software or any portion thereof may not be reproduced or used in any manner whatsoever without the development permission of the ODRE Labs, Inc.
Permission for the development of the software is Authorized ONLY for the developers of ODRD Labs, Inc.
Author: OUR DESTINY (A.A.I) Research And Development Labs <hariprasad@ODRDLabs>|<ribin@ODRDLabs>'''


import pyttsx3


print('Destiny V.0.0.2 Python Test Sequence')


destiny_engine = pyttsx3.init()                                                #Destiny Speech Engine Initialization Statement.
destiny_engine.setProperty('voice', 'malayalam')


print('\nInitializing Destiny, Basic Test Sequence.')                          #Text Output Of The Initial Text.
destiny_engine.say('Initializing Destiny, Basic Test Sequence.')               ##Audio Output Of The Initial Text.


print('\nHello, Boss!')                                                        #Text Output Of The Greeting Statement.
destiny_engine.say('Hello, Boss!')                                             ##Audio Output Of The Greeting Statement.


destiny_engine.runAndWait()
