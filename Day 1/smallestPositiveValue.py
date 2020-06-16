# Complicated Algo

# def smallest_positive1(in_list):
#     positiveNumber = []
#     for i in in_list:
#         if(i>0):
#             positiveNumber.append(i)
    
#     if(positiveNumber != []):  
#         return min(positiveNumber)
#     else:
#         return None

# Simple Algo

# def smallest_positive2(in_list):
#     smallest_pos = None
#     for num in in_list:
#         if num > 0:
#             if smallest_pos == None or num < smallest_pos:
#                 smallest_pos = num
#     return smallest_pos


# Test cases

print(smallest_positive([4, -6, 7, 2, -4, 10]))
# Correct output: 2

print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
# Correct output: 0.2

print(smallest_positive([-6, -9, -7]))
# Correct output: None

print(smallest_positive([]))
# Correct output: None