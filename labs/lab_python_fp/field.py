
goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
]


def field(items, *args):
    assert len(args) > 0
    

    for d in items:
        if len(args) == 1:
            yield d[args[0]]
        else:
            yield { d[x] for x in args }


a = field(goods, 'title', 'price')
#b = field(goods, 'title', 'price')

#print('a')
for x in a:
    print(x)
#print('b')
#for x in b:
#    print(x)
