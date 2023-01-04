#!/usr/bin/python3
"""prints text with specifications"""


def text_indentation(text):
    """print text indetation

    Args:
        Text: of type str, text to be indented
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    count = 0
    while count < len(text) and text[count] == ' ':
        count += 1

    while count < len(text):
        print(text[count], end="")
        if text[count] == "\n" or text[count] in ".?:":
            if text[count] in ".?:":
                print("\n")
            count += 1 
            while count < len(text) and text[count] == ' ':
                count += 1
            continue
        count += 1
