import math
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plot

class Life(object):
    """个体类"""
 
    def __init__(self, Gene=None, Score=0):
        self._gene = Gene
        self.score = Score

    def getgene(self):
        return self._gene

    def getscore(self):
        return self.score

class GeneticAlgorithm(object):
    
    def __init__(self, CrossRate, MutationRate, Number, LenChromosome, SelectingFuction):
        self._CrossRate = CrossRate #交叉概率
        self._MutationRate = MutationRate #突变概率
        self._Number = Number #所有个体数量
        self._LenChromosome = LenChromosome #染色体长度，基因数量
        self._selectingfuction = SelectingFuction
        self._lives = []
        self.generation = 1
        self.initFirstGeneration()

    def initFirstGeneration(self):
        """初始化第一代"""
        self._lives = []
        for i in range(self._Number):
            genes = [x for x in range(self._LenChromosome)]
            random.shuffle(genes)
            life = Life(genes)
            self._lives.append(life)
            for life in self._lives:
                life.score = self._selectingfuction(life)
    
    def child_crossover(self):
        """交叉"""
        index1 = random.randint(0, self._Number - 1)
        index2 = random.randint(0, self._Number - 1)
        p1 = self._lives[index1].getgene()
        p2 = self._lives[index2].getgene()
        index1 = random.randint(0, self._LenChromosome - 1)
        index2 = random.randint(index1, self._LenChromosome - 1)
        newchromosome1 = p1 + p2[index1:index2]
        newchromosome2 = p2 + p1[index1:index2]
        for i in p2[index1:index2]:
            newchromosome1.remove(i)
        for i in p1[index1:index2]:
            newchromosome2.remove(i)
        life1, life2 = Life(newchromosome1), Life(newchromosome2)
        return  life1, life2
        
    def child_mutation(self):
        """变异"""
        newgenes = []
        index = [x for x in range(self._Number)]
        temp = random.sample(index, int(self._MutationRate * self._Number))
        for i in temp:
            g = self._lives[i].getgene()
            random.shuffle(g)
            life = Life(g)
            newgenes.append(life)
        return newgenes


    def intothenextgeneration(self):
        """产生下一代"""
        newfromcross1, newfromcross2= self.child_crossover()
        newfrommutation = self.child_mutation()
        newfrommutation.append(newfromcross1)
        newfrommutation.append(newfromcross2)
        for life in newfrommutation:
            life.score = self._selectingfuction(life)
        self._lives += newfrommutation
        self._lives.sort(key=Life.getscore)
        # self._lives = self._lives[0:self._Number]
        del(self._lives[self._Number + 1:])
        return self._lives[0]

    

class WorldCitiesTSP(object):
    def __init__(self, Cycles = 10):
        self.addinCities()
        self._cycles = Cycles
        self._GeneticAlgorithm = GeneticAlgorithm(CrossRate=0.7,
                                                  MutationRate=0.5,
                                                  Number=self._cycles,
                                                  LenChromosome=len(self._cities),
                                                  SelectingFuction=self.selectingfuntion()
                                                )

    def addinCities(self):
        data = pd.read_csv('./worldcities.csv',encoding = 'UTF-8')
        self._cities = data.iloc[0:10, 2:4].values

    def distance(self, order):
        distance = 0.0
        for i in range(-1, len(self._cities) - 1):
            index1, index2 = order[i], order[i + 1]
            city1, city2 = self._cities[index1], self._cities[index2]
            distance += math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)
        return distance

    def selectingfuntion(self):
        return lambda life: self.distance(life.getgene())
    
    def runGA(self, n = 0):
        while n > 0: 
            ga = self._GeneticAlgorithm
            examplar = ga.intothenextgeneration()
            print(examplar.getscore())
            print(examplar.getgene())
            n -= 1

if __name__ == '__main__':
    tsp = WorldCitiesTSP()
    tsp.runGA(1000)

