"""
Question1 
"""
print("Question1")
words = ["apple", "banana", "orange", "peach", "kiwi"]
min_word_length = 5
filtered_words = [word for word in words if len(word) > min_word_length]
print( "min_word_length=",min_word_length )
for word in filtered_words:
    print(word)



"""
Question2
"""
print("\n\n\nQuestion2")
I1 = [1,2, 5]
I2 = [6, 2, 7]
common_elements = [x for x in I1 if x in I2]
print(common_elements)



"""
Question3
"""
print("\n\n\nQuestion3")
I1 = [1, 2, 3, 4, 4, 4, 4, 4, 4, 5, 6, 6, 8, 8, 12, 12, 12, 12, 13]
new_list = [I1[0]]
for i in range(1, len(I1)):
    if I1[i] != I1[i - 1]:
        new_list.append(I1[i])
print( new_list)



"""
Question4
"""
print("\n\n\nQuestion4")
Username = ['jack', 'bob', 'john']
Password = ['123', '859', 'hello']
user_password_dict = {}
for i in range(len(Username)):
    user_password_dict[Username[i]] = Password[i]
for username, password in user_password_dict.items():
    print("username:", username, " password:", password)



"""
Question5
"""
print("\n\n\nQuestion5")
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
combinations = [(color, size) for color in colors for size in sizes]
for color, size in combinations:
    print(f'Colors: {color}, Sizes: {size}')


"""
Question6
"""
print("\n\n\nQuestion6")
tuple1 = (90,34,-23,18,12)
max_value = max(tuple1)
min_value = min(tuple1)
print("Max:", max_value)
print("Min:", min_value)



"""
Question7
"""
print("\n\n\nQuestion7")
I1 = ['sklearn', 'Al', 'julyedu.com', 'Caffe', 'Al', 'sklearn']
word_freq_dict = {}
for word in I1:
    if word in word_freq_dict:
        word_freq_dict[word] += 1
    else:
        word_freq_dict[word] = 1
print("frequency:")
for word, freq in word_freq_dict.items():
    print("{}:{}".format(word,freq))




"""
Question8
"""
print("\n\n\nQuestion8")
leap_years = []
for year in range(1970, 2051):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap_years.append(year)
print(leap_years)



"""
Quesyion9
"""
print("\n\n\nQuestion9")
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
transposed_arr = [[row[i] for row in arr] for i in range(len(arr[0]))]
for row in transposed_arr:
    print(row)



"""
Question10
"""
print("\n\n\nQuestion10")
original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 2, 'e': 1}
reversed_dict = {val: key for key, val in original_dict.items()}
print(reversed_dict)



"""
Name: YangWenyan 
IDNumber: 2021364820
"""