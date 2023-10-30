# number = 1
# while number <= 10:
#     print(number)
#     number = number + 1

# number = int(input())
# while number !=0:
#     print(number + 5)
#     number = int(input())

digital_M = 7
digital_K = int(input())
n_attempt = 1
while digital_K != digital_M:
    n_attempt +=1
    digital_K = int(input())
print(n_attempt)