from randomizedMotiffs import *
from gibbsSampler import *


# ############ Randomized Motif Search ############
# with open("dataset_30307_5.txt", 'r') as f:
#     #print(f.readline())
#     k, d = map(int, f.readline().strip().split())

#     dna = f.readline().strip().split()
#     # print(dna)

#     #print(f.readline())
# result = repeated_randomized_motif_search(dna, k, d)
# print(' '.join(result))

# ###########Storing Resutls to output file ############
# with open("output.txt", 'w') as f:
#     f.write(' '.join(result))



########### Gibbs Sampler ############

with open("dataset_30309_11.txt", 'r') as f:
    k, t, N = map(int, f.readline().strip().split())
    Dna = f.readline().strip().split()
result = repeated_gibbs_sampler(Dna, k, t, N)
print(' '.join(result))

########### Storing Results to output file ############
with open("output_gibbs.txt", 'w') as f:
    f.write(' '.join(result))
