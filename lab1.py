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

