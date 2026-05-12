

seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'

def find_longest_orf(rna_seq):
    """Find the longest ORF starting with AUG anywhere in the sequence."""
    rna_seq = rna_seq.upper()
    start_codon = 'AUG'
    stop_codons = {'UAA', 'UAG', 'UGA'}
    longest_orf = ""
    max_length = 0
    n = len(rna_seq)
    
    for i in range(n - 2):
        if rna_seq[i:i+3] == start_codon:
            # Look for the first in-frame stop codon
            for j in range(i + 3, n - 2, 3):
                codon = rna_seq[j:j+3]
                if codon in stop_codons:
                    orf = rna_seq[i:j+3]
                    orf_length = len(orf)
                    if orf_length > max_length:
                        max_length = orf_length
                        longest_orf = orf
                    break  # only the first stop after this start
    return longest_orf, max_length

orf, length = find_longest_orf(seq)
print("Longest ORF:", orf)
print("Length:", length, "nucleotides")

