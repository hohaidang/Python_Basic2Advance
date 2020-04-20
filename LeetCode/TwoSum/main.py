def twoSum(nums, target):
    data = {}
    for (i, num) in enumerate(nums):
        n = target - num;
        if num not in data:
            data[n] = i;
        else:
            return [data[num], i];


data = [3, 1, 4, 1, 5]
test = twoSum(data, 6);
print(test)