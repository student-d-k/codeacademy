
people = {
    ('Jonas', 'Jonaitis'): 
        {
            'Asmens kodas': 38401010001,
            'Banko saskaita': 'LT750000111122223333',
        },
    ('Petras', 'Petraitis'): 
        {
            'Asmens kodas': 38401010002,
            'Banko saskaita': 'LT750000111144443333',
        },
}

for k, v in people.items():
    print('-'*120)
    print(
        f'| {k[0]}' + ' ' * (18-len(k[0])) + 
        f'| {k[1]}' + ' ' * (18-len(k[1])) + 
        f'| {v}' + ' ' * (77-len(str(v))) + 
        '|')
print('-'*120)
