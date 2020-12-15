#!/usr/bin/python3


def multiple_returns(sentence):
    for x in sentence:
        if sentence == "":
            return (0, None)
        else:
            return (len(sentence), sentence[0])
