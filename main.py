import random
def generate_population(size):
    return [random.uniform(-10,10) for i in range(size)]
def evolve(population:list, size, mutation_rate):
    # select parents via tournament selection from the population and replace old population with new generation
    new_population = []
    for i in range (size):
        parent_x = tournament(population)
        # remove first parent from population so they cannot be also the second parent
        population.pop(population.index(parent_x))
        parent_y = tournament(population)
        # add first parent back to the population pool
        # chances of this happening seem very small but i want to be sure
        population.append(parent_x)
        # create the child
        child = (parent_x + parent_y) / 2
        # randomly decide if child should be mutated, lifting mutation rate increases odds
        if random.random() < mutation_rate:
            # i found that range of -0.001 and 0.001 gave the most pleasant answers with mutation
            child += random.uniform(-0.001,0.001)
        new_population.append(child)
    return new_population
def tournament(pool:list):
    # select a random sample of 5 from the pool and return the lowest of them
    tournament_participants = random.sample(pool, 5)
    return min(tournament_participants)

def sga(pop_size, num_generations, mutation_rate = 0.1):
    population = generate_population(pop_size)
    original_population = population.copy()
    for i in range(num_generations):
        population = evolve(population, pop_size, mutation_rate)
    print("lowest value in population was: " + str(min(original_population)))
    print("lowest value in genetic algorithm is: " + str(min(population)))
    print("difference is: "+ str(abs(min(original_population) - min(population))))
    

def main():
    population_size = 100
    amount_of_generations = 1000
    print("Starting the genetic algorithm with population size of: "+str(population_size)+" and for "+str(amount_of_generations)+" generations")

    sga(population_size, amount_of_generations)

main()