'''DESTINY Autonimous Artificial Intelligence Programme (Python 3).
Copyright (c) 2012 - End Of Times | OUR DESTINY (A.A.I) Research And Development Labs,Inc.
All rights reserved. This software or any portion thereof may not be reproduced or used in any manner whatsoever without the development permission of the ODRE Labs, Inc.
Permission for the development of the software is Authorized ONLY for the developers of ODRD Labs, Inc.
Author: OUR DESTINY (A.A.I) Research And Development Labs <hariprasad@ODRDLabs>|<ribin@ODRDLabs>'''


import pyttsx3
import time, sys
import threading


print('Destiny V.0.0.4 Python Test Sequence')


destiny_engine = pyttsx3.init()                                                #Destiny Speech Engine Initialization Statement.
destiny_voice = destiny_engine.getProperty('voices')                           #Voice Tweak Statement.
destiny_engine.setProperty('voice', destiny_voice[2].id)
destiny_engine_initialize_text='\nInitializing Destiny, Basic Test Sequence!'  #Initial Text Declaration Statement.

def anim_print(str):                                                           #Function For Printing Output In TypeWriter Animation. 
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.045)
    

def initial_text():                                                            #Funtion For Printing Output Of The Initial Text.
    anim_print(destiny_engine_initialize_text)
    
    
def initial_speech():                                                          #Function For Audio Output Of The Initial Text.
    destiny_engine.say(destiny_engine_initialize_text)
    


t1 = threading.Thread(target=initial_speech)                                   #First Threading.
t2 = threading.Thread(target=initial_text)
t2.start()  
t1.start()
destiny_engine.runAndWait()                                                    #Logic Statement To Exit From The Infinite Threading Loop.(SOLVED - Infinite Loop In Thread For Speech Output)
t1.join() 
t2.join() 


greet_text='\n\nHello, Boss. Hope You Are Doing Fine.'                         #Greeting Text Declaration Statement.


def greet_user_text():                                                         #Funtion For Printing And Audio Output Of The Greeting Statement.
    
    anim_print(greet_text)


def greet_user_speech():
    destiny_engine.say(greet_text)
    
    
t3 = threading.Thread(target=greet_user_text)                                  #Second Threading.
t4 = threading.Thread(target=greet_user_speech)   
t3.start()
t4.start()
destiny_engine.runAndWait()
t3.join()
t4.join()
