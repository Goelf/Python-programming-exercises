# Longest Repetition

# Define a procedure, longest_repetition, that takes as input a
# list, and returns the element in the list that has the most
# consecutive repetitions. If there are multiple elements that
# have the same number of longest repetitions, the result should
# be the one that appears first. If the input list is empty,
# it should return None.


def longest_repetition(elements):
    best_e = None
    best_rep = 0
    current_e = None
    current_rep = 0
    if elements:
        for e in elements:
            if e != current_e:
                if best_rep < current_rep:
                    best_e = current_e
                    best_rep = current_rep
                current_rep = 1
                current_e = e
            else:
                current_rep = current_rep + 1
        if current_rep >  best_rep:
            best_e = current_e
        return best_e
    else:
        return None





# For example,

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([1, 2, 3, 4, 5])
# 1

print longest_repetition([])
# None

