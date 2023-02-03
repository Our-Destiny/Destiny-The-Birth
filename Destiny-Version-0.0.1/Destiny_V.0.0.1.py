'''DESTINY Autonimous Artificial Intelligence Programme (Python 3).
Copyright (c) 2012 - End Of Times | OUR DESTINY (A.A.I) Research And Development Labs,Inc.
All rights reserved. This software or any portion thereof may not be reproduced or used in any manner whatsoever without the development permission of the ODRE Labs, Inc.
Permission for the development of the software is Authorized ONLY for the developers of ODRD Labs, Inc.
Author: OUR DESTINY (A.A.I) Research And Development Labs <hariprasad@ODRDLabs>|<ribin@ODRDLabs>'''

import pyttsx3

print('Destiny V.0.0.1 Python Test Sequence')

destiny_engine = pyttsx3.init()                                                #Destiny Speech Engine Initialization Statement.
destiny_voice = destiny_engine.getProperty('voices')
destiny_engine.setProperty('voice', destiny_voice[0].id)
variable = "hello"
destiny_engine.say(variable)

destiny_engine.say('Initializing Destiny, Basic Test Sequence!')               #Audio Output Of The Initial Text.

destiny_engine.say('Hello, Boss!')                                             #Audio Output Of The Greeting Statement.

destiny_engine.runAndWait()
