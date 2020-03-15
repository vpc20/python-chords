all_notes = ['c', 'db', 'd', 'eb', 'e', 'f', 'gb', 'g', 'ab', 'a', 'bb', 'b']
interval_dict = {1: 'b2', 2: '2', 3: 'b3', 4: '3',
                 5: '4', 6: 'b5', 7: '5', 8: 'b6',
                 9: '6', 10: 'b7', 11: '7', }

all_interval_pair = {}
for i in range(len(all_notes)):
    rotated_all_notes = all_notes[i:] + all_notes[:i]
    for j in range(1, len(rotated_all_notes)):
        print((rotated_all_notes[0], rotated_all_notes[j]), interval_dict[j])
        all_interval_pair[(rotated_all_notes[0], rotated_all_notes[j])] = interval_dict[j]
print(all_interval_pair)
