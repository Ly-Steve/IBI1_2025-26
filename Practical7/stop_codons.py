import os

def parse_fasta(filename):
    """Parse FASTA file, return dict of gene_name: DNA_sequence"""
    genes = {}
    current_gene = None
    current_seq = []
    
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if current_gene:
                    genes[current_gene] = ''.join(current_seq)
                # Take only the first word as gene name 
                current_gene = line[1:].split()[0]
                current_seq = []
            else:
                current_seq.append(line)
        if current_gene:
            genes[current_gene] = ''.join(current_seq)
    return genes

# Main
fasta_file = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
if not os.path.exists(fasta_file):
    print(f"Error: {fasta_file} not found in current folder!")
else:
    genes = parse_fasta(fasta_file)
    stop_genes = []

    for gene_name, dna_seq in genes.items():
        mrna = dna_seq.replace('T', 'U')
        found_stops = set()
        
        for i in range(len(mrna) - 2):
            if mrna[i:i+3] == 'AUG':
                for j in range(i + 3, len(mrna) - 2, 3):
                    codon = mrna[j:j+3]
                    if codon in {'UAA', 'UAG', 'UGA'}:
                        found_stops.add(codon.replace('U', 'T'))  # store as TAA/TAG/TGA
                        break  # first stop for this ORF
        
        if found_stops:
            stops_str = '_'.join(sorted(found_stops))
            header = f">{gene_name}_{stops_str}"
            stop_genes.append((header, dna_seq))  # save original DNA sequence

    # Write output file
    with open('stop_genes.fa', 'w') as out:
        for header, seq in stop_genes:
            out.write(header + '\n')
            # Write sequence in lines of 60 characters 
            for i in range(0, len(seq), 60):
                out.write(seq[i:i+60] + '\n')
    
    print(f"stop_genes.fa created successfully! {len(stop_genes)} genes with in-frame stop codons.")