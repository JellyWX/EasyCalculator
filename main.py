import tkinter as tk
from tkinter import messagebox

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

  def quadratic(self):
    pass

class PythagorasCalc(tk.Tk):
  def __init__(self):
    tk.Tk.__init__(self)
    self.title('Pythagoras Calculator')

    self.a_tag = tk.Label(self,text='Height')
    self.b_tag = tk.Label(self,text='Width')
    self.h_tag = tk.Label(self,text='Hyp')

    self.entries = {
    'height' : tk.Entry(self),
    'width' : tk.Entry(self),
    'hyp' : tk.Entry(self)
    }

    self.button = tk.Button(self,text='Calculate!',command=self.calculate)

    j = 0
    for _,k in self.entries.items():
      k.grid(row=j,column=1)
      j+=1
    self.a_tag.grid(row=0)
    self.b_tag.grid(row=1)
    self.h_tag.grid(row=2)

    self.button.grid(row=3,columnspan=2)

  def calculate(self):
    values_available = 0
    for _,k in self.entries.items():
      if k.get() != '':
        try:
          x = float(k.get())
        except: return
        values_available += 1
    if values_available == 2:
      a = ''
      b = ''
      h = ''

      a = self.entries['height'].get()
      b = self.entries['width'].get()
      h = self.entries['hyp'].get()

      print('h' + h)
      print('b' + b)
      print('a' + a)

      if h == '':
        self.entries['hyp'].insert(0,str(sqrt(float(a)**2 + float(b)**2)))
      else:
        if a == '':
          self.entries['height'].insert(0,str(sqrt(float(h)**2 - float(b)**2)))
        if b == '':
          self.entries['width'].insert(0,str(sqrt(float(h)**2 - float(a)**2)))


app = App()
app.mainloop()
