import password_generator
import PySimpleGUI as sg
import pyperclip
from notifypy import Notify
notif = Notify()
notif.title = 'Password generator'
notif.message = 'Password has been generated!'
# All the stuff inside your window.
layout = [  [sg.Text('Password Generator')],
            [sg.Checkbox('Do you want numbers?')],
            [sg.Checkbox('Do you want symbols?')],
            [sg.Text('Password Lenght'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]
                        # layout = [  [sg.Text('Password Generator')],
                        # [sg.Text('Do you want numbers?'), sg.InputText()],
                        # [sg.Text('Do you want symbols?'), sg.InputText()],
                        # [sg.Text('Password Lenght'), sg.InputText()],
                        # [sg.Button('Ok'), sg.Button('Cancel')] ]
# Create the Window
window = sg.Window('Password Generator', layout)
# Event Loop to process "events" and get the "values" of the inputs

event, values = window.read()

window.close()
numbers = values[0]
symbols = values[1]
lenght = int(values[2])
# k = int(input("Unesite duzinu vase sifre: "))
# simboli = input("Da li zelite simbole u vasoj sifri: ")
# cifre = input("Da li zelite cifre u vasoj sifri: ")
notif.send()
sg.popup('Password has been copied to clipboard')
pyperclip.copy(password_generator.password_generator(numbers, symbols, lenght))
