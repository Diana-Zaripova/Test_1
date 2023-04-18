opposites_dict = {'big': 'small', 'long': 'short', 'thin': 'fat', 'fast': 'slow'}


def antonym(word):
    if opposites_dict.get(word):
        return opposites_dict.get(word)
    elif {value: key for key, value in opposites_dict.items()}.get(word):
        return {value: key for key, value in opposites_dict.items()}.get(word)
    else:
        print('Oops')


print(antonym('short'))
print(list(opposites_dict.values())[-1])
