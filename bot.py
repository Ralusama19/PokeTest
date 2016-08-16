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

questionPool = [None]*14

questionPool[0]=hardyPool

"""
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
"""
stats = {}
user_step = {}
lastQuestion = {}
user_cats = {}

def sendQuestion(catnum, qnum):
	user_step[cid] += 1
	lastQuestion[cid] = questionPool[catnum][qnum]
	answerSelect = types.ReplyKeyboardMarkup(one_time_keyboard=True)
	lenght = len(questionPool[catnum][qnum].answers)
	for i in range(0,lenght):
		answerSelect.add(chr(ord('a')+i)+") "+questionPool[catnum][qnum].answers[i].title)
	bot.send_message(cid, questionPool[catnum][qnum].title, reply_markup=answerSelect)

def newQuestion(cid):
	catnum = random.sample(user_cats[cid],1)[0]
	qnum = random.randint(0,len(questionPool[catnum]))
	user_cats[cid].remove(catnum)
	sendQuestion(catnum,qnum)

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
	user_cats[cid]=set(range(14))
	#catnum = random.randint(0,13)
	catnum = 0 #placeholder
	qnum = random.randint(0,len(questionPool[catnum]))
	#qnum = 0
	answerSelect = types.ReplyKeyboardMarkup(one_time_keyboard=True)
	lenght = len(questionPool[catnum][qnum].answers)
	for i in range(0,lenght):
		answerSelect.add(chr(ord('a')+i)+") "+questionPool[catnum][qnum].answers[i].title)
	bot.send_message(cid, questionPool[catnum][qnum].title, reply_markup=answerSelect)
	user_step[cid] = 1
	lastQuestion[cid] = questionPool[catnum][qnum]
	user_cats[cid].remove(catnum)

@bot.message_handler(func=lambda message: user_step[message.chat.id] > 0)
def getAnswer(m):
	cid = m.chat.id
	text = m.text
	rewards = lastQuestion[cid].answers[ord(text[0])-ord('a')].rewards
	for i in range(len(rewards)):
		stats[cid][rewards[i].a] += rewards[i].b
	print(stats[cid])
	nextQuestion = None
	if(lastQuestion[cid].number == 10 and m.text[0] == 'a'):
		sendQuestion(0,2)
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

