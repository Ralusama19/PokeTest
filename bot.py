import urllib3.contrib.pyopenssl
urllib3.contrib.pyopenssl.inject_into_urllib3()

import certifi
import urllib3
http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where())

import telebot 
from telebot import types
TOKEN = '187964536:AAEdn30pTPolGCZBG2pUn3caP1FP6mfFKoY'
bot = telebot.TeleBot(TOKEN)

import random
random.seed()

from sets import Set

class Categories:
	hardy , docile, brave, jolly, impish, naive, timid, hasty, sassy, calm, relaxed, lonely, quirky, miscellaneous = range(14)

class Pair:
	def __init__(self,a,b):
		self.a = a
		self.b = b

class Answer:
	def __init__(self, title):
		self.title = title
		self.rewards = []
	def addReward(self, category, many):
		self.rewards.append(Pair(category,many))

class Question:
	def __init__(self, title, number):
		self.title = title
		self.answers = []
		self.number = number
	def addAnswer(self, answer):
		self.answers.append(answer)

questionPool = [None]*14
hardyPool = []

q = Question("A test is coming up. How do you study for it?",1)

a = Answer("Study hard.")
a.addReward(Categories.hardy,2)
b = Answer("At the last second.")
b.addReward(Categories.relaxed,2)
c = Answer("Ignore it and play.")
c.addReward(Categories.impish,2)

q.addAnswer(a)
q.addAnswer(b)
q.addAnswer(c)

hardyPool.append(q)

q = Question("Can you focus on something you like?",2)

a = Answer("Yes.")
a.addReward(Categories.hardy,2)
a.addReward(Categories.docile,1)
b = Answer("No.")
b.addReward(Categories.quirky,2)


q.addAnswer(a)
q.addAnswer(b)

hardyPool.append(q)

q = Question("When the going gets tough, do you get going?",3)

a = Answer("Yes.")
a.addReward(Categories.hardy,2)
a.addReward(Categories.brave,2)
b = Answer("No.")
b.addReward(Categories.quirky,2)
b.addReward(Categories.sassy,2)

q.addAnswer(a)
q.addAnswer(b)

hardyPool.append(q)

q = Question("There is a bucket. If you put water in it, how high will you fill it?",4)

a = Answer("Full.")
a.addReward(Categories.hardy,2)
b = Answer("Half.")
b.addReward(Categories.calm,2)
c = Answer("A little.")
c.addReward(Categories.quirky,2)

q.addAnswer(a)
q.addAnswer(b)
q.addAnswer(c)

hardyPool.append(q)

questionPool[0]=hardyPool

docilePool = []

q = Question("You are offered a choice of two gifts. Which one will you take? ",5)

a = Answer("Big box.")
a.addReward(Categories.docile,2)
a.addReward(Categories.naive,1)

b = Answer("Small box.")
b.addReward(Categories.timid,2)
b.addReward(Categories.calm,1)

q.addAnswer(a)
q.addAnswer(b)

docilePool.append(q)

q = Question("You broke a rotten egg in your room! What will you do? ",6)

a = Answer("Open a window right away.")
a.addReward(Categories.docile,2)
a.addReward(Categories.hasty,1)

b = Answer("Take a sniff first.")
b.addReward(Categories.naive,2)
b.addReward(Categories.relaxed,1)

q.addAnswer(a)
q.addAnswer(b)

docilePool.append(q)


q = Question("A friend brought over something you'd forgotten. How do you thank your friend? ",7)

a = Answer("Say thank you regularly.")
a.addReward(Categories.docile,2)

b = Answer("Say thanks with a joke.")
b.addReward(Categories.naive,1)
b.addReward(Categories.lonely,1)

c = Answer("Say thanks, but be cool.")
c.addReward(Categories.sassy,2)

q.addAnswer(a)
q.addAnswer(b)
q.addAnswer(c)

docilePool.append(q)

q = Question("There is a wallet at the side of a road.",8)

a = Answer("Turn it in to the police!")
a.addReward(Categories.docile,2)

b = Answer("Yay! Yay!")
b.addReward(Categories.naive,2)

c = Answer("Is anyone watching...?")
c.addReward(Categories.impish,2)

q.addAnswer(a)
q.addAnswer(b)
q.addAnswer(c)

docilePool.append(q)

questionPool[1]=docilePool

bravePool = []

q = Question("You're going bungee jumping for the first time. Since it's scary, you decide to test the jump with a doll... And the bungee cord snaps! Will you still try to make a jump anyway? ",9)

a = Answer("Yes.")
a.addReward(Categories.brave,3)
a.addReward(Categories.impish,1)

b = Answer("No.")
b.addReward(Categories.timid,1)
b.addReward(Categories.docile,2)

q.addAnswer(a)
q.addAnswer(b)

bravePool.append(q)

q = Question("There is an alien invasion! What will you do? ", 10)

a = Answer("Fight.")
a.addReward(Categories.brave,0)

b = Answer("Run.")
b.addReward(Categories.timid,2)

c = Answer("Ignore it.")
c.addReward(Categories.relaxed,2)

q.addAnswer(a)
q.addAnswer(b)
q.addAnswer(c)

bravePool.append(q)


q = Question("You valiantly fight the aliens... But, you are defeated... An alien says to you... 'YOU HAVE IMPRESSED US. IT WAS A PLEASURE TO SEE. JOIN US, AND TOGETHER WE SHALL RULE THE WORLD.' What will you do? ",11)

a = Answer("Rule with the aliens.")
a.addReward(Categories.sassy,1)
a.addReward(Categories.relaxed,1)

b = Answer("Refuse.")
b.addReward(Categories.brave,4)

q.addAnswer(a)
q.addAnswer(b)

bravePool.append(q)


q = Question("A delinquent is hassling a girl on a busy city street! What will you do?", 12)

a = Answer("Help without hesitation.")
a.addReward(Categories.brave,3)

b = Answer("Help, even if scared.")
b.addReward(Categories.brave,2)
b.addReward(Categories.hardy,2)

c = Answer("Call the police.")
c.addReward(Categories.docile,1)
c.addReward(Categories.timid,1)
c.addReward(Categories.relaxed,1)

d = Answer("Do nothing out of fear.")
d.addReward(Categories.timid,1)

q.addAnswer(a)
q.addAnswer(b)
q.addAnswer(c)
q.addAnswer(d)

bravePool.append(q)

questionPool[2]=bravePool

"""
q = Question("A test is coming up. How do you study for it?",8)

a = Answer("Study hard.")
a.addReward(Categories.hardy,2)
b = Answer("At the last second.")
b.addReward(Categories.relaxed,2)
c = Answer("Ignore it and play.")
c.addReward(Categories.impish,2)

q.addAnswer(a)
q.addAnswer(b)
q.addAnswer(c)

hardyPool.append(q)
"""
stats = {}
user_step = {}
lastQuestion = {}
user_cats = {}
MAX_QUEST = 3

def sendQuestion(catnum, qnum, cid):
	user_step[cid] += 1
	print("sending question "+str(user_step[cid]))
	lastQuestion[cid] = questionPool[catnum][qnum]
	answerSelect = types.ReplyKeyboardMarkup(one_time_keyboard=True)
	lenght = len(questionPool[catnum][qnum].answers)
	for i in range(0,lenght):
		answerSelect.add(chr(ord('a')+i)+") "+questionPool[catnum][qnum].answers[i].title)
	bot.send_message(cid, questionPool[catnum][qnum].title, reply_markup=answerSelect)
		

def newQuestion(cid):
	if(user_step[cid] < MAX_QUEST): ######
		catnum = random.sample(user_cats[cid],1)[0]
		qnum = random.randint(0,len(questionPool[catnum]))
		while questionPool[catnum][qnum].number == 11:
			qnum = random.randint(0,len(questionPool[catnum]))
		user_cats[cid].remove(catnum)
		sendQuestion(catnum,qnum,cid)
	else:
		answerSelect = types.ReplyKeyboardMarkup(one_time_keyboard=True)
		answerSelect.add('Boy.','Girl.')
		bot.send_message(cid, "Are you a boy or a girl?", reply_markup=answerSelect)


@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    if not cid in stats:  # if user hasn't used the "/start" command yet:
        stats[cid]=[0]*14 
        user_step[cid] = 0
        bot.send_message(cid, "Hello, stranger, let me scan you...")
        bot.send_message(cid, "Scanning complete, I know you now")
    else:
        bot.send_message(cid, "your id is"+str(cid))


@bot.message_handler(commands=['help'])
def send_help(m):
	bot.reply_to(m, "help")


@bot.message_handler(commands=['cancel'])
def cancel_action(m):
	bot.reply_to(m, "cancel")


@bot.message_handler(commands=['newtest'])
def new_test(m):
	cid = m.chat.id
	bot.reply_to(m, "newtest")
	stats[cid]=[0]*14
	user_cats[cid]=set(range(MAX_QUEST)) #######
	user_step[cid] = 0
	newQuestion(cid)

@bot.message_handler(func=lambda message: user_step[message.chat.id] > MAX_QUEST) ####
def getSex(m):
	cid = m.chat.id
	print(m.text)
	print(stats[cid])

@bot.message_handler(func=lambda message: user_step[message.chat.id] > 0)
def getAnswer(m):
	cid = m.chat.id
	text = m.text
	rewards = lastQuestion[cid].answers[ord(text[0])-ord('a')].rewards
	for i in range(len(rewards)):
		stats[cid][rewards[i].a] += rewards[i].b
	print(stats[cid])
	if(lastQuestion[cid].number == 10 and m.text[0] == 'a'):
		sendQuestion(0,2,cid)
	else:
		newQuestion(cid)

bot.polling()


"""
action Keyboard

from telebot import types

markup = types.ReplyKeyboardMarkup()
markup.add('a', 'v', 'd')
tb.send_message(chat_id, message, None, None, markup)
# or use row method
markup = types.ReplyKeyboardMarkup()
markup.row('a', 'v')
markup.row('c', 'd', 'e')
tb.send_message(chat_id, message, None, None, markup)
"""

