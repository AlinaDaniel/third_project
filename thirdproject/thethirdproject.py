# Project №3.
# The program helps a user to refill his/her vocabulary.
# The program displays English words on the topic of IT, the user has to translate them.
# In a case of an incorrect translation, the program repeats the word after a while,
# until the user will remember all the words and their meaning.
# Then the program displays the translation of these words into Russian and the user must enter the meaning in English.
# In a case of an incorrect translation, the program repeats the word after a while,
# until the user will remember all the words and their meaning.

import local as lc
import vocabulary as v

# A user chooses how many words he wants to learn.
print(lc.TXT_QUESTION)
number = int(input())
repeat_word = []
repeat_translation = []

# The user translates words from English into Russian.
word = v.english_words
translation = v.russian_words

for i in range(number):
    print(lc.TXT_TRANSLATE_INTO_RU, word[i], '.', sep='')
    answer = str.lower(input())
    if answer == translation[i]:
        print(lc.TXT_CORRECT_ANSWER, '\n')
    else:
        print(lc.TXT_INCORRECT_ANSWER, word[i], lc.TXT_TRANSLATE_AS,
              translation[i], '.\n', sep='')
        repeat_translation.append(translation[i])
        repeat_word.append(word[i])

# The user repeats the words in which he made a mistake.
if repeat_word != []:
    print(lc.TXT_REPEAT_WORDS, '\n')
    while repeat_word != []:
        print(lc.TXT_TRANSLATE_INTO_RU, repeat_word[0], '.', sep='')
        answer = str.lower(input())
        if answer == repeat_translation[0]:
            print(lc.TXT_CORRECT_ANSWER, '\n')
            del repeat_word[0]
            del repeat_translation[0]
        else:
            print(lc.TXT_INCORRECT_ANSWER, repeat_word[0],
                  lc.TXT_TRANSLATE_AS, repeat_translation[0], '.\n', sep='')
            repeat_word.append(repeat_word[0])
            repeat_translation.append(repeat_translation[0])
            del repeat_word[0]
            del repeat_translation[0]

# The user translates words from Russian into English.
word = v.russian_words
translation = v.english_words

for i in range(number):
    print(lc.TXT_TRANSLATE_INTO_EN, word[i], '.', sep='')
    answer = str.lower(input())
    if answer == translation[i]:
        print(lc.TXT_CORRECT_ANSWER, '\n')
    else:
        print(lc.TXT_INCORRECT_ANSWER, word[i], lc.TXT_TRANSLATE_AS,
              translation[i], '.\n', sep='')
        repeat_translation.append(translation[i])
        repeat_word.append(word[i])

# The user repeats the words in which he made a mistake.
if repeat_word != []:
    print(lc.TXT_REPEAT_WORDS, '\n')
    while repeat_word != []:
        print(lc.TXT_TRANSLATE_INTO_EN, repeat_word[0], '.', sep='')
        answer = str.lower(input())
        if answer == repeat_translation[0]:
            print(lc.TXT_CORRECT_ANSWER, '\n')
            del repeat_word[0]
            del repeat_translation[0]
        else:
            print(lc.TXT_INCORRECT_ANSWER, repeat_word[0], lc.TXT_TRANSLATE_AS,
                  repeat_translation[0], '.\n', sep='')
            repeat_word.append(repeat_word[0])
            repeat_translation.append(repeat_translation[0])
            del repeat_word[0]
            del repeat_translation[0]
    else:
        print(lc.TXT_CONCLUSION)
else:
    print(lc.TXT_CONCLUSION)