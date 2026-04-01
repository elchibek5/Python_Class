# 1. String Concatenation
mystr = 'yes'
mystr += 'no'
mystr += 'yes'
print(f"1. Output: {mystr}")

# 2. String Repetition
mystr = 'abc' * 3
print(f"2. Output: {mystr}")

# 3. Counting Lowercase Characters
mystring = "Example String with LOWER and lower"
count = 0
for char in mystring:
    if char.islower():
        count += 1
print(f"3. Lowercase count: {count}")

# 4. Splitting a String
mystring = 'cookies>milk>fudge>cake>ice cream'
my_list = mystring.split('>')
print(f"4. Split list: {my_list}")

# 5. Symmetric Difference of Sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = set1.symmetric_difference(set2)
print(f"5. Elements not shared: {set3}")

# 6. Dictionary Key Lookup
dct = {'James': '555-1212', 'Alice': '555-1313'}
print("6. James Search:")
if 'James' in dct:
    print(dct['James'])
else:
    print("Key not found.")

# 7. Dictionary Key Deletion
dct['Jim'] = 'Delete Me'
if 'Jim' in dct:
    del dct['Jim']
print(f"7. Jim deleted. Dictionary state: {dct}")