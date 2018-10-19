
import logging
logging.captureWarnings(True)

import sys
import codecs
from kitchen.text.converters import getwriter
UTF8Writer = getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)

import telebot
from telebot import types

with open('token.txt', 'r') as myfile:
    TOKEN=myfile.read().replace('\n', '')
bot = telebot.TeleBot(TOKEN)

import pickle
import random
import time
seed = int(time.time())%1000000
print("the seed is "+str(seed))
from sets import Set
from questions import generateQuestionPool

class Categories:
	hardy , docile, brave, jolly, impish, naive, timid, hasty, sassy, calm, relaxed, lonely, quirky = range(13)

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

questionPool = generateQuestionPool()

stats = {}
user_step = {}
lastQuestion = {}
user_cats = {}
gender = {}
MAX_QUEST = 8
MAX_STAT = {}
POKEMONS = [["Charmander","Pikachu"],["Bulbasaur","Chikorita"],["Machop","Charmander"],["Squirtle","Totodile"],["Pikachu","Cubone"],["Totodile","Eevee"],["Cyndaquil","Mudkip"],["Torchic","Skitty"],["Treecko","Torchic"],["Mudkip","Bulbasaur"],["Psyduck","Squirtle"],["Cubone","Psyduck"],["Meowth","Treecko"]]
ME = 170303987
"""
def test(cid):
	for i in range(len(POKEMONS)):
		pokemon = POKEMONS[i][0]
		bot.send_photo(cid, open("Pics/"+pokemon+".png", 'rb'))
		pokemon = POKEMONS[i][1]
		bot.send_photo(cid, open("Pics/"+pokemon+".png", 'rb'))
"""

def sendWelcome():
	for i in stats:
		bot.send_message(i, "Sorry, my developer really needs some sleep... Anyway, the bot is up and running again!")

def loadStuff():
	global MAX_STAT
	global stats
	global user_step
	global gender
	global user_cats
	global lastQuestion
	__MAX_STAT= open(r'maxstat', 'rb')
	MAX_STAT = pickle.load(__MAX_STAT)
	__MAX_STAT.close()

	__stats = open(r'stats', 'rb')
	stats = pickle.load(__stats)
	__stats.close()

	__user_step= open(r'userstep','rb')
	user_step = pickle.load( __user_step)
	__user_step.close()

	__gender= open(r'gender', 'rb')
	gender = pickle.load(__gender)
	__gender.close()

	__user_cats= open(r'usercats', 'rb')
	user_cats = pickle.load(__user_cats)
	__user_cats.close()

	__lastQuestion= open(r'lastQuestion', 'rb')
	lastQuestion = pickle.load(__lastQuestion)
	__lastQuestion.close()


def saveMaxStat():
	__MAX_STAT = open(r'maxstat','wb')
	pickle.dump(MAX_STAT, __MAX_STAT)
	__MAX_STAT.close()

def saveStats():

	__stats= open(r'stats','wb')
	pickle.dump(stats, __stats)
	__stats.close()

def saveUserStep():

	__user_step= open(r'userstep','wb')
	pickle.dump(user_step, __user_step)
	__user_step.close()

def saveGender():

	__gender= open(r'gender','wb')
	pickle.dump(gender, __gender)
	__gender.close()

def saveUserCats():

	__user_cats= open(r'usercats','wb')
	pickle.dump(user_cats, __user_cats)
	__user_cats.close()

def saveLastQuestion():
	__lastQuestion= open(r'lastQuestion','wb')
	pickle.dump(lastQuestion, __lastQuestion)
	__lastQuestion.close()

def saveData():
	saveMaxStat()
	saveStats()
	saveUserStep()
	saveGender()
	saveUserCats()
	saveLastQuestion()


def calculate(cid):
	global MAX_STAT
	text = ""
	cats = ["*Hardy*" , "*Docile*", "*Brave*", "*Jolly*", "*Impish*", "*Naive*", "*Timid*", "*Hasty*", "*Sassy*", "*Calm*", "*Relaxed*", "*Lonely*", "*Quirky*"]
	for i in range(len(stats[cid])):
		text += cats[i]+": "+str(stats[cid][i])+"\n"
		if stats[cid][i] > MAX_STAT[cid].b:
			MAX_STAT[cid] = Pair(i,stats[cid][i])
			saveMaxStat()
	#bot.send_message(cid, text, parse_mode="Markdown")
	bot.send_message(cid, "Done!")
	print(text)
	bot.send_message(cid, "Your pokemon should be...")
	pokemon = POKEMONS[MAX_STAT[cid].a][gender[cid]]
	bot.send_message(cid, pokemon+"!!!")
	print(str(cid)+": "+pokemon)
	resetUser(cid)
	bot.send_photo(cid, open("Pics/"+pokemon+".png", 'rb'))

def resetUser(cid):
	MAX_STAT[cid]=Pair(-1,-1)
	stats[cid]=[0]*13
	user_step[cid] = 0
	gender[cid] = 0
	user_cats[cid]=set(range(14)) #######
	lastQuestion[cid] = None
	saveData()



def sendQuestion(catnum, qnum, cid):
	user_step[cid] += 1
	saveUserStep()
	print(str(cid)+": userstep just increased, is at "+str(user_step[cid]))
	print(str(cid)+": "+"sending question "+str(catnum)+" "+str(qnum)+": "+str(questionPool[catnum][qnum].number))
	lastQuestion[cid] = questionPool[catnum][qnum]
	saveLastQuestion()
	answerSelect = types.ReplyKeyboardMarkup(one_time_keyboard=True)
	lenght = len(questionPool[catnum][qnum].answers)
	for i in range(0,lenght):
		answerSelect.add(chr(ord('a')+i)+") "+questionPool[catnum][qnum].answers[i].title)
	bot.send_message(cid, questionPool[catnum][qnum].title, reply_markup=answerSelect)


def newQuestion(cid):
	if(user_step[cid] < MAX_QUEST):
		catnum = random.sample(user_cats[cid],1)[0]
		print(str(cid)+": "+"new catnum is "+str(catnum))
		qnum = random.randint(0,len(questionPool[catnum])-1)
		print(str(cid)+": "+"new qnum is "+str(qnum))
		print(str(cid)+": "+"drawn question "+str(questionPool[catnum][qnum].number))
		while questionPool[catnum][qnum].number == 11:
			qnum = random.randint(0,len(questionPool[catnum])-1)
			print(str(cid)+": "+"drawn question "+str(questionPool[catnum][qnum].number))

		user_cats[cid].remove(catnum)
		saveUserCats()
		sendQuestion(catnum,qnum,cid)
	else:
		user_step[cid] += 1
		saveUserStep()
		answerSelect = types.ReplyKeyboardMarkup(one_time_keyboard=True)
		answerSelect.add('Boy.','Girl.')
		bot.send_message(cid, "Are you a boy or a girl?", reply_markup=answerSelect)

"""  switch to debug
@bot.message_handler(func=lambda message: not message.chat.id == ME)
def debugging(m):
    cid = m.chat.id
    bot.send_message(cid, "we are fixing some issues, please try again later")
#"""


@bot.message_handler(func=lambda message: message.chat.id == ME and message.text[0] == '!') ####
def echo(m):
	cid = m.chat.id
	#print(m.from_user.first_name+": "+m.text)
	hideBoard = types.ReplyKeyboardHide()
	#bot.send_message(cid, "I'm sorry, I did not understand '"+m.text+"', use /help for a list of commands, or /answers to display de current answer keyboard.", reply_markup=hideBoard)
	#test(cid)
	if m.text == '!allusers':
		bot.send_message(cid, str(len(stats)), reply_markup=hideBoard)
	elif m.text == '!active':
		active = ''
		for i in user_step:
			if user_step[i] > 0:
				active += str(i)+'\n'
		bot.send_message(cid, active, reply_markup=hideBoard)

@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    hideBoard = types.ReplyKeyboardHide()
    if not cid in stats:  # if user hasn't used the "/start" command yet:
        resetUser(cid)
        bot.send_message(cid, "Welcome to the Pokemon personality test bot, i will add you to my database...", reply_markup=hideBoard)
        bot.send_message(cid, "Scanning complete, you can use the bot now. Use /help for a list of avalible commands.")
    else:
        bot.send_message(cid, "Welcome back user "+str(cid)+", need some /help ?")

@bot.message_handler(commands=['help'])
def send_help(m):
	cid = m.chat.id
	helptext = "This bot tells you which pokemon you are, based on a personality test.\n Commands are: \n"
	helptext += "/start: starts the bot\n"
	helptext += "/help: displays this dialog \n"
	helptext += "/newtest: deletes your progress and starts a new test \n"
	helptext += "/answers: displays the last unanswered question and it's answer keyboard\n"
	helptext += "/cancel: cancels actual command\n"
	bot.send_message(cid, helptext)


@bot.message_handler(commands=['cancel'])
def cancel_action(m):
	cid = m.chat.id
	hideBoard = types.ReplyKeyboardHide()
	bot.send_message(cid, "Action canceled", reply_markup=hideBoard)
	resetUser(cid)

@bot.message_handler(commands=['stop'])
def stop(m):
	cid = m.chat.id
	bot.send_message(cid, "Do you want to leave? :( Well... \nTo stop this bot you have to enter the menu in the bot's profile and select the 'Stop bot' option")



@bot.message_handler(commands=['answers'])
def cancel_action(m):
	cid = m.chat.id
	answerSelect = types.ReplyKeyboardMarkup(one_time_keyboard=True)
	if not lastQuestion[cid] == None:
		lenght = len(lastQuestion[cid].answers)
		for i in range(0,lenght):
			answerSelect.add(chr(ord('a')+i)+") "+lastQuestion[cid].answers[i].title)
		bot.send_message(cid, "Last question was:\n"+lastQuestion[cid].title, reply_markup=answerSelect)
	else:
		hideBoard = types.ReplyKeyboardHide()
		bot.send_message(cid, "You don't have any active question. Type /newtest to start a new test", reply_markup=hideBoard)

@bot.message_handler(commands=['newtest'])
def new_test(m):
	global MAX_QUEST
	cid = m.chat.id
	bot.send_message(cid, "Let's start a new personality test!")
	resetUser(cid)
	newQuestion(cid)


@bot.message_handler(func=lambda message: user_step[message.chat.id] > MAX_QUEST) ####
def getSex(m):
	cid = m.chat.id
	if m.text == "Girl.":
		gender[cid] = 1
		saveGender()
	print(str(cid)+m.from_user.first_name+": "+m.text+" "+str(gender[cid]))
	print(str(cid)+m.from_user.first_name+": "+str(stats[cid]))
	hideBoard = types.ReplyKeyboardHide()
	bot.send_message(cid, "Great, you finished the test! Calculating your results...", reply_markup=hideBoard)
	calculate(cid)

@bot.message_handler(func=lambda message: user_step[message.chat.id] > 0)
def getAnswer(m):
	global MAX_QUEST
	cid = m.chat.id
	text = m.text
	print(str(cid)+m.from_user.first_name+": "+"got answer for question number: "+str(lastQuestion[cid].number))
	choice = ord(text[0])-ord('a')
	if choice >= len(lastQuestion[cid].answers) or choice < 0:
		print(str(cid)+m.from_user.first_name+" "+"invalid answer: "+m.text)
		bot.send_message(cid, "That is not a valid answer, try again.")
	else:
		rewards = lastQuestion[cid].answers[choice].rewards
		for i in range(len(rewards)):
			stats[cid][rewards[i].a] += rewards[i].b
			saveStats()
		print(str(cid)+m.from_user.first_name+": ")
		print(stats[cid])

		if(lastQuestion[cid].number == 10 and m.text[0] == 'a'):
			MAX_QUEST += 1
			sendQuestion(2,2,cid)
		else:
			newQuestion(cid)

@bot.message_handler(func=lambda message: True) ####
def echo(m):
	cid = m.chat.id
	print(m.from_user.first_name+": "+m.text)
	hideBoard = types.ReplyKeyboardHide()
	bot.send_message(cid, "I'm sorry, I did not understand '"+m.text+"', use /help for a list of commands, /answers to display de current answer keyboard or try sending your request again later.", reply_markup=hideBoard)
	#test(cid)

loadStuff()
#sendWelcome()
bot.polling()
