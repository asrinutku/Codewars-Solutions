def DNA_strand(dna):
    
    comps = {
        'T': 'A',
        'C': 'G',
        'A': 'T',
        'G': 'C',
    }
    
    return ''.join([comps[i] for i in dna])
