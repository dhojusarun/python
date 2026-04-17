# #snake case
# #camel case (firstArray)
# #first_array
# a = 5.2 #loose typing/dynamic typing
# a: int = 5 #strict typing/static typing
# PI = 3.14 #constant variable
# b = 9.0


# a = 5.4
# b = 4.5
# # arithmetic operations j
# print (a + b) #sum
# print (a - b) #subtract
# print (a * b) #multiply
# print (a / b) #divide
# print (a // b) #floor division (gives only the whole number part of the division)
# print (a % b) #modulus
# print (a ** b) #exponentation / power of

# #string (array of characters) operations
# s = "Hello world"
# #indexing (kunai pani value ko euta specfic position nikalne)

# print (s[0]) #first character
# print (s[5]) #space
# print (s[6]) #7th character
# print (s[-1]) #last character

# #slicing (kunai pani value ko euta specfic position bata aru position samma nikalne)
# print (s[0:5]) #first 5 characters
# print (s[6:]) #from 7th character to end
# print (s[:5]) #from start to 5th character
# print (s[::2]) #every second character

# print (type(s)) #string ko type
# print (s.upper()) #convert to uppercase

# print (s.capitalize()) #capitalize first character
# print (s.startswith("H")) #check if string starts with "H"
# print (s.endswith("d")) #check if string ends with "d"
# s.split(" ") #split by space
# s.find("o")#finds the first occurrence of something
# s.replace("o", "a") #replace something

# l1 = [1, 2, 3, 4, 5] #list declaration
# print (l1[0])#first element of list
# #print (l1[6])#this will give error
# print (l1[1:4])#elements from index 1 to 3
# print (type(l1))
# l1.append(6) #add element to end of list
# print(l1)

# l2 = [102,150,160]
# l1.append(l2)
# print(l1)

# l1.extend(l2) #add elements of l2 to l1
# print(l1)

# print (l1*3)
# s = "hello"
# print (s*4)

# l1.pop() #removes last element of list
# l1.reverse() #reverses the list
# l1.sort() #sorts the list in ascending order


# # string concatenation
# s1 = "Sarun"
# s2 = "Dhoju"
# age = 21
# print("Hello, my name is " + s1 + " " + s2) #string concatenation
# print("Hello, my name is " +s1 + " " +s2 + " I am " + str(age) + "years old") #string concatenation with variables


# #string formatting
# print("Hello, my name is %s %s. I am %d years old" % (s1, s2, age)) #string formatting with % operator

# #f-string
# print("Hello, my name is {} {}. I am {} years old".format(s1, s2, age)) #string formatting with format method
# print(f"Hello, my name is {s1} {s2}. I am {age} years old") #string formatting with f-strings


# for loop
l = [1, 2, 34, 3, 6, 0]
# output = []
# for i in l:
#     if i<3:
#         output.append(i*2)
#     else:
#         output.append(i*3)
#     output.append(i*2)
#     print(output)

output = [i * 2 if i < 3 else i * 3 for i in l]  # list comprehension

print(output)

# dictionary - key of words and values
d = {
    "name": "Sarun",
    "age": 21,
    "hobbies": ["listening music", "traveling"],
    "grades": {"math": 90, "english": 85},
    "guardian": [
        {"name": "Suman", "relation": "father"},
        {"name": "Sita", "relation": "mother"},
    ],
    "is_student": True,
}
print(d["name"])  # access value of key "name"
# print(d["age"])  # access value of key "age"
# print(d["hobbies"])  # access value of key "hobbies"
# print(d["grades"]["math"])  # access value of key "math" in "grades"
# print(d["guardian"][1]["name"])  # access name of first guardian

# get all keys
for key in d.keys():
    print(key)

    # get all values
    for value in d.values():
        print(value)

# change value for a specific key
d["name"] = "Smiley"

# add new key-value pair
d["country"] = "Nepal"

#remove key-value pair
del d["is_student"]

print (d)

s = {1,2,3,5,6}
t = {2,3,4,5}

# remove duplicates from the below list
l = {111,111,23,33,42,111,98}
print (list(set(l))) #remove duplicates from list using set