import numpy as np

def fitness_func(ga_instance, chord_set: np.ndarray, chord_set_index: int):
    fitness = 0
    chord_fitness = np.array([0,0,0,0])
    # I am planning to do (sum of fitness of each chord) * (fitness of chord progression)
    
    # First we evaluate each chord for its consistency
    
    for i, chord in enumerate(chord_set):

        # Evaluate chord spacing
        spacing_fitness = 1 / np.sum(np.square(np.diff(chord)))
        chord_fitness[i] += np.sum(spacing_fitness)
        
        # Evaluate chord appropriateness
        # chord_components = chord % 12
        # chord_components.sort()
        # root_note = chord[0]
        
        
    # Evaluate rhythmic variation (if applicable)
    # fitness += evaluate_rhythmic_variation(chord_progression)

    return fitness