import pyautogui as p
from time import sleep


def del_Old_Mail(num):
    print("----Started----")
    for x in range(num):
        if x == 0:
            sleep(5)
            continue
        print(f"Processed {x} clicks")
        p.moveTo(280,200, duration =0.5)
        p.click()
        sleep(0.5)
        p.moveRel(165,0, duration=0.5)
        p.click()
        sleep(5)
    print("----Finished----")


# main function
def main():
    mail_count = int(input("Number of e-mails to delete: "))
    mails_per_page = int(input("Enter the e-mails visible per page: "))
    clicks = mail_count // mails_per_page
    del_Old_Mail(clicks)


main()
