import os
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.font as font
import time

#Generate window 
window = Tk()
#Name of window
window.title("Alexa Flashcards")
#Colour of window
window.configure(background="#000000")
#Window size and position
window.geometry("1920x1080+-10+0")
myFont = font.Font(family='Garamond')

#set a font
alexaFont = font.Font(family='Cambria', size=10, slant="italic")
alexaFont2 = font.Font(family='Alias', size=10)



#top left icon
window.call('wm', 'iconphoto', window._w, tk.PhotoImage(file=r"images\flash-cards.png"))

time.sleep(200)

#open new window(test)
def openNewWindow():
     
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(window)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("Settings")
 
    # sets the geometry of toplevel
    newWindow.geometry("350x400")
 
    # A Label widget to show in toplevel
    Label(newWindow,
          text ="This do be settings beepedy boppidy").pack()
    #icon
    window.call('wm', 'iconphoto', newWindow._w, tk.PhotoImage(file=r"images\settings.png"))



#alexa boxes change colour when hovering over
def changeOnHover1(btn1, colorOnHover, colorOnLeave, bdoh, bdol):
  
    # adjusting backgroung of the widget
    # background on entering widget
    btn1.bind("<Enter>", func=lambda e: btn1.config(
        background=colorOnHover, bd=bdoh, text="This command allows you\n to schedule flashcards so\n that your alexa will read\n them out at a specified time...\n",font=alexaFont2))
    
  
    # background color on leving widget
    btn1.bind("<Leave>", func=lambda e: btn1.config(
        background=colorOnLeave, bd=bdol, text='"Alexa, do this...\n 1"',font=alexaFont))

def changeOnHover2(btn2, colorOnHover, colorOnLeave, bdoh, bdol):
  
    # adjusting backgroung of the widget
    # background on entering widget
    btn2.bind("<Enter>", func=lambda e: btn2.config(
        background=colorOnHover, bd=bdoh, text="This command will respond\n with a randomly chosen card\n from all decks if none are\n specified or you may specify\n a deck...\n",font=alexaFont2))
    
  
    # background color on leving widget
    btn2.bind("<Leave>", func=lambda e: btn2.config(
        background=colorOnLeave, bd=bdol, text='"Alexa, do this...\n 2"',font=alexaFont))

def changeOnHover3(btn3, colorOnHover, colorOnLeave, bdoh, bdol):
  
    # adjusting backgroung of the widget
    # background on entering widget
    btn3.bind("<Enter>", func=lambda e: btn3.config(
        background=colorOnHover, bd=bdoh, text="This command does this...\n 3",font=alexaFont2))
    
  
    # background color on leving widget
    btn3.bind("<Leave>", func=lambda e: btn3.config(
        background=colorOnLeave, bd=bdol, text='"Alexa, do this...\n 3"',font=alexaFont))

def changeOnHover4(btn4, colorOnHover, colorOnLeave, bdoh, bdol):
  
    # adjusting backgroung of the widget
    # background on entering widget
    btn4.bind("<Enter>", func=lambda e: btn4.config(
        background=colorOnHover, bd=bdoh, text="This command Will read a\n flashcard (or multiple) that you\n have never seen before\n",font=alexaFont2))
    
  
    # background color on leving widget
    btn4.bind("<Leave>", func=lambda e: btn4.config(
        background=colorOnLeave, bd=bdol, text='"Alexa, do this...\n 4"',font=alexaFont))

def changeOnHover5(btn5, colorOnHover, colorOnLeave, bdoh, bdol):
  
    # adjusting backgroung of the widget
    # background on entering widget
    btn5.bind("<Enter>", func=lambda e: btn5.config(
        background=colorOnHover, bd=bdoh, text="This command will repeat a\n card (or multiple) which you\n have seen before, and are\n ordered by difficulty...\n",font=alexaFont2))
    
  
    # background color on leving widget
    btn5.bind("<Leave>", func=lambda e: btn5.config(
        background=colorOnLeave, bd=bdol, text='"Alexa, do this...\n 5"',font=alexaFont))

    

#toolbar
# Create menubar by setting the color
menubar = Menu(window, background='#00bcf2', fg='white')
  
# Declare file and edit for showing in menubar
file = Menu(menubar, tearoff=False)
edit = Menu(menubar, tearoff=False)
Help = Menu(menubar, tearoff=0)
  
# Add commands in in file menu
file.add_command(label="New")
file.add_command(label="Exit", command=window.destroy) # Open any program, text or office document)

# Add commands in edit menu
edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="Paste")

  
# Display the file and edit declared in previous step
menubar.add_cascade(label="File", menu=file)
menubar.add_cascade(label="Edit", menu=edit)
menubar.add_cascade(label="Help", menu=Help)

# Displaying of menubar in the app
window.config(menu=menubar)
  




#Top grey frame
bottomframe = Frame(window,height="150",width="1920",bg="#191919")
bottomframe.place(x=0, y=0)
bottomframe.pack()


#alexa command text change 1
#def toggleText1():  
#	if(btn1['text']=='This command does this\n beeep bop boop doopedy doop'):
#		btn1['text']='"Alexa, do this beep\n bop boop"'
#		btn1['font']=alexaFont
#	else:
#		btn1['text']='This command does this\n beeep bop boop doopedy doop'
#		btn1['font']=alexaFont2
                

#alexa command text change 2
#def toggleText2():  
#	if(btn2['text']=='This command does this\n beeep bop boop doopedy doop'):
#		btn2['text']='"Alexa, do this beep\n bop boop"'
#		btn2['font']=alexaFont
#	else:
#		btn2['text']='This command does this\n beeep bop boop doopedy doop'
#		btn2['font']=alexaFont2

#alexa command text change 3
#def toggleText3():  
#	if(btn3['text']=='Submit'):
#		btn3['text']='Submitted'
#	else:
#		btn3['text']='Submit'

#alexa command text change 4
#def toggleText4():  
#	if(btn4['text']=='Submit'):
#		btn4['text']='Submitted'
#	else:
#		btn4['text']='Submit'

#alexa command text change 5
#def toggleText5():  
#	if(btn5['text']=='Submit'):
#		btn5['text']='Submitted'
#	else:
#		btn5['text']='Submit'
#

#Top icons
# Resizing image to fit on button
photo_1 = PhotoImage(file = r"images\echo-dot.png")
photo_2 = PhotoImage(file = r"images\flash-cards.png")
photo_3 = PhotoImage(file = r"images\settings.png")
photo_4 = PhotoImage(file = r"images\alarm-clock.png")
photo_0 = PhotoImage(file = r"images\image.png")
photo_6 = PhotoImage(file = r"images\shuffle.png")
photo_7 = PhotoImage(file = r"images\numbers.png")
photo_8 = PhotoImage(file = r"images\new.png")
photo_9 = PhotoImage(file = r"images\repeat.png")



photo1 = photo_1.subsample(1, 1)
photo2 = photo_2.subsample(1, 1)
photo3 = photo_3.subsample(1, 1)
photo4 = photo_4.subsample(1, 1)
photo5 = photo_0.subsample(1, 1)
photo6 = photo_6.subsample(1, 1)
photo7 = photo_7.subsample(1, 1)
photo8 = photo_8.subsample(1, 1)
photo9 = photo_9.subsample(1, 1)


btnT1=Button(window, text = 'Commands',fg='#ffffff',image=photo1,bd='0', compound = TOP,cursor='hand2',background="#191919",height="76",width="62")
btnT1.place(x=500, y=40)

btnT2=Button(window, text = 'Decks',fg='#ffffff',image=photo2,bd='0', compound = TOP,cursor='hand2',background="#191919",height="76",width="48")
btnT2.place(x=600, y=40)

btnT3=Button(window, text = 'Settings',fg='#ffffff',image=photo3,bd='0', compound = TOP,cursor='hand2',background="#191919",height="76",width="64",command = openNewWindow)
btnT3.place(x=700, y=40)



#Alexa icons
btn1=Button(window, text = '"Alexa, do this...\n 1"',font=alexaFont, fg="#ffffff", bd="0", image=photo4, compound = TOP, background="#000000",height="200",width="200")
btn1.place(x=70, y=170)
changeOnHover1(btn1, "#191919", "#000000", "2", "0")


btn2=Button(window, text = '"Alexa, do this...\n 2"',font=alexaFont, fg="#ffffff", bd="0", image=photo6, compound = TOP, background="#000000",height="200",width="200")
btn2.place(x=300, y=170)
changeOnHover2(btn2, "#191919", "#000000", "2", "0")
# Set the position of button on the top of window.  

btn3=Button(window, text = '"Alexa, do this...\n 3"',font=alexaFont, fg="#ffffff", bd="0", image=photo7, compound = TOP, background="#000000",height="200",width="200")
btn3.place(x=530, y=170)
changeOnHover3(btn3, "#191919", "#000000", "2", "0")

btn4=Button(window, text = '"Alexa, do this...\n 4"',font=alexaFont, fg="#ffffff", bd="0", image=photo8, compound = TOP, background="#000000",height="200",width="200")
btn4.place(x=760, y=170)
changeOnHover4(btn4, "#191919", "#000000", "2", "0")

btn5=Button(window, text = '"Alexa, do this...\n 5"',font=alexaFont, fg="#ffffff", bd="0", image=photo9, compound = TOP, background="#000000",height="200",width="200")
btn5.place(x=990, y=170)
changeOnHover5(btn5, "#191919", "#000000", "2", "0")






window.mainloop()




#Colour pallet
#Alexa blue:"#31C4F3"
#Top fram dark gry:"#191919"
#background:"#000000"
