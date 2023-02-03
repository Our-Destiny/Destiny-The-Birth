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
import random


print('Destiny V.0.0.7 Python Test Sequence')                                  #Intro.


destiny_engine = pyttsx3.init()                                                #Destiny Speech Engine Initialization Statement.
destiny_voice = destiny_engine.getProperty('voices')                           #Voice Tweak Statement.
destiny_engine.setProperty('voice', destiny_voice[0].id)


destiny_engine_initialize_text='\nInitializing Destiny, Basic Test Sequence!'  #Initial Text Declaration Statement.


greet_by_time_text1 = '\n\nGood Morning!,Boss. Have a great day'               #Greet By Time Reply Input.
greet_by_time_text2 = '\n\nGood Afternoon!,Boss.'
greet_by_time_text3 = '\n\nGood Evening!,Boss. How was your day?'


ask_dailougue = '\n\nWhat Would You Like Me To Do!\n\n'                        #Command Request Text.


def destiny_thread(destiny_speech,destiny_print):                              #Statement For Initializing Threading.
        t1 = threading.Thread(target= destiny_speech)
        t2 = threading.Thread(target= destiny_print)
        t2.start()  
        t1.start()
        destiny_engine.runAndWait()                                            #Logic Statement To Exit From The Infinite Threading Loop.(SOLVED - Infinite Loop In Thread For Speech Output)
        t1.join() 
        t2.join() 


def anim_print(str):                                                           #Function For Printing Output In TypeWriter Animation. 
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.048)
    

def initial_text():                                                            #Funtion For Printing Output Of The Initial Text.
    anim_print(destiny_engine_initialize_text)
    
    
def initial_speech():                                                          #Function For Audio Output Of The Initial Text.
    destiny_engine.say(destiny_engine_initialize_text)
    

def greet_by_time_text():                                                      #Function For Printing Greet By Time
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        anim_print(greet_by_time_text1)

    elif hour>=12 and hour<16:
        anim_print(greet_by_time_text2)  

    else:
        anim_print(greet_by_time_text3)


def greet_by_time_speech():                                                    #Function For Speaking Greet By Time
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        destiny_engine.say(greet_by_time_text1)

    elif hour>=12 and hour<16:
        destiny_engine.say(greet_by_time_text2)   

    else:
        destiny_engine.say(greet_by_time_text3)      


def user_custom_text_ask():                                                    #Funtion For Printing Custom Input Dailougue.
    anim_print(ask_dailougue)
    
    
def user_custom_speech_ask():                                                  #Function For Audio Output For Custom User Text.
    destiny_engine.say(ask_dailougue)


def play_music():                                                              #Function For Playing Random Audio From A Specified Folder.

    music_dir = 'D:\\OS\\User Data\\Music'
    songs = os.listdir(music_dir)
    length = len(songs)
    random_element = random.randrange(length)
    os.startfile(os.path.join(music_dir, songs[random_element]))


destiny_thread(initial_speech,initial_text)                                    #Threading Statement For Initialization Output.
destiny_thread(greet_by_time_speech,greet_by_time_text)                        #Threading Statement For Greeting.
destiny_thread(user_custom_speech_ask,user_custom_text_ask)                    #Threading Statement For Custom User Input.


while True:                                                                    #Shell Commands.

    custom_text = input('Enter A Command > ').lower()


    if 'honey' in custom_text:

        destiny_engine.say('Yes, Boss!')
        destiny_engine.runAndWait()
        

    elif 'play music' in custom_text:
    
        destiny_engine.say('I Have Choosen, A Random Song For You. Enjoy!')
        destiny_engine.runAndWait() 
        play_music()

    elif 'thankyou' in custom_text:
        
        destiny_engine.say('For U Boss! Always.')
        destiny_engine.runAndWait()
        break
    
    elif 'the time' in custom_text:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            destiny_engine.say(f"the time is {strTime}")
            destiny_engine.runAndWait()
    
    elif 'bye' in custom_text:

        destiny_engine.say('Sure. See You Later.')
        destiny_engine.runAndWait()
        break

    else:

        destiny_engine.say('Sorry, Iam Under Development. Currently, This Far Is Only I Can Do. Thankyou.')
        destiny_engine.runAndWait()
        break 


print('\n\nDestiny V.0.0.7 Python Test Sequence Status : Passed')              #Outro.
