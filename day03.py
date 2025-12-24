Q-)learn and practice about list comprehenc, map, filter, reduce and inbuilt function.
1-)WAP to remove negative number using list comprehence.
code-)  nums = [-5, 3, -1, 10, -20, 7]

positive_nums = [x for x in nums if x >= 0]
print(positive_nums)

2-)WAP to print the name which is length is grater than 4.
   names = ["Akhilesh,"Vivek","Rinki","Ram","Shya"]
code-) names = ["Akhil", "Akhilesh", "Rahul", "Neha"]

long_names = [name for name in names if len(name) > 4]
print(long_names)

3-)WAP Using map(), double each element in the following list.
  nums = [2,4,5,3,8,7]
code-)nums = [1, 2, 3, 4, 5]

double_nums = list(map(lambda x: x * 2, nums))
print(double_nums)

4-)WAP Convert all the strings in the list to uppercase using map.
   words = ["python", "django", "api"]
code-)words = ["python", "django", "api"]

upper_words = list(map(lambda w: w.upper(), words))
print(upper_words)

5-)Using filter(), extract only the even numbers from the list.
   nums = [10, 15, 20, 25, 30]
code-)nums = [10, 15, 20, 25, 30]

even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)
6-)WAP Using filter(), select only the words whose length is greater than 4.
   words = ["sky", "apple", "cloud", "sun"]
code-)words = ["sky", "apple", "cloud", "sun"]

long_words = list(filter(lambda w: len(w) > 4, words))
print(long_words)
7-)Using filter(), extract only the positive numbers from the list.
   nums = [-10, 5, -3, 8, 0, 12]
code-)nums = [-10, 5, -3, 8, 0, 12]

positive_nums = list(filter(lambda x: x > 0, nums))
print(positive_nums)
8-)Using reduce(), calculate the product of all elements in the list.
  nums = [1, 2, 3, 4]
code-)from functools import reduce

nums = [1, 2, 3, 4]

product = reduce(lambda x, y: x * y, nums)
print(product)