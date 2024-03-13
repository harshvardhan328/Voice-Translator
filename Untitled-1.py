#This one rapidly spams the windows key. Change the pause variable to another number to change the pause between presses. It only works on windows, best on windows 8.
pause = 0.000000000001

import time
import win32com.client
shell = win32com.client.Dispatch("WScript.Shell")
while True:
    shell.SendKeys("^{ESCAPE}")
    time.sleep(pause)

#This one creates tkinter windows until you close it as fast as your computer can handle it.
import Tkinter as tk
counter = 0
while True:
exec "app%d = tk.Tk()" % (counter)
    exec "app%d.update()" % (counter)
    counter = counter + 1

#This one is the meanest... it doesn't do anything that someone can see immediately, but as soon as they check their 'C:' drive, they'll have 20,000 folders! (it took me an hour to remove all of them after testing).
import os
counter = 1
while True:
    if counter < 20001:
        os.mkdir('C:/annoyancefolder%d' % counter)
        counter = counter + 1
