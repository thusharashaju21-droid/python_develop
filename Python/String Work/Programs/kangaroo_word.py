def is_kangaroo_word(word1, word2):

    for ch in word1:

        if ch not in word2.lower():

            print(False)
            break

    else:

        print(True)


is_kangaroo_word("hen", "chicken")
is_kangaroo_word("cat", "chicken")