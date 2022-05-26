t = input("Write a sentence: ")
word_list = t.split(' ')
appear = len(list(set(word_list)))
print(appear)