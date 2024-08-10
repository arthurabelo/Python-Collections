import time

from collections import defaultdict, Counter, OrderedDict, deque, ChainMap, namedtuple, UserDict, UserList, UserString

class Containers:
    def __init__(self):
        self.dict_container = dict()
        self.list_container = list()
        self.set_container = set()
        self.tuple_container = tuple()
        #self.namedtuple_container = namedtuple('Exemplo', ['exemplo'])
        self.defaultdict_container = defaultdict()
        self.counter_container = Counter()
        self.ordereddict_container = OrderedDict()
        self.deque_container = deque()
        self.chainmap_container = ChainMap()
        self.userdict_container = UserDict()
        self.userlist_container = UserList()
        self.userstring_container = UserString('')
    
    # QUESTÃO 1 - INSERÇÃO
    def insert_dict(self, palavras):
        for palavra in palavras:
            self.dict_container[palavra] = None
        return self.dict_container

    def insert_list(self, palavras):
        for palavra in palavras:
            self.list_container.append(palavra)
        return self.list_container

    def insert_set(self, palavras):
        for palavra in palavras:
            self.set_container.add(palavra)
        return self.set_container

    def insert_tuple(self, palavras):
        self.tuple_container = tuple(palavras)
        return self.tuple_container

    def insert_namedtuple(self, palavras):
        return None # ERRO
        valid_palavras = [palavra for palavra in palavras if palavra.isidentifier()]
        if valid_palavras:
            NamedTupleClass = namedtuple('NamedTupleClass', valid_palavras)
            self.namedtuple_container = NamedTupleClass(*valid_palavras)
        return self.namedtuple_container
    
    def insert_defaultdict(self, palavras):
        for i in range(len(palavras)):
            self.defaultdict_container[palavras[i]] = i
        return self.defaultdict_container
        
    def insert_counter(self, palavras):
        self.counter_container.update(palavras)
        return self.counter_container
        
    def insert_ordereddict(self, palavras):
        for i in range(len(palavras)):
            self.ordereddict_container[palavras[i]] = i
        return self.ordereddict_container

    def insert_deque(self, palavras):
        self.deque_container.extend(palavras) # Insere por iterable
        return self.deque_container
        
    def insert_chainmap(self, palavras):
        new_map = {palavra: palavra for palavra in palavras}
        self.chainmap_container = self.chainmap_container.new_child(new_map)
        return self.chainmap_container
        
    def insert_userdict(self, palavras):
        for i in range(len(palavras)):
            self.userdict_container[palavras[i]] = i
        return self.userdict_container
        
    def insert_userlist(self, palavras):
        self.userlist_container.extend(palavras)
        return self.userlist_container
        
    def insert_userstring(self, palavras):
        self.userstring_container = UserString(",".join(palavras))
        return self.userstring_container
        
def medir_tempo(func, palavras):

    start_time = time.time()
    func(palavras)

    end_time = time.time()

    return end_time - start_time


if __name__ == '__main__':
    # TESTE

    # Leitura do arquivo

    with open('leipzig100k.txt', 'r') as file:

        text = file.read()


    palavras = text.split()


    # Medir o tempo de inserção para cada container

    containers = Containers()

    methods = [

        containers.insert_dict, containers.insert_list, containers.insert_set, containers.insert_tuple,

        containers.insert_namedtuple, containers.insert_defaultdict, containers.insert_counter,

        containers.insert_ordereddict, containers.insert_deque, containers.insert_chainmap,

        containers.insert_userdict, containers.insert_userlist, containers.insert_userstring

    ]


    for method in methods:

        time_taken = medir_tempo(method, palavras)

        print(f"{method.__name__}: {time_taken:.6f} seconds")