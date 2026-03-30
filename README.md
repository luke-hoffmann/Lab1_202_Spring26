# Lab 1: Python Review

## Overview

This lab is a structured review of core Python programming concepts with an emphasis on **code quality, type hints, and validation**. You are expected to already be comfortable with Python at the level of CSC 101.

The purpose of this lab is to establish **coding standards** that will be used throughout the course.

In particular, this lab focuses on:

- Writing clear and well-typed function interfaces
- Understanding the role and limitations of type hints
- Implementing basic algorithms with proper structure
- Validating inputs where appropriate
- Writing simple test cases, including failure cases
- Improving class design using `@dataclass`

> **Important:** Python type hints are not enforced at runtime. They are a tool for readability and static analysis, not a substitute for correct logic or validation.

---

## Submission and Signoff

This lab will be checked through **oral signoff**.

When you are finished:

1. Ensure all tasks are complete and clearly written.
2. Be prepared to explain your code and design decisions.
3. Go to the professor or TA for **signoff**.
4. Submit your **signoff sheet**.

You may be asked to explain:
- Your use of type hints
- Your input validation decisions
- Your test cases
- Edge cases in your implementations

---

## Coding Expectations

All code in this lab should:

- Use **type hints** in function headers
- Use meaningful variable and function names
- Follow consistent formatting
- Avoid hard-coded or special-case logic
- Handle edge cases where appropriate
- Be written for clarity, not just correctness

---

# Task 1: Type Aliases

## Goal
Define meaningful **type aliases** to improve code readability and express intent. A type alias gives a descriptive name to an existing type.

### 1.a — Average
Define a type alias representing an **average value**.
- This should reflect a numeric value that may include decimals.

### 1.b — Sequence of Names
Define a type alias representing a **sequence of names**.
- Each name should be a string.
- The sequence should preserve order.

### 1.c — Population Count
Define a type alias representing a **population count**.
- This should represent a whole number quantity.

### 1.d — Sequence of Stock Prices
Define a type alias representing a **sequence of stock prices over time**.
- Each price should be numeric.
- The sequence should preserve order.

---

# Task 2: Linear Search with Type Checking

## Goal
Implement a linear search function using proper type hints and thoughtful input handling. Make sure the input is a list and each element is an int.

### Required Function Header
```python
def linear_search(values: list[int], target: int) -> int:
    """Search through the list and return the index of the first occurrence."""
    ...
```

### Expected Behavior
- Search through the list from left to right.
- Return the **index** of the first occurrence of `target`.
- Return `-1` if the target is not found.

### Additional Requirements
- Consider whether you need to validate inputs.
- If validation is included, it should be consistent and justified.
- Do not assume inputs are always correct.


---

# Task 3: Convert a Class to a Dataclass

## Goal
Refactor an existing class into a `@dataclass`.

### Instructions
You will be given a class definition. Your task is to:
- Convert it into a dataclass using the `@dataclass` decorator.
- Preserve the original structure and intent.
- Remove unnecessary boilerplate (like `__init__`) where appropriate.

### Requirements
- Maintain all fields.
- Ensure type hints are present for all attributes.
- Do not change the logical meaning of the class.

---

# Task 4: Testing Merge of Two Sorted Lists

## Goal
Write comprehensive test cases for a function that merges two sorted lists into one single sorted list.

### Instructions
- Create a suite of tests that cover typical use cases.
- Include **edge cases** (e.g., empty lists, lists of different lengths).
- Include **assertException* for non-list inputs.
