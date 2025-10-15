def stringCompositions(k, text):
    return [text[i:i+k] for i in range(len(text)-k+1)]

def genomePathProblem(kmers):

    string = ""

    for i in range(len(kmers)-1):

        if kmers[i][1:] == kmers[i+1][:-1]:

            if i == 0:

                string += kmers[i]

            string += kmers[i+1][-1]

            

        else:

            print("No valid genome path exists")

            return
    return string

