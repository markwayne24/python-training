given_number = 8
# holder = 1
# for x in range(1, given_number + 1):
#     holder = holder * x
# print(holder)

results = [x for x in range(1, given_number + 1)]


def multiply_list_function(my_list):
    holder = 1
    for x in my_list:
        holder *= x
    return holder


print(multiply_list_function(results))
