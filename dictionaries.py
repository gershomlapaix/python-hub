import enum
ex_dictionary = {'key1': 'value1', 'key2': 'value2'}
print(ex_dictionary)

prices_lookup = {'apple': 2.99, 'oranges': 3.44, 'milk': '5.8'}
print(f"The price for an apple is {prices_lookup['apple']}.")

ex_mixed = {'k1': 425, 'k2': ["Gersh", "Nesta", 499], 'k3': {'insideKey': 100}}
print(f'An advanced dictionary: {ex_mixed}')
print(ex_mixed['k3']['insideKey'])

# doing some changes
ex_mixed['k1'] = "pos_down"
print(ex_mixed)

print(f'\n\n {ex_mixed.items()}')
print(f'\n\n {ex_mixed.values()}')
print(f'\n\n {ex_mixed.keys()}')


class RespName(enum.Enum):
    CHOIR_SINGER = 'choir_singer',
    DEACON = 'deacon',
    SECTRETARY = 'secretary',

print(RespName.CHOIR_SINGER)
    
