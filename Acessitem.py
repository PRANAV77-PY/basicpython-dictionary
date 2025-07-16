thisdict = {
    'brand ':'Ford',
    'model': 'Mustang',
    'year' : 1964
}
#x = thisdict["model"]
x = thisdict.get('model')
print(x)
#practice
dict = {
    'brand': 'tesla',
    'model': 'Y',
    'Year' : '2020',
    'price':'$50k'
}
x = dict.get('price')
print(x)