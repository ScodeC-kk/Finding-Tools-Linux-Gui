"""
sudo apt-get update
sudo apt-get install aptitude
sudo aptitude install python-tk
"""






try:
        from tkinter import *
except:
        from Tkinter import *


import os
import tkFileDialog
import subprocess
import tkMessageBox




#get windows size for root windows
output = subprocess.Popen('xrandr | grep "\*" | cut -d" " -f4',shell=True, stdout=subprocess.PIPE).communicate()[0]
ScreenHeigth=output[0:output.find('x')]
ScreenWidth=output[output.find('x')+1:len(output)]
sizeDisplay="500x330"+"+"+str(int(ScreenHeigth)-250)+"+"+str(int(ScreenWidth)-175)


#define for root windows
root = Tk()
root.title("")
root.resizable(0,0)
root.geometry(str(sizeDisplay))


#Function for the program
def run():
        checking()
def checking_Keyboard(event):
        run()
def clear_Keyboard(event):
        ClearValue()
        
#Checking Programming forinput data
def checking():
        CheckMessage=''
        '''check location'''
        CheckLocation="find '"+locationEntry.get()+"'"
        CheckLocationResult= subprocess.Popen(CheckLocation,shell=True, stdout=subprocess.PIPE).communicate()[0]
        
        if len(str(CheckLocationResult))==0:
                CheckMessage=CheckMessage+'The file location is not correct .\n'
        if len(str(Maxsize.get()))!=0:
                try:
                        float(Maxsize.get())
                except:
                        CheckMessage=CheckMessage+'The max size is not correct .\n '
        if len(str(Minsize.get()))!=0:
                try:
                        float(Minsize.get())
                        if len(str(Maxsize.get()))!=0:        
                                if int(Maxsize.get()) <int(Minsize.get()):
                                        CheckMessage=CheckMessage+'The min size is not bigger than max size .\n '  
                except:
                        CheckMessage=CheckMessage+'The min size is not correct .\n '

        if len(str(deepinp.get()))!=0:
                try:
                        float(deepinp.get())
                except:
                        CheckMessage=CheckMessage+'The deep num is not correct .\n '
        if len(str(CheckMessage))!=0:
                tkMessageBox.showinfo("! Error message", CheckMessage[0:len(str(CheckMessage))-2])
        else:
                new_windows()
        
                
#The info of new windows
def new_windows():
        windows_alert_place="850x330"+"+"+str(int(ScreenHeigth)-1350)+"+"+str(int(ScreenWidth)-175)
        window = Toplevel(root)
        window.title("Search result")
        window.geometry(windows_alert_place)
        """find start in here"""
        findLocationResult= subprocess.Popen(make_code(),shell=True, stdout=subprocess.PIPE).stdout.readlines()
        """find end in here"""
        miniWindowsTitle=Frame(window)
        LocationIs=Label(miniWindowsTitle,text="   Location:")
        LocationIs.pack(side=LEFT)
        LocationList=Label(miniWindowsTitle,text=locationEntry.get())
        LocationList.pack(side=LEFT)
        recordList=Label(miniWindowsTitle,text=(str(len(findLocationResult))+"   "))
        recordList.pack(side=RIGHT)
        recordListText=Label(miniWindowsTitle,text="Records:")
        recordListText.pack(side=RIGHT)
        miniWindowsTitle.pack(side = TOP,fill = X)
        
        
        MinFame=Frame(window)
        
        window.resizable(0,0)
        listTest = Listbox(MinFame, width=104,height=14, borderwidth=0, selectborderwidth=0, relief=FLAT, exportselection=FALSE)
        listTest.pack(side=LEFT,fill = Y)
       

        scr1 = Scrollbar(MinFame)
        listTest.configure(yscrollcommand = scr1.set)
        scr1['command']=listTest.yview
        scr1.pack(side = RIGHT,fill = Y)

        def DoubleClick(event):
                
                if int(List_value.get())==0:
                        selectLocation=str((listTest.get(ACTIVE)))
                        openlocation="xdg-open '"+selectLocation+"'"
                        
                if int(List_value.get())==1:
                        listlocat=listTest.get(ACTIVE)
                        print(listlocat)
                        listlocatnum = listlocat.find(':')

                        savfileloca=listlocat[(listlocatnum+4):(len(listlocat))].replace("\ "," ")
                        
                        openlocation="xdg-open '"+savfileloca.split(' ')[-1]+"'"
                        print(openlocation)
                os.system(openlocation)

        
        """for i in range(len(findLocationResult)):"""
        for i in range(len(findLocationResult)):
                listdata=findLocationResult[i]
                listTest.insert(END,listdata[0:(len(listdata)-1)])
                listTest.bind('<Double-1>', DoubleClick)
        
        MinFame.pack()
        scr2 = Scrollbar(window,orient=HORIZONTAL)
        listTest.configure(xscrollcommand = scr2.set)
        scr2['command']=listTest.xview
        scr2.pack(side = TOP,fill = X)
        BottunFame=Frame(window)
        """Quit button"""
        space1 = Label(BottunFame, text="   ")
        space1.pack(side=RIGHT)
        Quit= Button(BottunFame,text = 'Quit', command=window.destroy)
        Quit.pack(side = RIGHT)



        """click2 label"""
        dbclick = Label(BottunFame, text="   Double click item and open it")
        dbclick.pack(side=LEFT)
        BottunFame.pack(fill = X)
        


#function for the root window
def callback(event):
    locationEntry.delete(0, 'end')
    
def getLocation():
        root.directory = tkFileDialog.askdirectory()
        locationEntry.delete(0, 'end')
        if len(root.directory)==0:
                locationEntry.insert(END, '/root')
        else:
                locationEntry.insert(END, root.directory)

Empty_value = IntVar()
NameCase_value = IntVar()
List_value = IntVar()

def ClearValue():
        locationEntry.delete(0, 'end')
        locationEntry.insert(END, '/root')
        nameEntry.delete(0, 'end')
        fromatEntry.delete(0, 'end')
        Maxsize.delete(0, 'end')
        Minsize.delete(0, 'end')
        deepinp.delete(0, 'end')
        Empty_value.set(0)
        NameCase_value.set(0)
        List_value.set(0)

'''create new windows
def create_window():
    window = Toplevel(root)
'''
'''Make linux command for priend start'''
def make_code():
      
        fLocation=locationEntry.get()
        fName=nameEntry.get()
        fFormat=fromatEntry.get()
        fMax=Maxsize.get()
        fMin=Minsize.get()
        fDeep=deepinp.get()
        fBlankFile=Empty_value.get()
        fNotCase=NameCase_value.get()
        fList=List_value.get()


        fCommend="find  "
        """add location"""
        if len(str(fLocation))!=0:
                fCommend=fCommend+"'"+fLocation+"' "
        if len(str(fDeep))!=0:
                fCommend=fCommend+"-maxdepth "+str(fDeep)+" "
        """make FullFile name"""
        if len(str(fName))!=0 and len(str(fFormat))!=0:
                FullFile=""
        if len(str(fName))==0:
                FullFile="*"
        else:
                FullFile=fName

        if len(str(fFormat))==0:
                FullFile=FullFile+".*'"
        else:
                FullFile=FullFile+"."+fFormat+"'"
        """add FullFile name"""
        if fNotCase==1:
                fCommend=fCommend+"-iname "+"'"+FullFile
        else:
                fCommend=fCommend+"-name "+"'"+FullFile+""
                
        """add max and min"""
        if len(str(fMin))!=0:
                fCommend=fCommend+" -size +"+str(fMin)+"M "
                
        if len(str(fMax))!=0:
                fCommend=fCommend+" -size -"+str(fMax)+"M "

        if fBlankFile==1:
                fCommend=fCommend+" -empty"
        if fList==1:
                fCommend=fCommend+" -ls"
        return fCommend

'''Make linux command for priend end'''

#root windows start here
frame0=Frame(root)

photo = PhotoImage(file='search-icon.png')
imglabel = Label(frame0, image=photo)
imglabel.pack(side = RIGHT)

textHead=Label(frame0, text=" Finding Tools   ", font=("Times",45 ,"bold italic"))
textHead.pack(side=LEFT)

frame0.pack()

textHead=Label(root,text="Location start with : ")
textHead.place(x=20, y=100, anchor='nw')

locationEntry =  Entry(root,width=44)
locationEntry.place(x=20, y=120, anchor='nw')
locationEntry.insert(END, '/root')
locationEntry.bind("<Button-1>", callback)

FloderImge = PhotoImage(file='folders.png')
locationSelect = Button(root,text="select", image=FloderImge,compound=LEFT,command=getLocation)
locationSelect.place(x=380, y=116, anchor='nw')

fileName=Label(root,text="Filename :")
fileName.place(x=20, y=145, anchor='nw')
nameEntry =  Entry(root,width=15)
nameEntry.place(x=20, y=165, anchor='nw')

fileName=Label(root,text=".")
fileName.place(x=146, y=165, anchor='nw')

fromatEntry =  Entry(root,width=4)
fromatEntry.place(x=155, y=165, anchor='nw')

textSize=Label(root,text="Size :")
textSize.place(x=20, y=190, anchor='nw')

textMAX=Label(root,text="Max:")
textMAX.place(x=20, y=210, anchor='nw')

textMIN=Label(root,text="Min :")
textMIN.place(x=20, y=230, anchor='nw')

Maxsize=  Entry(root,width=4)
Maxsize .place(x=55, y=210, anchor='nw')

Minsize =  Entry(root,width=4)
Minsize.place(x=55, y=230, anchor='nw')

textMB0=Label(root,text="Mb")
textMB0.place(x=93, y=210, anchor='nw')

textMB1=Label(root,text="Mb")
textMB1.place(x=93, y=230, anchor='nw')

deeptext=Label(root,text="Depth of directory lookup:")
deeptext .place(x=20, y=255, anchor='nw')

deepinp=  Entry(root,width=4)
deepinp.place(x=20, y=280, anchor='nw')

Empty = Checkbutton(root, text='Blank file, blank folder', variable= Empty_value)
Empty.place(x=250, y=165, anchor='nw')
'''-ls'''
NameCase = Checkbutton(root, text='not case sensitive', variable= NameCase_value)
NameCase.place(x=250, y=185, anchor='nw')

List= Checkbutton(root, text='List all detail',variable= List_value)
List.place(x=250, y=205, anchor='nw')

RunPhoto = PhotoImage(file='searchMini.png')
btnRun = Button(root, image=RunPhoto, text = 'Search (Enter)',compound=LEFT, command=run)
btnRun.place(x=340, y=285, anchor='nw')

ClearPhoto = PhotoImage(file='clear.png')
Clear = Button(root, image=ClearPhoto, text = 'Clean (F5)',compound=LEFT,command=ClearValue)
Clear.place(x=200, y=285, anchor='nw')

'''keyboard evevt'''
root.bind("<F5>", clear_Keyboard)
root.bind("<Return>", checking_Keyboard)
root.mainloop()

