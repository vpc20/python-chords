enharmonic = {'c#': 'db', 'd#': 'eb', 'f#': 'gb', 'g#': 'ab', 'a#': 'bb'}

print(enharmonic)
x = {v: k for k, v in enharmonic.items()}
print(x)
