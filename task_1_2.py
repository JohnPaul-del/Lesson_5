from itertools import islice

nums = int(input("Enter nums: "))
print(*islice((i for i in range(1, nums+1) if i % 2 == 1), nums))
