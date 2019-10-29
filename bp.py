import random

poem ='''
Hold fast to dreams 
For if dreams die
Life is a broken-winged bird
That cannot fly.
Hold fast to dreams
For when dreams go
Life is a barren field
Frozen with snow.
'''
#TODO: get a list of strings that contains lines of poem

def lines_printed_backwards(poem_lines_list):
    poem_lines_list.reverse()
    for poem_line in poem_lines_list:
        print(poem_line)
        # print(lines_printed_backwards)
    ''' This function takes in a list of 
    strings containing the lines of 
    your poem as arguments and 
    will print the poem 
    lines out in reverse 
    with the line numbers reversed.'''
    

def lines_printed_random():
    # poem.randint()
    index = 0
    while index < len(poem):
        print(poem[index])
        index += 1
    ''' Your code should implement the lines_printed_random() 
    function which will randomly select lines from a list of 
    strings and print them out in random order. Repeats are 
    okay and the number of lines printed should be equal 
    to the original number of lines in the poem 
    (line numbers don't need to be printed). 
    Hint: try using a loop and randint()  '''
    pass
 
def my_custom():
    '''
    Does something of my choosing
    '''
    pass 

#TODO: get a list of strings that contains lines of poem
#Use lines = poem.split("\n")
 
 
#Testing code
# lines_printed_backwards(poem_lines_list)