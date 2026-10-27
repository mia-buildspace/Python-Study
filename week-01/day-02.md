# Day 02: Numbers and Strings

## 1. Number Data Type

A number is a value used for calculations.

숫자형(Number)은 숫자를 나타내는 자료형이다.

### 1.1 Integer

An integer is a whole number. It has no decimal part.

정수(Integer)는 소수점이 없는 숫자다.

```python
a = 145
b = -134
c = 0
```

### 1.2 Floating-Point Number

A floating-point number is a number with a decimal point.

실수형(Floating-point)은 소수점을 포함하는 숫자를 나타낸다.

```python
a = 2.14
b = -2.13
c = 4.24e10
d = 4.24e-10
```

Python uses `e` or `E` to write numbers in scientific notation.

- `4.24e10` means `4.24 × 10¹⁰`.
- `4.24e-10` means `4.24 × 10⁻¹⁰`.

### 1.3 Octal and Hexadecimal

Python supports octal and hexadecimal numbers.

Python은 8진수와 16진수도 지원한다.

**Octal (8진수)**

An octal number starts with `0o` or `0O`.

```python
a = 0o177
b = 0o25
```

**Hexadecimal (16진수)**

A hexadecimal number starts with `0x` or `0X`.

```python
a = 0x8ff
b = 0xABC
```

These numbers are useful in some programming tasks, but beginners do not need to use them often.

### 1.4 Complex Number

A complex number has a real part and an imaginary part.

복소수(Complex number)는 실수 부분과 허수 부분으로 이루어진 숫자다.

Python uses `j` to represent the imaginary unit.

```python
a = 1 + 2j
b = 3 - 4j
```

You can access the parts of a complex number using attributes and methods.

**Real part**

```python
a = 1 + 2j
print(a.real)
```

Output:

```text
1.0
```

`real` returns the real part.

**Imaginary part**

```python
print(a.imag)
```

Output:

```text
2.0
```

`imag` returns the imaginary part.

**Complex conjugate**

```python
print(a.conjugate())
```

Output:

```text
(1-2j)
```

`conjugate()` returns the complex conjugate.

**Absolute value**

```python
print(abs(a))
```

Output:

```text
2.23606797749979
```

`abs()` returns the absolute value. For a complex number, it calculates the distance from zero.

### 1.5 Arithmetic Operators

Arithmetic operators are used for calculations.

산술 연산자(Arithmetic operators)는 계산할 때 사용한다.

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division | `5 / 2` | `2.5` |
| `**` | Exponentiation | `2 ** 3` | `8` |
| `%` | Modulo (remainder) | `5 % 2` | `1` |
| `//` | Floor division | `5 // 2` | `2` |

`//` returns the floor of the division result. For positive numbers, this removes the decimal part.

`//`는 나눗셈 결과에서 소수점 아래를 버리는 연산자로 배울 수 있다. 정확하게는 결과보다 크지 않은 가장 큰 정수를 반환하므로, 음수에서는 단순히 소수점 아래를 자르는 것과 다를 수 있다.

```python
print(5 // 2)    # 2
print(-5 // 2)   # -3
```

---

## 2. String Data Type

A string is a sequence of characters.

문자열(String)은 문자들이 이어진 데이터다.

Strings can contain letters, numbers, spaces, and symbols.

```python
a = "Hello World"
b = "a"
c = "123"
```

Even `"123"` is a string because it is inside quotation marks.

`"123"`은 따옴표로 감싸져 있으므로 숫자형이 아니라 문자열이다.

## 2.1 Creating Strings

Python supports single quotes, double quotes, and triple quotes.

Python에서는 작은따옴표, 큰따옴표, 세 개의 따옴표를 사용해 문자열을 만들 수 있다.

**Single quotes**

```python
a = 'Hello World'
```

**Double quotes**

```python
a = "Hello World"
```

**Triple quotes**

Triple quotes are useful for creating strings that contain multiple lines.

세 개의 따옴표는 여러 줄로 된 문자열을 만들 때 유용하다.

```python
a = """Life is too short.
You need Python."""
```

You can use either three single quotes or three double quotes.

```python
a = '''Hello
Python'''
```

## 2.2 Using Quotes Inside Strings

You can use double quotes around a string that contains a single quote.

문자열 안에 작은따옴표가 있다면 큰따옴표로 감쌀 수 있다.

```python
food = "I'm hungry."
```

You can also use single quotes around a string that contains double quotes.

```python
say = 'He said, "Python is easy."'
```

You can use a backslash (`\`) to include quotation marks inside a string.

```python
say = "\"Python is very easy,\" he says."
```

A backslash can change how the next character is interpreted.

백슬래시(`\`)는 뒤에 오는 문자가 특별한 의미를 갖도록 할 때 사용한다.

## 2.3 Escape Sequences

Escape sequences are special character combinations used inside strings.

이스케이프 시퀀스(Escape sequences)는 문자열 안에서 줄 바꿈이나 탭 같은 특별한 동작을 표현하는 문자 조합이다.

| Escape sequence | Meaning |
|---|---|
| `\n` | New line (줄 바꿈) |
| `\t` | Tab (탭 간격) |
| `\\` | Backslash (`\`) |
| `\'` | Single quote (`'`) |
| `\"` | Double quote (`"`) |

Example:

```python
text = "Life is too short\nYou need Python"
print(text)
```

Output:

```text
Life is too short
You need Python
```

## 2.4 String Concatenation

Concatenation means joining strings together.

문자열 연결(Concatenation)은 여러 문자열을 하나로 이어 붙이는 것이다.

You can use the `+` operator.

```python
head = "Python "
tail = "is fun!"

print(head + tail)
```

Output:

```text
Python is fun!
```

## 2.5 Repeating Strings

You can use the `*` operator to repeat a string.

`*` 연산자를 사용하면 문자열을 반복할 수 있다.

```python
a = "Python"
print(a * 2)
```

Output:

```text
PythonPython
```

Example: Creating a simple title.

```python
print("=" * 30)
print("My Program")
print("=" * 30)
```

Output:

```text
==============================
My Program
==============================
```

---

## 3. String Indexing and Slicing

Indexing and slicing let you access parts of a string.

인덱싱(Indexing)은 특정 위치의 문자를 가져오는 것이고, 슬라이싱(Slicing)은 문자열의 일부를 잘라 가져오는 것이다.

Let's use this string:

```python
a = "Life is too short, You need Python"
```

### 3.1 Indexing

Python starts counting string positions from `0`.

Python은 문자열의 위치를 `0`부터 센다.

| Character | Index |
|---|---:|
| `L` | `0` |
| `i` | `1` |
| `f` | `2` |
| `e` | `3` |
| Space | `4` |

You can access a character using square brackets.

```python
print(a[3])
```

Output:

```text
e
```

**Negative indexing**

Negative indexes count from the end of the string.

음수 인덱스는 문자열의 뒤에서부터 센다.

```python
print(a[-1])  # n
print(a[-5])  # y
print(a[-0])  # L
```

`a[-0]` is the same as `a[0]` because `-0` equals `0`.

### 3.2 Slicing

Slicing extracts part of a string.

슬라이싱은 문자열에서 원하는 부분을 가져오는 방법이다.

```python
a = "Life is too short, You need Python"

print(a[0:4])
```

Output:

```text
Life
```

The basic syntax is:

```python
string[start:end]
```

- `start`: The index where the slice begins.
- `end`: The index where the slice stops.
- The character at `end` is not included.

시작 위치는 포함하지만 끝 위치는 포함하지 않는다.

For example:

```python
print(a[0:3])
```

Output:

```text
Lif
```

**Useful slicing examples**

```python
print(a[0:5])    # Life 
print(a[19:])    # You need Python
print(a[:17])    # Life is too short
print(a[:])      # The entire string
print(a[19:-7])  # You need
```

You can leave out the start or end index.

- `a[19:]`: From index 19 to the end.
- `a[:17]`: From the beginning to index 16.
- `a[:]`: The entire string.

### 3.3 Splitting a String with Slicing

You can use slicing to separate parts of a string.

슬라이싱으로 문자열의 일부를 나눠서 각각의 변수에 저장할 수 있다.

```python
a = "20010331Rainy"

date = a[:8]
weather = a[8:]

print(date)
print(weather)
```

Output:

```text
20010331
Rainy
```

---

## 4. String Formatting

String formatting means putting values into a string.

문자열 포매팅(String formatting)은 문자열 안에 원하는 값을 넣는 방법이다.

For example, you can change the temperature in a message without rewriting the entire string.

```python
temperature = 20
print("The temperature is %d degrees." % temperature)
```

Output:

```text
The temperature is 20 degrees.
```

### 4.1 Using `%` Formatting

You can use `%d` for an integer and `%s` for a string.

```python
print("I eat %d apples." % 3)
print("I eat %s apples." % "five")
```

Output:

```text
I eat 3 apples.
I eat five apples.
```

You can also use a variable.

```python
number = 3
print("I eat %d apples." % number)
```

### 4.2 Formatting Multiple Values

Use a tuple to insert two or more values.

두 개 이상의 값을 넣으려면 `%` 뒤에 괄호를 사용하고, 각 값을 쉼표로 구분한다.

```python
number = 10
day = "three"

print("I ate %d apples. I was sick for %s days." % (number, day))
```

Output:

```text
I ate 10 apples. I was sick for three days.
```

### 4.3 Format Codes

| Format code | Meaning |
|---|---|
| `%s` | String |
| `%c` | A single character |
| `%d` | Integer |
| `%f` | Floating-point number |
| `%o` | Octal number |
| `%x` | Hexadecimal number |
| `%%` | A literal percent sign (`%`) |

### 4.4 Alignment and Spaces

You can control the width and alignment of a string.

문자열이 차지할 공간의 길이와 정렬 방향을 지정할 수 있다.

```python
print("%10s" % "hi")
```

Output:

```text
        hi
```

`%10s` reserves a width of 10 characters and right-aligns the text.

Use `-` for left alignment.

```python
print("%-10sjane." % "hi")
```

Output:

```text
hi        jane.
```

### 4.5 Decimal Places

You can control the number of decimal places.

소수점 아래에 표시할 자리 수를 지정할 수 있다.

```python
print("%.4f" % 3.42134234)
```

Output:

```text
3.4213
```

`%.4f` displays four digits after the decimal point.

You can also specify the total width.

```python
print("%10.4f" % 3.42134234)
```

Output:

```text
    3.4213
```

`%10.4f` means a total width of 10 characters, with 4 digits after the decimal point.

### 4.6 Modern Formatting with f-Strings

Python also supports f-strings, which are often easier to read.

Python에서는 f-string도 많이 사용한다. 변수 이름을 문자열 안에 직접 넣을 수 있어 편리하다.

```python
number = 3
print(f"I eat {number} apples.")
```

Output:

```text
I eat 3 apples.
```

You do not need to memorize every formatting method today. First, understand how `%` formatting works, then practise using f-strings.

---

## 5. String Methods

A method is a function associated with an object.

메서드(Method)는 객체에 연결되어 있는 함수다.

Python provides many string methods for counting, searching, changing, and splitting strings.

Python은 문자열을 세고, 검색하고, 변환하고, 나누는 데 사용할 수 있는 여러 메서드를 제공한다.

### 5.1 `count()`

`count()` returns the number of times a substring appears.

문자열 안에서 특정 문자가 몇 번 나타나는지 반환한다.

```python
a = "hobby"
print(a.count("b"))
```

Output:

```text
2
```

### 5.2 `find()`

`find()` returns the index of the first occurrence of a substring.

문자열에서 특정 문자가 처음 나타나는 위치를 반환한다.

```python
a = "Python is best choice"

print(a.find("b"))
print(a.find("k"))
```

Output:

```text
10
-1
```

If the substring does not exist, `find()` returns `-1`.

### 5.3 `index()`

`index()` also returns the index of the first occurrence of a substring.

`index()`도 특정 문자열이 처음 나타나는 위치를 반환한다.

```python
a = "Life is too short"

print(a.index("t"))
```

Output:

```text
8
```

If the substring does not exist, `index()` raises a `ValueError`.

```python
a = "Life is too short"
print(a.index("k"))
```

This code raises an error because `"k"` is not in the string.

**Difference between `find()` and `index()`:**

- `find()`: Returns `-1` if the substring is not found.
- `index()`: Raises a `ValueError` if the substring is not found.

### 5.4 `join()`

`join()` inserts a string between the characters or items in an iterable.

`join()`은 여러 문자열 사이에 특정 문자열을 삽입한다.

```python
separator = ","
print(separator.join("abcd"))
```

Output:

```text
a,b,c,d
```

The string `","` is inserted between each character.

### 5.5 `upper()` and `lower()`

`upper()` converts letters to uppercase.

`upper()`는 영문자를 대문자로 바꾼다.

```python
a = "hi"
print(a.upper())
```

Output:

```text
HI
```

`lower()` converts letters to lowercase.

```python
a = "HI"
print(a.lower())
```

Output:

```text
hi
```

### 5.6 `lstrip()`, `rstrip()`, and `strip()`

These methods remove whitespace from strings.

이 메서드들은 문자열의 양끝에 있는 공백을 제거한다.

```python
a = "    hi    "

print(a.lstrip())  # "hi    "
print(a.rstrip())  # "    hi"
print(a.strip())   # "hi"
```

- `lstrip()`: Removes whitespace from the left.
- `rstrip()`: Removes whitespace from the right.
- `strip()`: Removes whitespace from both sides.

By default, these methods remove whitespace at the edges, not spaces in the middle.

### 5.7 `replace()`

`replace()` replaces one substring with another.

`replace()`는 문자열의 특정 부분을 다른 문자열로 바꾼다.

```python
a = "Life is too short"
print(a.replace("Life", "Your leg"))
```

Output:

```text
Your leg is too short
```

### 5.8 `split()`

`split()` splits a string into a list.

`split()`은 문자열을 나눠 리스트(List)로 반환한다.

By default, `split()` separates a string at whitespace.

```python
a = "Life is too short"
print(a.split())
```

Output:

```text
['Life', 'is', 'too', 'short']
```

You can also specify a separator.

```python
a = "a:b:c:d"
print(a.split(":"))
```

Output:

```text
['a', 'b', 'c', 'd']
```

---

## 6. Key Points to Remember

- **Integer**: A whole number.
- **Floating-point number**: A number that can have a decimal part.
- **Complex number**: A number with real and imaginary parts.
- **String**: A sequence of characters.
- **Indexing**: Accessing a character by its position.
- **Slicing**: Extracting part of a string.
- **String formatting**: Putting values into a string.
- **Method**: A function associated with an object.
- **`find()` vs. `index()`**: `find()` returns `-1` when a substring is not found; `index()` raises an error.
- **`split()`**: Splits a string into a list.
- **`join()`**: Joins items together using a separator.

## 7. Practice

Try to solve these problems without looking at the examples above.

### Exercise 1: Numbers

```python
a = 17
b = 5

# Print the sum of a and b.
# Print the remainder when a is divided by b.
# Print the result of a divided by b, without the decimal part.
```

### Exercise 2: String Indexing

```python
text = "Python is fun"

# Print the first character.
# Print the last character.
# Print the character at index 7.
```

### Exercise 3: String Slicing

```python
text = "Hello Python"

# Print "Hello".
# Print "Python".
# Print the entire string.
```

### Exercise 4: String Formatting

```python
name = "Mia"
age = 24

# Print: My name is Mia and I am 24 years old.
```

### Exercise 5: String Methods

```python
text = "  hello python  "

# Convert the string to uppercase.
# Remove whitespace from both sides.
# Replace "python" with "world".
# Split "apple,banana,orange" at each comma.
```

Try writing your answers in `day-02.py`. Keep the explanations in `day-02.md` and use the Python file to practise writing and running code.
