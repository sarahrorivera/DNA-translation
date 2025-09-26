# Import the helper module with the amino acid dictionary and chunk function
import helper

# Define the transcription function
def transcription(dna_sequence):
    # Create an empty string to store the mRNA sequence
    mrna = ""
    
    # Replace Thymine with Uracil (T with U)
    mrna = dna_sequence.replace('T', 'U')
    
    # Create the Base Pair Complement
    complement = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}
    mrna = ''.join(complement[nucleotide] for nucleotide in mrna)
    
    return mrna

# chunks
def chunk(string, chunk_size):
    chunk_list = [string[i:i+chunk_size] for i in range(0, len(string), chunk_size)]
    return chunk_list

#translation
def translate(mrna):
    # Create an empty string to store the protein sequence
    protein = ""
    
    # triplets
    triplets = chunk(mrna, 3)
    
    # dictionaryy
    for triplet in triplets:
        if triplet in helper.amino_acids:
            amino_acid = helper.amino_acids[triplet]
            if amino_acid == 'STOP':
                break
            protein += amino_acid + ' '
    
    return protein

#dnaaaaaa
dna = input("enter a dna sequence: ")
print(f"DNA: {dna} ")

#DNA to mRNA
mrna = transcription(dna)
print("mRNA Sequence: ", mrna)

#mRNA to protein
protein = translate(mrna)
print("Protein Sequence: ", protein)
