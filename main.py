
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

# ******************************
# Make your Code
# ******************************

# print ('True') or print ('False')

subset = True

for i in range(len(num2)):
    try:
        num1.index(num2[i])
    except ValueError:
        subset = False

print(subset)