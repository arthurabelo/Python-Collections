from tkinter import *
from tkinter import messagebox

import matplotlib.pyplot as plt

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title('Collections do Python')
        self.geometry('500x500')
        self.wm_state('zoomed')
        
        self.canvas = Canvas(self, width=self.winfo_screenwidth(), height=self.winfo_screenheight() / 0.01, bg="slategrey", relief=RAISED, bd=12)
        
        self.canvas.bind('<MouseWheel>', self.zoom)
        self.canvas.bind("<ButtonPress-1>", self.start_drag)
        self.canvas.bind("<B1-Motion>", self.dragging)
                        
        self.create_widgets()

    def create_widgets(self):
        button_frame = Frame(self)
        button_frame.pack(anchor="n", pady=5)
        
        Button(button_frame, text="Questão 1", command=self.questao1).pack(side="left", padx=1)
        Button(button_frame, text="Questão 2", command=self.questao2).pack(side="left", padx=1)
        Button(button_frame, text="Questão 3", command=self.questao3).pack(side="left", padx=1)
        Button(button_frame, text="Questão 4", command=self.questao4).pack(side="left", padx=1)
                
        self.canvas.pack(pady = 2)
            
    def questao1(self):
        # Implementar visualização de arquivo PDF com explicação no canvas
        try:
            with open('entrada.txt', 'r') as file:
                data = file.read().strip().split(',')
            for name in data:
                if name:
                    ##
                    if self.bst.exists(self.bst.root, name):
                        pass
                        #messagebox.showerror("Erro", f"'{name}' já existe na BST")
                    else:
                        self.bst.insert(name)
            self.reset_zoom()
            # messagebox.showinfo("Sucesso! ", "Dados carregados com sucesso")
        except FileNotFoundError:
            messagebox.showerror("Erro", "Arquivo 'entrada.txt' não encontrado")
            
    def questao2(self):
        try:
            with open('leipzig100k.txt', 'r') as file:
                data = file.read().strip().split(' ').split('   ').split('\n').split(',').split('.')
            for name in data:
                if name:
                    if self.bst.exists(self.bst.root, name):
                        pass
                        #messagebox.showerror("Erro", f"'{name}' já existe na BST")
                    else:
                        self.bst.insert(name)
            self.reset_zoom()
            # messagebox.showinfo("Sucesso! ", "Dados carregados com sucesso")
        except FileNotFoundError:
            messagebox.showerror("Erro", "Arquivo 'entrada.txt' não encontrado")
                
    def exportar_entrada(self):
        try:
            # Obtém os nomes da BST usando level_order
            data = self.bst.levelOrderTraversal()
            data = ','.join(data)
            
            # Escreve os dados no arquivo 'entrada.txt'
            with open('entrada.txt', 'w') as file:
                file.write(data)
            
            # Optionally, show a success message
            messagebox.showinfo("Sucesso! ", "Dados exportados com sucesso")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao exportar dados: {str(e)}")
            
    def zoom(self, event):
        scale = 1.0
        if event.delta > 0 or event.num == 4:
            scale = 1.1
        elif event.delta < 0 or event.num == 5:
            scale = 0.9
        self.canvas.scale("all", event.x, event.y, scale, scale)
        
    def start_drag(self, event):
        self.canvas.scan_mark(event.x, event.y)

    def dragging(self, event):
        self.canvas.scan_dragto(event.x, event.y, gain=1)
    
    def insert_name(self):
        name = self.name_entry.get()
        if name:
            if self.bst.exists(self.bst.root, name):
                messagebox.showerror("Erro", f"'{name}' já existe na BST")
            else:
                self.bst.insert(name)
                self.reset_zoom()
                # messagebox.showinfo("Sucesso! ", f"'{name}' foi inserido na BST")
            self.name_entry.delete(0, 'end')
            
    def delete_name(self):
        if self.bst.root is None:
            messagebox.showerror("Erro", "A árvore está vazia")
            self.canvas.delete("all")
        name = self.name_entry.get()
        if name == '':
                name = self.bst.maxValueNode(self.bst.root)
        if self.bst.exists(self.bst.root, name) == False:
            messagebox.showerror("Erro", f"'{name}' não existe na BST")
        else:
            if self.bst.remove(name):
                # messagebox.showinfo("Sucesso! ", f"'{name}' foi removido da BST")
                self.reset_zoom()
        self.name_entry.delete(0, 'end')
    
    def show_info(self):
        size = self.bst.size(self.bst.root)
        height = self.bst.height(self.bst.root)
        if self.bst.root:
            min_val = self.bst.minValueNode(self.bst.root)
            max_val = self.bst.maxValueNode(self.bst.root)
        else:
            min_val = max_val = "A árvore está vazia"
        leaves = self.bst.leafNodes(self.bst.root, [])
        internal_path_length, calculo_internal_path_length = self.bst.internalPathLength(self.bst.root)
        is_balanced = self.bst.isBalanced(self.bst.root)
        info = f"Tamanho: {size}\nAltura: {height}\nValor Mínimo: {min_val}\nValor Máximo: {max_val}\nNós folhas: {leaves}\n\nEstá balanceada? {is_balanced}"
        messagebox.showinfo("Informação da Árvore", info)
        messagebox.showinfo("Cálculo Comprimento Interno", f'Comprimento Interno: {internal_path_length}\n\n{calculo_internal_path_length}')

    def show_traversals(self):
        inorder = self.bst.inorderTraversal(self.bst.root, [])
        postorder = self.bst.postorderTraversal(self.bst.root, [])
        preorder = self.bst.preorderTraversal(self.bst.root, [])
        levelorder = self.bst.levelOrderTraversal()
        traversals = f"Pré ordem: {', '.join(preorder)}\nEm ordem: {', '.join(inorder)}\nPós ordem: {', '.join(postorder)}\nLevel order: {', '.join(levelorder)}"
        messagebox.showinfo("Travessias na Árvore", traversals)
    
    def reset_zoom(self):
        # Limpa o canvas
        self.canvas.delete("all")
        # Redefine a posição de rolagem do canvas para a posição inicial
        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)
        # Redesenha a árvore a partir da raiz
        self.draw_tree(self.bst.root)
        
    def draw_tree(self, node, x=None, y=30, layer=-1, pos={}):
        if x is None:
            x = self.canvas.winfo_width() / 2
        if node is not None:
            # Calcular a largura do nó com base no tamanho do nome
            node_width = max(50, len(node.val) * 10)
            node_height = 30  # Altura fixa

            # Calcular a posição do nó
            if node not in pos:
                pos[node] = (x, y)

            # Obter a altura total da árvore
            total_height = self.bst.height(self.bst.root)

            # Ajustar espaçamento horizontal e vertical
            horizontal_spacing = 8 * (2 ** (total_height - layer))
            vertical_spacing = 50

            # Desenhar as arestas e calcular as posições dos filhos
            if node.left:
                left_x = x - horizontal_spacing
                left_y = y + vertical_spacing
                self.canvas.create_line(x, y, left_x, left_y)
                self.draw_tree(node.left, left_x, left_y, layer + 1, pos)
            if node.right:
                right_x = x + horizontal_spacing
                right_y = y + vertical_spacing
                self.canvas.create_line(x, y, right_x, right_y)
                self.draw_tree(node.right, right_x, right_y, layer + 1, pos)
                
            # Desenhar o nó
            self.canvas.create_oval(x - node_width / 2, y - node_height / 2, x + node_width / 2, y + node_height / 2, fill="green", outline="blue")
            self.canvas.create_text(x, y, text=node.val)

if __name__ == "__main__":
    app = App()
    app.mainloop()