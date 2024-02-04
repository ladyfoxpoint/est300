from .logger import Logger

class Estat:
    def __init__(self, datasetobj=[], mapobj=[]):
        self.logger = Logger('est', '#FFB344')
        self.logger.log('info', 'Modulo estatistica inicializado!')

        self.dataset = datasetobj
        self.map = mapobj
    
    def search_map(self, column, query, query2=None):
        try:
            if  query2:
                return self.map[column][query][query2]
            else:
                return self.map[column][query]
        except:
            self.logger.log('error', f'Erro ao buscar [{column}][{query}] no map!')
            return False
    
    def reverse_search_map(self, column, query, query2=None):
        try:
            if  query2:
                for key, value in self.map[column][query].items():
                    if value == query2:
                        return key
            else:
                for key, value in self.map[column].items():
                    if value == query:
                        return key
        except:
            self.logger.log('error', f'Erro ao buscar [{column}][{query}] no map!')
            return False


    def set_dataset(self, datasetobj, mapobj=[]):
        if not mapobj:
            self.logger.log('warning', 'Nenhum map setado!')
        else:
            try:
                self.map = mapobj
                self.logger.log('info', 'Novo map setado!')
            except:
                self.logger.log('error', 'Erro ao setar novo map!')
        
        try:
            self.dataset = datasetobj
            self.logger.log('info', 'Novo dataset setado!')
            return True
        
        except:
            self.logger.log('error', 'Erro ao setar novo dataset!')
            return False
    

    def total_of(self, column, value):
        total = 0
        for row in self.dataset:
            if row[column] == value:
                total += 1
        
        return total
    

    def total_of_each(self, column):
        totals = {}
        for row in self.dataset:
            if row[column] in totals:
                totals[row[column]] += 1
            else:
                totals[row[column]] = 1
        
        for key in self.map[column]:
            if key not in totals:
                totals[key] = 0
        
        sorted_totals = {}
        if self.map and column in self.map:
            for key in self.map[column]:
                if key in totals:
                    sorted_totals[key] = totals[key]
        
        return sorted_totals


    def all_of(self, column, value):
        result = []
        for row in self.dataset:
            if row[column] == value:
                result.append(row)
        
        return result