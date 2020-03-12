#============================================#
#                   SET                      #
#============================================#
#Set contains Unordered and Unindexed elements
#Set are written within Curly Braces.

#Creating Set
#Empty Set
example = set()

print((dir(example))
print()

#Adding items in the empty set

example.add(42)
example.add("Abhishek")
example.add(56.12)
example.add(False)

#All of the above item will be added in the set.
#It is possible that the order might be different than the way we added it.

{False, 42, 56.12, 'Abhishek'}

#In a set if you add a duplicate value, you won't get any error but there will be only a single copy of that item.

example.add(42)
print(example)

#Even though we added 42 again, there will only be a single 42 value in it.

#Removing an item using remove()

example.remove(42)
print(example)

#42 will be removed

#What if we try removing a value which doesnot exist in the function?
#An error will prompt then
#To avoid the Error even an element doesnot exist, we can use discard()

example.discard()

#Another way of creating set is to pre-populate the value while creating set.

example2 = set([28,"Natasha",34.5,False])
print(example2)

#Rather than creating a set and then populating it, here we are pre-filling the values

#Clearing all the element of a set using clear()

example2.clear()
print(len(example2))


Performing Union/Intersection on Set

odds = set([1,3,5,7,9])
evens = set([2,4,6,8,10])
primes = set([2,3,5,7])
composites = set([4,6,8,9,10])

print(odds.union(evens))
#Print all the element from odds and even

print(odds.intersection(primes))
#print only matching elements from both the sets

print(primes.intersection(evens))
#Print only {2} as it is the only common element in both

#Check if element in a set

2 in primes

OR

if 2 in primes:
    print("Yes")

#Check if element not in a set

9 not in evens

#OR

if 9 not in evens:
    print("Yes")

#Other Methods that can be used with set()

#=================================================================================================================
#	Method							Description
#=================================================================================================================
add()							             Adds an element to the set
clear()							           Removes all the elements from the set
copy()							           Returns a copy of the set
difference()					         Returns a set containing the difference between two or more sets
difference_update()			       Removes the items in this set that are also included in another, specified set
discard()						           Remove the specified item
intersection()					       Returns a set, that is the intersection of two other sets
intersection_update()		       Removes the items in this set that are not present in other, specified set(s)
isdisjoint()					         Returns whether two sets have a intersection or not
issubset()						         Returns whether another set contains this set or not
issuperset()					         Returns whether this set contains another set or not
pop()							             Removes an element from the set
remove()						           Removes the specified element
symmetric_difference()			   Returns a set with the symmetric differences of two sets
symmetric_difference_update()	 inserts the symmetric differences from this set and another
union()							           Return a set containing the union of sets
update()						           Update the set with the union of this set and others
#=================================================================================================================
