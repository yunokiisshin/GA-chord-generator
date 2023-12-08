import pygad
import numpy as np
import random
import music21 as m21

from module.ChordProgression import ChordProgression
from module.fitness_func import fitness_func

def main():
    for i in range(3):

        instance = ChordProgression()
        instance.randomlyInitializeChordSet()
        print(instance.getChordSet())
        instance.play()


if __name__ == "__main__":
    main()
