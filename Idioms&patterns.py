# Different comprehensions

# List comprehension
list_comprehension = [x for x in range(0, 5)]

# Set comprehension
set_comprehension = {x for x in range(0, 5)}

# Dictionary comprehension
dict_comprehension = {x: x for x in range(0, 5)}

# Tuple comprehension
tuple_comprehension = tuple(x for x in range(0, 5))

# Generator expression
gen_expression = (x for x in range(0, 5))

print("Different comprehension: "
      "- list comprehension {}"
      "- set comprehensin {}"
      "- dictionary comprehension {}"
      "- tuple comprehension {}".format(list_comprehension, set_comprehension, dict_comprehension, tuple_comprehension))

# Generator expression example
data = [x for x in range(0, 10)]

# We've got list of numbers in range 0-10
print(data)

for x in data:
    print(x)
    if x == 3:
        break

print(x)

# When we use in this code generator...
data = (x for x in range(0, 10))

# We've got generator
print(data)

for x in data:
    print(x)
    if x == 6:
        break

# As result we've got 7,8,9 - why?
# Because generator expression executes one's and forget about it
print(list(data))

# Usage of generator epression
result = (x for x in range(0, 5))

# It prints next value till the end
print(next(result))

# While loop

data = ['styczeń', 'luty', 'marzec', 'kwiecień']

i = 0

while i < len(data):
    month = data[i]
    print(i, month)
    i += 1

# Enumerate:
for i, month in enumerate(data, start=1):
    print(i, month)

# Enumerate dict
result = {}
for i, month in enumerate(data, start=1):
    result[i] = month

print(result)

# Enumerate dict2
result_2 = {i: mth for i, mth in enumerate(data, start=1)}
print(result_2)

# Zfill function:
i = 1
month = 'styczeń'

f'{i}'.zfill(2)  # fill free places with zeros

# Enumerate 3 with formatted i
result_3 = {f'{i:02d}': mth for i, mth in enumerate(data, start=1)}
print(result_3)

# Enumerate 4:
i = 2
f'{i:02d}'

# Dict comprehension: reverse value with key
temp = {}
data = {'a': 1, 'b': 2, 'c': 3}

for key, value in data.items():
    temp[value] = key

print(temp)

# OR
temp2 = {v: k for k, v in data.items()}
print(temp2)

# After loop, x become last value:
DATA = [1, 2, 3]

for x in DATA:
    print(x)

print(x)
del (x)
# With list comprehension last value doesn't stay in memory:
[x for x in range(0, 5)]
# print(x)


#
DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor')]

headline = DATA[0]
data = DATA[1:]

# print(headline)
# print(data)

headline, *data = DATA

# Filtering values:
setosa_val = [features for *features, label in DATA if label == 'setosa']
print(setosa_val)

# Unpacking
a, *b, c = 1, 2
print(a, b, c)

for measurements, *label in data:
    print(label)


#FUnction that prints measurements for every species:

def function(data, specific_species):
    result = []
    for *measurements, species in data:
        if specific_species == species:
            result.append(measurements)
    return result


fun = function(data, 'species')


#Function that prints measurements for the species - usage of generator:
def generator(data, specific_species):
    for *measurements, species in data:
        if species == specific_species:
            yield measurements


gen = generator(data, 'setosa')

#Printing generator
print(gen)
#Printing values
print(next(gen))

#Let's compare size of both function: genrator is twice bigger than fun....
import sys

print(sys.getsizeof(gen))
print(sys.getsizeof(fun))

#but when we increase number of data:

fun_big = function(data*10000, 'species')
gen_big = generator(data*10000, 'setosa')


print(sys.getsizeof(gen_big))
print(sys.getsizeof(fun_big))


