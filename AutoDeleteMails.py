#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pyautogui as p
from time import sleep

#
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

# main function
def main():
    main_count = int(input("Number of e-mails to delete: "))
    mails_per_page = int(input("Enter the e-mails visible per page: "))
    clicks = mail_count // mails_per_page
    print(f"Number of Clicks: {clicks}")
    del_Old_Mail(clicks)


main()


# In[ ]:




