import sys
import cv2
import time
import datetime
import pyautogui
import numpy as np
import keyboard
import os, os.path
from PIL import Image

############
# Settings #
NAME = 'kiminonawa'
PAUSE_TIME = 1.5
TIMING_MULT = 1.5
CLOSENESS_THRESHOLD = 0.8
ROLLS_FOLDER = 'rolls'
############

pyautogui.PAUSE = PAUSE_TIME
pyautogui.FAILSAFE = True

HOME_BUTTON = {'x': 1900, 'y': 1000}
HOME = {'x': 1800, 'y': 70}
GO_ICON = {'x': 240, 'y': 240}
CLEAR_DATA_ICON = {'x': 420, 'y': 380}
SKIP_BUTTON = {'x': 1757, 'y': 90}
CONFIRM = {'x': 1757, 'y': 200}
CONFIRM2 = {'x': 1132, 'y': 788}
CONFIRMPULL = {'x': 940, 'y': 950}
SKILL1 = {'x': 1444, 'y': 930}
AREASKILL1 = {'x': 1000, 'y': 500}
AREASKILL2 = {'x': 1575, 'y': 375}

RECRUIT = {'x': 1375, 'y': 972}
STUDENT = {'x': 500, 'y': 1000}
MAIL = {'x': 1670, 'y': 90}
PULL = {'x': 1600, 'y': 780}
POSTBATTLECONFIRM = {'x': 1700, 'y': 990}
EXCAL = {'x': 400, 'y': 250}
NAME_FIELD = {'x': 950, 'y': 566}
RESET_FIELD = {'x': 950, 'y': 510}
NAME_CONFIRM = {'x': 950, 'y': 744}
RESET_CONFIRM = {'x': 1120, 'y': 750}
NAME_CONFIRM_2 = {'x': 850, 'y': 600}
NEXT = {'x': 1110, 'y': 700}
CLOSE = {'x': 640, 'y': 590}
MENU = {'x': 1190, 'y': 715}
LEFT_EDGE = {'x': 900,'y': 600}
SKIP_EDGE = {'x': 1740,'y': 100}
RIGHT_EDGE = {'x': 1781,'y': 178}
RIGHT_EDGE2 = {'x': 1635,'y': 205}
RIGHT_EDGE3 = {'x': 1400,'y': 245}

def wait(given_time):
    time.sleep(TIMING_MULT * given_time)

def touch(x, y):
    pyautogui.click(x=x, y=y)

def skip_scene():
    touch(**SKIP_BUTTON)
   
    touch(**CONFIRM)

    touch(**CONFIRM2)

def tskip_scene():
    touch(**SKIP_BUTTON)
    wait(0.5)
    touch(**CONFIRM)
    wait(0.5)
    touch(**CONFIRM2)
    wait(0.5)

def skip_scene2():
    touch(**SKIP_BUTTON)
    touch(**CONFIRM2)

def close_app():
    touch(**HOME_BUTTON)
    touch(x= 1900, y= 1045)                                            # App Switcher
    touch(x= 1300, y= 140)
    wait(1)

def select_card(card_no):
    locations = {1: 1290, 2: 1450, 3: 1580}
    touch(x=locations[card_no], y=940)

def image_is_on_screen(template_name):
    template = cv2.imread(os.path.join(
                                'screenshots', 
                                template_name + '.png'), 
                    cv2.IMREAD_GRAYSCALE)
    image = cv2.cvtColor(
                np.array(pyautogui.screenshot(
                        region=(0, 0, 1980, 1080))), 
                cv2.COLOR_BGR2GRAY)

    res = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= CLOSENESS_THRESHOLD)

    # Not sure why this works but okay
    for pt in zip(*loc[::-1]):
        return True

    return False

def click_until(*images):
    pyautogui.PAUSE = 0.2 * PAUSE_TIME
    while True:
        for pos, image in enumerate(images):
            if image_is_on_screen(image):
                pyautogui.PAUSE = PAUSE_TIME
                wait(0.5)
                return pos

        for _ in range(5):
            touch(**LEFT_EDGE)

def home_until(*images):
    pyautogui.PAUSE = 0.2 * PAUSE_TIME
    while True:
        for pos, image in enumerate(images):
            if image_is_on_screen(image):
                pyautogui.PAUSE = PAUSE_TIME
                wait(0.5)
                return pos

        for _ in range(5):
            touch(**HOME)

def tutor_until(*images):
    pyautogui.PAUSE = 0.2 * PAUSE_TIME
    while True:
        for pos, image in enumerate(images):
            if image_is_on_screen(image):
                pyautogui.PAUSE = PAUSE_TIME
                wait(0.5)
                return pos

        for _ in range(4):
            tskip_scene()

def click_until2(*images):
    pyautogui.PAUSE = 0.2 * PAUSE_TIME
    while True:
        for pos, image in enumerate(images):
            if image_is_on_screen(image):
                pyautogui.PAUSE = PAUSE_TIME
                wait(0.5)
                return pos

        for _ in range(5):
            touch(**RIGHT_EDGE)

def click_until3(*images):
    pyautogui.PAUSE = 0.2 * PAUSE_TIME
    while True:
        for pos, image in enumerate(images):
            if image_is_on_screen(image):
                pyautogui.PAUSE = PAUSE_TIME
                wait(0.5)
                return pos

        for _ in range(5):
            touch(**RIGHT_EDGE2)

def click_until4(*images):
    pyautogui.PAUSE = 0.2 * PAUSE_TIME
    while True:
        for pos, image in enumerate(images):
            if image_is_on_screen(image):
                pyautogui.PAUSE = PAUSE_TIME
                wait(0.5)
                return pos

        for _ in range(5):
            touch(**RIGHT_EDGE3)

def gacha_until(*images):
    pyautogui.PAUSE = 0.2 * PAUSE_TIME
    while True:
        for pos, image in enumerate(images):
            if image_is_on_screen(image):
                pyautogui.PAUSE = PAUSE_TIME
                wait(0.5)
                return pos

        for _ in range(5):
            touch(**SKIP_EDGE)


def wait_until(*images):
    while True:
        for pos, image in enumerate(images):
            if image_is_on_screen(image):
                wait(0.5)
                return pos

if __name__ == '__main__':

    if not os.path.exists(ROLLS_FOLDER):
        os.mkdir(ROLLS_FOLDER)

    try:
        while True:
      
            touch(**HOME_BUTTON)
            touch(**GO_ICON)                                            # Game Icon

            wait_until('iklan', 'title_screen')
            touch(**SKIP_BUTTON) 
            wait_until('title_screen')
            touch(**LEFT_EDGE) 



            

            folder_name = os.path.join(ROLLS_FOLDER,
                datetime.datetime.now().strftime('%y_%m_%d_%H_%M'))
            
            lock_file = os.path.join(folder_name, '.done')

            try:
                os.mkdir(folder_name)
                open(lock_file, 'a').close()
            except FileExistsError:
                pass                                                    # Tbh idk what to do if this happens
            except WindowsError:                                
                pass                                                    # Folder already exists

            # Intro
            click_until('firsttime')
            touch(**CONFIRM)                                            # First time account
        
            # Name
            wait_until('nameenter')
            touch(**NAME_FIELD)
            pyautogui.typewrite(NAME, interval = 0.25)
            touch(**NAME_CONFIRM)
            wait(0.3)
            touch(**NAME_CONFIRM)
            wait(0.3)
            touch(**NAME_CONFIRM)
            wait(0.3)
            touch(**NAME_CONFIRM)
            wait(0.3)
            # First Battle
            wait_until('welcometo')
            touch(**LEFT_EDGE) 
            wait(1)
            touch(**LEFT_EDGE) 
            
            wait_until('introskipbg')
            touch(**LEFT_EDGE) 
            skip_scene()

            click_until('attack1m')
            select_card(2)
            touch(**AREASKILL2)

            click_until('attack1m')
            wait(1)
            select_card(1)
            touch(**AREASKILL1)

            wait_until('prolog_complete')
            wait(1)
            touch(**POSTBATTLECONFIRM)
            wait(2)

            

            wait_until('skipseq2')
            skip_scene()


            wait_until('skipseq2')
            skip_scene()

            tutor_until('attack1m')
            select_card(1)
            touch(**AREASKILL2)

            wait_until('prolog_complete')
            wait(1)
            touch(**POSTBATTLECONFIRM)

            wait_until('skipseq2')
            wait(1)
            skip_scene()

            wait_until('skip_the')
            skip_scene()
            wait(5)
            skip_scene2()   

            click_until('pointerrecruit')
            touch(**RECRUIT)

            wait_until('tutorpull')
            touch(**PULL)

            wait(2)
            touch(**CONFIRM2)

            gacha_until('confirm_gacha')
            wait(2)
            img1 = pyautogui.screenshot(
                    region=(0, 0, 1980, 1080))
            img1.save(os.path.join(
                                    folder_name, 'gacha1.png'))
            wait(1)
            touch(**CONFIRMPULL)

            click_until('pointermisi')
            touch(x=1633, y=382) 

            click_until('pointer2')
            touch(x=1300, y=800) 

            click_until('start1')
            touch(x=770, y=725) 

            click_until('formation')
            touch(x=1750, y=323)

            click_until2('mobilize')
            touch(**POSTBATTLECONFIRM)

            click_until('beginmission')
            wait(2)
            touch(**POSTBATTLECONFIRM)

            click_until2('step2')
            touch(x=985, y=700)

            wait_until('battlecomplete')
            wait(1)
            touch(**POSTBATTLECONFIRM)
            wait(1)
            touch(x=950, y=990)

            click_until('endphase')
            touch(**POSTBATTLECONFIRM)

            click_until('step3')
            touch(x=1100, y=600)

            wait_until('battlecomplete2')
            wait(1)
            touch(**POSTBATTLECONFIRM)
            wait(1)
            touch(x=950, y=990)

            wait_until('mission_complete')
            touch(x=1500, y=1000)

            click_until('gotolobby')
            touch(x=750, y=1000)

            click_until('momotalk')
            touch(x=250, y=250)

            click_until('momopointer')
            touch(x=255, y=436)

            click_until3('tete')
            touch(**MAIL)

            wait_until('receiveall')
            touch(**POSTBATTLECONFIRM)

            click_until3('nomail')
            touch(**HOME)

            click_until3('students')
            touch(**STUDENT)

            wait(2)
            touch(**LEFT_EDGE)
            wait(1)
            touch(x=200,y=500)
            wait(1)
            touch(x=200,y=500)

            home_until('theacc')
            touch(x=1100,y=540)

            click_until('pleaselink')
            touch(**HOME)

            click_until4('tete')
            touch(**RECRUIT)

            wait_until('gacha')
            touch(x=1300,y=260)
            wait(1)
            touch(**PULL)

            wait(1)
            touch(**CONFIRM2)

            gacha_until('confirm_gacha')
            wait(2)
            img1 = pyautogui.screenshot(
                    region=(0, 0, 1980, 1080))
            img1.save(os.path.join(
                                    folder_name, 'gacha2.png'))
            wait(1)
            touch(x=950,y=950)
            wait(1)
            touch(x=1100,y=950)
            wait(0.5)
            touch(x=1100,y=750)

            gacha_until('confirm_gacha')
            wait(2)
            img1 = pyautogui.screenshot(
                    region=(0, 0, 1980, 1080))
            img1.save(os.path.join(
                                    folder_name, 'gacha3.png'))
            wait(1)
            touch(x=950,y=950)
            wait(1)
            touch(x=1100,y=950)
            wait(0.5)
            touch(x=1100,y=750)

            gacha_until('confirm_gacha')
            wait(2)
            img1 = pyautogui.screenshot(
                    region=(0, 0, 1980, 1080))
            img1.save(os.path.join(
                                    folder_name, 'gacha4.png'))
            wait(1)
            touch(x=950,y=950)
            wait(1)
            touch(x=750,y=950)
            wait_until('gacha')
            touch(**HOME)

            txt = input("Rerollagain ? (y/n) : ")
            if txt == 'y':
                touch(**HOME)
                wait(0.5)
                touch(x=1100,y=540)
                wait_until('pleaselink')
                touch(**HOME)
                touch(x=1304,y=562)

                wait_until('resetprompt')
                touch(**RESET_FIELD)
                pyautogui.typewrite("BlueArchive", interval = 0.25)
                touch(**RESET_CONFIRM)
                wait(0.3)
                touch(**RESET_CONFIRM)

                os.remove(lock_file)

                close_app()
                wait(1)

            else:
                break

    except KeyboardInterrupt:
        sys.exit()
