def fitness_func(population, target):
    fitness_scores = []
    for chromosome in population:
        fitness_scores.append(fitness_score(chromosome, target))
    return fitness_scores