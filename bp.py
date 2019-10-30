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

    lines.reverse()
    for line in lines:
        print(line)
        # print(lines_printed_backwards)
    ''' lines printed backwards when function is called'''
    

def lines_printed_random(random_lines):
    for random_line in random_lines:
        print(random_line)
    ''' lines printed at random when the function is called'''
    
 
def my_custom(lines):
    lines.sort()
    lines.append('Zebras sleep in the dark')
    for line in lines:
        print(line)
    '''
    lines printed in alphabetical order when funtion is called
    '''

def shuffle(lines):
    random.shuffle(lines)
    for line in lines:
        print(line)
    '''
    lines will be placed randomly in the poem. the differnce between this function and lines_printed_random is that this function 
    displays the entire poem and not just singular lines
    '''

#TODO: get a list of strings that contains lines of poem
lines = poem.split("\n")
random_lines = random.choice(lines).split("\n")

# Testing code
print(lines_printed_backwards(lines))
print(lines_printed_random(random_lines))
print(my_custom(lines))
print(shuffle(lines))