import random
from random import randint

poem ='''lightning flash across the sky
silver clouds begin to cry
our clothes are cold and soaking wet
but we don't run inside just yet

if I said I'm ready now
darling, would you show me how
to blindly run through fields, unplowed
until the thunder roars?

fire races through my spine
warm hands meet my cold waistline
let's dance together, intertwined
like flowers in a storm
'''

#TODO: get a list of strings that contains lines of poem

def lines_printed_backwards(lines):
    # lines_list = poem.split("\n")
    # print(lines_list)
    lines.reverse()
    for line in lines:
        print(line)
        # print(lines_printed_backwards)
    ''' This function takes in a list of 
    strings containing the lines of 
    your poem as arguments and 
    will print the poem 
    lines out in reverse 
    with the line numbers reversed.'''
    

def lines_printed_random(lines, random_lines):
    for random_line in random_lines:
        print(random_line)
    ''' Your code should implement the lines_printed_random() 
    function which will randomly select lines from a list of 
    strings and print them out in random order. Repeats are 
    okay and the number of lines printed should be equal 
    to the original number of lines in the poem 
    (line numbers don't need to be printed). 
    Hint: try using a loop and randint()  '''
    
 
def my_custom(lines):
    lines.sort()
    lines.append('Zebras sleep in the dark')
    for line in lines:
        print(line)
    '''
    Does something of my choosing
    '''

#TODO: get a list of strings that contains lines of poem
lines = poem.split("\n")

random_lines = random.choice(lines).split("\n")

#Testing code
# print(lines_printed_backwards(lines))
print(lines_printed_random(lines, random_lines))
# print(my_custom(lines))