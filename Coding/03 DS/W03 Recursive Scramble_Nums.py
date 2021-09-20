
def scramble_nums(remain_nums, scram_nums):
    if len(remain_nums) == 0:
        print(scram_nums[0], scram_nums[1], scram_nums[2], sep='')
    else:
        for i in range(len(remain_nums)):
            tmp_remain_nums = remain_nums[:] # Make a copy.
            tmp_removed_num = tmp_remain_nums[i] 
            tmp_remain_nums.pop(i) # Remove element at i
            scram_nums.append(tmp_removed_num)
            scramble_nums(tmp_remain_nums, scram_nums)
            scram_nums.pop() # Remove last element

nums_to_scramble = []
result_nums = []

nums_to_scramble.append(7);
nums_to_scramble.append(2);
nums_to_scramble.append(4);
   
scramble_nums(nums_to_scramble, result_nums);


# Reverse
def scramble_nums(remain_nums, scram_nums):
    if len(remain_nums) == 0:
        print(scram_nums[0], scram_nums[1], scram_nums[2], sep='')
    else:
        for i in reversed(range(len(remain_nums))): # New: This line changed
            tmp_remain_nums = remain_nums[:] # Make a copy.
            tmp_removed_num = tmp_remain_nums[i] 
            tmp_remain_nums.pop(i) # Remove element at i
            scram_nums.append(tmp_removed_num)
            scramble_nums(tmp_remain_nums, scram_nums)
            scram_nums.pop() # Remove last element

nums_to_scramble = []
result_nums = []

nums_to_scramble.append(1);
nums_to_scramble.append(6);
nums_to_scramble.append(5);
   
scramble_nums(nums_to_scramble, result_nums);