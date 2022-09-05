#checkfor concatenation of the youtuber name to subscribe feature

youtuber = "Prakash Ayyanagoudar"
print('subscribe to ' + youtuber)
#or
print('subscribe to {}'.format(youtuber))
#or 
print(f'subscribe to {youtuber}')

adj = input ('Adjective :')
verb1 = input ('Verb: ')
verb2 = input ('Verb: ')
famous_person= input ('Famous person: ')
madlib = f'Computer programming so {adj}! It makes me so excited all the time beause \
    I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!'

print (madlib)