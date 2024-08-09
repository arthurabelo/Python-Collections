import tkinter as tk
from tkinter import Canvas
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Análise de Containers em Python")
        self.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Selecione uma questão:")
        self.label.pack()

        self.listbox = tk.Listbox(self)
        self.listbox.insert(1, "Questão 1")
        self.listbox.insert(2, "Questão 2")
        self.listbox.insert(3, "Questão 3")
        self.listbox.insert(4, "Questão 4")
        self.listbox.pack()

        self.canvas = Canvas(self, width=800, height=400)
        self.canvas.pack()

        self.button = tk.Button(self, text="Mostrar Resultado", command=self.show_result)
        self.button.pack()

    def show_result(self):
        selected = self.listbox.curselection()
        if selected:
            question = selected[0] + 1
            if question == 1:
                self.display_pdf()
            else:
                self.display_chart(question)

    def display_pdf(self):
        pass  # Implementação para exibir PDF no canvas

    def display_chart(self, question):
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