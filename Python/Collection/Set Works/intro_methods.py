"""

st={10,20} ,set()
unorded [indexing not supported]
mutable
no duplication

methods:

add(value) add value to set
union(set) -combine both set
intersection(set)-common elements
difference(set)- set a difference set b -B elements A remove akum
is_superset() 
is_subset()


"""
print("=========class dictionary=======")
stt={10,20}
print(type(stt))

print("======no duplicates======")
st={10,20,30,40,30,40}
print(st)

print("========add=======")
st.add(100)
print(st)

print("======union======")
set_a={10,20,30,40}
set_b={10,20,100,200,300,400}
union_set=set_a.union(set_b)
print(union_set)

print("=====intersection=====")
intersection_set=set_a.intersection(set_b)
print(intersection_set)

print("=====difference set a remove====")
difference_set=set_a.difference(set_b)
print(difference_set)
print("=====difference set b remove====")
difference_set=set_b.difference(set_a)
print(difference_set)

print("======superset======")
set_c={10,20,30,40,50}
set_d={10,30,50}
print(set_c.issuperset(set_d))

print("======subset=====")
print(set_d.issubset(set_c))