def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    vowels = set("aeiou")

    stringlist = list(s)
    i = 0
    j = len(s) - 1

    while i < j:
        if stringlist[i].lower() not in vowels:
            i += 1
        elif stringlist[j].lower() not in vowels:
            j -= 1
        else:
            stringlist[i], stringlist[j] = stringlist[j], stringlist[i]
            i += 1
            j -= 1

    return "".join(stringlist)
