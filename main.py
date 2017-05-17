import tkinter as tk
from tkinter import messagebox

try:
  from PIL import Image, ImageTk
  pil_enabled = True
except ImportError:
  pil_enabled = False
  
from math import sqrt

class App(tk.Tk):
  def __init__(self):
    tk.Tk.__init__(self)
    self.geometry('250x250')
    self.title('EasyCalc')

    button_pyth = tk.Button(self,text='Pythagoras Calculator',command=self.pythagoras,width=self.winfo_reqwidth())
    button_pyth.pack()
    button_quadratic = tk.Button(self,text='Quadratic Calculator',command=self.quadratic,width=self.winfo_reqwidth())
    button_quadratic.pack()

  def pythagoras(self):
    calc_win = PythagorasCalc()
    calc_win.mainloop()

  def quadratic(self):
    calc_win = QuadraticCalc()
    calc_win.mainloop()

class QuadraticCalc(tk.Toplevel):
  def __init__(self):
    global pil_enabled
    
    tk.Toplevel.__init__(self)
    self.title('Quadratic Calculator')
    self.wm_attributes('-topmost',1)
    self.locked = True

    self.form_tag = tk.Label(self,text='ax^2 + bx + c = 0')

    self.tags = [
    tk.Label(self,text='Value A'),
    tk.Label(self,text='Value B'),
    tk.Label(self,text='Value C')
    ]

    self.complete_sqr = tk.Label(self,text='Complete square will show here')
    self.ans = tk.Label(self,text='x=')
    self.ans2=tk.Label(self,text='x=')

    self.entries = [
    tk.Entry(self),
    tk.Entry(self),
    tk.Entry(self)
    ]

    self.button = tk.Button(self,text='Calculate!',command=self.calculate)

    if pil_enabled:
      self.lock_i = Image.open('lock.gif')
      self.unlock_i = Image.open('unlock.gif')

      self.lock_i = self.lock_i.resize((15,15))
      self.unlock_i = self.unlock_i.resize((15,15))

      self.lock = ImageTk.PhotoImage(self.lock_i)
      self.unlock = ImageTk.PhotoImage(self.unlock_i)

      self.lock_b = tk.Button(self,image=self.lock,width='15',height='15',command=self.unlock_win)

    j = 1
    for k in self.entries:
      k.grid(row=j,column=1)
      j+=1

    j = 1
    for k in self.tags:
      k.grid(row=j,column=0)
      j+=1

    self.button.grid(row=4,columnspan=2)
    self.form_tag.grid(row=0,columnspan=2)

    self.complete_sqr.grid(row=5,columnspan=2)
    self.ans.grid(row=6,column=0)
    self.ans2.grid(row=6,column=1)

    if pil_enabled:
      self.lock_b.grid(row=7,column=0)

  def unlock_win(self):
    if self.locked:
      self.wm_attributes('-topmost',0)
      self.locked = False
      self.lock_b.config(image=self.unlock)
    elif not self.locked:
      self.wm_attributes('-topmost',1)
      self.locked = True
      self.lock_b.config(image=self.lock)

  def calculate(self):
    a = ''
    b = ''
    c = ''

    a = float(self.entries[0].get())
    b = float(self.entries[1].get())
    c = float(self.entries[2].get())

    b = b/a
    c = c/a

    b2 = -1*(b/2)
    c2 = abs(c - (b2**2))

    complete_sqr = str(b2) + '± √' + str(c2) + ' = x'

    ans1 = b2 + sqrt(c2)
    ans2 = b2 - sqrt(c2)

    ans1 = round(ans1,4)
    ans2 = round(ans2,4)

    self.complete_sqr['text'] = complete_sqr
    self.ans['text'] = 'x=' + str(ans1)
    self.ans2['text'] = 'x=' + str(ans2)


class PythagorasCalc(tk.Tk):
  def __init__(self):
    tk.Tk.__init__(self)
    self.title('Pythagoras Calculator')

    self.a_tag = tk.Label(self,text='Height')
    self.b_tag = tk.Label(self,text='Width')
    self.h_tag = tk.Label(self,text='Hyp')

    self.entries = [
    tk.Entry(self),
    tk.Entry(self),
    tk.Entry(self)
    ]

    self.button = tk.Button(self,text='Calculate!',command=self.calculate)

    j = 0
    for k in self.entries:
      k.grid(row=j,column=1)
      j+=1
    self.a_tag.grid(row=0)
    self.b_tag.grid(row=1)
    self.h_tag.grid(row=2)

    self.button.grid(row=3,columnspan=2)

  def calculate(self):
    values_available = 0
    for k in self.entries:
      if k.get() != '':
        try:
          x = float(k.get())
        except: return
        values_available += 1
    if values_available == 2:
      a = ''
      b = ''
      h = ''

      a = self.entries[0].get()
      b = self.entries[1].get()
      h = self.entries[2].get()

      print('h' + h)
      print('b' + b)
      print('a' + a)

      if h == '':
        self.entries[2].insert(0,str(sqrt(float(a)**2 + float(b)**2)))
      else:
        if a == '':
          self.entries[0].insert(0,str(sqrt(float(h)**2 - float(b)**2)))
        if b == '':
          self.entries[1].insert(0,str(sqrt(float(h)**2 - float(a)**2)))


app = App()
app.mainloop()
