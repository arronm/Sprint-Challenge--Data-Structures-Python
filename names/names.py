import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# 64 duplicates
duplicates = []

# ORIGINAL:
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


# Truly 124 duplicates total
# create dictionary
# unique = {}

# loop over recording unique names
# for i in range(max(len(names_1), len(names_2))):
#     if names_1[i] == names_2[i]:
#         unique_1[names_1[i]] = True
#         unique_2[names_2[i]] = True
#         duplicates.append(names_1[i])

#     # check for duplicate, add to list
#     if names_1[i] in unique.keys():
#         duplicates.append(names_1[i])

#     if names_2[i] in unique.keys():
#         duplicates.append(names_2[i])
    
#     unique[names_1[i]] = True
#     unique[names_2[i]] = True


# SPRINT SOLUTION:
# unique = { i : True for i in names_1 }

# for i in range(len(names_2)):
#     if names_2[i] in unique.keys():
#         duplicates.append(names_2[i])


# STRETCH SOLUTION:
from bisect import bisect_left

# binary search with bisect
def binary_search(list, item, low=0, high=None):
    high = high if high is not None else len(list)
    pos = bisect_left(list, item, low, high)
    return (pos if pos != high and list[pos] == item else -1)

# In place sort to save memory
names_2.sort()

# Search for every name in list 1, to see if it's in list 2
for name in names_1:
    name_2 = names_2[binary_search(names_2, name)]
    if name_2 == name:
        duplicates.append(name_2)


# ALTERNATE SOLUTION:
# set_1 = set(names_1)
# set_2 = set(names_2)
# duplicates = [i for i in set_1.intersection(set_2)]


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# if __name__ == '__main__':
    # print(len(names_1), len(names_2))