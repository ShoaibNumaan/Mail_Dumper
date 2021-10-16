import tkinter as tk
import AutoDeleteOldMails as adm

app = tk.Tk()
#window specs
app.title("Mail Dumper")
app.geometry("400x600")

def delete():
    tm = int(mt_ent.get())
    mpp = int(mp_ent.get())
    clicks = tm // mpp
    adm.del_Old_Mail(clicks)
    app.destroy()    
    

header = tk.Label(app, text = "MAIL DUMPER", fg = "Cyan", font=("Times New Roman", "20"), pady = 20)
header.pack()

mails_tot = tk.Label(app, text = "Total Mails", fg = "Orange", font=("Aerial", "13"), pady = 2)
mails_tot.place(x = 50, y = 100)

mt_ent = tk.Entry(app, width = 23, bd = 3)
mt_ent.place(x = 200, y = 100)

mail_pp = tk.Label(app, text = "Mails Per-Page", fg = "Orange", font=("Aerial", "13"), pady = 2)
mail_pp.place(x = 50, y = 150)

mp_ent = tk.Entry(app, width = 23, bd = 3)
mp_ent.place(x = 200, y = 150)

submit = tk.Button(app, text = "START", width = 30, bd = 3, bg = "red", fg = "black", command = delete)
submit.place(x = 100, y = 250)


app.mainloop()
