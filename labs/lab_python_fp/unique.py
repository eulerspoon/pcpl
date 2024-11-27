
class Unique(object):
    def __init__(self, items, **kwargs):
        self.visited = set()
        self.items = iter(items)
        self.ignore_case = kwargs.get('ignore_case', False)
        self.buff = None

    def __next__(self):
        while True:
            if self.buff is not None:
                item = self.buff
                self.buff = None
            else:
                item = next(self.items)
            # print(next(self.items))
            
            if isinstance(item, str) and self.ignore_case:
                key = item.lower()
            else:
                key = item

            if key not in self.visited:
                self.visited.add(key)
                return item
        # x = self.items[self.cur_index]
        # if self.cur_index + 1 <= len(self.items):
        #     self.cur_index += 1 
        # if x not in self.visited:
        #     self.visited.append(x)
        #     return x

    def __iter__(self):
        return self


data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']

a = Unique(data1)
for x in a: print(x)
print()
b = Unique(data2)
for x in b: print(x)
print()
c = Unique(data2, ignore_case=True)
for x in c: print(x)