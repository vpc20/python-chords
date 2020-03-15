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
        '1 3 4 5': 'add4',  # Added Fourth
        '1 3 5 6': '6',  # Sixth
        '1 3 6': '6',
        '1 3 5 6 2': '6/9',  # Six Nine
        '1 3 6 2': '6/9',
        '1 3 5 7': 'maj7',  # Major 7th
        '1 3 7': 'maj7',
        '1 3 5 7 2': 'maj9',  # Major Ninth
        '1 3 7 2': 'maj9',
        '1 3 5 7 2 4': 'maj11',  # Major Eleventh
        '1 3 7 2 4': 'maj11',
        '1 3 5 7 4': 'maj11',
        '1 3 7 4': 'maj11',
        '1 3 5 7 2 4 6': 'maj13',  # Major Thirteenth
        '1 3 7 2 4 6': 'maj13',
        '1 3 5 7 4 6': 'maj13',
        '1 3 7 4 6': 'maj13',
        '1 3 5 7 2 6': 'maj13',
        '1 3 7 2 6': 'maj13',
        '1 3 5 7 6': 'maj13',
        '1 3 7 6': 'maj13',
        '1 3 5 7 b5': 'maj7#11',  # Major seven sharp eleventh
        '1 3 7 b5': 'maj7#11',
        '1 3 b5': '-',  # Major Flat Five
        '1 b3 5': 'm',  # Minor
        '1 b3 4 5': 'madd4',  # Minor added fourth
        '1 b3 5 6': 'm6',  # Minor sixth
        '1 b3 6': 'm6',
        '1 b3 5 b7': 'm7',  # Minor seventh
        '1 b3 b7': 'm7',
        '1 b3 5 2': 'madd9',  # Minor added ninth
        '1 b3 5 6 2': 'm6/9',  # Minor six add nine
        '1 b3 6 2': 'm6/9',
        '1 b3 5 b7 2': 'm9',  # Minor ninth
        '1 b3 b7 2': 'm9',
        '1 b3 5 b7 2 4': 'm11',  # Minor eleventh
        '1 b3 b7 2 4': 'm11',
        '1 b3 5 b7 4': 'm11',
        '1 b3 b7 4': 'm11',
        '1 b3 5 b7 2 4 6': 'm13',  # Minor thirteenth
        '1 b3 b7 2 4 6': 'm13',
        '1 b3 5 b7 4 6': 'm13',
        '1 b3 b7 4 6': 'm13',
        '1 b3 5 b7 2 6': 'm13',
        '1 b3 b7 2 6': 'm13',
        '1 b3 5 b7 6': 'm13',
        '1 b3 b7 6': 'm13',
        '1 b3 5 7': 'm/maj7',  # Minor/Major seventh
        '1 b3 7': 'm/maj7',
        '1 b3 5 7 2': 'm/maj9',  # Minor/Major ninth
        '1 b3 7 2': 'm/maj9',
        '1 b3 5 7 2 4': 'm/maj11',  # Minor/Major eleventh
        '1 b3 7 2 4': 'm/maj11',
        '1 b3 5 7 4': 'm/maj11',
        '1 b3 7 4': 'm/maj11',
        '1 b3 5 7 2 4 6': 'm/maj13',  # Minor/Major thirteenth
        '1 b3 7 2 4 6': 'm/maj13',
        '1 b3 5 7 4 6': 'm/maj13',
        '1 b3 7 4 6': 'm/maj13',
        '1 b3 5 7 6': 'm/maj13',
        '1 b3 7 6': 'm/maj13',
        '1 b3 b5 b7': 'ø',  # Half-diminished
        '1 3 5 b7': '7',  # Seventh
        '1 3 5 b7 2': '9',  # Ninth
        '1 3 5 b7 2 4': '11',  # Eleventh
        '1 3 5 b7 2 4 6': '13',  # Thirteenth
        '1 3 b6 b7': '7#5',  # Seven sharp five
        '1 3 b5 b7': '7b5',  # Seven flat five
        '1 3 5 b7 b2': '7b9',  # Seven flat ninth
        '1 3 b7 b2': '7b9',
        '1 3 5 b7 b3': '7#9',  # Seven sharp ninth
        '1 3 b6 b7 2': '9#5',  # Nine sharp five
        '1 3 b5 b7 2': '9b5',  # Nine flat five
        '1 3 b6 b7 b3': '7#5#9',  # Seven sharp five sharp nine
        '1 3 b6 b7 b2': '7#5b9',  # Seven sharp five flat nine
        '1 3 b5 b7 b3': '7b5#9',  # Seven flat five sharp nine
        '1 3 b5 b7 b2': '7b5b9',  # Seven flat five flat nine
        '1 3 5 b7 b5': '7#11',  # Seven sharp eleven
        '1 b3 b5': '°',  # Diminished
        '1 b3 b5 6': '°7',  # Diminished Seventh
        '1 3 b6': '+',  # Augmented
        '1 5': '5',  # Fifth
        '1 b5': '-5',  # Flat Fifth
        '1 4 5': 'sus4',  # Suspended Fourth
        '1 2 5': 'sus2',  # Suspended Second
        '1 5 b5': '#11',  # Sharp Eleven
        '1 3 5 2': 'add9',  # Add Nine
        '1 3 2': 'add9'
    }
    chord_name_list = []

    orig_root_note, reformatted_chord = reformat_chord(reformatted_chord)
    chord_inversions = [perms for perms in permutations(reformatted_chord.split())]
    for chord_inv in chord_inversions:
        chord_formula = gen_chord_formula(' '.join(chord_inv))
        # print(chord_inv, '-->', chord_formula)
        if chord_formula in chord_dict:
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

    # print(chord_id('e c g '))
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
    print(chord_id('c e g '))
    print(chord_id('db f ab f'))
    print(chord_id('db e ab '))
    print(chord_id('gb bb db eb ab c'))
    print(chord_id('e g b eb gb'))
