from dictionaries import *

dna_strand = input("> Enter Forward DNA Strand : ").lower()
rna_strand = ""
protein_strings = ""

# DNA Strand -> RNA Strand 3' --- 5'
for i in dna_strand:
    if(i=='a' or i=='t' or i=='c' or i=='g'):
        rna_strand += dnarna[i]
    else:
        print("> Enter Correct DNA Strand")
        exit()

# print("> RNA Strand : ",end="")
# print("3' " + rna_strand + " 5'")
print("> RNA Strand : ",end="")
print("5' " + rna_strand + " 3'")
# print(len(rna_strand))

total_proteins = rna_strand.count("aug")
# print(total_proteins)

if(total_proteins > 0):
    print("> Proteins : ",end="")
    for i in range(len(rna_strand)-2):
        if("aug" == rna_strand[i:i+3]):
            j = i+3
            protein_strings += rnaprotein[rna_strand[i:i+3]]
            while j+2 < len (rna_strand) and rnaprotein[rna_strand[j:j+3]]!="Stp":
                protein_strings += "-" + rnaprotein[rna_strand[j:j+3]]
                j+=3
            if(j>=len(rna_strand)-2):
                protein_strings+="-"
            break
    print(protein_strings)
else:
    print("> Start Codon Not Found!")