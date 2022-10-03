
from engtext import eng
from gertext import ger


def translator():


    word_list_eng = eng
    word_list_ger = ger


    wort = input("Write an english word to translate it in german: ")
    if wort in word_list_eng:
        num_index = word_list_eng.index(wort)
        print(word_list_ger[num_index])

    else:
        print("Write a valid word")




translator()

