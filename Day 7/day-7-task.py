from itertools import permutations
def allPermutations(str):
    # Get all permutations of string 'str'
    permList = sorted([''.join(p) for p in permutations(str)])
    return permList

# Driver program
if __name__ == "__main__":
    str = "ABCD"
    for i in allPermutations(str):
        print(i)

