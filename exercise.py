##problem 1: Use indexing to print out the following
##given
s='fullstackslp'

#f
print(s[0])

#p
print(s[11])

#stack
print(s[4:9])

#slp
print(s[9:12])

#cks
print(s[7:10])

#reverse the string
reversed_s = s[::-1]
print (reversed_s)


##problem 2: given this nested list;
x = [3,7,5,1,4,'hello']
#reassign hello to goodbye:
x[5]='goodbye'
print(x)

##problem3- dictionaries
#Using keys and indexing, grab the'hello' from the following dictionaries:
d1={'simple_key':'hello'}
d2 = {'k1':'easy','k2':'hello'}
d3 = {'k1':['nested_key','this is deep','hello']}

print(d1['simple_key'])
print(d2['k2'])
print(d3['k1'][2])

##problem4- sets
#Use a set to find the unqiue values of the list below below:
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]

new_list = set(mylist)
print(new_list)

##problem 5-formatting
#you are gien two variable
age = 45
name = "Kyle"
#use print formatting to print the following string:
"Hello my dog's name is Kyle and he looks 45 years old"
my_string = "Hello my dog's name is {} and he looks {} years old".format(name,age)
print(my_string)
