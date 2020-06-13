'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0
    if word == '':
        return count
    # check if first letter is t
    ## check is second is h
    elif word[0] == 't' and len(word) >= 2 and word[1] == 'h':
        ## increment count
        count += 1
        new_word = word.replace(word[0] + word[1], '', 1)
        count += count_th(new_word)
    # remove first letter from word and call count_th(word)
    else:
        new_word = word.replace(word[0], '', 1)
        count += count_th(new_word)

    return count
