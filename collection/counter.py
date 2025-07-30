## collections module
from collections import Counter
clount =["dragon", "tiger", "lion", "elephant", "giraffe","dragon", "lion", "tiger", "lion", "lion"]
print(Counter(["lion"]))
print(Counter(clount))
#ordered dict
from collections import OrderedDict
od = OrderedDict()
od['a'] = 1
od['b'] = 2  
od['c'] = 3
od['d'] = 4
for key, value in od.items():
    print(key, value)
print(od)
od.pop('b')
print(od)
od['e'] = 5
print(od)
#default dict
from collections import defaultdict
dd = defaultdict(list)
for i in range(5):
    dd[i].append(i * 2)
print(dd)
#deque
from collections import deque
d = deque([1, 2, 3, 4, 5])
d.append(6)
d.pop()
d.popleft()
d.appendleft(0)
print(d)
#named tuple
from collections import namedtuple
college = namedtuple('College', ['name', 'location', 'established'])
clg =college("smvec","pondy","1967")
li =["abc","chn","1990"]
di ={"name": "xyz", "location": "delhi", "established": "2000"}
print(college._make(li))
print(clg._asdict())
#ChainMap
from collections import ChainMap
hero ={"name": "spiderman", "power": "web-slinging"}
villain = {"name": "green goblin", "power": "glider"}
heroine = {"name": "black widow", "power": "martial arts"}
result = ChainMap(hero, villain, heroine)
print(result)

