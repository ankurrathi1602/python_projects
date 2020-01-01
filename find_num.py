# Find the number btn 1500 and 2700 which is divisible by 7 and multiply by 5
nums = []
for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        nums.append(str(i))
print(",".join(nums))

