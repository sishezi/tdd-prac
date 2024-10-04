def sum_of_even(nums):
    sum = 0
    for num in nums:            #loop through numbers to see if the divisible by 2, if so, then add to the sum and return the sum of the even numbers
        if num % 2 == 0:
            sum += num
    return sum
print(sum_of_even([2,5,6,7,9,10]))



def calculate_median(nums):
    nums.sort()             #used sort method to add them in ascending order
    length = len(nums)      #to find median of the numbers, I calculated the length of numbers within the list
    if length == 0:             
        return None         
    elif length % 2 == 0:   #if the length of numbers is an even number...
        return (nums[length//2 - 1] + nums[length//2]) / 2     #then calculate the sum of the two middle values and divide by 2
    else:
        return nums[length//2] 
print(calculate_median([3,6,9,12]))



def find_missing_number(nums):
    max_num = max(nums)
    for i in range(1, max_num + 1): #loops throught the numbers list and check if the number does exist, if not found, that number will be returned
        if i not in nums:
            return i
print(find_missing_number([1,2,3,5,6,7]))



def remove_duplicates(s):
    result = ""
    for char in s:             #loop through a string(word) to check if there is a character that is repeated within the word
        if char not in result: #if the character is not duplicated, then it will return the entire word as it is...
            result += char      #but for duplicated characters, it will be returned only once
    return result
print(remove_duplicates("Sinenhlanhla"))


def first_non_repeating_char(s):
    for char in s:              #loop through a string(word) to locate a character which is only used once in a word...
        if s.count(char) == 1:  #if found, then only that character will be returned , 
            return char
    return None                 #if not found then nothing will be returned
print(first_non_repeating_char("Penelope"))
    