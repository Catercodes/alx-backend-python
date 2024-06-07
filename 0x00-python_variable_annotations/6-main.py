#!/usr/bin/env python3

sum_mixed_list = __import__('6-sum_mixed_list').sum_mixed_list

print(sum_mixed_list.__annotations__)
mixed = [5, 4, 3.14, 666, 0.99]
#chris = sum_mixed_list([1.11, 2.22, 3.33, 4, 5, 6, -666])
ans = sum_mixed_list(mixed)
print(ans == sum(mixed))
#print(chris)
print("sum_mixed_list(mixed) returns {} which is a {}".format(ans, type(ans)))