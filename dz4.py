##########1############

print(input().count('0'))

##########2############

n = int(input())
if (n == 0):
    print(1)
    exit()
countZero = 0
while (n % 10 == 0):
    n //= 10
    countZero += 1
print(countZero)

##########3###########

my_list_1, my_list_2 = [1, 2, 3, 4, 5], [6, 7, 8, 9]
my_result = [my_list_1[i]
for i in range(len(my_list_1))
if my_list_1[i] % 2 == 0] + [my_list_2[i]
for i in range(len(my_list_2))
if my_list_2[i] % 2 == 1]
print(my_result)

##########4###########

my_list = [1, 2, 3, 4]
new_list = my_list[1:] + [my_list[0]]
print(f"{new_list=}")
print(f"{my_list=}")
my_reversed_list = list(reversed(my_list))

##########5###########

my_list = [1, 2, 3, 4]
list_value = my_list.pop(0)
my_list.append(list_value)
print(my_list)
#########6#############

my_string = "43 > 34 < 56"
my_str_list = my_string.split()
counter = 0

for item in my_str_list:
    if item.isdigit():
        counter += int(item)

print(counter)
result_list = [i for i in range(100)]
copy_list = result_list[::]

result_list_2 = []
for i in range(100):
    result_list_2.append(i)
print(f"{result_list_2=}")
###########7###############

my_str = "My long string"
l_limit, r_limit = "o", "g"
l_index = my_str.find(l_limit) + 1
r_index = my_str.rfind(r_limit)
sub_str = my_str[l_index: r_index]

sub_str = my_str[my_str.find(l_limit) + 1: my_str.rfind(r_limit)]

print(sub_str)
############8#############

example = 'abcde'

result_list = []
EXAMPLE_LENGTH = len(example)
for index in range(0, EXAMPLE_LENGTH, 2):
    if index < EXAMPLE_LENGTH - 1:
        result_list.append(example[index] + example[index + 1])
    else:
       result_list.append(example[index] + '_')

print(result_list)

better_result = []
for index in range(0, EXAMPLE_LENGTH, 2):
    better_result.append(example[index: index + 2].ljust(2, '_'))
print(better_result)

result_best = [example[i: i + 2].ljust(2, '_') for i in
               range(0, EXAMPLE_LENGTH, 2)]
print(result_best)
##############9###############
my_list = [2, 4, 1, 5, 3, 9, 0, 7]
print(sum(my_list))
counter = 0

for index in range(1, len(my_list) - 1):
    if my_list[index] > sum([my_list[index - 1], my_list[index + 1]]):
        counter += 1







