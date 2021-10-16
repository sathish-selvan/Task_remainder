from tkinter import *
from PIL import ImageTk,Image
import calendar
from datetime import date
from tkcalendar import *
import sqlite3
from tktimepicker import AnalogPicker, AnalogThemes


#Data base

#Creating a data base
# conn = sqlite3.connect("task_remainder.db")

#Creating a cursor
# c = conn.cursor()

# c.execute("""CREATE TABLE remainder(
#     date text,
#     task text,
#     time text
#     )""")


root = Tk()
root.geometry("900x600")
root.wm_attributes("-topmost", True)
#root.wm_attributes("-transparent", True)
#root.config(bg='systemTransparent')

bg = PhotoImage(file = "background.png")

label1 = Label( root, image = bg)

# label1.pack(fill=BOTH, expand=True)
label1.place(x = 0, y = 0,relwidth=1, relheight=1)


def get_TD(time_picker,cal,inputtxt):
    a = str(time_picker.time())
    b = str(cal.get_date())
    txt = str(inputtxt.get(1.0,"end-1c"))
    print(type(a),type(b),type(txt))
    conn = sqlite3.connect("task_remainder.db")

    #Creating a cursor
    c = conn.cursor()
    c.execute('''INSERT INTO remainder (date,task,time) VALUES (?, ?, ?)''',
            [
                b,
                txt,
                a,
            ])
    #commit changes
    conn.commit()

    #close connection
    conn.close()

def addEvent():
    newWindow = Toplevel()
    
    # sets the title of the
    # Toplevel widget
    newWindow.title("Add Event")
    newWindow.configure(bg="#004d3b")
    # sets the geometry of toplevel
    newWindow.geometry("900x600")
    today = date.today()

    # dd/mm/YY
    d1 =list(map(int,today.strftime("%d/%m/%Y").split("/")))
    cal= Calendar(newWindow, selectmode="day",year= d1[2], month=d1[1], day=d1[0])
    cal.place(relx=.25, rely=.3,height=325, width=325, anchor="center")
    # A Label widget to show in toplevel
    time_picker = AnalogPicker(newWindow)
    time_picker.place(relx=.7, rely=.3, anchor="center")
    theme = AnalogThemes(time_picker)
    theme.setDracula()
    
    ef = Frame(newWindow,width=760,height=50)
    ef.place(relx=.49, rely=.7, anchor="center")
    lab1 = Label(ef, text="ADD EVENT",height=5,width=10)
    lab1.pack(side=LEFT)
    var = StringVar()
    inputtxt = Text(ef,height=5,width=70)
  
    inputtxt.pack(fill=BOTH,side=RIGHT)
    but1 = Button( newWindow, text = "ADD",command=lambda:get_TD(time_picker,cal,inputtxt))
    but1.place(relx=.5, rely=.85, anchor="center")

# back.place(relx=.5, rely=.5, anchor="center")
# Add buttons
photo = PhotoImage(file = r"Addevent.png")
photo = photo.subsample(3,3)
button1 = Button(root,text="Add Event",height = 100, width = 150, image=photo, borderwidth=0,bg="#161616",command=addEvent)
button1.place(relx=.6, rely=.6, anchor="center")

photo1 = PhotoImage(file = r"Viewevent.png")
photo1 = photo1.subsample(3,3)
button2 = Button( root, text = "Start",height = 100, width = 150,image=photo1, borderwidth=0,bg="#161616")
button2.place(relx=.6, rely=.8, anchor="center")

photo2 = PhotoImage(file = r"Todayevent.png")
photo2 = photo2.subsample(3,3)
button3 = Button( root, text = "Reset",height = 100, width = 150,image=photo2, borderwidth=0,bg="#161616")
button3.place(relx=.8, rely=.6, anchor="center")

photo3 = PhotoImage(file = r"Todayevent.png")
photo3 = photo3.subsample(3,3)
button4 = Button( root, text = "Quit",height = 100, width = 150,image=photo3, borderwidth=0,bg="#161616")
button4.place(relx=.8, rely=.8, anchor="center")

root.resizable(True, True)
root.lift()
root.attributes('-topmost',True)
root.after_idle(root.attributes,'-topmost',False)
root.mainloop()




