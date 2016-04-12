import sys

"""
To make a new scale, import this class and create a scale like this:
`scaleName = Scale('key')`
The key can be any note other than B#, Cb, E#, or Fb.
To calculate the notes, write something like this:
'scaleName.mode()'
This will return an array of notes of the scale in the key.
"""


class Scale:
    sharps = {1: 'A', 2: 'A#', 3: 'B', 4: 'C', 5: 'C#', 6: 'D', 7: 'D#', 8: 'E', 9: 'F', 10: 'F#', 11: 'G', 12: 'G#'}
    flats = {1: 'A', 2: 'Bb', 3: 'B', 4: 'C', 5: 'Db', 6: 'D', 7: 'Eb', 8: 'E', 9: 'F', 10: 'Gb', 11: 'G', 12: 'Ab'}

    notes = sharps

    def __init__(self, key):
        self.key = key
        try:
            if 'b' is list(key)[1]:
                self.notes = self.flats
            elif '#' is list(key)[1]:
                self.notes = self.sharps
            else:
                print('Note name not valid.')
                print(list(key)[1])
                sys.exit(0)
        except IndexError:
            pass

    def scaleCalc(self, intervals):
        nScale = []
        x = list(self.notes.keys())[list(self.notes.values()).index(self.key)]
        for interval in intervals:
            try:
                nScale.append(self.notes[x])
                x += interval
            except KeyError:
                x = 1
                nScale.append(self.notes[x])
                x += interval
        nScale.append(self.notes[list(self.notes.keys())[list(self.notes.values()).index(self.key)]])
        return nScale

class Diatonic(Scale):

    def major(self):
        return self.ionian()

    def minor(self):
        return self.aeolian()

    def ionian(self):
        scale = self.scaleCalc([2, 2, 1, 2, 2, 2, 1])
        return scale

    def dorian(self):
        scale = self.scaleCalc([2, 1, 2, 2, 2, 1, 2])
        return scale

    def phrygian(self):
        scale = self.scaleCalc([1, 2, 2, 2, 1, 2, 2])
        return scale

    def lydian(self):
        scale = self.scaleCalc([2, 2, 2, 1, 2, 2, 1])
        return scale

    def mixolydian(self):
        scale = self.scaleCalc([2, 2, 1, 2, 2, 1, 2])
        return scale

    def aeolian(self):
        scale = self.scaleCalc([2, 1, 2, 2, 1, 2, 2])
        return scale

    def locrian(self):
        scale = self.scaleCalc([1, 2, 2, 1, 2, 2, 2])
        return scale
