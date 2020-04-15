from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from datetime import datetime, timedelta
import data_manage
import api
import hidden
import webbrowser
import socket
import time

def is_connected():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

def check_key():
    key = hidden.head()
    key = key['x-rapidapi-key']
    if len(key) > 50 or len(key) < 50:
        msgbox = messagebox.showerror("KeyError", "Invalid X-Rapidapi-Key")
        return False
    return True

def checking():

    if is_connected() is True:
            style.configure('BW.TLabel', font =
                    ('calibri', 10),
                        background = 'grey')
            cl = Label(window,style="BW.TLabel")
            cl.grid(row=14, column=0, sticky='ew', columnspan=7)
            l1 = Label(window,text="Connected to Internet",style="BW.TLabel")
            l1.grid(row=14, column=3, sticky='ew', columnspan=7)
    else:
            style.configure('BW.TLabel', font =
                   ('calibri', 10),
                    background = 'red')
            cl = Label(window,style="BW.TLabel")
            cl.grid(row=14, column=0, sticky='ew', columnspan=7)
            l1 = Label(window,text="No Internet Connection", style="BW.TLabel")
            l1.grid(row=14, column=3, sticky='ew', columnspan=6)

def refresh():

    def bar():
        def task():
            progress['value'] = 20
            popup.update_idletasks()
            time.sleep(1)

            progress['value'] = 40
            popup.update_idletasks()
            time.sleep(1)

            api.main()

            progress['value'] = 50
            popup.update_idletasks()
            time.sleep(1)

            progress['value'] = 60
            popup.update_idletasks()
            time.sleep(1)

            progress['value'] = 80
            popup.update_idletasks()
            time.sleep(1)

            progress['value'] = 100
            popup.update_idletasks()
            time.sleep(1)

            time.sleep(1)
            popup.destroy()

        popup = Tk()
        popup.title("Loading..")
        popup.iconbitmap(dir_img)
        progress = Progressbar(popup, orient = HORIZONTAL,
        			length = 100, mode = 'determinate')
        l21 = Label(popup,text="Waiting for task to finish.",font='Helvetica 10 bold').grid(row=1, column=1)
        l1 = Label(popup,text="                        ").grid(row=1, column=0)
        l2 = Label(popup,text="                        ").grid(row=1, column=2)
        l3 = Label(popup,text="                        ").grid(row=2, column=0)
        l4 = Label(popup,text="                        ").grid(row=4, column=0)
        progress.grid(row=3,column=1)
        popup.after(200, task)
        popup.mainloop()

    if is_connected() is True:
        checking()
        if check_key() is True:
            bar()
    else:
        msgbox = messagebox.showerror("Error", "Internet Connection Error")
        checking()

def startuprestart():
        def task():
            progress['value'] = 20
            popup.update_idletasks()
            time.sleep(1)

            progress['value'] = 40
            popup.update_idletasks()
            time.sleep(1)

            api.main()

            progress['value'] = 50
            popup.update_idletasks()
            time.sleep(1)

            progress['value'] = 60
            popup.update_idletasks()
            time.sleep(1)

            progress['value'] = 80
            popup.update_idletasks()
            time.sleep(1)

            progress['value'] = 100
            popup.update_idletasks()
            time.sleep(1)

            time.sleep(1) # Replace this with the code you want to run
            l21 = Label(popup,text="Task is finished and data has loaded.",font='Helvetica 10 bold').grid(row=1, column=1)
            l22 = Label(popup,text="Please Restart the Software.",font='Helvetica 10 bold').grid(row=5, column=1)
            b1=Button(popup,text="Close", width=14, command=popup.quit).grid(row=6,column=1)

        popup = Tk()
        popup.title("Loading...")
        popup.iconbitmap(dir_img)
        if check_key() is False:
            popup.destroy()
        progress = Progressbar(popup, orient = HORIZONTAL,
        			length = 100, mode = 'determinate')
        l21 = Label(popup,text="Wait for task to finish.",font='Helvetica 10 bold').grid(row=1, column=1)
        l1 = Label(popup,text="                        ").grid(row=1, column=0)
        l2 = Label(popup,text="                        ").grid(row=1, column=2)
        l3 = Label(popup,text="                        ").grid(row=2, column=0)
        l4 = Label(popup,text="                        ").grid(row=4, column=0)
        l5 = Label(popup,text="                        ").grid(row=7, column=0)

        progress.grid(row=3,column=1)
        popup.after(200, task)
        popup.quit()
        popup.mainloop()

def popupkey():

    def f_open():
        webbrowser.open('secretkey.txt')

    def callback():
        webbrowser.open_new("https://bit.ly/3e2dHK6")

    popup = Tk()
    popup.wm_title("x-rapidapi-key")
    popup.iconbitmap(dir_img)
    l = Label(popup,text="                             ")
    l.grid(row=0, column=4)
    l1 = Label(popup,text="for x-rapidapi-key sign up on this website - ",font='Helvetica 10 bold')
    l1.grid(row=1, column=1)
    l2 = Label(popup,text="                             ")
    l2.grid(row=2, column=4)
    l3 = Label(popup,text="After you get the x-rapidapi-key, copy the x-rapidapi-key and paste ",font='Helvetica 10 bold')
    l3.grid(row=3,column=1)
    l5 = Label(popup,text="And dont forget to save the file.",font='Helvetica 10 bold')
    l5.grid(row=4,column=1)
    l4 = Label(popup,text="                             ")
    l4.grid(row=6, column=4)
    l6 = Label(popup,text="                             ")
    l6.grid(row=0, column=0)
    link3 = Button(popup,text='File', command=f_open).grid(row=5,column=1)
    link4 = Button(popup,text='rapidapi.com', command=callback).grid(row=2,column=1)
    popup.mainloop()

def popupaboutus():
    def callback():
        webbrowser.open_new("https://github.com/nayan-bagale/")

    popup = Tk()
    popup.wm_title("About Us")
    popup.iconbitmap(dir_img)
    l1 = Label(popup,text="Covid-19 India 1.0.0 Beta",font='Helvetica 10 bold').grid(row=0, column=1)
    l1 = Label(popup,text="                        ").grid(row=1, column=0)
    l2 = Label(popup,text="Thanks for using this FREE program.",font='Helvetica 10 ').grid(row=1,column=1)
    l3 = Label(popup,text=" We hope you like it.",font='Helvetica 10').grid(row=2,column=1)
    link3 = Button(popup,text='GitHub', command=callback).grid(row=3,column=0)
    close = Button(popup,text='Close', command=popup.destroy).grid(row=3,column=2)

    popup.mainloop()

def view_command():
    checking()
    list1.delete(0,END)
    try:
        for row in data_manage.search(search_text.get()):
            name = search_text.get()
            if len(row) is 7:
                date = 'Date: '+ str(row[1])
                active = 'Active: ' + str(row[2])
                confirmed = 'Confirmed: '+str(row[3])
                recovered = 'Recovered: '+str(row[4])
                deaths = 'Deaths: '+str(row[5])
                row = date + ': ' + active + ', ' +confirmed+ ', ' +recovered+ ', ' +deaths
            elif len(row) is 4:
                date = 'Date: '+ str(row[1])
                confirmed = 'Confirmed: '+str(row[2])
                row = date + ': '+', ' +confirmed
            elif len(row) is 8:
                country = str(row[1])
                active = 'Active: ' + str(row[2])
                confirmed = 'Conf: '+str(row[3])
                recovered = 'Rec: '+str(row[5])
                deaths = 'Deaths: '+str(row[6])
                date = 'Date:'+str(row[7])
                row = '"'+country + '" ' + active + ', ' +confirmed+ ', ' +recovered+ ', ' +deaths+ ', ' +date
            elif row is '~':
                row = 'Not found: '+ str(name)
            list1.insert(END,row)
    except Exception as e:
        print(e)
        row = 'No data found'
        list1.insert(END,row)

donothing = 'None'
dir_img = 'img/favicon.ico'
title = 'Covid-19 India 1.0.0 Beta'

if is_connected() is False:
    msgbox = messagebox.showerror("Error", "Internet Connection Error")
    quit()

date = datetime.strftime(datetime.now(), '%d-%B')

#total india data
try:
    india = data_manage.india_data()
except:
    try:
        startuprestart()
        quit()
    except Exception as e:
        print(e)
        #msgbox = messagebox.showerror("Error", "Internet Connection Error")
        quit()

in_active = india[2]
in_confirmed = india[3]
in_recovered = india[5]
in_deaths = india[6]

#Global database
g_data = data_manage.world_f()
total_confirmed = g_data[2]
total_recovered = g_data[4]
total_deaths = g_data[3]
new_cases = g_data[5]



window=Tk()
style = Style()

# Setting icon of master window
window.wm_title(title)
window.iconbitmap(dir_img)

menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Refresh",command=refresh)
filemenu.add_command(label="About Us", command=popupaboutus)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="Menu", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="X-Rapidapi-Key", command=popupkey)
menubar.add_cascade(label="Key", menu=helpmenu)

window.config(menu=menubar)
checking()
i1 = Label(window,text="India:",font='Helvetica 10 bold')
i1.grid(row=1, column=0,)

l9 = Label(window,text=date,font='Helvetica 10 bold')
l9.grid(row=0, column=6)

l1 = Label(window,text="Active:")
l1.grid(row=1, column=2)
l2 = Label(window,text=in_active)
l2.grid(row=1, column=3)

l3 = Label(window,text="Confirmed:")
l3.grid(row=2, column=2)
l4 = Label(window,text=in_confirmed)
l4.grid(row=2, column=3)

l5 = Label(window,text="Recovered:")
l5.grid(row=1, column=4)
l6 = Label(window,text=in_recovered)
l6.grid(row=1, column=5)

l7 = Label(window,text="Deaths:")
l7.grid(row=2, column=4)
l8 = Label(window,text=in_deaths)
l8.grid(row=2, column=5)

search_text=StringVar()
e1=Entry(window, textvariable=search_text, width=45)
e1.grid(row=3,column=0,columnspan=6)

b1=Button(window,text="Search", width=14, command=view_command)
b1.grid(row=3,column=6)

list1 = Listbox(window, height=20, width=75)
list1.grid(row=4,column=0,rowspan=7,columnspan=7)

l10 = Label(window,text="Global:",font='Helvetica 10 bold')
l10.grid(row=12, column=0)

l10 = Label(window,text="Confirmed:")
l10.grid(row=12, column=2)
l10 = Label(window,text=total_confirmed)
l10.grid(row=12, column=3)

l11 = Label(window,text="Recovered:")
l11.grid(row=13, column=2)
l11 = Label(window,text=total_recovered)
l11.grid(row=13, column=3)

l12 = Label(window,text="Deaths:")
l12.grid(row=12, column=4)
l12 = Label(window,text=total_deaths)
l12.grid(row=12, column=5)

l12 = Label(window,text="N/C:")
l12.grid(row=13, column=4)
l12 = Label(window,text=new_cases)
l12.grid(row=13, column=5)



window.mainloop()
