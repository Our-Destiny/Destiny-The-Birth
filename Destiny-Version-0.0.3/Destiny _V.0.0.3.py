'''DESTINY Autonimous Artificial Intelligence Programme (Python 3).
Copyright (c) 2012 - End Of Times | OUR DESTINY (A.A.I) Research And Development Labs,Inc.
All rights reserved. This software or any portion thereof may not be reproduced or used in any manner whatsoever without the development permission of the ODRE Labs, Inc.
Permission for the development of the software is Authorized ONLY for the developers of ODRD Labs, Inc.
Author: OUR DESTINY (A.A.I) Research And Development Labs <hariprasad@ODRDLabs>|<ribin@ODRDLabs>'''


import pyttsx3
import time, sys


print('Destiny V.0.0.3 Python Test Sequence')


destiny_engine = pyttsx3.init()                                                #Destiny Speech Engine Initialization Statement.
destiny_engine.setProperty('voice', 'malayalam')


def anim_print(str):                                                           #Function For Printing Output In TypeWriter Animation. 


  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.1)
    

destiny_engine_initialize_text='\nInitializing Destiny, Basic Test Sequence!'  #Initial Text Declaration Statement.


def initial_text():                                                            #Funtion For Printing And Audio Output Of The Initial Text.
    
    anim_print(destiny_engine_initialize_text)
    destiny_engine.say(destiny_engine_initialize_text)


greet_text='\n\nHello, Boss!'                                                  #Greeting Text Declaration Statement.


def greet_user():                                                              #Funtion For Printing And Audio Output Of The Greeting Statement.
    
    anim_print(greet_text)
    destiny_engine.say(greet_text)



initial_text()
greet_user()
destiny_engine.runAndWait()
