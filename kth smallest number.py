# Program to find the kth smallest element in an array
# Anand.G.Murugan
# 20BCE2441
# anandmurugan.g2020@vit.ac.in

# Bubble Sort will be used to sort the array
def bubbleSort(list):
    n = len(list)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]


# Inputting the data
# n->number of elements in the array
print("Input number of elements:")
n = int(input())

# k->kth smallest element to find
print("Input k:")
k = int(input())

# array of n numbers
array = []
print("Input array:")
for i in range(0, n):
    t = int(input())
    array.append(t)

# Sorting
bubbleSort(array)

# Output
print(array)
print(array[k - 1])
