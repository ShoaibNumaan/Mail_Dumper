import pyautogui as p
from time import sleep


def del_Old_Mail(num):
    for x in range(num):
        if x == 0:
            sleep(5)
            continue
        p.moveTo(280,200, duration =0.5)
        p.click()
        sleep(0.5)
        p.moveRel(165,0, duration=0.5)
        p.click()
        sleep(5)

