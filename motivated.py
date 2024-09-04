import random

# An array of statements 
attr = ['Be simple and intelligent like', 'Be disciplined and hardworking like', 'Be open source like', 'Stay focused like', 'Become wealthy like', 'Read books like', 'Perform miracles like', 'Be tactical like']

# an array of my personal inspiration
engrs = ['Oghenekparobo Joel Onosemuode', 'Linus Torvalds', 'Elon Musk', 'Mark Zuckerberg', 'Sandeep Jain', 'Bill Gates']



# call this function to get a particular statement
def getAttribute(attribute): # enter desired attribute and see who fits in
    while True:
        i = random.randint(0, len(attr)-1)
        j = random.randint(0, len(engrs)-1)
        if attr[i] == attribute:
            print(f'{attr[i]} {engrs[j]}')
            break

# call this function to get a particular engineer          
def getIndividual(individual): # enter desired engineer and see what attributes fits in
    while True:
        i = random.randint(0, len(attr)-1)
        j = random.randint(0, len(engrs)-1)
        if who[k][j] == individual:
            print(f'{attr[i]} {engrs[j]}')
            break
            


# call this function to get a randomly generated sentence
def motivate(): # print(motivate()) to call this function 
    i = random.randint(0, len(attr)-1)
    j = random.randint(0, len(engrs)-1)
    return f'{attr[i]} {engrs[j]}'
    
# this function takes the output of motivate() and gives a more appealing individual
def neuralmot(input_sentence): # neuralmot means neural-link motivation
    import re, random
    focus = re.compile(r'focus|work', re.I)
    
    adverbs = ['You\'ll be fine', 'Yeah', 'Surely', 'Indeed', '', 'Definitely', 'True']
    adv_intro = ['you should', 'do', '', 'it would be a good thing to']
    
    if focus.search(input_sentence) != None:
        neuralmotengrs = ['Joel Oghenekparobo', 'Elon Musk', 'Mark Zuckerberg', 'Murphy Akpovi', 'Cristiano Ronaldo', 'Pep Guardiola']
        return f'{adverbs[random.randint(0, len(adverbs)-1)]}, {adv_intro[random.randint(0,len(adv_intro)-1)]} stay focused like {neuralmotengrs[random.randint(0, len(neuralmotengrs)-1)]}'
    else:
        return f'{sentence}'
sentence = motivate() # I stored the motivate() in this sentence variable for illegibility 
print(neuralmot(sentence)) # I use print(neuralmot(sentence)) because I return the values in the motivate() function