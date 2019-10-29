import random

poem ='''
Once more unto the breach, dear friends, once more;
Or close the wall up with our English dead.
In peace there's nothing so becomes a man
As modest stillness and humility:
But when the blast of war blows in our ears,
Then imitate the action of the tiger;
Stiffen the sinews, summon up the blood,
Disguise fair nature with hard-favour'd rage;
Then lend the eye a terrible aspect;
Let pry through the portage of the head
Like the brass cannon; let the brow o'erwhelm it
As fearfully as doth a galled rock
O'erhang and jutty his confounded base,
Swill'd with the wild and wasteful ocean.
Now set the teeth and stretch the nostril wide,
Hold hard the breath and bend up every spirit
To his full height. On, on, you noblest English.
Whose blood is fet from fathers of war-proof!
Fathers that, like so many Alexanders,
Have in these parts from morn till even fought
And sheathed their swords for lack of argument:
Dishonour not your mothers; now attest
That those whom you call'd fathers did beget you.
Be copy now to men of grosser blood,
And teach them how to war. And you, good yeoman,
Whose limbs were made in England, show us here
The mettle of your pasture; let us swear
That you are worth your breeding; which I doubt not;
For there is none of you so mean and base,
That hath not noble lustre in your eyes.
I see you stand like greyhounds in the slips,
Straining upon the start. The game's afoot:
Follow your spirit, and upon this charge
Cry 'God for Harry, England, and Saint George!'
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
    

def lines_printed_random(lines):
    # poem.randint()
    num_lines = 0
    while num_lines < len(poem):
        print(poem)
        num_lines += 1
    ''' Your code should implement the lines_printed_random() 
    function which will randomly select lines from a list of 
    strings and print them out in random order. Repeats are 
    okay and the number of lines printed should be equal 
    to the original number of lines in the poem 
    (line numbers don't need to be printed). 
    Hint: try using a loop and randint()  '''
    pass
 
def my_custom(lines):
    lines.sort()
    # del lines[-1]
    for line in lines:
        print(line)
    '''
    Does something of my choosing
    '''
    pass 

#TODO: get a list of strings that contains lines of poem
lines = poem.split("\n")
lines_list = poem.split("\n")
# print(lines_list)
 
#Testing code
# print(lines_printed_backwards(lines))
# print(lines_printed_random)
print(my_custom(lines))