# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.


def rotate(letter, n):
    string = ''
    for i in letter:
        if i != ' ':
            string += shift_n_letters(i, n)
        else:
            string += i
    return string


def shift_n_letters(letter, n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if alphabet.find(letter)+n > 25:
        return alphabet[(alphabet.find(letter)+n)-26]
    else:
        return alphabet[alphabet.find(letter)+n]





print rotate ('sarah', 13)
#>>> 'fnenu'
print rotate('fnenu',13)
#>>> 'sarah'
print rotate('dave',5)
#>>>'ifaj'
print rotate('ifaj',-5)
#>>>'dave'
print rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu sv rscv kf ivru kyzj"),-17)
#>>> ???
print rotate("this course teaches you to code",7)
#>>> "aopz jvbyzl alhjolz fvb av jvkl"