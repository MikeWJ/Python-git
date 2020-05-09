# A first Python Script, playing around with strings, loops and conditions.

print('This is my first script') # and this is a comment
string1 = 'hello'
string2 = 'world'

# strings can be concatenated with + and repeated with *
print(string1 + ' ' + string2 + '!'*3 )

twoOnThree = 2/3
print('2 divided by 3 is about {}' .format(twoOnThree)) # you can print variables
print('or with fewer decimal points: {: f}' .format(twoOnThree)) # you can explicitly format the output


import math #Usually we put imports at the start. I put it here for context.
string3 = 'more'
print('you can print {0} than one variable, here\'s Pi: {1}. That makes {2} variables!' .format(string3,math.pi,3))

print('\nCounting in Twos:') # a blank line before the text
for num in range(2,10,2):
    print(num)

print('\n') # a blank line

a = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1] # This is an array

# Here's a FOR loop with an IF statement inside!
for element in a: # For every element in a, do something
    if element == max(a): # looks for the largest number in a
        print(element*'=')
        print('We reached the largest')
    print(element*'=')
    
for q in range (-5,26,5):
    print (q)
    
    