import os

import tkinter as tk
from tkinter import ttk
from tkinter import Canvas
from tkinter import Frame

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
        button_frame = Frame(self)
        button_frame.pack(anchor="n", pady=3)
    
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
        self.button = tk.Button(button_frame, text="Mostrar Resultado", command=self.show_result)
        self.button.pack(side="left", padx=1)
        self.button_tratar = tk.Button(button_frame, text="Tratar arquivo", command=self.tratar_arquivo)
        self.button_tratar.pack(side="left", padx=1)
    
    def tratar_arquivo(self):
        # Leitura do arquivo
        with open('leipzig100k.txt', 'r') as file:
            text = file.read()

        # Dividir o texto com base em múltiplos delimitadores
        import re
        palavras = re.split(r'[ \t\n\d\W]+', text)
        duvida = True # CASO NÃO SEJA PARA TRATAR AS REPETIÇÕES NEM TRANSFORMAR AS LETRAS PARA MAIÚSCULAS COLOQUE False
        if duvida:
            for i in range(len(palavras)):
                palavras[i] = palavras[i].lower() # Transforma cada letra em minúscula
                if palavras[i] == '':
                    palavras.pop(i) # Remove palavra vazia
                    i -= 1
            palavras = list(set(palavras)) # Removendo repetições
        # Escrever arquivo com as novas palavras separadas por vírgulas
        with open('leipzig100k_tratado.txt', 'w') as file:
            file.write(','.join(palavras))
    
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

        fig, ax = plt.subplots()
        if questao == 2:
            if hasattr(self, 'canvas2'):
                self.canvas2.get_tk_widget().pack_forget()
            ax.bar(labels, values)
            ax.set_title('Tempo de Inserção por Container')
            plt.xlabel('Containers')
            plt.ylabel('Tempo de Inserção (s)')
            self.canvas2 = FigureCanvasTkAgg(fig, master=self.aba2)
            self.canvas2.draw()
            self.canvas2.get_tk_widget().pack(pady=4)
        elif questao == 3:
            if hasattr(self, 'canvas3'):
                self.canvas3.get_tk_widget().pack_forget()
            ax.bar(labels, values)
            ax.set_title('Tempo de Consulta por Container')
            plt.xlabel('Containers')
            plt.ylabel('Tempo de Consulta (s)')
            self.canvas3 = FigureCanvasTkAgg(fig, master=self.aba3)
            self.canvas3.draw()
            self.canvas3.get_tk_widget().pack(pady=4)
        elif questao == 4:
            if hasattr(self, 'canvas4'):
                self.canvas4.get_tk_widget().pack_forget()
            ax.bar(labels, values)
            ax.set_title('Tempo de Exclusão por Container')
            plt.xlabel('Containers')
            plt.ylabel('Tempo de Exclusão (s)')
            self.canvas4 = FigureCanvasTkAgg(fig, master=self.aba4)
            self.canvas4.draw()
            self.canvas4.get_tk_widget().pack(pady=4)

if __name__ == '__main__':
    app = App()
    app.mainloop()