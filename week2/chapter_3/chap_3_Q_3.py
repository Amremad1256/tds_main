set1 = {2, 4, 6, 8, 10, 'McArthur'}
set2 = {'Smith', 'McArthur', 'Wilson', 'Johansson'}
def complement(set1, set2):
    return set2.difference(set1)
print (complement(set1, set2))