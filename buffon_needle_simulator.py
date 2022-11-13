from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import random as rd
import pandas as pd

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

janela = Tk() 



janela.title("Botões")

"""
figura = plt.Figure(figsize=(8,4),dpi=60)

grafico = figura.add_subplot(111)

canva = FigureCanvasTkAgg(figura,janela)
canva.get_tk_widget().grid(row=5,column=5)
"""

janela2 = Tk() 



janela2.title("Simulador")

janela2.geometry('400x385')

def needle_simulation(sim):

  sample_size = sim
  sig_figs = 10000
  fig = plt.figure(figsize=[4, 4])

  fig.subplots_adjust(hspace=.4)

  board = fig.add_subplot(1, 1, 1)

  canva = FigureCanvasTkAgg(fig,janela2)
  canva.get_tk_widget().grid(row=5,column=0)

  board.set_xlim(0, 5)
  board.set_ylim(0, 5)

  board.axis('off')

  needles = pd.DataFrame({'x_point':[],'y_point':[],'x_end_point':[],'y_end_point':[],'crossed_line':[]})


  for n in range(0,sample_size):

      x = rd.randrange(sig_figs,(4*sig_figs))/ sig_figs
      y = rd.randrange(sig_figs, (4*sig_figs)) / sig_figs
      theta = rd.randrange(0,360*sig_figs) / sig_figs

      x_end = x + np.sin(np.rad2deg(theta))
      y_end = y + np.cos(np.rad2deg(theta))

      board.plot([x, x_end], [y, y_end])

      if abs(int(x)-int(x_end))==1:
          crossed = True
      else:
          crossed = False

      new_needle = [x,y,x_end,y_end,crossed]

      needles.loc[n]=new_needle

  yard_lines = [[[1,1],[0,5]],[[2,2],[0,5]],[[3,3],[0,5]],[[4,4],[0,5]]]

  for n in range(0,4):
      board.plot(yard_lines[n][0],yard_lines[n][1],'k-')

  crossed_count = len(needles[needles['crossed_line']==True])

  pi_est = 0

  try:
    pi_est = (2*sample_size)/crossed_count

  except ZeroDivisionError:
    pass

  text = 'Valor estimado de pi: {}'.format(round(pi_est,2))
  fig.text(.01, .075, text,fontsize=10)

  #return  plt.show()

def func1():
    needle_simulation(1)

def func2():
    needle_simulation(10)

def func3():
    needle_simulation(25)


def func4():
    needle_simulation(50)


def func5():
    needle_simulation(75)


def func6():
    needle_simulation(100)

def func7():
    needle_simulation(125)

def func8():
    needle_simulation(150)

def func9():
    needle_simulation(300)

botao1 = Button(janela,text="1",width = 10,height=2,command=func1)
botao1.grid(column=0,row=0)

botao2 = Button(janela,text="10",width = 10,height=2,command=func2)
botao2.grid(column=1,row=0)

botao3 = Button(janela,text="25",width = 10,height=2,command=func3)
botao3.grid(column=2,row=0)

botao4 = Button(janela,text="50",width = 10,height=2,command=func4)
botao4.grid(column=0,row=1)

botao5 = Button(janela,text="75",width = 10,height=2,command=func5)
botao5.grid(column=1,row=1)

botao6 = Button(janela,text="100",width = 10,height=2,command=func6)
botao6.grid(column=2,row=1)

botao7 = Button(janela,text="125",width = 10,height=2,command=func7)
botao7.grid(column=0,row=2)

botao8 = Button(janela,text="150",width = 10,height=2,command=func8)
botao8.grid(column=1,row=2)

botao8 = Button(janela,text="300",width = 10,height=2,command=func9)
botao8.grid(column=2,row=2)


janela.mainloop()