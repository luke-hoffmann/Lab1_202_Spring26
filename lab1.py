"""
Lab 1: Python Review
Core Python programming concepts, code quality, type hints, and validation.
"""

from typing import TypeAlias
from dataclasses import dataclass
# ==========================================
# Task 1: Type Aliases
# ==========================================
# comment for part 1 here: 
Average: TypeAlias = float
NameSequence: TypeAlias = list[str]
PopulationCount: TypeAlias = int
StockPriceSequence: TypeAlias = list[float]
InventoryRecord: TypeAlias = dict[int,str]
# ==========================================
# Task 2: Linear Search with Type Checking
# ==========================================

def linear_search(values: list[int], target: int) -> int:
    """
    Search through the list from left to right.
    Returns the index of the first occurrence of target, or -1 if not found.
    """
    # Validate target to be an integers
    if (not isinstance(target,int)): raise TypeError
    
    # Validate values to be a list of integers
    if (not isinstance(values, list)): raise TypeError
    
    # Loop through values 
    #   If value is not an int throw type error
    #   If value equals target return index
    #   Else continue
    for i, value in enumerate(values):
        if (not isinstance(values[i],int)): raise TypeError
        if (value == target): return i
        
    # Return -1 if no match was found in the loop
    return -1


# ==========================================
# Task 3: Convert a Class to a Dataclass
# ==========================================

# ORIGINAL CLASS (for reference):
# class Student:
#     def __init__(self, name: str, id_number: int, gpa: float):
#         self.name = name
#         self.id_number = id_number
#         self.gpa = gpa

@dataclass
class Student:
    name: str
    id_number: int
    gpa : float



# ==========================================
# Task 4: Testing Merge of Two Sorted Lists
# ==========================================

def merge_sorted_lists(list1: list[int], list2: list[int]) -> list[int]:
    """
    Merges two sorted lists of integers into a single sorted list.
    """
    # Validation: Raise TypeError for non-lists
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("Both arguments must be lists.")

    merged = []
    i, j = 0, 0

    # Two-pointer approach to merge
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    # Append any remaining elements
    merged.extend(list1[i:])
    merged.extend(list2[j:])

    return merged



def min(arr: list[int])->int:
  if len(arr) ==0: raise IndexError
  return min_recursive(arr,arr[0],0)  
def min_recursive(arr: list[int],min: int, i: int)->int:
  if len(arr) ==0: raise IndexError
  if i>= len(arr): return min
  if arr[i] <= min: min = arr[i]
  return min_recursive(arr,min,i+1)  

print(min([0,1,2,3,4,5,6,7,-10,2,5,-4,1251]))


# 9. Merging Sorted Lists
# Write a function merge_sorted_lists(list1, list2) that takes two sorted lists of integers and returns a single, combined sorted list.
# Constraint: You may not simply concatenate the lists and call .sort(). You must iterate through the lists and build the new list in order.

def merge_sorted_lists(l1: list[int], l2: list[int]):
    return merge_sorted_lists_recursive(l1,l2,0,0,[])
    
def merge_sorted_lists_recursive(l1: list[int], l2: list[int], l1Index: int, l2Index: int, newList: list[int])->list[int]:
    if (not (l1Index >= len(l1)) and l1[l1Index] < l2[l2Index]): 
        newList.append(l1[l1Index])
        return merge_sorted_lists_recursive(l1,l2,l1Index+1,l2Index,newList)
    elif not (l2Index >= len(l2)):
        newList.append(l2[l2Index])
        return merge_sorted_lists_recursive(l1,l2,l1Index,l2Index+1,newList)
    return newList
    
print(merge_sorted_lists([0,2,4,6,8,10,11],[0,1,2,3,4,5,6,7,8,9,10,11,12]))


# You are given a list of stock prices where the index represents the day, and the value represents the price of the stock on that day. Write a function max_profit(prices) that calculates the maximum profit you can achieve by buying on one day and selling on a future day.
# • Constraint: You cannot sell a stock before you buy it. If no profit can be made, return 0.


stock_prices = [10,4,20,19,18,10,5,1,10,11,30]

def max_profit(prices: list[int])->int:
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            profit = prices[j] -prices[i]
            if max_profit < (profit) :
                max_profit = profit
    return max_profit                
            
print(max_profit(stock_prices))
        