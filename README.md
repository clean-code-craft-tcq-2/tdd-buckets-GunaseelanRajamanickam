# Test Driven Ranges

The charging current varies during the process of charging.
We need to capture the range of current measurements -
what range of currents are most often encountered while charging.

> **DO NOT** jump into implementation! Read the example and the starting task below.

## Example

### Input

A set of periodic current samples from a charging session,
as an array of integers. For example:
`3, 3, 5, 4, 10, 11, 12`

### Functionality

The continuous ranges in there are: `3,4,5` and `10,11,12`.

The task is to detect the ranges and
output the number of readings in each range.

In this example,

- the `3-5` range has `4` readings
- the `10-12` range has `3` readings.

### Output

The expected output would be in comma-separated (csv format):

```
Range, Readings
3-5, 4
10-12, 3
```

## Tasks

Establish quality parameters: 

- What is the maximum complexity (CCN) per function? 3 CCN and create corresponding yml in the `.github/workflows` folder
- How many lines of duplicate code will you tolerate? 3 the number of lines and create corresponding yml in the `.github/workflows` folder
- Ensure 100% line and branch coverage at every step. Include the coverage yml in the workflows.

Adapt/adopt/extend the `yml` files from one of your previous workflow folders.

Start Test-driven approach

1. Write the smallest possible failing test: give input `4,5`. assert output to be `4-5, 2`.
1. Write the minimum amount of code that'll make it pass.
1. Refactor any assumptions, continue to pass this test. Do not add any code without a corresponding test.

# Test Specification
### 1. Create a simple range detection with a method:
```
infers_readings(readings)
```
The method can take up to two numbers, separated by commas, and will return their range.
For example `""` or `"3"` or `"4,5"` as inputs.
For an empty string it will return False.

### 2. Allow the infers_readings method to handle an unknown amount of numbers.

### 3. Allow the infers_readings method to handle unsorted readings:
The following input is ok: `"3, 3, 5, 4, 10, 11, 12"` (will equal `"3, 3, 4, 5, 10, 11, 12"`)

### 4. Allow the infers_readings method to detect ranges in readings: To detect a range, 
##### 4.1. Find the differences of increasing values in list. Like `(3-3),(4-3), ..` If the difference is <=1, then it will be part of a range:
(Also, insert a 0 in the front, just to account for the 1st element and make the obtained list’s length equal to original list) 
```
diff = [j-i for i, j in zip(readings[:-1], readings[1:])]
diff.insert(0, 0)
```

##### 4.2. Now get positions in above list where difference is >= 2. This is to detect the ranges:
(Again, insert a 0 in the front, just to account for the 1st element, and make sure it gets picked in range detection)
```
ind = [i for i,v in enumerate(diff) if v >= 2]
ind.insert(0, 0)
```

##### 4.3. Group the elements together that will form ranges, using the ind list obtained:
```
groups = [readings[i:j] for i,j in zip(ind, ind[1:]+[None])]
```

### 5. Support infers_readings method to convert the range in csv format:
For example, `3-5, 4`

### 6. Support infers_reading method to print the formatted string in console


