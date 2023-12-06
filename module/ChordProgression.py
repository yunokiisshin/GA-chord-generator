import numpy as np
import pygad


# note to self: utilize chord generator from previous project

class ChordProgression:
    
    '''
    param chord_list: list of chords in strings. Ex: ['C', 'Dm', 'Em', 'F', 'G', 'Am', 'Bdim', 'C]
                      implied that the chords are in the key of C major
                      implied that len(chord_list) == len(num_bars) for now
    param num_notes: number of notes in each chord; default is 4
    param num_bars: number of bars in the chord progression; default is 4
    '''
    def __init__(self, chord_list: list, num_notes: int = 4, num_bars: int = 4):
        self.num_bars = num_bars
        self.chord_list = chord_list
        self.chord_set = np.zeros((num_bars, num_notes))
        
        
    def randamlyInitializeChordSet(self):
        # for i, chord in enumerate(self.chord_list):
            
        
    def getBarLength(self):
        return self.num_bars
    
    def getChordList(self):
        return self.chord_list
    
    def getChordSet(self):
        return self.chord_set

# use example: instance = ChordProgression(['C', 'Dm', 'Em', 'F'])