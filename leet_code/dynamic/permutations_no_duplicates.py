


"""
Permutations without Dups:
Write a method to compute all permutations of a string of
unique characters

abcdefgh

abcdefgh
abcdefg
abcdef
abcde
abcd
abc
ab
a
bcdefgh
bcdefg
bcdef
bcde
bcd
bc
b

"""

# The Base Case and Build approach will be useful
def print_permutations(sequence,index):
    if sequence is None:
        return None
    
    permutations = None     
    if(len(sequence) == index):
        permutations = []
        permutations.append("")
        return permutations
    else:
        local_permutations = []
        word = sequence[index]
        permutations = print_permutations(sequence,index+1)
        for permutation in permutations:
            temp = permutation+word
            print(temp)
            local_permutations.append(temp)
        permutations.extend(local_permutations)
    return permutations

         




if __name__ == "__main__":
    print_permutations("abcdefgh",0)