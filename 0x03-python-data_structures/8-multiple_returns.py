#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return len(sentence), None
    else:
        new_tuple = tuple(list(sentence))
        return len(new_tuple), new_tuple[0]
