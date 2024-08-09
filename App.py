import os
import tkinter as tk
from tkinter import ttk
from tkinter import Canvas
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkPDFViewer import tkPDFViewer as pdf

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Análise de Containers em Python")
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
            question = self.abas.index(selected) + 1
            if question == 1:
                self.display_pdf()
            else:
                self.display_grafico(question)
            self.create_canvas(selected)
    
    def create_canvas(self, tab):
        canvas = Canvas(tab, width=800, height=400, background="grey")
        canvas.pack()
        
    def display_pdf(self):
        os.startfile('Questão 1.pdf')

    def display_grafico(self, question):
        labels = ['A', 'B', 'C']  # Example labels
        values = [1, 2, 3]  # Example values

        fig, ax = plt.subplots()
        if question == 2:
            ax.bar(labels, values)
            ax.set_title('Tempo de Inserção por Container')
        elif question == 3:
            ax.bar(labels, values)
            ax.set_title('Tempo de Consulta por Container')
        elif question == 4:
            ax.bar(labels, values)
            ax.set_title('Tempo de Exclusão por Container')

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack()

if __name__ == '__main__':
    app = App()
    app.mainloop()