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

iconlocation = 'icon.ico'
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
    window.iconbitmap(iconlocation)

except FileNotFoundError:
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
