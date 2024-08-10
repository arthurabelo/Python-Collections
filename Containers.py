import time

from collections import defaultdict, Counter, OrderedDict, deque, ChainMap, namedtuple

from collections import UserDict, UserList, UserString


class Containers:
    

    def insert_dict(self, palavras):

        return {palavra: None for palavra in palavras}


    def insert_list(self, palavras):

        return [palavra for palavra in palavras]


    def insert_set(self, palavras):
        return set(palavras)


    def insert_tuple(self, palavras):
        return tuple(palavras)


    def insert_namedtuple(self, palavras):

        Palavra = namedtuple('Palavra', ['value'])

        return [Palavra(palavra) for palavra in palavras]


    def insert_defaultdict(self, palavras):

        d = defaultdict(int)

        for palavra in palavras:

            d[palavra] += 1
        return d


    def insert_counter(self, palavras):

        return Counter(palavras)


    def insert_ordereddict(self, palavras):

        d = OrderedDict()

        for palavra in palavras:

            d[palavra] = None
        return d


    def insert_deque(self, palavras):

        return deque(palavras)


    def insert_chainmap(self, palavras):

        return ChainMap({palavra: None for palavra in palavras})


    def insert_userdict(self, palavras):

        return UserDict({palavra: None for palavra in palavras})


    def insert_userlist(self, palavras):

        return UserList(palavras)


    def insert_userstring(self, palavras):

        return UserString(''.join(palavras))

def medir_tempo(func, palavras):

    start_time = time.time()
    func(palavras)

    end_time = time.time()

    return end_time - start_time


if __name__ == '__main__':

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