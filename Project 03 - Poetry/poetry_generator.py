# IAE 101
# Project 03 - Poetry Generator
# Minhaj Alok
# 114868408
# malok
# 11/22/2024
# poetry_generator.py (v.7)

import nltk
import pronouncing
import random

# This uses the King James Bible as the corpus
# Use: nltk.corpus.gutenberg.fileids()
# to see which other gutenberg works are available.
#pre_my_corpus = nltk.corpus.gutenberg.words('bible-kjv.txt')

# This uses all the words in the entire gutenberg corpus
#pre_my_corpus = nltk.corpus.gutenberg.words()

# This loop constructs a corpus from all the shakespeare plays included in the
# shakespeare corpus included in NLTK
# Use: nltk.corpus.shakespeare.fileids()
# to see which shakespeare works are included.
pre_my_corpus = []
for fid in nltk.corpus.shakespeare.fileids():
    pre_my_corpus += nltk.corpus.shakespeare.words(fid)

my_corpus = []
for w in pre_my_corpus:
    my_corpus.append(w.lower())

bigrams = nltk.bigrams(my_corpus)
cfd = nltk.ConditionalFreqDist(bigrams)

# next_word_generator
# This function...
def next_word_generator(source = None):
    result = None
    #print()
    #print("SOURCE:", source)
    if (source == None) or (source not in cfd) or (not source.isalpha()):
        while result == None or not result.isalpha():
            result = random.choice(my_corpus)
    else: 
        #print("CFD ENTRY:")
        #print(cfd[source])
        init_list = list(cfd[source].elements())
        #print("INIT_LIST:")
        #print(init_list)
        choice_list = [x for x in init_list if x.isalpha()]
        #print("CHOICE_LIST:")
        #print(choice_list)
        #print()
        if len(choice_list) > 0:
            result = random.choice(choice_list)
        else:
            while result == None or not result.isalpha():
                result = random.choice(my_corpus)
    return result


# This function takes a single input:
# word - a string representing a word
# The function returns the number of syllables in word as an
# integer.
# If the return value is 0, then word is not available in the CMU
# dictionary.
def count_syllables(word):
    phones = pronouncing.phones_for_word(word)
    count_list = [pronouncing.syllable_count(x) for x in phones]
    if len(count_list) > 0:
        result = max(count_list)
    else:
        result = 0
    return result

# This function takes a single input:
# word - a string representing a word
# The function returns a list of words that rhyme with
# the input word.
def get_rhymes(word):
    result = []
    pre_result = pronouncing.rhymes(word)
    for w in pre_result:
        if w in my_corpus:
            result.append(w)
    #print()
    #print("PRE_RESULT:", len(pre_result))
    #print(pre_result)
    #print("RESULT:", len(result))
    #print(result)
    #print()
    return result

# This function takes a single input:
# word - a string representing a word
# The function returns a list of strings. Each string in the list
# is a sequence of numbers. Each number corresponds to a syllable
# in the word and describes the stress placed on that syllable
# when the word is pronounced.
# A '1' indicates primary stress on the syllable
# A '2' indicates secondary stress on the syllable
# A '0' indicates the syllable is unstressed.
# Each element of the list indicates a different way to pronounce
# the input word.
def get_stresses(word):
    result = pronouncing.stresses_for_word(word)
    return result

# A test function that demonstrates how each of the helper functions included
# in this file work.  You supply a word and it will run each of the above
# functions on that word.
def test():
    keep_going = True
    while keep_going:
        sw = input("Please enter a word (Enter '0' to quit): ")
        if sw == '0':
            keep_going = False
        elif sw == "":
            pass
        else:
            print("Random 5 words following", sw)
            wl = [sw]
            iw = sw
            for i in range(4):
                elements = list(cfd[iw].elements())
                print()
                nw = next_word_generator(iw)
                print("NW:", nw)
                print("COUNT:", elements.count(nw))
                print()
                wl.append(nw)
                iw = nw
            print(" ".join(wl))
            print()
            print("Pronunciations of", sw)
            print(pronouncing.phones_for_word(sw))
            print()
            print("Syllables in", sw)
            print(count_syllables(sw))
            print()
            print("Rhymes for", sw)
            print(get_rhymes(sw))
            print()
            print("Stresses for", sw)
            print(get_stresses(sw))
            print()


############################################################
##                                                         #
### STUDENT SECTION                                        #
##                                                         #
############################################################

# generate_rhyming_line()
# Complete this function so that it returns a list. The list
# must contain two strings of 5 words each. Each string
# corresponds to a line. The two lines you return must rhyme.
def generate_rhyming_lines():
    lines = []
    first = []
    second = []

    # generate first line
    for i in range(4):
        first.append(next_word_generator())
        second.append(next_word_generator())
    
    fifth = ""
    rhymes = []

    while (len(rhymes) == 0):
        fifth = next_word_generator()
        rhymes = get_rhymes(fifth)

    first.append(fifth)
    second.append(random.choice(rhymes))

    lines.append(" ".join(first))
    lines.append(" ".join(second))
    return lines



# generate_10_syllable_lines()
# Complete this function so that it returns a list. The list
# must contain two strings of 10 syllables each. Each string
# corresponds to a line and each line must be composed of words
# whose number of syllables add up to 10 syllables total.
def generate_10_syllable_lines():
    lines = []
    
    while len(lines) < 2:
        count = 0
        words = []
        while count != 10:
            word = next_word_generator()
            if count + count_syllables(word) <= 10:
                words.append(word)
                count += count_syllables(word)
        lines.append(" ".join(words))

    return lines




# generate_metered_line()
# Complete this function so that it returns a string. This string
# will be composed of randonly selected words, will contain 10
# syllables, and the rhythm of the line must match the following
# pattern of stresses: 0101010101
def generate_metered_line():
    line = ""
    total_syls = 0
    pattern = "0101010101"

    while total_syls != 10:
        word = next_word_generator()
        syls = count_syllables(word)
        stresses = get_stresses(word)
        for stress in stresses:
            if stress == pattern[:syls]:
                line += word + " "
                total_syls += syls
                pattern = pattern[syls:]
                break
    
    return line

# generate_line()
# Use this function to generate each line of your poem.
# This is where you will implement the rules that govern
# the construction of each line.
# For example:
#     -number of words or syllables in line
#     -stress pattern for line (meter)
#     -last word choice constrained by rhyming pattern
# Add any parameters to this function you need to bring in
# information about how a particular line should be constructed.
def generate_line(syls):
    words = []
    total_syls = 0
    word = ''

    while total_syls != syls:
        previous_word = word
        if(word == ''):
            word = next_word_generator()
        else:
            word = next_word_generator(word)
        
        if(count_syllables(word) == 0):
            word = previous_word
            continue

        if(total_syls + count_syllables(word) <= syls):
            words.append(word)
            total_syls += count_syllables(word)

    return " ".join(words)

# generate_poem()
# Use this function to construct your poem, line by line.
# This is where you will implement the rules that govern
# the structure of your poem.
# For example:
#     -The total number of lines
#     -How the lines relate to each other (rhyming, syllable counts, etc)
def generate_poem():
    lines = []

    max_syls = 7
    format = []
    format.append(max_syls)
    max_syls -= 2

    while max_syls > 2:
        format.insert(0, max_syls)
        format.append(max_syls)
        max_syls -= 2

    print(format)

    for syls in format:
        lines.append(generate_line(syls))

    return "\n".join(lines)

    


if __name__ == "__main__":

    test()
    print()
        
    result1 = generate_rhyming_lines()
    print("RHYMING LINES:")
    print(result1)
    print()

    result2 = generate_10_syllable_lines()
    print("10 SYLllABLE LINES:")
    print(result2)
    print()

    result3 = generate_metered_line()
    print("METERED LINE:")
    print(result3)
    print()

    my_poem = generate_poem()
    print("A POEM:")
    print(my_poem)
    print("\n\nIf this is all you see, try uncommenting some lines in main.\n\n")
    
    