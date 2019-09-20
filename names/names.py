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

unique = { i : True for i in names_1 }

for i in range(len(names_2)):
    if names_2[i] in unique.keys():
        duplicates.append(names_2[i])



end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# if __name__ == '__main__':
    # print(len(names_1), len(names_2))