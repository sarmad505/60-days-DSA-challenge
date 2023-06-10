#!/usr/bin/env python
# coding: utf-8

# # Two Sum Easy
# Given an array of integers nums and an integer target , return indices
# of the two numbers such that they add up to target
# You may assume that each input would have exactly one solution, and
# you may not use the same element twice.
# You can return the answer in any order.



 




def arrSum(target,list):
    for i in list:
        for j in list:
            
            if i+j == target:                
                return list.index(i) , list.index(j)
        
        


list = [9,3,4,5,1,7]
print(list)
print("Index of sum of target values are")
print(arrSum(19,list))
        


# In[ ]:




