from collections import deque
import heapq

class Grafo:
    def __init__(self):
        self.grafo = {}
        # Lista de arestas válidas (tuplas) com base nos relacionamentos fornecidos
        self.arestas_validas = set([
            ('frankfurt', 'wurzburg'),
            ('wurzburg', 'frankfurt'),
            ('frankfurt', 'mannheim'),
            ('mannheim', 'frankfurt'),
            ('mannheim', 'karlsruhe'),
            ('karlsruhe', 'mannheim'),
            ('karlsruhe', 'stuttgart'),
            ('stuttgart', 'karlsruhe'),
            ('karlsruhe', 'basel'),
            ('basel', 'karlsruhe'),
            ('mannheim', 'nurnberg'),
            ('nurnberg', 'mannheim'),
            ('nurnberg', 'bayreuth'),
            ('bayreuth', 'nurnberg'),
            ('nurnberg', 'passau'),
            ('passau', 'nurnberg'),
            ('wurzburg', 'nurnberg'),
            ('nurnberg', 'wurzburg'),
            ('wurzburg', 'stuttgart'),
            ('stuttgart', 'wurzburg'),
            ('wurzburg', 'ulm'),
            ('ulm', 'wurzburg'),
            ('stuttgart', 'ulm'),
            ('ulm', 'stuttgart'),
            ('basel', 'bern'),
            ('bern', 'basel'),
            ('basel', 'zurich'),
            ('zurich', 'basel'),
            ('bern', 'zurich'),
            ('zurich', 'bern'),
            ('zurich', 'memmingen'),
            ('memmingen', 'zurich'),
            ('ulm', 'memmingen'),
            ('memmingen', 'ulm'),
            ('munchen', 'memmingen'),
            ('memmingen', 'munchen'),
            ('ulm', 'nurnberg'),
            ('nurnberg', 'ulm'),
            ('ulm', 'munchen'),
            ('munchen', 'ulm'),
            ('nurnberg', 'munchen'),
            ('munchen', 'nurnberg'),
            ('passau', 'linz'),
            ('linz', 'passau'),
            ('passau', 'munchen'),
            ('munchen', 'passau'),
            ('rosenheim', 'munchen'),
            ('munchen', 'rosenheim'),
            ('linz', 'salzburg'),
            ('salzburg', 'linz'),
            ('rosenheim', 'salzburg'),
            ('salzburg', 'rosenheim'),
            ('rosenheim', 'innsbruck'),
            ('innsbruck', 'rosenheim'),
            ('landeck', 'innsbruck'),
            ('innsbruck', 'landeck')
        ])

    def adicionar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []

    def adicionar_arco(self, vertice_origem, vertice_destino, peso=1):
        if vertice_origem not in self.grafo:
            self.grafo[vertice_origem] = []
        if vertice_destino not in self.grafo:
            self.grafo[vertice_destino] = []

        self.grafo[vertice_origem].append((vertice_destino, peso))
        self.grafo[vertice_destino].append((vertice_origem, peso))

    def busca_em_largura(self, vertice_inicial, destino):
        print("\nBusca em Largura:")
        visitados = set()
        fila = deque([vertice_inicial])
        predecessores = {vertice_inicial: None}

        while fila:
            vertice = fila.popleft()
            if vertice in visitados:
                continue
            visitados.add(vertice)
            print(f"Visitando {vertice}")

            if vertice == destino:
                caminho = []
                while vertice is not None:
                    caminho.append(vertice)
                    vertice = predecessores[vertice]
                caminho.reverse()
                print(f"\nCaminho mais curto encontrado: {' -> '.join(caminho)}")
                return

            for vizinho, _ in self.grafo.get(vertice, []):
                if vizinho not in visitados and (vertice, vizinho) in self.arestas_validas:
                    fila.append(vizinho)
                    if vizinho not in predecessores:
                        predecessores[vizinho] = vertice

        print("Não existe caminho.")

    def busca_em_profundidade(self, vertice_inicial, destino, visitados=None, predecessores=None):
        if visitados is None:
            print("\nBusca em Profundidade:")
            visitados = set()
            predecessores = {}

        visitados.add(vertice_inicial)
        print(f"Visitando {vertice_inicial}")

        if vertice_inicial == destino:
            caminho = []
            while vertice_inicial is not None:
                caminho.append(vertice_inicial)
                vertice_inicial = predecessores.get(vertice_inicial)
            caminho.reverse()
            print(f"\nCaminho encontrado: {' -> '.join(caminho)}")
            return

        for vizinho, _ in self.grafo.get(vertice_inicial, []):
            if vizinho not in visitados and (vertice_inicial, vizinho) in self.arestas_validas:
                predecessores[vizinho] = vertice_inicial
                self.busca_em_profundidade(vizinho, destino, visitados, predecessores)
                if destino in visitados:
                    return

    def busca_uniforme(self, vertice_inicial, destino):
        print("\nBusca de Custo Uniforme:")
        fila_prioridade = [(0, vertice_inicial)]
        distancias = {vertice: float('inf') for vertice in self.grafo}
        distancias[vertice_inicial] = 0
        predecessores = {vertice_inicial: None}

        while fila_prioridade:
            custo_atual, vertice = heapq.heappop(fila_prioridade)

            if custo_atual > distancias[vertice]:
                continue

            print(f"Visitando {vertice} com custo acumulado {custo_atual}")

            if vertice == destino:
                caminho = []
                while vertice is not None:
                    caminho.append(vertice)
                    vertice = predecessores[vertice]
                caminho.reverse()
                print(f"\nCaminho mais curto encontrado: {' -> '.join(caminho)}")
                print(f"Custo total do caminho: {custo_atual}")
                return

            for vizinho, peso in self.grafo.get(vertice, []):
                if (vertice, vizinho) in self.arestas_validas or (vizinho, vertice) in self.arestas_validas:
                    novo_custo = custo_atual + peso
                    if novo_custo < distancias[vizinho]:
                        distancias[vizinho] = novo_custo
                        predecessores[vizinho] = vertice
                        heapq.heappush(fila_prioridade, (novo_custo, vizinho))

        print("Não existe caminho.")


    def __str__(self):
        return str(self.grafo)

grafo = Grafo()
cidades = [
    'basel',
    'bern',
    'frankfurt',
    'innsbruck',
    'karlsruhe',
    'landeck',
    'linz',
    'mannheim',
    'memmingen',
    'munchen',
    'nurnberg',
    'passau',
    'rosenheim',
    'salzburg',
    'stuttgart',
    'ulm',
    'wurzburg',
    'zurich'
]

for cidade in cidades:
    grafo.adicionar_vertice(cidade)

arestas = [
    ('basel', 'bern', 91),
    ('basel', 'zurich', 85),
    ('bern', 'zurich', 120),
    ('frankfurt', 'mannheim', 85),
    ('frankfurt', 'wurzburg', 111),
    ('karlsruhe', 'basel', 191),
    ('karlsruhe', 'stuttgart', 64),
    ('landeck', 'innsbruck', 73),
    ('linz', 'salzburg', 126),
    ('mannheim', 'karlsruhe', 67),
    ('mannheim', 'nurnberg', 230),
    ('munchen', 'memmingen', 115),
    ('nurnberg', 'bayreuth', 75),
    ('nurnberg', 'munchen', 170),
    ('nurnberg', 'passau', 220),
    ('passau', 'linz', 102),
    ('passau', 'munchen', 189),
    ('rosenheim', 'innsbruck', 93),
    ('rosenheim', 'munchen', 59),
    ('rosenheim', 'salzburg', 81),
    ('stuttgart', 'ulm', 107),
    ('ulm', 'memmingen', 55),
    ('ulm', 'munchen', 123),
    ('ulm', 'nurnberg', 171),
    ('wurzburg', 'nurnberg', 104),
    ('wurzburg', 'stuttgart', 140),
    ('wurzburg', 'ulm', 183),
    ('zurich', 'memmingen', 184)
]

for origem, destino, peso in arestas:
    grafo.adicionar_arco(origem, destino, peso)

grafo.busca_em_largura('zurich', 'bayreuth')
grafo.busca_em_profundidade('zurich', 'bayreuth')
grafo.busca_uniforme('zurich', 'bayreuth')