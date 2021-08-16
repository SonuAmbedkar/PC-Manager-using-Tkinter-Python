from tkinter import *
from tkinter import ttk
import sqlite3
import tkinter.messagebox
from  datetime import date
from tkinter import filedialog
import shutil
import os
from tkinter import Text,Tk
import datetime
from  PIL import Image, ImageTk
import PIL
import win32con, win32api,os
import subprocess
#import win32api
def backuppwd():
    os.system("cmd /c CREDWIZ")
	
def registryedit():
    os.system("cmd /c regedit")
	
def controlpanel1():
    os.system("cmd /c control")	

def windowversion():
    os.system("cmd /c winver")

def windowexplorer():
    os.system("cmd /c explorer")

def TaskManager():
    os.system("cmd /c Taskmgr")	
	
	
now = datetime.datetime.now()
today=date.today()
print ('Software is Running......')


def pcsequrity():

    root.destroy()
    root4=Tk()
    root4.title("YOUR SECURITY")
    root4.geometry("1600x1000+0+0")
    def destroy():
        root4.destroy()
        mainwindow()
   # C1 = Canvas(root, bg="blue", height=250, width=300)
    filename1 = ImageTk.PhotoImage(Image.open("offer3.jpg"))
    background_label = Label(root4, image=filename1)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    global entry
    entry=StringVar()



    label = Label(root4,text="PC Security",font=("times new roman",30))
    label.place(x=450, y=20)
    def hide():
        global findfile

        root4.filename=filedialog.askopenfilename(initialdir="/",title="Select File",filetypes=(("jpeg files","*.jpg"),("all files","*.*")))
        entry12.delete(0, END)

        entry12.insert(0, root4.filename)
        findfile=root4.filename
        if root4.filename==None:
            entry12.delete(0, END)
            filename1 = ImageTk.PhotoImage(Image.open("offer3.jpg"))
            background_label = Label(root4, image=filename1)
            background_label.place(x=0, y=0, relwidth=1, relheight=1)

            entry12.insert(0, 'NO FILE SELECTED')







    def hidefile():


        import win32file
        import win32con
        import win32api
        flags = win32file.GetFileAttributesW(findfile)
        win32file.SetFileAttributes(findfile,
                                    win32con.FILE_ATTRIBUTE_HIDDEN | flags)
        x = tkinter.messagebox.showinfo("SuccessFull", "File is Successfully Hide")
    def unhidefile():
        file1=entry.get()
        import win32file
        import win32con
        import win32api
        # Set the file attributes back to their defaults
        ShiraAttribs = win32con.FILE_ATTRIBUTE_NORMAL
        win32api.SetFileAttributes(file1, ShiraAttribs)
        x = tkinter.messagebox.showinfo("Successfull",
                                            "File is Successfully unhide")





    button3 = Button(root4, text="HideFile", font=("times new roman", 15), command=hidefile)
    button3.place(x=350, y=300)
    button3 = Button(root4, text="UnHide File", font=("times new roman", 15),command=unhidefile)
    button3.place(x=200, y=300)
    entry12 = Entry(root4, font=(20),textvar=entry, state="normal",width=60)
    entry12.place(x=200, y=200)
    button=Button(root4,width=15,text="SELECT FILE", font=("times new roman",15),command=hide)
    button.place(x=800,y=200)
    button15 = Button(root4, width=7, text="BACK", font=("times new roman", 15),command=destroy)
    button15.place(x=0, y=0)
    root4.mainloop()


def pcmanager():
    root.destroy()
    root1=Tk()
    root1.title("Schedule")
    root1.geometry("1600x1000+0+0")
    filename1 = ImageTk.PhotoImage(Image.open("offer3.jpg"))
    background_label = Label(root1, image=filename1)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    #filename = ImageTk.PhotoImage(Image.open("offer2.jpg"))
    #background_label = Label(root1, image=filename)
    #background_label.place(x=0, y=0, relwidth=1, relheight=1)
    #schedule=Label(root1)
    #photot=PhotoImage(file="Original_237x75.png",width=200,height=100)
    #schedule.config(image=photot)
    #schedule.place(x=400,y=100)
    label=Label(root1,text= now.strftime("%Y-%m-%d %H:%M"),font=("times new roman",20))
    label.place(x=800 ,y=300)
    label=Label(root1,text="Current System Time",font=("times new roman",20))
    label.place(x=300 ,y=300)
    label = Label(root1, text="After:", font=("times new roman", 20))
    label.place(x=330, y=350)
    box2 = ttk.Combobox(root1, state="readonly", font=("arial", 12, "bold"), width=5)
    box2['values'] = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    box2.current(0)
    box2.place(x=380,y=400)
    label2 = Label(root1, text="Hour", font=("times new roman", 12))
    label2.place(x=330,y=400)
    label2 = Label(root1, text="Minute", font=("times new roman", 12))
    label2.place(x=330,y=500)
    label3=Label(root1)
    entry1=Entry(root1,width=7,font=("arial", 12, "bold"))
    entry1.place(x=380,y=500)
    def time():
        if entry1.get()!="":
            if int(float(entry1.get()))>59:
                x = tkinter.messagebox.showinfo("INVALID TIME", "Please enter valid minutes between 0 to 59")
        else:
            x = tkinter.messagebox.showinfo("INVALID TIME", "Enter Minute")
			
    def shutdown():
        msg = tkinter.messagebox.askyesno("CONFIRMATION",
                                          " WARNING: ARE YOU SURE TO TURN OFF PC")
        if msg>0:
            os.system("shutdown /r /t 1")
    def restart():
        msg = tkinter.messagebox.askyesno("CONFIRMATION",
                                          " WARNING: ARE YOU SURE TO RESTART PC")
        if msg>0:
            win32api.InitiateSystemShutdown()

	
	


    exit = Button(root1, width=10, font=("arial", 10), text="shutdown", bg="MediumOrchid2", command=time)
    # photo=PhotoImage(file="config.png")
    # enquiry.config(image=photo, width="200", height="100")
    exit.place(x=800, y=400)
    exit = Button(root1, width=10, font=("arial", 10), text="restart", bg="MediumOrchid2",command=restart)
    # photo=PhotoImage(file="config.png")
    # enquiry.config(image=photo, width="200", height="100")
    exit.place(x=800, y=470)
    exit3 = Button(root1, width=12, font=("arial", 10), text="shutdown now", bg="MediumOrchid2",command=shutdown)
    # photo=PhotoImage(file="config.png")
    # enquiry.config(image=photo, width="200", height="100")
    exit3.place(x=930, y=400)
    exit3 = Button(root1, width=12, font=("arial", 10), text="restart now", bg="MediumOrchid2", command=restart)
    # photo=PhotoImage(file="config.png")
    # enquiry.config(image=photo, width="200", height="100")
    exit3.place(x=930, y=470)
    exit3 = Button(root1, width=10, font=("arial", 10), text="cancel", bg="MediumOrchid2", command=root1.destroy)
    # photo=PhotoImage(file="config.png")
    # enquiry.config(image=photo, width="200", height="100")
    exit3.place(x=850, y=550)
    def back():
        root1.destroy()
        mainwindow()

    exit5 = Button(root1, width=10, font=("arial", 10), text="BACK", command=back)
    exit5.place(x=0,y=0)
    root1.mainloop()
def allopen():
    os.system("devmgmt.msc . /r /t 1")
def system():
    os.system("sysdm.cpl")
def keybord():
    os.system("cmd /c control keyboard")

def internetseting():
    os.system("inetcpl.cpl")
def netsetup():
    os.system("ncpa.cpl")
def internetseting():
    os.system("inetcpl.cpl")
def firewall():
    os.system("cmd /c wf.msc")
def addremove():
    os.system("appwiz.cpl")
def display():
    subprocess.Popen([r"C:\Windows\System32\DpiScaling.exe"])

def timedate():
    os.system("cmd /c timedate.cpl")
def mouse():
    os.system("cmd /c main.cpl")
def control():
    os.system("control keybord.cpl")



def pcprograms():
    root2=Tk()
    root2.title('PC CONFIGURATION')
    root2.geometry("1600x1000+0+0")
    def back():
        root2.destroy()
        mainwindow()
    label=Label(root2)
    filename = ImageTk.PhotoImage(Image.open("offer2.jpg"))
    background_label = Label(root2, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    photo=PhotoImage(file="pc.png")
    label.config(image=photo,width=200, height=100)
    label.place(x=450,y=0)
    button1=Button(root2,width=20, font=("arial",15), text="Device Manager", command=allopen )
    button1.place(x=100,y=300)
    button3 = Button(root2,width=20, font=("arial", 15), text="System Properties", command=system)
    button3.place(x=100, y=370)
    button2 = Button(root2,width=20, font=("arial", 15), text="Network Setup", command=netsetup)
    button2.place(x=100, y=440)
    button4 = Button(root2,width=20, font=("arial", 15), text="Internet Setting", command=internetseting)
    button4.place(x=100, y=510)
    button4 = Button(root2, width=20, font=("arial", 15), text="Fire Wall", command=firewall)
    button4.place(x=900, y=300)
    button4 = Button(root2, width=20, font=("arial", 15), text="Add and Remove", command=addremove)
    button4.place(x=900, y=370)
    button4 = Button(root2, width=20, font=("arial", 15), text="Date and Time", command=timedate)
    button4.place(x=900, y=440)
    button4 = Button(root2, width=20, font=("arial", 15), text="Mouse", command=mouse)
    button4.place(x=900, y=510)
    button4 = Button(root2, width=20, font=("arial", 15), text="Display", command=display)
    button4.place(x=900, y=580)
    button4 = Button(root2, width=20, font=("arial", 15), text="Keyboard", command=keybord)
    button4.place(x=100, y=580)
    button4 = Button(root2, width=20, font=("arial", 15), text="Back", command=back)
    button4.place(x=100, y=100)

    root2.mainloop()
    def pcprogramsdestroy():
        root2.destroy()
        mainwindow()
def pcprograms1():
        root.destroy()
        pcprograms()
def pcschedule1():
    pcmanager()
	
from subprocess import  call
def cal():
    call(["calc.exe"])


def mainwindow():
    global root
    root=Tk()
    root.title("PC MANAGER")
    root.geometry("1600x1000+0+0")
    user1=Label()
    C = Canvas(root, bg="blue", height=250, width=300)
    filename = ImageTk.PhotoImage(Image.open("offer2.jpg"))
    background_label = Label(root, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="PC Scheduler", command=pcmanager)
    filemenu.add_separator()
    filemenu.add_command(label="Security", command=pcsequrity)
    filemenu.add_separator()
    filemenu.add_command(label="PC Programs", command=configration)
    menubar.add_cascade(label="File", menu=filemenu)
    root.config(menu=menubar)
    photo8=PhotoImage(file="White_on_emblems_color_background_355x75.png")
    user1.config(image=photo8,width=220,height=70)
    user1.place(x=400,y=0)
    exit = Button(root,command=root.destroy)
    photo=PhotoImage(file="exit.png")
    exit.config(image=photo, width=120, height=35)
    exit.place(x=1110, y=0)
    enquiry1 = Button(root,command=pcschedule1)
    photo1=PhotoImage(file="schedule.png")
    enquiry1.config(image=photo1, width=220, height=70)
    photo3=PhotoImage(file="config.png")
    enquiry1.place(x=300, y=400)
    enquiry2 = Button(root,command=pcprograms1)
    enquiry2.config(image=photo3, width=220, height=70)
    enquiry2.place(x=300, y=500)
    enquiry34 = Button(root,command=pcsequrity)
    photo9=PhotoImage(file="Original_without_effects_256x75.png")
    enquiry34.config(image=photo9,width=220,height=70)
    enquiry34.place(x=800, y=400)
    enquiry4 = Button(root,command=configration)
    photo10=PhotoImage(file="pc.png")
    enquiry4.config(image=photo10,width=220,height=70)
    enquiry4.place(x=800, y=500)
    filemenu.add_separator()
    filemenu.add_command(label="PC CONFIGURATION", command=pcprograms1)

    #photo = PhotoImage(file="pcmanager.png")
    #user1.config(image=photo, width=50, height=50)
    #user1.place(x=610, y=120)

    root.mainloop()
	
def configration():
    root.destroy()
    root2=Tk()
    root2.title('PC PROGRAMS')
    root2.geometry("1600x1000+0+0")
    def back():
        root2.destroy()
        mainwindow()
    def notepad():
        subprocess.call(['notepad.exe'])
    label=Label(root2)
    filename = ImageTk.PhotoImage(Image.open("offer2.jpg"))
    background_label = Label(root2, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    photo=PhotoImage(file="pc.png")
    label.config(image=photo,width=200, height=100)
    label.place(x=450,y=0)
    button1=Button(root2,width=23, font=("arial",13), text="BACKUP AND PASSWORD", command=backuppwd)
    button1.place(x=100,y=300)
    button3 = Button(root2,width=20, font=("arial", 15), text="REGISTRY", command=registryedit)
    button3.place(x=100, y=370)
    button2 = Button(root2,width=20, font=("arial", 15), text="CONTROL PANEL", command=controlpanel1)
    button2.place(x=100, y=440)
    button4 = Button(root2,width=20, font=("arial", 15), text="WIN VERSION", command=windowversion)
    button4.place(x=100, y=510)
    button4 = Button(root2, width=20, font=("arial", 15), text="EXPLORER", command=windowexplorer)
    button4.place(x=900, y=300)
    button4 = Button(root2, width=20, font=("arial", 15), text="NOTEPAD", command=notepad)
    button4.place(x=900, y=370)
    button4 = Button(root2, width=20, font=("arial", 15), text="CALCULATOR", command=cal)
    button4.place(x=900, y=440)
    button4 = Button(root2, width=20, font=("arial", 15), text="TASK MANAGER", command=TaskManager)
    button4.place(x=900, y=510)
    button4 = Button(root2, width=20, font=("arial", 15), text="Back", command=back)
    button4.place(x=0, y=0)

    root2.mainloop()
    def pcprogramsdestroy():
        root2.destroy()
        mainwindow()
mainwindow()

	
	

