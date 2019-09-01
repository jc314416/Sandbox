# def main():
#     func_2()
#
#
# def fn(x, y):
#     z = x + y
#
#
# print(fn(1, 2))
#
#
# def func_2():
#     print("Hello")
#
#
# main()

# name = str(input("Name: "))
# number_of_vowels = 0
# VOWEL = "aeiou"
# for character in name.lower():
#     if character in VOWEL:
#         number_of_vowels += 1
# print("Out of {} letters, {} has {} vowels".format(len(name), name, number_of_vowels))


# def main():
#     value = process(4, 4, 4)
#     print(value)
#
#
# def process(x, y=2, z=3):
#     return x + y + z


words = ["aye", "bee", "bee", "sea", "bee", "sea"]
# print(" / ".join(words))

# string = ""
# if len(string) == 0:
#     print("Yes")
word_to_count = {}
for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1

print(word_to_count)