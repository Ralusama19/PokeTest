from bot import Categories, Pair, Answer, Question

def generateQuestionPool():
    questionPool = [None]*14

    ########################################################
    ######################################################################################### 0
    ########################################################

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

    ########################################################
    #######################################################################################  1
    ########################################################
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

    ########################################################
    ################################################################################### 2
    ########################################################
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
    ########################################################
    #################################################################################### 3
    ########################################################
    jollyPool = []

    q = Question("Are you a cheerful personality?",13)

    a = Answer("Yes.")
    a.addReward(Categories.jolly,2)
    a.addReward(Categories.naive,1)

    b = Answer("No.")
    b.addReward(Categories.sassy,1)
    b.addReward(Categories.quirky,2)

    q.addAnswer(a)
    q.addAnswer(b)

    jollyPool.append(q)

    q = Question("Do you like to noisily enjoy yourself with others?",14)

    a = Answer("Yes.")
    a.addReward(Categories.jolly,2)
    a.addReward(Categories.lonely,1)

    b = Answer("No.")
    b.addReward(Categories.timid,1)

    q.addAnswer(a)
    q.addAnswer(b)

    jollyPool.append(q)


    q = Question("It's the summer holidays! Where would you like to go?",15)

    a = Answer("The beach!")
    a.addReward(Categories.jolly,2)

    b = Answer("Spas.")
    b.addReward(Categories.calm,2)

    c = Answer("Anywhere.")
    c.addReward(Categories.quirky,2)

    q.addAnswer(a)
    q.addAnswer(b)
    q.addAnswer(c)

    jollyPool.append(q)


    q = Question("A foreign person has started up a conversation with you. To be honest, you don't have a clue what this fellow is saying. How do you reply?",16)

    a = Answer("Haha! Yes. Very funny!")
    a.addReward(Categories.jolly,3)

    b = Answer("Um... Could you say that again?")
    b.addReward(Categories.hardy,2)

    c = Answer("Right... Well, I gotta go.")
    c.addReward(Categories.timid,2)

    q.addAnswer(a)
    q.addAnswer(b)
    q.addAnswer(c)

    jollyPool.append(q)

    questionPool[3]=jollyPool
    ########################################################
    #################################################################################### 4
    ########################################################
    impishPool = []

    q = Question("Have you ever made a pitfall trap?",17)

    a = Answer("Yes.")
    a.addReward(Categories.impish,2)
    a.addReward(Categories.lonely,1)

    b = Answer("No.")
    b.addReward(Categories.calm,2)

    q.addAnswer(a)
    q.addAnswer(b)

    impishPool.append(q)

    q = Question("Do you like pranks?",18)

    a = Answer("Yes.")
    a.addReward(Categories.impish,2)

    b = Answer("No.")
    b.addReward(Categories.docile,1)
    b.addReward(Categories.relaxed,1)

    q.addAnswer(a)
    q.addAnswer(b)

    impishPool.append(q)

    q = Question("Are there many things that you would like to do? ",19)

    a = Answer("Yes.")
    a.addReward(Categories.impish,2)
    a.addReward(Categories.hardy,1)

    b = Answer("No.")
    b.addReward(Categories.sassy,1)
    b.addReward(Categories.quirky,2)

    q.addAnswer(a)
    q.addAnswer(b)

    impishPool.append(q)

    q = Question("Your friend is being bullied! What do you do? ",20)

    a = Answer("Face up to the bully.")
    a.addReward(Categories.brave,3)

    b = Answer("Caution the bully from afar.")
    b.addReward(Categories.timid,2)

    c = Answer("Heckle the bully from behind.")
    c.addReward(Categories.impish,2)

    q.addAnswer(a)
    q.addAnswer(b)
    q.addAnswer(c)

    impishPool.append(q)


    questionPool[4]=impishPool
    ########################################################
    ########################################################################################### 5
    ########################################################
    naivePool = []

    q = Question("Do you like groan-inducing puns? ",21)

    a = Answer("Love them!")
    a.addReward(Categories.impish,1)
    a.addReward(Categories.naive,3)

    b = Answer("A little.")
    b.addReward(Categories.jolly,2)


    c = Answer("Spare me.")
    c.addReward(Categories.sassy,2)

    q.addAnswer(a)
    q.addAnswer(b)
    q.addAnswer(c)

    naivePool.append(q)


    q = Question("Do you tend to laugh a lot?",22)

    a = Answer("Yes.")
    a.addReward(Categories.docile,1)
    a.addReward(Categories.naive,2)

    b = Answer("No.")
    b.addReward(Categories.quirky,2)

    q.addAnswer(a)
    q.addAnswer(b)

    naivePool.append(q)


    q = Question("Do others often call you childish?",23)

    a = Answer("Yes.")
    a.addReward(Categories.jolly,1)
    a.addReward(Categories.naive,2)

    b = Answer("No.")
    b.addReward(Categories.calm,2)

    q.addAnswer(a)
    q.addAnswer(b)

    naivePool.append(q)


    q = Question("Do you like to imagine things for your amusement? ",24)

    a = Answer("Yes.")
    a.addReward(Categories.naive,2)

    b = Answer("No.")
    b.addReward(Categories.hasty,2)

    q.addAnswer(a)
    q.addAnswer(b)

    naivePool.append(q)

    questionPool[5]=naivePool

    ########################################################
    ############################################################################### 6
    ########################################################
    timidPool = []

    q = Question(" A human hand extends out of a toilet! What would you do? ",25)

    a = Answer("Scream and run.")
    a.addReward(Categories.timid,2)

    b = Answer("Close the lid without a word.")
    b.addReward(Categories.calm,2)
    b.addReward(Categories.hardy,1)

    c = Answer("Shake hands with it.")
    c.addReward(Categories.brave,2)
    c.addReward(Categories.naive,1)
    c.addReward(Categories.impish,1)

    q.addAnswer(a)
    q.addAnswer(b)
    q.addAnswer(c)

    timidPool.append(q)


    q = Question("Grab any digit on your left hand with your right hand. Which digit did you grab? ",26)

    a = Answer("Thumb.")
    a.addReward(Categories.timid,2)

    b = Answer("Index finger.")
    b.addReward(Categories.hasty,2)

    c = Answer("Middle finger.")
    c.addReward(Categories.jolly,2)

    d = Answer("Ring finger.")
    d.addReward(Categories.sassy,2)

    e = Answer("Little finger.")
    e.addReward(Categories.lonely,2)

    q.addAnswer(a)
    q.addAnswer(b)
    q.addAnswer(c)
    q.addAnswer(d)
    q.addAnswer(e)

    timidPool.append(q)

    q = Question("You are suddenly locked inside a pitch-black room! What do you do? ",27)

    a = Answer("Kick the door.")
    a.addReward(Categories.timid,2)

    b = Answer("Cry.")
    b.addReward(Categories.lonely,2)

    c = Answer("Clean it.")
    c.addReward(Categories.impish,2)
    c.addReward(Categories.quirky,1)

    q.addAnswer(a)
    q.addAnswer(b)
    q.addAnswer(c)

    timidPool.append(q)

    q = Question("Can you go into a haunted house? ",28)

    a = Answer("No problem!")
    a.addReward(Categories.brave,3)

    b = Answer("Uh... N-no...")
    b.addReward(Categories.timid,2)

    c = Answer("With someone I like.")
    c.addReward(Categories.sassy,2)

    q.addAnswer(a)
    q.addAnswer(b)
    q.addAnswer(c)

    timidPool.append(q)

    questionPool[6]=timidPool


    ########################################################
    ############################################################################### 7
    ########################################################
    hastyPool = []

    q = Question("You receive a gift! But you don't know what's in it. You're curious, so what do you do?",29)

    a = Answer("Open it now.")
    a.addReward(Categories.hasty,2)

    b = Answer("Open it later.")
    b.addReward(Categories.calm,2)

    c = Answer("Get someone to open it.")
    c.addReward(Categories.timid,2)

    q.addAnswer(a)
    q.addAnswer(b)
    q.addAnswer(c)

    hastyPool.append(q)
    #-----------------
    q = Question("You win a lottery! What do you do with the money?", 30)

    a = Answer("Spend it now.")
    a.addReward(Categories.jolly,2)
    a.addReward(Categories.hasty,1)

    b = Answer("Save it.")
    b.addReward(Categories.calm,1)
    b.addReward(Categories.hardy,1)

    c = Answer("Give it away.")
    c.addReward(Categories.brave,2)
    c.addReward(Categories.quirky,2)

    q.addAnswer(a)
    q.addAnswer(b)
    q.addAnswer(c)

    hastyPool.append(q)
    #-----------------
    q = Question("You come across a treasure chest! What do you do?", 31)

    a = Answer("Open it right away!")
    a.addReward(Categories.hasty,2)

    b = Answer("No... Could be a trap...")
    b.addReward(Categories.timid,2)

    c = Answer("It's going to be empty...")
    c.addReward(Categories.sassy,2)

    q.addAnswer(a)
    q.addAnswer(b)
    q.addAnswer(c)

    hastyPool.append(q)
    #-----------------
    q = Question("Your friend fails to show up for a meeting at the promised time. What do you do?", 32)

    a = Answer("Become irritated.")
    a.addReward(Categories.docile,1)
    a.addReward(Categories.hasty,2)

    b = Answer("Wait patiently.")
    b.addReward(Categories.relaxed,2)

    c = Answer("Get angry and bail.")
    c.addReward(Categories.hasty,3)

    q.addAnswer(a)
    q.addAnswer(b)
    q.addAnswer(c)

    hastyPool.append(q)

    questionPool[7]=hastyPool


    ########################################################
    ############################################################################### 8
    ########################################################

    sassyPool = []

    q = Question("Your country's leader is in front of you. How do you speak to him or her?",33)

    a = Answer("Speak calmly.")
    a.addReward(Categories.hardy,2)

    b = Answer("Speak nervously.")
    b.addReward(Categories.docile,2)

    c = Answer("WHATEVER!!")
    c.addReward(Categories.sassy,2)

    q.addAnswer(a)
    q.addAnswer(b)
    q.addAnswer(c)

    sassyPool.append(q)
    #------------------
    q = Question("Do others tell you to watch what you say?",34)

    a = Answer("Yes.")
    a.addReward(Categories.impish,1)
    a.addReward(Categories.sassy,2)

    b = Answer("No.")
    b.addReward(Categories.calm,2)

    q.addAnswer(a)
    q.addAnswer(b)

    sassyPool.append(q)
    #------------------
    q = Question("Do you think you are cool? Be honest.",35)

    a = Answer("Yes.")
    a.addReward(Categories.sassy,2)

    b = Answer("No.")
    b.addReward(Categories.relaxed,2)

    q.addAnswer(a)
    q.addAnswer(b)

    sassyPool.append(q)
    #------------------
    q = Question("Can you sincerely thank someone when you feel grateful?",36)

    a = Answer("Yes.")
    a.addReward(Categories.docile,2)
    a.addReward(Categories.calm,1)

    b = Answer("No.")
    b.addReward(Categories.sassy,2)
    b.addReward(Categories.quirky,1)

    q.addAnswer(a)
    q.addAnswer(b)

    sassyPool.append(q)

    questionPool[8] = sassyPool



    ########################################################
    ############################################################################### 9
    ########################################################

    calmPool = []

    q = Question("Do you occasionally consider yourself dull and overly cautious? ",37)

    a = Answer("Yes.")
    a.addReward(Categories.calm,2)
    a.addReward(Categories.lonely,1)

    b = Answer("No.")
    b.addReward(Categories.hardy,2)

    q.addAnswer(a)
    q.addAnswer(b)

    calmPool.append(q)

    q = Question("Do you dream of lounging around idly without much excitement? ",38)

    a = Answer("Yes.")
    a.addReward(Categories.calm,2)

    b = Answer("No.")
    b.addReward(Categories.impish,2)

    q.addAnswer(a)
    q.addAnswer(b)

    calmPool.append(q)

    q = Question("Do you like to fight? ",39)

    a = Answer("Yes.")
    a.addReward(Categories.timid,2)
    a.addReward(Categories.impish,1)

    b = Answer("No.")
    b.addReward(Categories.calm,2)
    b.addReward(Categories.lonely,1)

    q.addAnswer(a)
    q.addAnswer(b)

    calmPool.append(q)


    q = Question("Do you often yawn?  ",40)

    a = Answer("Yes.")
    a.addReward(Categories.calm,2)
    a.addReward(Categories.relaxed,1)

    b = Answer("No.")
    b.addReward(Categories.hasty,2)
    b.addReward(Categories.hardy,1)

    q.addAnswer(a)
    q.addAnswer(b)

    calmPool.append(q)

    questionPool[9] = calmPool

    ########################################################
    ############################################################################### 10
    ########################################################

    relaxedPool = []

    q = Question("Are you often late for school or meetings? ",41)

    a = Answer("Yes.")
    a.addReward(Categories.relaxed,2)
    a.addReward(Categories.sassy,1)

    b = Answer("No.")
    b.addReward(Categories.hardy,2)
    b.addReward(Categories.hasty,1)

    q.addAnswer(a)
    q.addAnswer(b)

    relaxedPool.append(q)

    q = Question("Do you get the feeling that you've slowed down lately? ",42)

    a = Answer("Yes.")
    a.addReward(Categories.relaxed,2)

    b = Answer("No.")
    b.addReward(Categories.hasty,2)
    b.addReward(Categories.impish,1)

    q.addAnswer(a)
    q.addAnswer(b)

    relaxedPool.append(q)


    q = Question("It is a pleasant day at the beach. How do you feel? ",43)

    a = Answer("This feels great!")
    a.addReward(Categories.jolly,2)

    b = Answer("Snore...")
    b.addReward(Categories.relaxed,2)

    c = Answer("I want to go home soon!")
    c.addReward(Categories.hasty,2)

    q.addAnswer(a)
    q.addAnswer(b)
    q.addAnswer(c)

    relaxedPool.append(q)

    q = Question(" Do you fall asleep without noticing? ",44)

    a = Answer("Yes.")
    a.addReward(Categories.relaxed,2)
    a.addReward(Categories.calm,1)

    b = Answer("No.")
    b.addReward(Categories.hardy,2)

    q.addAnswer(a)
    q.addAnswer(b)

    relaxedPool.append(q)

    questionPool[10] = relaxedPool

    ########################################################
    ############################################################################### 11
    ########################################################



    lonelyPool = []

    q = Question("Do you feel lonesome when you are alone?",45)

    a = Answer("Yes.")
    a.addReward(Categories.lonely,2)
    a.addReward(Categories.timid,1)

    b = Answer("No.")
    b.addReward(Categories.sassy,2)

    q.addAnswer(a)
    q.addAnswer(b)

    lonelyPool.append(q)


    q = Question("Do you hate to be the last person to leave class at the end of a school day?",46)

    a = Answer("Yes.")
    a.addReward(Categories.lonely,2)
    a.addReward(Categories.timid,1)

    b = Answer("No.")
    b.addReward(Categories.brave,3)
    b.addReward(Categories.relaxed,1)

    q.addAnswer(a)
    q.addAnswer(b)

    lonelyPool.append(q)

    q = Question("What do you do with your room's light when you're going to bed at night?",47)

    a = Answer("Leave it on.")
    a.addReward(Categories.lonely,2)
    a.addReward(Categories.timid,1)

    b = Answer("Turn it off.")
    b.addReward(Categories.calm,2)

    q.addAnswer(a)
    q.addAnswer(b)

    lonelyPool.append(q)

    q = Question("It's a weekend, but no one will play with you... What do you do?",48)

    a = Answer("Go on a trip.")
    a.addReward(Categories.jolly,1)
    a.addReward(Categories.lonely,1)

    b = Answer("Hang around vacantly.")
    b.addReward(Categories.calm,1)
    b.addReward(Categories.relaxed,2)

    c = Answer("Huddle in a corner.")
    c.addReward(Categories.timid, 1)
    c.addReward(Categories.lonely, 3)


    q.addAnswer(a)
    q.addAnswer(b)
    q.addAnswer(c)

    lonelyPool.append(q)

    questionPool[11] = lonelyPool


    ########################################################
    ############################################################################### 12
    ########################################################


    quirkyPool = []

    q = Question("Do you sometimes run out of things to do all of a sudden?",49)

    a = Answer("Yes.")
    a.addReward(Categories.quirky,2)

    b = Answer("No.")
    b.addReward(Categories.hardy,2)

    q.addAnswer(a)
    q.addAnswer(b)

    quirkyPool.append(q)

    q = Question("How quickly do you respond to an e-mail?",50)

    a = Answer("Reply right away.")
    a.addReward(Categories.hardy,1)
    a.addReward(Categories.hasty,1)

    b = Answer("May replay, may not.")
    b.addReward(Categories.quirky,2)

    c = Answer("Too much trouble")
    c.addReward(Categories.sassy,2)

    q.addAnswer(a)
    q.addAnswer(b)
    q.addAnswer(c)

    quirkyPool.append(q)

    q = Question("There is a person you like... But there's no opportunity to get close. What do you do?",51)

    a = Answer("Bravely declare my love.")
    a.addReward(Categories.hardy,1)
    a.addReward(Categories.brave,3)

    b = Answer("Might say hello...")
    b.addReward(Categories.quirky,2)

    c = Answer("Pull a prank to get attention.")
    c.addReward(Categories.impish,2)

    d = Answer("Look from afar.")
    d.addReward(Categories.timid,2)

    q.addAnswer(a)
    q.addAnswer(b)
    q.addAnswer(c)
    q.addAnswer(d)

    quirkyPool.append(q)

    q = Question("The road forks to the right and left. You are told there is a treasure on the right side. What do you do?",52)

    a = Answer("Instantly go right.")
    a.addReward(Categories.docile,2)

    b = Answer("It's a trap! Go left.")
    b.addReward(Categories.sassy,2)

    c = Answer("Choose either side.")
    c.addReward(Categories.quirky,2)

    q.addAnswer(a)
    q.addAnswer(b)
    q.addAnswer(c)

    quirkyPool.append(q)

    questionPool[12] = quirkyPool


    ########################################################
    ############################################################################### 13
    ########################################################

    miscPool = []

    q = Question("On vacation outings, you want to... ",53)

    a = Answer("Go alone.")
    a.addReward(Categories.hasty,1)
    a.addReward(Categories.quirky,1)

    b = Answer("Go with others.")
    b.addReward(Categories.jolly,1)
    b.addReward(Categories.lonely,1)

    q.addAnswer(a)
    q.addAnswer(b)

    miscPool.append(q)


    q = Question("It's the summer festival! Do you like carnivals? ",54)

    a = Answer("Love them!")
    a.addReward(Categories.jolly,2)

    b = Answer("Don't care.")
    b.addReward(Categories.sassy,1)
    b.addReward(Categories.quirky,1)

    q.addAnswer(a)
    q.addAnswer(b)

    miscPool.append(q)

    q = Question('Somebody calls you "weird but funny." How does that make you feel?',55)

    a = Answer("Happy!")
    a.addReward(Categories.lonely,1)
    a.addReward(Categories.naive,1)

    b = Answer("Not happy.")
    b.addReward(Categories.sassy,1)
    b.addReward(Categories.hasty,1)

    q.addAnswer(a)
    q.addAnswer(b)

    miscPool.append(q)

    questionPool[13] = miscPool
    return questionPool
