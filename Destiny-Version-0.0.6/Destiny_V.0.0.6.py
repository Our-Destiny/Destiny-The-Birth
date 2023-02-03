'''DESTINY Autonimous Artificial Intelligence Programme (Python 3).
Copyright (c) 2012 - End Of Times | OUR DESTINY (A.A.I) Research And Development Labs,Inc.
All rights reserved. This software or any portion thereof may not be reproduced or used in any manner whatsoever without the development permission of the ODRE Labs, Inc.
Permission for the development of the software is Authorized ONLY for the developers of ODRD Labs, Inc.
Author: OUR DESTINY (A.A.I) Research And Development Labs <hariprasad@ODRDLabs>|<ribin@ODRDLabs>'''


import pyttsx3
import time, sys
import threading
import datetime
import os


print('Destiny V.0.0.6he Python Test Sequence')


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
    


t1 = threading.Thread(target=initial_speech)                                   #First Threading For Parallel Text And Voice Output Of Initial Text.
t2 = threading.Thread(target=initial_text)
t2.start()  
t1.start()
destiny_engine.runAndWait()                                                    #Logic Statement To Exit From The Infinite Threading Loop.(SOLVED - Infinite Loop In Thread For Speech Output)
t1.join() 
t2.join() 


text1 = '\n\nGood Morning!,Boss. Have a great day'
text2 = '\n\nGood Afternoon!,Boss. Had Lunch?'
text3 = '\n\nGood Evening!,Boss. How was your day?'


def greet_by_time_text():                                                      #Function For Printing Greet By Time
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        anim_print(text1)

    elif hour>=12 and hour<16:
        anim_print(text2)  

    else:
        anim_print(text3)


def greet_by_time_speech():                                                    #Function For Speaking Greet By Time
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        destiny_engine.say(text1)

    elif hour>=12 and hour<16:
        destiny_engine.say(text2)   

    else:
        destiny_engine.say(text3)        



t3 = threading.Thread(target=greet_by_time_text)                               #Second Threading For Parellel Text And Voice Output Of Greet By Time Function.
t4 = threading.Thread(target=greet_by_time_speech)
t3.start()  
t4.start()
destiny_engine.runAndWait()                                                    
t3.join() 
t4.join() 



ask_dailougue = '\n\nBoss! What Would You Like Me To Say?\n\n'


def user_custom_text_ask():                                                    #Funtion For Printing Custom Input Dailougue.
    anim_print(ask_dailougue)
    
    
def user_custom_speech_ask():                                                  #Function For Audio Output For Custom User Text.
    destiny_engine.say(ask_dailougue)


t5 = threading.Thread(target=user_custom_text_ask)
t6 = threading.Thread(target=user_custom_speech_ask)
t5.start()
t6.start()
destiny_engine.runAndWait()
t5.join()
t6.join()


custom_text = input()


def user_custom_text():                                                        #Funtion For Printing The Custom User Text.
    anim_print('\nYou Said : ' + custom_text)
    
    
def user_custom_speech():                                                      #Function For Audio Output Of The Custom User Text.
    destiny_engine.say(custom_text)


t7 = threading.Thread(target=user_custom_text)
t8 = threading.Thread(target=user_custom_speech)
t7.start()
t8.start()
destiny_engine.runAndWait()
t7.join()
t8.join()


print('\n\nDestiny V.0.0.6 Python Test Sequence Status : Passed')
