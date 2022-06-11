# Week 2 session 2

# Prompt:
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You   may assume that the majority element always exists in the array.

# Undestand:
# Can we have edge cases: yes
# Is time or space complexity more important: space

# Plan:
# Given an array of numbers
# Loop through the array
# if element is not in the hashmap, we add it, make reps=1
# if element is in the hashmap, we increment reps
# select highest reps, compare it with n/2, return if reps > n/2

# EG:
# Hashmap: 2 -> reps
#          3 -> reps


def is_maj_ele(num_list):
    map = {}

    for i in num_list:
        # if i in map:
        if i in map:
            map[i] = map[i] + 1
            if map[i] >=len(num_list)/2:
              return i   
        else:
            map[i] = 1

    


def main():
  #num_list = [3, 2, 3] #-> passed
  num_list = [2,2,1,1,1,2,2]
  # num_list = [1, 2, 3, 3, 3, 1] -> passed
  # num_list = [0,0,0,0,0,0,0,0] -> passed 
  # num_list = [None, None, None, None, None] 
  # num_list = [0,0,00,00,00,00,00,00] 
  # num_list = None
  # num_list = [1]
  # num_list = [9999999999, 9999999999, 9999999999,9999999999, 2, 3,4 2] 
 
  print("num_list: " + str(num_list))
  print("is_maj_ele(num_list): " + str(is_maj_ele(num_list)))


if __name__ == '__main__': main()
