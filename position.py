from time import sleep
import pyautogui as p


for x in range(100):     
    c = p.position()     
    sleep(1)     
    print(c)
