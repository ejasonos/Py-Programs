import re, sys
# Enter username
username = input('Please enter a username: ')
print(f"\nhello {username}, I am a reply robot\nHow may I help you?\n")
# interactive shell
while True:
    inputText = input('enter query: ')
    # default ai checks and responsesoruueoooooooooooisdhdbfooooooooooooooooooooooooooooooooori              oruese





    
    aicheck1 = re.compile(r'H(o)?(w)? (a)?(r)?(e)? (y)?(o)?u', re.I)
    aicheck2 = re.compile(r'(how|what|why|when|where|who|would|could|which)', re.I)
    airesponse1 = 'I\'m fine thank you, how can I help you'
    def call():
        if aicheck2.search(inputText) != None:
            return aicheck2.search(inputText).group()
        else:
            return 'uhmm'
    airesponse2 = f'uhmm {username}, you mean {call()}?.. \nSorry, I don\'t know'
    exit = re.compile(r'(exit|out|leave)', re.I)
    exitReply = re.compile(r'y(e)?(s)?|yeah|ok(ay)?', re.I)
    # code for interaction
    if aicheck1.search(inputText) != None:
        print(f'{airesponse1}\n')
        continue
    if aicheck2.search(inputText) != None:
        print(f'{airesponse2}\n')
        continue
    if exit.search(inputText) != None:
        reply = input('do you mean to exit the program? ')
        if exitReply.search(reply) != None:
            sys.exit()
    print('I couldn\'t get that')