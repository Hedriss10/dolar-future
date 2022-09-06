# criando a aplicação gráfica 
import tkinter as tk 
import time 
from datetime import date
import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from indicador import soupText, linesPrice, priceClose, priceOpen, priceVarietion



root = Tk()
root.title("Indicador-Dolar-future")
root.geometry('600x450')
label = Label(root, text='Indicador dolar', font=('arial', 30), background="#8E8787")
label.grid(row=0, column=0, columnspan=8, rowspan=2, padx=50, pady=40)



# startIndicador = Label(root, text='Inciar o indicador', font=('Arial ', 15))
# startIndicador.grid(row=3, column=0, columnspan=1, padx=50, pady=5)

# compraBox = Entry(root, width=55, bd=1, font=('Arial', 15))
# compraBox.grid(row=6, column=1, columnspan=4, padx=5, pady=0)
my_tree =  ttk.Treeview(root)
# windowsJanela = Tk()
# windowsJanela.geometry("330x120")
# windowsJanela.title("Análise feita")
# infowindows = Label(windowsJanela, text="Analise feita !COMPRA!", font=("Arial ", 10))
# infowindows.grid(row=0 ,column=3,columnspan=8, rowspan=2, padx=50,pady=40)






def refrestable():
    my_tree.tag_configure('orow', background="#EEEEE", font=("Arial", 20))
    my_tree.grid(row=8, column=0, columnspan=5, rowspan=11, padx=10, pady=20)


def refresh():
    pass 

def iniciar():
    while True:
        time.sleep(2)    
        volume = linesPrice
        abertura = priceOpen
        fechamento = priceClose
        variacao = priceVarietion

        estrategy_abertura = [i.text for i in abertura] # "1.84%"
        estrategy_volume = [i.text for i in volume] # 300.035
        estrategy_fechamento = [i.text for i in fechamento] # 5.012,00
        estrategy_variacao = [i.text for i in variacao] # 92,50

        smak = []
        
        
        for x in estrategy_abertura, estrategy_volume, estrategy_fechamento, estrategy_variacao:
            smak.append(x)
            print(smak)
            
        








def desligar():
    pass


    


startButton = Button(
    root, text="Ligar o indicador", padx=50, pady=5, width=10,
    bd=1, font=('Arial', 10), bg="#03F62B", command=iniciar, 
)
startButton.grid(row=7, column=0, columnspan=1, padx=50, pady=5)

statbuttonOff = Button(
    root, text="Desligar o indicador", padx=50, pady=5, width=10,
    bd=1, font=("Arial", 10), bg="#F00B0B", command=root.destroy
)
statbuttonOff.grid(row=8, column=0, columnspan=1, padx=50, pady=5)







root.mainloop()