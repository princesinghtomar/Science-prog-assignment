from dictionaries import *

sequence = input("> Enter You Forward DNA Strand : ").lower()

print(sequence)

rec_sites = []

def ad_palindrome(k,j,diff):
    rec_string = ""
    while(j<len(sequence) and k>=0 and sequence[k] == dnacompliment[sequence[j]]):
        rec_string = sequence[k] + rec_string + sequence[j]
        k-=1
        j+=1
    if(j-k > diff ):
        rec_sites.append(rec_string)

for i in range(len(sequence)):
    if(sequence[i]!='a' and sequence[i]!='t' and sequence[i]!='c' and sequence[i]!='g'):
        print("> Enter Correct DNA Strand")
        exit()
    else:
        k = i
        j = i+1
        ad_palindrome(i,i+1,3)
        ad_palindrome(i-1,i+1,7)

print("len(rec_sites) : " + str(len(rec_sites)) )
if(len(rec_sites) > 0):
    print("> Restriction Recognition Sites : ")
    for i in rec_sites:
        print(i)
else:
    print("> No Restriction Recognition Sites Present")