import infoFetcher
from tkinter import *
import tkinter.filedialog
import os





root=Tk()
root.config(bg="black")
root.geometry("600x600")
root.resizable(False,False)
frame=Frame(root)

frame.winfo_toplevel().title("Network Scanner")
scroll=Scrollbar(frame,orient=VERTICAL)
list_box=Listbox(frame,width=100,height=100,yscrollcommand=scroll.set)
scroll.config(command=list_box.yview)
scroll.pack(side=RIGHT,fill=Y)
list_box.config(bg="black",fg="#00FF00")
list_box.pack()

def scan():
    list_box.delete(0,END)
    infoFetcher.scan()
    info = infoFetcher.info
    for key, value in info.items():
        list_box.insert(END, str(key) + " : " + "\n")
        list_box.insert(END, "    ")
        for key1, value1 in value.items():
            if type(value1) != list:
                list_box.insert(END, "- " + key1 + " : " + value1)

            else:
                for e in value1:
                    list_box.insert(END, "- Email : " + e)
            list_box.insert(END, " ")
        list_box.insert(END, "////////////////"+" \n")
        list_box.insert(END, "                 " + " \n")
        list_box.insert(END, "       ")
    unident=infoFetcher.unidentified
    if unident:
        list_box.insert(END, "//////////////// Unidentified IP Address Below ; Further Control Is Needed !!")
        list_box.itemconfig(END, fg="#FF0000")
        for e in unident:
            list_box.insert(END, "       ")
            list_box.insert(END, e)
            list_box.itemconfig(END,fg="#FF0000")
            list_box.insert(END, "       ")
            list_box.insert(END, "       ")
            list_box.insert(END, "       ")
            list_box.insert(END, "       ")
            list_box.insert(END, "       ")
            list_box.insert(END, "       ")
            list_box.insert(END, "       ")
            list_box.insert(END, "       ")



def write():
    try:
        root = tkinter.Tk()
        root.withdraw()
        currdir = os.getcwd()
        tempdir = tkinter.filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
        root.destroy()
        infoFetcher.write(tempdir)
    except :
        pass    



buttonScan=Button(frame,text="Scan",bg="black",command=scan,padx=40)

buttonScan.place_configure(x=210,y=570)

writing=Button(frame,text="Write",bg="black",command=write,padx=40)

writing.place_configure(x=210,y=540)


frame.pack()
root.mainloop()