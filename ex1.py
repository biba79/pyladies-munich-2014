from sys import argv

script, user_name = argv
prompt = '~~> '

print "Hello %s, anything interesting happening in Munich?" % (user_name)
meetup = raw_input(prompt)

print "Cool! When?"
time = raw_input(prompt)

print "Where?"
place = raw_input(prompt)

print "How do I sign up?"
signup = raw_input(prompt)

print """
Alright, so you said %r, 
happening on %r, 
at %r. 
And to sign up I should %r.
""" % (meetup, time, place, signup)

#print "Hi %s, I'm the %s script." % (user_name, script)
#print "I'd like to ask you a few questions."
#print "Do you like me %s?" % user_name
#likes = raw_input(prompt)

#print "Where do you live %s?" % user_name
#lives = raw_input(prompt)

#print "What kind of computer do you have?"
#computer = raw_input(prompt)

#print """
#Alright, so you said %r about liking me.
#You live in %r. Not sure where that is.
#And you have a %r computer. Nice.
#""" % (likes, lives, computer)