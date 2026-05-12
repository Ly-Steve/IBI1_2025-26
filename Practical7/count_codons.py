import matplotlib.pyplot as plt
import os
from collections import Counter

def parse_fasta(filename):
    genes = {}
    current_gene = None
    current_seq = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if current_gene:
                    genes[current_gene] = ''.join(current_seq)
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
    print(f"Error: {fasta_file} not found!")
else:
    stop_input = input("Enter one of the stop codons (TAA, TAG, or TGA): ").strip().upper()
    if stop_input not in {'TAA', 'TAG', 'TGA'}:
        print("Invalid stop codon! Must be TAA, TAG or TGA.")
    else:
        genes = parse_fasta(fasta_file)
        codon_counter = Counter()
        valid_genes = 0
        
        stop_rna = stop_input.replace('T', 'U')
        
        for gene_name, dna_seq in genes.items():
            mrna = dna_seq.replace('T', 'U')
            longest_orf_len = 0
            best_orf_start = -1
            
            # Find the longest ORF ending with the specified stop codon
            for i in range(len(mrna) - 2):
                if mrna[i:i+3] == 'AUG':
                    for j in range(i + 3, len(mrna) - 2, 3):
                        if mrna[j:j+3] == stop_rna:
                            orf_len = j + 3 - i
                            if orf_len > longest_orf_len:
                                longest_orf_len = orf_len
                                best_orf_start = i
                            break  # only first stop for this start
            
            if longest_orf_len > 0:
                # Extract codons upstream of the stop 
                orf = mrna[best_orf_start:best_orf_start + longest_orf_len - 3]
                for k in range(0, len(orf), 3):
                    codon = orf[k:k+3]
                    if len(codon) == 3:
                        codon_counter[codon] += 1
                valid_genes += 1
        
        if valid_genes == 0:
            print(f"No genes found containing {stop_input} in-frame stop codon.")
        else:
            # Report
            print(f"\nProcessed {valid_genes} genes containing {stop_input} stop codon.")
            print(f"Total codons counted: {sum(codon_counter.values())}")
            
            # Pie chart
            labels = list(codon_counter.keys())
            sizes = list(codon_counter.values())
            
            plt.figure(figsize=(10, 8))
            plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
            plt.title(f'Distribution of in-frame codons upstream of {stop_input} stop codon\n'
                      f'({valid_genes} genes)')
            plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            
            # Save to file 
            output_file = f'codon_frequency_{stop_input}.png'
            plt.savefig(output_file, dpi=150, bbox_inches='tight')
            plt.close()
            print(f"Pie chart saved as: {output_file}")