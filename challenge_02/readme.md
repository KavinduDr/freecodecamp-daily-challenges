# Base Check

Given a string representing a number and an integer base from 2 to 36, determine whether the number is valid in that base.

## Problem Statement

- The string may contain digits and uppercase or lowercase letters.
- The check should be **case-insensitive**.
- The base can be any integer from **2 to 36**.
- A number is **valid** if every character is a valid digit in the given base.

## Valid Digits by Base

- **Base 2:** 0-1
- **Base 8:** 0-7
- **Base 10:** 0-9
- **Base 16:** 0-9, A-F
- **Base 36:** 0-9, A-Z

## Example

| Input         | Base | Output |
|---------------|------|--------|
| `"1011"`      | 2    | True   |
| `"1A3F"`      | 16   | True   |
| `"GHI"`       | 16   | False  |
| `"abc"`       | 12   | True   |
| `"5G3F8F"`    | 17   | True   |

## Usage

See [`is_valid_number`](challenge_02/base_check.py) in [base_check.py](challenge_02/base_check.py):

```python
print(is_valid_number('ABC', 20))      # True
print(is_valid_number('5G3F8F', 17))   # True
```

## Solution

See [base_check.py](challenge_02/base_check.py) for the implementation.