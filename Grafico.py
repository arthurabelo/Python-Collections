from Containers import *
class Grafico:
    def __init__(self, questao):
        self.questao = questao

    def construir_grafico(self):
        # Leitura do arquivo
        with open('leipzig100k_tratado.txt', 'r') as file:
            text = file.read()

        palavras = text.strip().split(',')
 
        # Medir o tempo de inserção para cada container
        containers = Containers()
        
        metodos = [containers.insert_dict, containers.insert_list, containers.insert_set, 
                   containers.insert_tuple,containers.insert_namedtuple, containers.insert_defaultdict, 
                   containers.insert_counter,containers.insert_ordereddict, containers.insert_deque, 
                   containers.insert_chainmap,containers.insert_userdict, containers.insert_userlist, 
                   containers.insert_userstring]
        
        values = []
        for metodo in metodos:
            tempo_decorrido = medir_tempo(metodo, palavras)
            values.append(tempo_decorrido)
            
        labels = ['dict','list','set','tuple','namedtuple','defaultdict','counter','ordereddict','deque','chainmap','userdict','userlist','userstring']
            
        return labels, values
    
if __name__ == '__main__':
    # TESTE
    grafico = Grafico(2)
    grafico.construir_grafico()