from itertools import count


def check_occrance(str1):
    counts=dict()
    words = str1.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
print(check_occrance("this in jagadeesh, working in omics"))