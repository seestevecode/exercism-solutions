"""Translate an RNA sequence into proteins"""

CODONS_TO_ACID = [
    [['AUG'], 'Methionine'],
    [['UUU', 'UUC'], 'Phenylalanine'],
    [['UUA', 'UUG'], 'Leucine'],
    [['UCU', 'UCC', 'UCA', 'UCG'], 'Serine'],
    [['UAU', 'UAC'], 'Tyrosine'],
    [['UGU', 'UGC'], 'Cysteine'],
    [['UGG'], 'Tryptophan'],
    [['UAA', 'UAG', 'UGA'], 'STOP']
]

CODON_TO_ACID = {
    codon: acid
    for codons, acid in CODONS_TO_ACID
    for codon in codons
}

def proteins(strand):    
    result = []
    for codon in [strand[index:index+3] for index in range(0, len(strand), 3)]:
        acid = CODON_TO_ACID[codon]
        if acid == 'STOP':
            break
        result.append(acid)
    return result
    