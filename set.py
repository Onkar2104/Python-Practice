#set

'''
set is collection of elements
The elements in the set is unique.
The elements in the set are immutable.
However, a set itself a mutable.
There is no index attached to any elements.


Creating a set:-
A set is created by using the set() function or placing the elements within a pair of curly braces.'''

s1={1,2,3,4}
s2={2,3,4,1}
print(s1==s2)
s1.add(3)
print(s1)
s1.add(6)
print(s1)



# A={10,20,30,40,70}
# B={10,20,60,80,90}
# print(A.difference(B))
# print(B.difference(A))

# chr


# s1=input("Enter String1:")
# s2=input("Enter String2:")
# print("Comma: ", set(s1)| set(s2))
# x=set(s1) | set(s2)
# for i in x:
#     print(i)


# set1={1,2,3,4}
# set2={5,6}
# both=set1.issubset(set2)
# print(both)

set1={"a","b","c"}
set2={"a","b"}
sub=set2.issubset(set1)
print(sub)


#pop(),remove(),update()