from typing import Optional
# Integer type
def calculate_square_area(side_length: int) -> int:
   return side_length ** 2
# Float type
def calculate_circle_area(radius: float) -> float:
   return 3.14 * radius * radius
# String type
def greet(name: str) -> str:
   return f"Hello, {name}"
# Boolean type
def is_adult(age: int) -> bool:
   return age >= 18
# None type
def no_return_example() -> None:
   print("This function does not return anything")
# Optional type (Union of int or None)
def safe_divide(x: int, y: Optional[int]) -> Optional[float]:
   if y is None or y == 0:
      return None
   else:
      return x / y
# Example usage
print(calculate_square_area(5))
print(calculate_circle_area(3.0))
print(greet("Alice"))
print(is_adult(22))
no_return_example()
print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide(10, None))

# collectionTypes
from typing import List, Tuple, Dict, Set, Iterable, Generator
# List of integers
def process_numbers(numbers: List[int]) -> List[int]:
   return [num * 2 for num in numbers]
# Tuple of floats
def coordinates() -> Tuple[float, float]:
   return (3.0, 4.0)
# Dictionary with string keys and integer values
def frequency_count(items: List[str]) -> Dict[str, int]:
   freq = {}
   for item in items:
      freq[item] = freq.get(item, 0) + 1
   return freq
# Set of unique characters in a string
def unique_characters(word: str) -> Set[str]:
   return set(word)
# Iterable of integers
def print_items(items: Iterable[int]) -> None:
   for item in items:
      print(item)
# Generator yielding squares of integers up to n
def squares(n: int) -> Generator[int, None, None]:
   for i in range(n):
      yield i * i
# Example usage
numbers = [1, 2, 3, 4, 5]
print(process_numbers(numbers))
print(coordinates())
items = ["apple", "banana", "apple", "orange"]
print(frequency_count(items))
word = "hello"
print(unique_characters(word))
print_items(range(5))
gen = squares(5)
print(list(gen))

# optional types
from typing import Optional
def divide(a: float, b: float) -> Optional[float]:
   if b == 0:
      return None
   else:
      return a / b
result1: Optional[float] = divide(10.0, 2.0)   # result1 will be 5.0
result2: Optional[float] = divide(10.0, 0.0)   # result2 will be None
print(result1)
print(result2)

# any types
from typing import Any
def print_value(value: Any) -> None:
   print(value)
print_value(10)
print_value("hello")
print_value(True)
print_value([1, 2, 3])
print_value({'key': 'value'})