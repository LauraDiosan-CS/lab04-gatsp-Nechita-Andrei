import random
from v2 import Project_manager

#am urmarit un tutorial de pe youtube pentru a intelege mai bine problema: https://youtu.be/zumC_C0C25c

def problemaLab4(gen):
    project=Project_manager()

    target=project.get_target()[1] # iau ca si target solutia de la problema 2
    marime_populatie =int(project.get_length())# ca si marimea populatiei iau numarul de orase data la problema 2 in fisier
    print("salut")
    print(marime_populatie)
    print(target)
    elite = 1
    tounament_size = 4
    mutation_rate = 0.25


    class Chromosome:
        def __init__(self):
            self._gena = []
            self._fintness = 0
            i = 0
            while i < target.__len__():
                if self._gena.__len__() == 0:
                    self._gena.append(0)
                else:
                    element = random.randint(1, marime_populatie - 1)
                    if element not in self._gena:
                        self._gena.append(element)
                    else:
                        while element in self._gena:
                            element = random.randint(1, marime_populatie - 1)
                        self._gena.append(element)
                i = i + 1

        def get_gena(self):
            return self._gena

        def get_fitness(self):
            self._fintness = 0
            for i in range(marime_populatie):
                if self._gena[i] == target[i]:
                    self._fintness += 1
            return self._fintness

        def __str__(self):
            return self._gena.__str__()

    class Populatie:
        def __init__(self, size):
            self._chromosomes = []
            i = 0
            while i < size:
                self._chromosomes.append(Chromosome())
                i += 1

        def get_chromosomes(self):
            return self._chromosomes

    class GeneticAlgorithm:
        @staticmethod
        def evolve(populatie):
            return GeneticAlgorithm._mutate_population(GeneticAlgorithm._crossover_population(populatie))

        @staticmethod
        def _crossover_population(populatie):
            crossover_pop = Populatie(0)
            for i in range(elite):
                crossover_pop.get_chromosomes().append(populatie.get_chromosomes()[i])
            i = 1
            while i < marime_populatie:
                chromosome1 = GeneticAlgorithm._select_tournament_population(populatie).get_chromosomes()[0]
                chromosome2 = GeneticAlgorithm._select_tournament_population(populatie).get_chromosomes()[0]
                crossover_pop.get_chromosomes().append(
                    GeneticAlgorithm._crossover_chromosomes(chromosome1, chromosome2))
                i += 1
            return crossover_pop

        @staticmethod
        def _mutate_population(populatie):
            for i in range(elite, marime_populatie):
                GeneticAlgorithm._mutate_chromosome(populatie.get_chromosomes()[i])
            return populatie

        @staticmethod
        def _crossover_chromosomes(chromosome1, chromosome2):
            crossover_chrom = Chromosome()
            for i in range(target.__len__()):
                if random.random() >= 0.5:
                    crossover_chrom.get_gena()[i] = chromosome1.get_gena()[i]
                else:
                    crossover_chrom.get_gena()[i] = chromosome2.get_gena()[i]
            return crossover_chrom

        @staticmethod
        def _mutate_chromosome(chromosome):
            for i in range(target.__len__()):
                if random.random() < mutation_rate:
                    element1 = random.randint(1, marime_populatie - 1)
                    element2 = chromosome.get_gena()[i]
                    for j in range(1, target.__len__() - 1):
                        if chromosome.get_gena()[j] == element1:
                            chromosome.get_gena()[j] = element2
                    chromosome.get_gena()[i] = element1;

        @staticmethod
        def _select_tournament_population(populatie):
            tournament_populatie = Populatie(0)
            i = 0
            while i < tounament_size:
                tournament_populatie.get_chromosomes().append(
                    populatie.get_chromosomes()[random.randrange(0, marime_populatie)])
                i += 1
            tournament_populatie.get_chromosomes().sort(key=lambda x: x.get_fitness(), reverse=True)
            return tournament_populatie

    def _print_populatie(pop, generatie):
        print("\n---------------------")
        print("generatia #", generatie, "| cel mai bun:", pop.get_chromosomes()[0].get_fitness())
        print("-----------------------")
        i = 0
        for x in pop.get_chromosomes():
            print("Chromosome #", i, ":", x, "| fitness: ", x.get_fitness())
            i += 1

    populatie = Populatie(marime_populatie)
    populatie.get_chromosomes().sort(key=lambda x: x.get_fitness(), reverse=True)
    _print_populatie(populatie, 0)
    generatie = 1
    while populatie.get_chromosomes()[0].get_fitness() < target.__len__() and generatie < gen:
        populatie = GeneticAlgorithm.evolve(populatie)
        populatie.get_chromosomes().sort(key=lambda x: x.get_fitness(), reverse=True)
        _print_populatie(populatie, generatie)
        generatie += 1