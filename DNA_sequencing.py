def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """

    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """

    return len(dna1) > len(dna2)

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """

    count = 0

    for char in dna:
        if nucleotide == char:
            count = count + 1

    return count

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """

    contains = False

    if dna2 in dna1:
        contains = True

    return contains

def is_valid_sequence(dna):

    ''' (str) -> bool

    Return True if and only if dna only contain characters A,T,C and G.
    
    >>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_sequence('AHICL')
    False
    '''

    valid = True

    for char in dna:
        if char in 'ATCG':
            valid = True
        else: valid = False
    
    return valid

def insert_sequence(dna1,dna2,index):
        
    '''(str, str, int) -> str

    Return the dna sequence obtained by inserting the dna2 into the dna1
    at the given index.


    >>> insert_sequence('CCGG','AT',2):
    CCATGG
    >>> insert_sequence('ATGC','CC',1):
    ACCTGC
    '''

    dna = dna1[:index] + dna2 + dna1[index:]

    return dna

def get_complement(nucleotide):

    '''(str) -> str

    Return the nucleotide's complement.

    >>> get_complement('A')
    T
    >>> get_complement('C')
    G
    '''

    complement = ''
       
    if nucleotide == 'A':
            complement = 'T'
    elif nucleotide == 'T':
            complement = 'A'
    elif nucleotide == 'C':
            complement = 'G'
    elif nucleotide == 'G':
            complement = 'C'
    else: complement = '#'
                
    return complement

def get_complementary_sequence(dna):
    
    ''' (str) -> str

    Return the DNA sequence that is complementary to dna.
    
    >>> get_complementary_sequence('AT')
    TA
    >>> get_complementary_sequence('CG')
    GC
    '''

    complement_sequence = ''

    for char in dna:
        complement_sequence = complement_sequence + get_complement(char)

    return complement_sequence




