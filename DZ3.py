my_list = [23, 567, 109, 4, 0]
for i in my_list:
    if i >= 100:
        print([i])


################################
my_list = [23, 567, 109, 4, 0]
my_results = []
for i in range(len(my_list)):
    my_results.append(100)
    print(my_results)
################################

if len(my_list) >= 2:
    my_list.append(my_list[-1] + my_list[-2])
else:
    my_list.append(0)

print(my_list)

print(sum(my_list[-2:]))
################################

my_string = '0123456789'
result = []

for symbol_1 in my_string:
    for symbol_2 in my_string:
        result.append(int(symbol_1 + symbol_2))

print(result)







