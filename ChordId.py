from itertools import permutations


# generate chord inversions
# def gen_chord_inv(chord):
#     # p1 = [perms for perms in permutations(chord.split())]
#     # return [' '.join(item) for item in p1]
#     return [' '.join(perms) for perms in permutations(chord.split())]


# get interval between 2 notes
def get_interval(note1, note2):
    notes = ['c', 'db', 'd', 'eb', 'e', 'f', 'gb', 'g', 'ab', 'a', 'bb', 'b']
    intervals = {1: 'b2', 2: '2', 3: 'b3', 4: '3',
                 5: '4', 6: 'b5', 7: '5', 8: 'b6',
                 9: '6', 10: 'b7', 11: '7', }

    semitone_dist = notes.index(note2) - notes.index(note1)
    if semitone_dist < 0:
        semitone_dist += 12
    return intervals[semitone_dist]


# generate chord formula
def gen_chord_formula(chord):
    chord_formula = ['1']
    notes = chord.split()
    for i in range(1, len(notes)):
        chord_formula.append(get_interval(notes[0], notes[i]))
    return ' '.join(chord_formula)


# change to lower case, remove duplicate notes, change sharps to flats
def reformat_chord(chord):
    chord = chord.lower()  # change to lower case

    # remove duplicate notes, retain sequence of notes
    seen = set()
    unique_notes = []
    for note in chord.split():
        if note not in seen:
            unique_notes.append(note)
            seen.add(note)
    chord = ' '.join(unique_notes)

    # orig_chord = chord
    orig_root_note = chord.split()[0]
    # replace sharps with flats
    enharmonic_eqv = [('c#', 'db'), ('d#', 'eb'), ('f#', 'gb'), ('g#', 'ab'), ('a#', 'bb')]
    for sharp_note, flat_note in enharmonic_eqv:
        chord = chord.replace(sharp_note, flat_note)
    return orig_root_note, chord


# get chord name
def chord_id(reformatted_chord):
    chord_dict = {
        '1 3 5': 'maj',  # Major
        '1 3 5 6': '6',  # Sixth
        '1 3 5 6 2': '6/9',  # Six Nine
        '1 3 5 2': 'add9',  # Add Nine
        '1 3 5 4': 'add11',  # Add 11
        '1 3 5 b5': '(#11)',  # Add sharp 11
        '1 3 5 2 b5': '(9,#11)',
        #
        '1 b3 5': 'm',  # Minor
        # '1 b3': 'm',
        '1 b3 5 6': 'm6',  # Minor sixth
        '1 b3 5 2': 'madd9',  # Minor added ninth
        '1 b3 5 6 2': 'm6/9',  # Minor six add nine
        '1 b3 6 2': 'm6/9',
        '1 b3 5 4': 'm(11)',  # Minor added 11

        #
        '1 3 5 b7': '7',  # Dominant seventh
        '1 3 b7': '7',
        '1 3 5 b7 2': '9',  # Ninth
        '1 3 b7 2': '9',
        '1 3 5 b7 2 4': '11',  # Eleventh
        '1 3 b7 2 4': '11',
        '1 3 5 b7 2 4 6': '13',  # Thirteenth
        '1 3 b7 2 4 6': '13',
        '1 3 5 b7 2 6': '13',
        '1 3 b7 2 6': '13',
        #
        '1 3 5 7': 'maj7',  # Major 7th
        '1 3 7': 'maj7',
        '1 3 7 b5': 'maj7-5',  # Major seven flat five
        '1 3 5 7 b6': 'maj7+5',  # Major seven sharp five
        '1 3 7 b6': 'maj7+5',
        '1 3 5 7 b5': 'maj7+11',  # Major seven sharp eleven
        '1 3 5 7 6': 'maj7add13',  # Major seven add thirteen
        '1 3 7 6': 'maj7add13',
        '1 3 5 7 2': 'maj9',  # Major Ninth
        '1 3 7 2': 'maj9',
        '1 3 5 7 2 b5': 'maj9+11',  # Major ninth sharp eleven
        '1 3 7 2 b5': 'maj9+11',
        # '1 3 5 7 2 4': 'maj11',  # Major Eleventh
        # '1 3 7 2 4': 'maj11',
        '1 3 5 7 2 4 6': 'maj13',  # Major Thirteenth
        '1 3 5 7 2 6': 'maj13',
        '1 3 5 7 2 b5 6': 'maj13+11',  # Major ninth sharp eleven
        '1 3 7 2 b5 6': 'maj13+11',
        #
        '1 b3 5 b7': 'm7',  # Minor seventh
        '1 b3 b7': 'm7',
        '1 b3 b7 b6': 'm7+5',  # Minor seventh sharp five
        # '1 b3 b7 b5': 'm7',
        '1 b3 5 b7 2': 'm9',  # Minor ninth
        '1 b3 b7 2': 'm9',
        '1 b3 5 b7 2 4': 'm11',  # Minor eleventh
        '1 b3 b7 2 4': 'm11',
        '1 b3 5 b7 2 4 6': 'm13',  # Minor thirteenth
        '1 b3 b7 2 4 6': 'm13',
        #
        '1 b3 5 7': 'm/maj7',  # Minor/Major seventh
        '1 b3 7': 'm/maj7',
        '1 b3 5 7 2': 'm/maj9',  # Minor/Major ninth
        '1 b3 7 2': 'm/maj9',
        '1 b3 5 7 2 4': 'm/maj11',  # Minor/Major eleventh
        '1 b3 7 2 4': 'm/maj11',
        '1 b3 5 7 2 4 6': 'm/maj13',  # Minor/Major thirteenth
        '1 b3 7 2 4 6': 'm/maj13',
        #
        # '1 3 4 b7 2': '9sus4',  # Ninth suspended
        # '1 3 4 5 b7': '7sus4',  # Seventh suspended
        # '1 3 4 b7': '7sus4',
        #
        '1 3 b6': '+',  # Augmented
        '1 3 b6 b7': '7+5',
        '1 3 b6 b7 2': '9+5',
        # '1 3 b6 7': '+maj7',
        #
        '1 3 b5 b7': '7-5',
        '1 3 b5 b7 b2': '7-9-5',
        '1 3 b5 b7 b3': '7+9-5',
        '1 3 5 b7 b2': '7-9',
        '1 3 b6 b7 b2': '7-9+5',
        '1 3 b6 b7 b3': '7+9+5',
        '1 3 5 b7 b3': '7+9',
        '1 3 5 b7 b5': '7+11',
        '1 3 5 b7 b2 b5': '7+11-9',
        '1 3 5 b7 b3 b5': '7+11+9',
        '1 3 b5 b7 2': '9-5',
        '1 3 5 b7 2 b5': '9+11',
        '1 3 5 b7 b2 6': '13-9',
        '1 3 b7 b2 6': '13-9',
        '1 3 5 b7 b3 6': '13+9',
        '1 3 b7 b3 6': '13+9',
        '1 3 5 b7 2 b5 6': '13+11',
        '1 3 b7 2 b5 6': '13+11',
        '1 b3 b5 b7 2 4': 'm11-5',
        #
        '1 b3 5 b7 4': 'm7add11',
        '1 b3 b7 4': 'm7add11',
        '1 b3 5 b7 6': 'm7add13',
        #
        '1 b3 b5': '°',  # Diminished
        # '1 b3 b5 b7': 'ø',  # Half-diminished
        '1 b3 b5 b7': 'm7-5',
        '1 b3 b5 b7 4': 'm7-5add11',
        '1 b3 b5 6': '°7',  # Diminished Seventh
        #
        '1 5': '5',  # Fifth
        '1 b5': '-5',  # Flat Fifth
        '1 3 b5': '-',  # Major Flat Five
        #
        '1 4 5': 'sus4',  # Suspended Fourth
        '1 4 5 b2': 'sus4-9',  # Suspended Fourth flat nine
        '1 4 5 b7': '7sus4',  # Seventh Suspended Fourth
        '1 4 b7': '7sus4',
        '1 4 5 7': 'maj7sus4',  # Major Seventh Suspended Fourth
        '1 4 5 b7 2': '9sus4',  # Ninth Suspended Fourth
        '1 4 5 b7 2 6': '13sus4',  # Thirteenth Suspended Fourth
        '1 2 5': 'sus2',  # Suspended Second
        '1 2 5 b7': '7sus2',  # Seventh Suspended Second
        '1 2 5 7': 'maj7sus2'  # Major Seventh Suspended Second
    }
    enharmonic = {'db': 'c#', 'eb': 'd#', 'gb': 'f#', 'ab': 'g#', 'bb': 'a#'}
    chord_name_list = []
    orig_root_note, reformatted_chord = reformat_chord(reformatted_chord)

    chord_inversions = [list(perms) for perms in permutations(reformatted_chord.split())]
    for chord_inv in chord_inversions:
        chord_formula = gen_chord_formula(' '.join(chord_inv))
        # print(chord_inv, '-->', chord_formula)
        if chord_formula in chord_dict:
            # if chord_inv[0] in enharmonic and enharmonic[chord_inv[0]] == orig_root_note:  # restore sharp
            if chord_inv[0] in enharmonic \
                    and enharmonic[chord_inv[0]].endswith('#') \
                    and orig_root_note.endswith('#'):  # restore sharp
                chord_inv[0] = enharmonic[chord_inv[0]]
            chord_name = f"{chord_inv[0].title()}{chord_dict[chord_formula]}"
            if chord_inv[0] != orig_root_note:  # slash chords
                chord_name = f'{chord_name}/{orig_root_note.title()}'
            chord_name_list.append(chord_name)
    return chord_name_list


if __name__ == '__main__':
    # print(gen_chord_inv('  c   e    g '))
    # print(semitone_distance(('a', 'c')))
    # print(get_interval(11))

    # print(get_interval(('c', 'e')))
    # print(get_interval(('e', 'g')))
    #
    # print(gen_chord_formula('c e g'))

    assert chord_id('c e g') == ['Cmaj']
    assert chord_id('c eb g') == ['Cm']
    assert chord_id('c g') == ['C5']
    assert chord_id('c d g') == ['Csus2', 'D7sus4/C', 'Gsus4/C']
    assert chord_id('c f g') == ['Csus4', 'Fsus2/C', 'G7sus4/C']
    assert chord_id('c e g bb') == ['C7']
    assert chord_id('c e g b') == ['Cmaj7']
    assert chord_id('c eb g bb') == ['Cm7', 'Eb6/C']
    assert chord_id('c eb g b') == ['Cm/maj7']
    assert chord_id('c e g bb d') == ['C9']
    assert chord_id('c e g b d') == ['Cmaj9']
    assert chord_id('c eb g bb d') == ['Cm9', 'Ebmaj7add13/C']
    assert chord_id('c e g d') == ['Cadd9', 'Em7+5/C']
    assert chord_id('c eb g d') == ['Cmadd9', 'Ebmaj7add13/C']
    assert chord_id('c e g a') == ['C6', 'Am7/C']
    assert chord_id('c eb g a') == ['Cm6', 'Am7-5/C']
    assert chord_id('c e g a d') == ['C6/9', 'Am7add11/C', 'D9sus4/C']
    assert chord_id('c eb g a d') == ['Cm6/9', 'Am7-5add11/C']
    assert chord_id('c e gb bb') == ['C7-5', 'Gb7-5/C']
    assert chord_id('c e g bb db') == ['C7-9']
    assert chord_id('c e g bb eb') == ['C7+9']
    assert chord_id('c f g bb') == ['C7sus4', 'Gm7add11/C']
    assert chord_id('c eb gb') == ['C°']
    assert chord_id('c eb gb a') == ['C°7', 'Eb°7/C', 'Gb°7/C', 'A°7/C']
    assert chord_id('c eb gb bb') == ['Cm7-5', 'Ebm6/C']
    assert chord_id('c e ab') == ['C+', 'E+/C', 'Ab+/C']
    assert chord_id('c e ab bb') == ['C7+5']
    assert chord_id('c e g bb d f') == ['C11']
    assert chord_id('c f g bb d') == ['C9sus4', 'Gm7add11/C', 'Bb6/9/C']
    assert chord_id('c eb g bb d f') == ['Cm11', 'Ebmaj13/C', 'F13sus4/C']
    assert chord_id('c e g bb d f a') == ['C13', 'Gm13/C', 'Bbmaj13+11/C', 'Fmaj13/C']

    # print(chord_id('c f'))
    # print(chord_id('e a  e  b '))

    # print(chord_id('e g c'))
    # print(chord_id('c e g '))

    # print(gen_chord_inv('c e g'))
    # print(gen_chord_inv('c e g b'))

    # print(reformat_chord('c e g'))
    # print(reformat_chord('c e G'))
    # print(reformat_chord('c e G c e g'))
    # print(reformat_chord('c e G e g'))
    # print(reformat_chord('a c# E '))
    # print(chord_id('c e g '))
    # print(chord_id('db f ab f'))
    # print(chord_id('db e ab '))
    # print(chord_id('gb bb db eb ab c'))
    # print(chord_id('e g b eb gb'))

    # print(chord_id('g c f a b'))
    # print(chord_id('g c f b d'))
    # print(chord_id('g c f b e'))
    # print(chord_id('c f b e a'))
    # print(chord_id('d g c f b'))
    # print(chord_id('g b f ab db f'))
    #
    # print(chord_id('c e b d g'))
    # print(chord_id('c e b d gb a'))
    # print(chord_id('c eb bb eb g'))
    # print(chord_id('c eb bb d f bb'))
    #
    # print(chord_id('c e bb db e a'))
    # print(chord_id('c e bb eb ab c'))
    # print(chord_id('c e bb db gb bb'))
    # print(chord_id('c e bb d gb a'))
    #
    # print(chord_id('c e g f'))
    # print(chord_id('c e g gb'))
    # print(chord_id('c e ab bb'))
    # print(chord_id('c f g bb d'))
    # print(chord_id('c eb g bb f'))
    # print(chord_id('c eb g bb a'))
    # print(chord_id('c e ab bb'))

    # print(chord_id('g c d f'))
    # print(chord_id('g c f a'))
    # print(chord_id('g c e f a'))
    # print(chord_id('g d f a'))
    # print(chord_id('g c d f a'))

    # print(chord_id('bb db eb gb'))
    # print(chord_id('a# c# d# f#'))
    # print(chord_id('f# c#'))
    # print(chord_id('ab gb bb c f'))
    # print(chord_id('c e g# bb d'))
    # print(chord_id('c e gb bb db'))
    # print(chord_id('c eb g bb d'))
    # print(chord_id('c eb g d'))

    # ezkeys chords
    print(chord_id('c e g'))  # major
    print(chord_id('c e g#'))
    print(chord_id('c e g a'))
    print(chord_id('c e g b'))
    print(chord_id('c e g d'))
    print(chord_id('c e g b d'))
    print(chord_id('c e g a d'))
    print(chord_id('c e g a b'))
    print(chord_id('c e gb b'))
    print(chord_id('c e g# b'))
    print(chord_id('c e g b f#'))
    print(chord_id('c e g b d f#'))
    print(chord_id('c e g b d f# a'))

    print(chord_id('c eb g'))  # minor
    print(chord_id('c eb g a'))
    print(chord_id('c eb g bb'))
    print(chord_id('c eb g# bb'))
    print(chord_id('c eb g b'))
    print(chord_id('c eb g d'))
    print(chord_id('c eb g a d'))
    print(chord_id('c eb g bb d'))
    print(chord_id('c eb g b d'))
    print(chord_id('c eb g bb f'))
    print(chord_id('c eb g bb d f'))
    print(chord_id('c eb g bb d f a'))

    print(chord_id('c e g bb'))  # dominant
    print(chord_id('c e g bb d'))
    print(chord_id('c g bb d f'))
    print(chord_id('c e g bb d a'))
    print(chord_id('c f g bb'))
    print(chord_id('c f g bb d a'))

    print(chord_id('c e gb bb'))
    print(chord_id('c e gb bb d'))
    print(chord_id('c e g# bb'))
    print(chord_id('c e g# bb d'))
    print(chord_id('c e g bb db'))

    print(chord_id('c e g bb d#'))
    print(chord_id('c e gb bb db'))
    print(chord_id('c e gb bb d#'))
    print(chord_id('c e g# bb db'))
    print(chord_id('c e g# bb d#'))

    print(chord_id('c e g bb f#'))
    print(chord_id('c e g bb d f#'))
    print(chord_id('c e g bb d f# a'))
    print(chord_id('c e g bb db a'))
    print(chord_id('c e g bb d# a'))

    print(chord_id('c f g'))  # suspended
    print(chord_id('c d g'))
    print(chord_id('c db f g'))

    print(chord_id('c eb gb bb'))  # half-diminished
    print(chord_id('c eb gb bb f'))

    print(chord_id('c eb gb'))  # diminished
    print(chord_id('c eb gb a'))

    print(chord_id('c g'))  # power chord

    print(chord_id('c# b f#'))
    print(chord_id('c# f# b e'))
    print(chord_id('e c f# a'))




