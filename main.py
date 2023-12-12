import tkinter
from tkinter import messagebox
import GUI


latintomorsedictionary = {'A': '.-', 'B': '-...', 'C': '-.-.',
                          'D': '-..', 'E': '.', 'F': '..-.',
                          'G': '--.', 'H': '....', 'I': '..',
                          'J': '.---', 'K': '-.-', 'L': '.-..',
                          'M': '--', 'N': '-.', 'O': '---',
                          'P': '.--.', 'Q': '--.-', 'R': '.-.',
                          'S': '...', 'T': '-', 'U': '..-',
                          'V': '...-', 'W': '.--', 'X': '-..-',
                          'Y': '-.--', 'Z': '--..',

                          '0': '-----', '1': '.----', '2': '..---',
                          '3': '...--', '4': '....-', '5': '.....',
                          '6': '-....', '7': '--...', '8': '---..',
                          '9': '----.', ' ': ' ', '	': '	'
                          }

morsetolatindictionary = {value: key for key, value in latintomorsedictionary.items()}


def morsetolatin():
    try:
        GUI.resulttext.delete('1.0', 'end')
        entry = GUI.entrytext.get("1.0", 'end-1c') + ' '

        entry = entry.replace(' /', '/')
        entry = entry.replace(' / ', '/')
        entry = entry.replace('/ ', '/')

        word = ''
        result = ''

        for x in entry:

            if x != ' ' and x != '/':
                word += x

            elif x == '/':
                result += morsetolatindictionary.get(word)
                word = ''
                result += ' '

            else:
                result += morsetolatindictionary.get(word)
                word = ''

        GUI.resulttext.insert(tkinter.END, result)

    except TypeError:
        errorbox = tkinter.messagebox.showerror('Error', 'Not found! Please try again.')


def latintomorse():
    try:
        GUI.resulttext.delete('1.0', 'end')
        entry = GUI.entrytext.get("1.0", 'end-1c')
        result = ' '.join(latintomorsedictionary.get(i.upper()) for i in entry)
        GUI.resulttext.insert(tkinter.END, result)

    except TypeError:
        errorbox = tkinter.messagebox.showerror('Error', 'Not found! Please try again.')
