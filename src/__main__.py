import csv
import json

from .utils.estat import Estat
from .utils.logger import Logger
from .utils.plot import Plot

class Aluno:
    def __init__(self, idade, genero, periodo, dieta, frequenta):
        self.idade = idade
        self.genero = genero
        self.periodo = periodo
        self.dieta = dieta
        self.frequenta = frequenta
    
    def setup_frequenta(self, frequencia, vegetariano, qualidade, preco):
        self.frequencia = frequencia
        self.vegetariano = vegetariano
        self.qualidade = qualidade
        self.preco = preco

    def setup_nao_frequenta(self, porque, como):
        self.porque = porque
        self.como = como


def readData(src):
    logger.log('info', f'Lendo banco de dados (csv) @ <{src}>...')
    with open(f'{src}', 'r', encoding='utf-8') as rawcsv:
        reader = csv.DictReader(rawcsv)
        raw = []
        for row in reader:
            raw.append(row)
    return raw

def parseData(estat, logger, data):
    estat = estat
    parsed = []
    for row in data:
        aluno = Aluno(
            estat.search_map('idade', row[' Qual a sua idade?']), 
            estat.search_map('genero', row['Qual seu gênero?']), 
            estat.search_map('periodo', row['Qual período você está cursando?']), 
            estat.search_map('dieta', row['Qual tipo de refeição você consome no seu dia a dia?']), 
            estat.search_map('frequenta', row['Você frequenta o Restaurante Universitário? '])
        )
        
        if aluno.frequenta == 'sim':
            aluno.setup_frequenta({
                                    "almoco": estat.search_map('frequencia', 'almoco', row['Quantas  vezes por semana você almoça no RU?']),
                                    "janta": estat.search_map('frequencia', 'janta', row['Quantas  vezes por semana você janta no RU?'])
                                   },
                                    estat.search_map('vegetariano', row['Você consome as refeições vegetarianas no Restaurante Universitário?']), 
                                    estat.search_map('qualidade', row['Como você avalia a qualidade das refeições oferecidas no Restaurante Universitário?']), 
                                    estat.search_map('preco', row['Como você avalia o preço das refeições no Restaurante Universitário?']))
        
        if aluno.frequenta == 'nao':
            aluno.setup_nao_frequenta(estat.search_map('porque', row['Por que você não frequenta Restaurante Universitário?']), 
                                      estat.search_map('como', row['Como você faz suas refeições - almoço e jantar - durante os dias úteis (de segunda à sexta-feira)?']))
        
        logger.log('debug', f'Novo Aluno! <{aluno.__dict__}>')
        parsed.append(aluno)
    
    return parsed


if __name__ == '__main__':
    logger = Logger('main', '#FFB344', 2)
    
    with open('./data/maps.json', 'r', encoding='utf-8') as mapfile:
        mapobj = json.load(mapfile)
    estat = Estat(mapobj=mapobj)
    
    logger.log('info', 'Iniciando aplicação...')

    raw_data = readData('./data/raw.csv')
    logger.log('info', 'Dados lidos com sucesso')

    parsed_data = parseData(estat, logger, raw_data)
    logger.log('info', 'Dados organizados com sucesso!')

    logger.log('info', 'Plotando...')
    # Now onto plotting data...
    plot = Plot(estat)

    # Genero
    generos = {}
    for x in estat.map['genero'].values():
        generos[x] = 0
    
    for aluno in parsed_data:
        generos[str(aluno.genero)] += 1
    
    plot.pie(generos, 'GRÁFICO 1 – GRÁFICO DE PIZZA PARA A VARIÁVEL GÊNERO', 'genero_pizza')

    # Idades
    idades = {}
    for x in estat.map['idade'].values():
        idades[x] = 0
    
    for aluno in parsed_data:
        idades[str(aluno.idade)] += 1
    
    plot.hist(idades, 'GRÁFICO 2 – HISTOGRAMA PARA A VARIÁVEL IDADE', 'Qnt Alunos', 2.0, 'idade_hist')

    # Periodo
    periodos = {}
    for x in estat.map['periodo'].values():
        periodos[x] = 0
    
    for aluno in parsed_data:
        periodos[str(aluno.periodo)] += 1
    
    plot.bar(periodos, 'GRÁFICO 3 – GRÁFICO PARA A VARIÁVEL PERÍODO DO CURSO DE ESTATÍSTICA', 'Qnt Alunos', 2.0, 'periodo_bar')


    # Dieta
    dietas = {}
    for x in estat.map['dieta'].values():
        dietas[x] = 0
    
    for aluno in parsed_data:
        dietas[str(aluno.dieta)] += 1
    
    plot.bar(dietas, 'GRÁFICO 4 – GRÁFICO PARA A VARIÁVEL DIETA', 'Qnt Alunos', 5.0, 'dieta_bar')


    # Frequenta
    frequenta = {}
    for x in estat.map['frequenta'].values():
        frequenta[x] = 0
    
    for aluno in parsed_data:
        frequenta[str(aluno.frequenta)] += 1
    
    plot.pie(frequenta, 'GRÁFICO 5 – GRÁFICO PARA A VARIÁVEL  FREQUÊNCIA DO RESTAURANTE UNIVERSITÁRIO', 'freq_pie')


    # Refeicoes Almoco
    almoco = {}
    for x in estat.map['frequencia']['almoco'].values():
        almoco[str(x)] = 0
    
    for aluno in parsed_data:
        if aluno.frequenta == 'sim':
            almoco[str(aluno.frequencia['almoco'])] += 1
    
    plot.column(almoco, 'GRÁFICO 6 – GRÁFICO PARA A VARIÁVEL FREQUÊNCIA DAS REFEIÇÕES NO ALMOÇO', 'Qnt Alunos', 1.0, 'almoco_col')
    

    # Refeicoes Janta
    janta = {}
    for x in estat.map['frequencia']['janta'].values():
        janta[str(x)] = 0
    
    for aluno in parsed_data:
        if aluno.frequenta == 'sim':
            janta[str(aluno.frequencia['janta'])] += 1
    
    plot.column(janta, 'GRÁFICO 7 – GRÁFICO PARA A VARIÁVEL FREQUÊNCIA DAS REFEIÇÕES NA JANTA', 'Qnt Alunos', 1.0, 'janta_col')


    # Vegetariano
    vegetariano = {}
    for x in estat.map['vegetariano'].values():
        vegetariano[x] = 0
    
    for aluno in parsed_data:
        if aluno.frequenta == 'sim':
            vegetariano[str(aluno.vegetariano)] += 1
    
    plot.bar(vegetariano, 'GRÁFICO 8 – GRÁFICO PARA A VARIÁVEL VEGETARIANO', 'Qnt Alunos', 1.0, 'vegetariano_bar')


    # Qualidade
    qualidade = {}
    for x in estat.map['qualidade'].values():
        qualidade[x] = 0

    for aluno in parsed_data:
        if aluno.frequenta == 'sim':
            qualidade[str(aluno.qualidade)] += 1
    
    plot.bar(qualidade, 'GRÁFICO 9 – GRÁFICO PARA A VARIÁVEL QUALIDADE', 'Qnt Alunos', 1.0, 'qualidade_bar')


    # Preco
    preco = {}
    for x in estat.map['preco'].values():
        preco[x] = 0
    
    for aluno in parsed_data:
        if aluno.frequenta == 'sim':
            preco[str(aluno.preco)] += 1
    
    plot.pie(preco, 'GRÁFICO 10 – GRÁFICO PARA A VARIÁVEL PREÇO', 'preco_pie')


    # Como
    como = {}
    for x in estat.map['como'].values():
        como[x] = 0
    
    for aluno in parsed_data:
        if aluno.frequenta == 'nao':
            como[str(aluno.como)] += 1
    
    plot.bar(como, 'GRÁFICO 11 – GRÁFICO PARA A VARIÁVEL COMO', 'Qnt Alunos', 1.0, 'como_bar')


    # Porque
    porque = {}
    for x in estat.map['porque'].values():
        porque[x] = 0

    for aluno in parsed_data:
        if aluno.frequenta == 'nao':
            porque[str(aluno.porque)] += 1
    
    plot.bar(porque, 'GRÁFICO 12 – GRÁFICO PARA A VARIÁVEL PORQUE', 'Qnt Alunos', 1.0, 'porque_bar')




