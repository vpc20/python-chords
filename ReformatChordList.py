s = '''Major 	Maj 	1-3-5
Added Fourth 	add4 	1-3-4-5
Sixth 	6 	1-3-5-6
Six Nine 	6/9 	1-3-5-6-9
Major 7th 	Maj7 	1-3-5-7
Major Ninth 	Maj9 	1-3-5-7-9
Major Eleventh 	Maj11 	1-3-5-7- (9)-11
Major Thirteenth 	Maj13 	1-3-5-7-(9)-(11)-13
Major seven sharp eleventh 	Maj7#11 	1-3-5-7- #11
Major Flat Five 	- 	1-3-b5
Minor 	m 	1-b3-5
Minor added fourth 	madd4 	1-b3-4-5
Minor sixth 	m6 	1-b3-5-6
Minor seventh 	m7 	1-b3-5-b7
Minor added ninth 	madd9 	1-b3-5-9
Minor six add nine 	m6/9 	1-b3-5-6-9
Minor ninth 	m9 	1-b3-5-b7-9
Minor eleventh 	m11 	1-b3-5-b7-(9)-11
Minor thirteenth 	m13 	1-b3-5-b7-(9)-(11)-13
Minor/Major seventh 	m/Maj7 	1-b3-5-7
Minor/Major ninth 	m/Maj9 	1-b3-5-7-9
Minor/Major eleventh 	m/Maj11 	1-b3-5-7-(9)-11
Minor/Major thirteenth 	m/Maj13 	1-b3-5-7-(9)-(11)-13
Half-diminished 	ø 	1-b3-b5-b7
Seventh 	7 	1-3-5-b7
Ninth 	9 	1-3-5-b7-9
Eleventh 	11 	1-(3)-5-b7-(9)-11
Thirteenth 	13 	1-3-5-b7-(9)-(11)-13
Seven sharp five 	7#5 	1-3-#5-b7
Seven flat five 	7b5 	1-3-b5-b7
Seven flat ninth 	7b9 	1-3-5-b7-b9
Seven sharp ninth 	7#9 	1-3-5-b7-#9
Nine sharp five 	9#5 	1-3-#5-b7-9
Nine flat five 	9b5 	1-3-b5-b7-9
Seven sharp five sharp nine 	7#5#9 	1-3-#5-b7-#9
Seven sharp five flat nine 	7#5b9 	1-3-#5-b7-b9
Seven flat five sharp nine 	7b5#9 	1-3-b5-b7-#9
Seven flat five flat nine 	7b5b9 	1-3-b5-b7-b9
Seven sharp eleven 	7#11 	1-3-5-b7-#11
Diminished 	° 	1-b3-b5
Diminished Seventh 	°7 	1-b3-b5-6
Augmented 	+ 	1-3-#5
Fifth 	5 	1-5
Flat Fifth 	-5 	1-b5
Suspended Fourth 	sus4 	1-4-5
Suspended Second 	sus2 	1-2-5
Sharp Eleven 	#11 	1-5-#11'''

chord_list = [item.split('\t') for item in (s.split('\n'))]
print(chord_list)

for item in chord_list:
    chord_type = item[0]
    chord_symbol = item[1].strip().lower()
    chord_formula = item[2].strip().replace('-', ' ').replace('(', '').replace(')', '').replace('#5', 'b6') \
        .replace('9', '2').replace('11', '4').replace('13', '6'). replace('#2', 'b3'). replace('#4', 'b5')
    print("'{}' : '{}',  # {}".format(chord_formula, chord_symbol, chord_type))
