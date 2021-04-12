from tkinter import *
from tkinter.scrolledtext import scrolledtext
from tkinter import messagebox, fieldialog
import threading

class Pybot:
    def __init__ (self,root):
        self.root = root
        self.font = ('arial,14')
        self.background_color = '#7e7a7a1'
        self.text_color = '#ffffff'
        
if __name__ == "__main__":
    root = TK()
    root.title ("Pybot-UDAY")
    root.geometry ("500*520")
    root.config (bg="#403b4a")
    root.resizable (0,0)
    Pybot (root)
    root.mainloop ()
    
menubar = menu (self.root)
option_menu = menu (menubar,tearoff = 0)
option_menu.add_command (label = "clear chat", command = self.clear_chat)
option_menu.add_command (label = "save chat", command = self.save_chat)
option_menu.add_separator ()
option_menu.add_command (label = "exit", command = self.root.quit)
menubar.add_cascade (label = "options", menu = option_menu)
self.root.cpnfig (menu = menubar)

self.text_area = scrolledtext (self.root, font = self.font, bg = self.background_colour, fg = self.text_color)
self = text_area.place (x=10, y=10, width=480, height=440)
frame = frame (self.root, bg = self.background_color)
frame.place (x=10, y=460, width=480, heoght=50)

self.entry_box = entry (frame,font = ('arial,14'))
self.entry_box.grid (row = 0, column = 0, pady = 7, padx = 5)

self.send_button = button (frame,text = "send", command = self.human_input)
self.send_button.grid (row = 0, column = 1, pady = 9, padx = 5)

def human_input (self):4
input = self.entry_box.get ()
if input:
    self.text_Area.insert (END,"HUMAN : "+input)
    self.entry_box.delete(0,END)
    self.call_bot (input)
                           
def bot_output (self,input):
    answer = next (res.results).text
if answer:
    self.text_Area.insert (END,"\nPyBot : "+answer +'\n')
    
def call_bot (self,input):
  x = threading.thread (target = self . bot_output,args = (input,))
  x.start ()
    
def save_chat (self):
    filename = filedialog = asksaveasfile ()
    if fileame:
        with open(filename,"w") as f:
            f.write (self.text_area.get (0.0,END))
            
def clear_chat ():
    if messagebox.askyesno ("PyBot says","are you sure"):
        self.text_area.delete (0.0,END)