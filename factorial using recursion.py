# Program to find the factorial of a number using recursion
# Anand.G.Murugan
# 20BCE2441
# anandmurugan.g2020@vit.ac.in

# Inputting the number
n = int(input())

t = 1
# Recursive function
for i in range(1, n + 1):
    t = t * i

print(t)
