import itertools

letters = "ABC"

perms = list(itertools.permutations(letters))

for p in perms:
    print("".join(p))
