#!/usr/bin/python

#String

print "String Examples..!!"
str = "Hello Python guys..!!"
print str
print str*2
print str[0]
print str[3:6]
print str[4:]
print str+"concat"
if (str == "hello"):
    print "its true..!!\n"
print "\n"

#List

print "List Examples..!!"
lst = ["hi", 123, 456.78, "world"];
print lst
print lst*2
print lst[0]
print lst[1:3]
print lst[3:]
if (123 in lst):
    print "123 is there..!!"
print "\n"

#Dictionary
print "Dictionary Examples..!!"
dct = {}
dct[1] = 123
dct["two"] = "I am two"

print dct
print dct[1]
print dct["two"]
print dct.keys()
print dct.values()
print "\n"

raw_input("\n\nPress the enter key to exit.")
