
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
            temp = {}
            for arg in args:
                temp[arg] = d[arg]
            yield temp
            # yield { d[x] for x in args }


a = field(goods, 'title')
b = field(goods, 'title', 'price')
c = field(goods, 'title', 'price', 'color')
print(list(a))
print(list(b))
print(list(c))
