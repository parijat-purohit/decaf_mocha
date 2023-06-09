def mutable_list_1(n, l=[]): # initialized the list
    l.append(n)
    return l

def mutable_list_2(n):
    l = None
    l = []
    l.append(n)
    return l

def immutable_string(st):
    try:
        st[0] = 'e'
        return st
    except Exception as e:
        return e

print(mutable_list_1(5))
print(mutable_list_1(10))

print(mutable_list_2(5))
print(mutable_list_2(10))

st = 'old'
print(immutable_string(st))
# st is not changed at all.
print(st)