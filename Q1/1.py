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

print("> RNA Strand : ",end="")
print("3' " + rna_strand + " 5'")
rna_strand_5_3 = rna_strand[::-1] # convert rna string to 5' --- 3' for protein
print("> RNA Strand : ",end="")
print("5' " + rna_strand_5_3 + " 3'")
# print(len(rna_strand))

total_proteins = rna_strand_5_3.count("aug")
# print(total_proteins)

if(total_proteins > 0):
    print("> Proteins : ",end="")
    for i in range(len(rna_strand_5_3)-2):
        if("aug" == rna_strand_5_3[i:i+3]):
            j = i+3
            protein_strings += rnaprotein[rna_strand_5_3[i:i+3]]
            while j+2 < len (rna_strand_5_3) and rnaprotein[rna_strand_5_3[j:j+3]]!="Stp":
                protein_strings += "-" + rnaprotein[rna_strand_5_3[j:j+3]]
                j+=3
            if(j>=len(rna_strand_5_3)-2):
                protein_strings+="-"
            break
    print(protein_strings)
else:
    print("> Start Codon Not Found!")