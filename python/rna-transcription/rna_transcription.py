"""Determine the RNA complement of a given DNA sequence"""

TRANSLATION = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}

def to_rna(dna_strand):
    return ''.join(TRANSLATION[char] for char in dna_strand)
