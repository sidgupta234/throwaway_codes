def sseq(a):
    if a == "":
        return [""]
        
    else:
        first_char = a[0]
        rest_chars = a[1:]
        #print(first_char, rest_chars)
        rest_sequences = sseq(rest_chars)

        all_sequences = []
        
        for sequence in rest_sequences:
            #print("rr is", rr)
            all_sequences.append(sequence)
            all_sequences.append(first_char+sequence)
            
        return all_sequences

print(sseq("abcdef"))
