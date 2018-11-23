import random

exes = [40,60,70,70,60,40,10,10]
whys = [10,10,30,50,70,70,50,30]

class Citizen:
    def __init__(self,x,y):
        self.x = x else 0
        self.y = y else 0

class Population:
    def __init__(self,length,sampleCitizen)
        self.folks = [for sampleCitizen in len(length)]

    def create_population(self,folks):
        for i in len(self.folks):
            self.folks[i] = folks[i]

def evaluate(chromosome):
    pass
    
def selection(chromosome):
    pass

def crossover(chromosome):
    pass

def mutation(chromosome):
    pass

def main():
    
    zaandam = Population(8,Citizen(2,2))
    pseudoZaandam = zaandam.folks
    for i in len(pseudozaandam):
        pseudoZaandam[i] = Citizen(exes[i],whys[i])
    zaandam.create_population(pseudoZaandam)
    evolve()
