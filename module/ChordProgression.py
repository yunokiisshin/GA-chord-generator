import numpy as np
import pygad
import random
import music21 as m21
import pygame as pg


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
        
        
    def randomlyInitializeChordSet(self):
        for i, chord in enumerate(self.chord_list):
            random_chord = sorted([int(random.randint(36,96)) for i in range(4)])
            self.chord_set[i] = random_chord
            
        
    def getBarLength(self):
        return self.num_bars
    
    def getChordList(self):
        return self.chord_list
    
    def getChordSet(self):
        return self.chord_set
    
    def saveAsMIDI(self):
        # Create a music21 stream
        s = m21.stream.Stream()

        # Iterate over each chord in the chord set
        for chord in self.chord_set:
            # Create a list of music21 note objects from MIDI numbers
            midi_notes = [m21.note.Note(midi=int(midi_num)) for midi_num in chord]
            # Create a chord from these notes
            midi_chord = m21.chord.Chord(midi_notes)
            # Add the chord to the stream
            s.append(midi_chord)

        # Write the stream to a MIDI file
        midi_path = "./output/output.mid"
        s.write('midi', fp=midi_path)
        return midi_path
    
    
    def play(self):
        
        midi_path = self.saveAsMIDI()
        # Play the MIDI file using pygame
        pg.mixer.init()
        pg.mixer.music.load(midi_path)
        pg.mixer.music.play()

        # Keep the program running until the music stops
        while pg.mixer.music.get_busy():
            pg.time.Clock().tick(10)
        
    

instance = ChordProgression(['C', 'Dm', 'Em', 'F'])
instance.randomlyInitializeChordSet()
print(instance.getChordSet())
instance.play()
