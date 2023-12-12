import base64
from tkinter import scrolledtext
from tkinter import messagebox
import tkinter.ttk
import main


def newwindow():
    checkwindow = messagebox.askyesno('Confirming...', 'Are you sure to exit the program?')

    if checkwindow:
        window.quit()

    else:
        pass


methodobject = main

icon = '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'
icondata = base64.b64decode(icon)
tempFile= "icon.ico"
iconfile= open(tempFile,"wb")
iconfile.write(icondata)
iconfile.close()

windowwidth = 600
windowheight = 400

window = tkinter.Tk()

screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()

x = (screenwidth - windowwidth) / 2
y = (screenheight - windowheight) / 2

window.geometry('%dx%d+%d+%d' % (windowwidth, windowheight, x, y))
window.title('Morse Converter')
try:
    window.iconbitmap(tempFile)

except tkinter.TclError:
    errorwindow = messagebox.showerror('ERROR', 'Window Icon Not Found!')

window.configure(bg='#242424')
window.resizable(False, False)

infoarea = tkinter.LabelFrame(master=window, text='Info', labelanchor='nw', font=('azonix', 15), bg='#242424',
                              foreground='white')
infoarea.place(x=5, y=0, width=235, height=180)

infotext1 = tkinter.Label(master=infoarea, bg='#242424', foreground='white', text='Welcome to\nMorse\nConverter.',
                          font=('azonix', 20), fg='white', height=3)
infotext1.place(x=10, y=0)

infotext2 = tkinter.Label(master=infoarea, bg='#242424', foreground='white',
                          text='Please use \'/\' to insert\nspaces between\nMorse words.', font=('azonix', 10),
                          fg='white', height=3)
infotext2.place(x=15, y=100)

entryarea = tkinter.LabelFrame(master=window, text='Entry', labelanchor='ne', font=('azonix', 15), bg='#242424',
                               foreground='white')
entryarea.place(x=245, y=0, width=350, height=180)

entrytext = tkinter.Text(master=entryarea, bg='#242424', foreground='white', font=('azonix', 15),
                         insertbackground='white')
entrytext.pack(padx=5, pady=5)

resultarea = tkinter.LabelFrame(master=window, text='Result', font=('azonix', 15), labelanchor='nw', bg='#242424',
                                foreground='white')
resultarea.place(x=5, y=185, width=350, height=210)

resulttext = scrolledtext.ScrolledText(master=resultarea, font=('azonix', 20), bg='#242424', foreground='white')
resulttext.place(relx=.01, rely=.0, width=340, height=185)

processarea = tkinter.LabelFrame(master=window, text='Process', font=('azonix', 15), labelanchor='ne', bg='#242424',
                                 foreground='white')
processarea.place(x=360, y=185, width=235, height=210)

morsetolatinbutton = tkinter.Button(master=processarea, text='Morse to Latin', font=('azonix', 15), bg='#242424',
                                    foreground='white')
morsetolatinbutton.pack(pady=10)

latintomorsebutton = tkinter.Button(master=processarea, text='Latin to Morse', font=('azonix', 15), bg='#242424',
                                    foreground='white')
latintomorsebutton.pack(pady=10)

quitbutton = tkinter.Button(master=processarea, text='Quit', font=('azonix', 15), bg='#242424', foreground='white')
quitbutton.pack(pady=10)

signaturelabel = tkinter.Label(master=processarea, text='Written by Seferhan KAYA', font=('azonix', 10), bg='#242424',
                               foreground='white')
signaturelabel.pack()

quitbutton['command'] = newwindow

latintomorsebutton['command'] = methodobject.latintomorse

morsetolatinbutton['command'] = methodobject.morsetolatin

window.mainloop()
