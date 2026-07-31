# set operations

friend_A_Hobbies = {"Reading", "Writing", "Cricket", "Coding","Traveling","Shopping"}

friend_B_Hobbies = {"Reading", "Cricket", "Photography", "Cooking","Coding"}

print(friend_A_Hobbies & friend_B_Hobbies)
print(friend_A_Hobbies ^ friend_B_Hobbies)
print(friend_A_Hobbies - friend_B_Hobbies)
print(friend_B_Hobbies <= friend_A_Hobbies)
print(friend_B_Hobbies >= friend_A_Hobbies)
print(friend_A_Hobbies.isdisjoint(friend_B_Hobbies))




shopping_list1 = {"Tomatoes","Onions","Curd","Cookies","Bread"}

shopping_list2 = {"Curd", "Milk","Paneer","Butter", "Cookies","Bread","Cheese","Ghee"}

print(shopping_list1 & shopping_list2)
print(shopping_list1 - shopping_list2)
print(shopping_list2 - shopping_list1)


# Attendance

rollcall = set()
for i in range(1,101):
    rollcall.add(i)
print(rollcall)


# Anagram example

string1 = "listn"
string2 = "silent"
set1 = set(string1)
set2 = set(string2)
if set1 == set2 :
    print("Same characters")
else:
    print("Different characters")


# Paragraph comparison

para1 = "A paragraph is defined by its thought and structure rather than a strict number of lines. While a typical paragraph runs 5 to 7 sentences—which often translates to about 5 to 7 lines depending on the document—there are no universal formatting rules."

para2 = "The three-paragraph format is highly effective when you need to condense points, make a quick and punchy argument, or build a foundation for beginning writers. For more comprehensive tips on sentence counts and pacing, check out the Mastering the 3-Paragraph Essay Guide or explore Chegg's Writing Guide for further academic support"

set1 = set(para1.split())
set2 = set(para2.split())

print(set1)
print(set2)
print(set1 & set2)


# Sentence unique words

sentence = "Python is easy and Python is powerful"

sentence_set = set(sentence.split())
print(sentence_set)
print(len(sentence_set))
