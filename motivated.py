import random


# An array of statements 
attr = ['Be simple and intelligent like','Focus, work and plan like', 'Be Smart like', 'Think like', 'Be disciplined like', 'Be open source like', 'Stay focused like', 
'Use the Word like', 'Be wealthy like', 'Read books like', 'Look smart like', 'Grow like', 'Be like', 
'Practice the presence of God like', 'Perform miracles like', 'Be Hardworking like', 'Be detailed and intelligent like']

# an array of personal Mentors 
engrs = ['Jesus Christ of Nazareth', 'Oghenekparobo Joel Onosemuode', 'Linus Torvalds', 'Elon Musk', 'Mark Zuckerberg', 'Sandeep Jain', 'Vue Founder']
inspiration = ['Pastor Murphy Akpovi', 'Bill Gates', 'Carlos Ejakpevweoghene', 'Benny Hinn', 'Cristiano Ronaldo', 'Pep Guardiola', 'Zinedine Zidane']
who = [engrs, inspiration]

# call this function to get a randomly generated statement 
def motivation():
    i = random.randint(0,14)
    j = random.randint(0, 6)
    k = random.randint(0,1)
    return f'{attr[i]} {who[k][j]}'
  
# call this function to get a particularly generated statement
def getAttribute(att):
    while True:
        i = random.randint(0,14)
        j = random.randint(0, 6)
        k = random.randint(0,1)
        attribute = attr[i]
        if attr[i] == att:
            print(f'{attr[i]} {who[k][j]}')
            break
   
# call this function to get a particularly generated Mentor            
def getIndividual(ind):
    while True:
        i = random.randint(0,14)
        j = random.randint(0, 6)
        k = random.randint(0,1)
        individual = who[k][j]
        if who[k][j] == ind:
            print(f'{attr[i]} {who[k][j]}')
            break
            
# makes the statement more random            
def mot():
    while True:            
        for i in range(38):
            motivation()
        print(motivation())    
        break        
        
# the call        
mot()        