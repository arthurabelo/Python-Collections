import os

import tkinter as tk
from tkinter import ttk
from tkinter import Canvas

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from Grafico import *

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Análise de Containers Collections em Python")
        self.geometry("800x800")
        self.wm_state('zoomed')
        self.create_widgets()
    
    def create_widgets(self):
        self.abas = ttk.Notebook(self)
        
        self.aba1 = ttk.Frame(self.abas)
        self.aba2 = ttk.Frame(self.abas)
        self.aba3 = ttk.Frame(self.abas)
        self.aba4 = ttk.Frame(self.abas)
        
        self.abas.add(self.aba1, text='Questão 1')
        self.abas.add(self.aba2, text='Questão 2')
        self.abas.add(self.aba3, text='Questão 3')
        self.abas.add(self.aba4, text='Questão 4')
        
        self.abas.pack(expand=1, fill="both")
    
        self.button = tk.Button(self.abas, text="Mostrar Resultado", command=self.show_result)
        self.button.pack()
    
    def show_result(self):
        selected = self.abas.select()
        if selected:
            questao = self.abas.index(selected) + 1
            if questao == 1:
                self.display_pdf()
            else:
                self.display_grafico(questao)
        
    def display_pdf(self):
        os.startfile('questoes/Questão 1.pdf')

    def display_grafico(self, questao):
        grafico = Grafico(questao)
        labels, values = grafico.construir_grafico()
        labels = ['A', 'B', 'C']  # Example labels
        values = [1, 2, 3]  # Example values

        fig, ax = plt.subplots()
        if questao == 2:
            if hasattr(self, 'canvas2'):
                self.canvas2.get_tk_widget().pack_forget()
            ax.bar(labels, values)
            ax.set_title('Tempo de Inserção por Container')
            self.canvas2 = FigureCanvasTkAgg(fig, master=self.aba2)
            self.canvas2.draw()
            self.canvas2.get_tk_widget().pack(pady=4)
        elif questao == 3:
            if hasattr(self, 'canvas3'):
                self.canvas3.get_tk_widget().pack_forget()
            ax.bar(labels, values)
            ax.set_title('Tempo de Consulta por Container')
            self.canvas3 = FigureCanvasTkAgg(fig, master=self.aba3)
            self.canvas3.draw()
            self.canvas3.get_tk_widget().pack(pady=4)
        elif questao == 4:
            if hasattr(self, 'canvas4'):
                self.canvas4.get_tk_widget().pack_forget()
            ax.bar(labels, values)
            ax.set_title('Tempo de Exclusão por Container')
            self.canvas4 = FigureCanvasTkAgg(fig, master=self.aba4)
            self.canvas4.draw()
            self.canvas4.get_tk_widget().pack(pady=4)

if __name__ == '__main__':
    app = App()
    app.mainloop()