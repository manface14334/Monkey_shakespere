import random
from pynput.keyboard import Key,Controller
import time 
import os
import gtts


title=["My Rant"]
signature=["By: Cave Johnson"]
#rant_name = ["Rant 1", "Rant 2", "Rant 3", "Rant 4", "Rant 5", "Rant 6", ]
limited_monkey=Controller()
randj = []
f = open('cave_john.txt','r')

for line in f:
    randj.append(line.replace(' ',' ')) # We don't want newlines in our list, do we?
#print(randj)
f.close()

print(randj[0])
print(len(randj))
john_limit=0

time.sleep(1.5)
Title_end=0
Written_end=0
start_end= False

Title_char=0
title_simple=title[0]

sig_char=0
sig_simple=signature[0]

if start_end != True:
    while Title_char < len(title_simple):
        limited_monkey.press(title_simple[Title_char])
        limited_monkey.release(title_simple[Title_char])    
        Title_char+=1
    
    limited_monkey.press(Key.enter)
    limited_monkey.release(Key.enter)
    limited_monkey.press(Key.enter)
    limited_monkey.release(Key.enter)
    while sig_char < len(sig_simple):
        limited_monkey.press(sig_simple[sig_char])
        limited_monkey.release(sig_simple[sig_char])    
        sig_char+=1
    start_end=True    
limited_monkey.press(Key.enter)
limited_monkey.release(Key.enter)
limited_monkey.press(Key.enter)
limited_monkey.release(Key.enter)

how_many_rants=random.randint(10,20) #change this variable to change amount of rants
rant_count=1


time.sleep(3)
while rant_count <= how_many_rants:
    limited_monkey.press(Key.enter)
    limited_monkey.release(Key.enter)
    time.sleep(1)
    #print(rant_count,"chap count")
    limited_monkey.press(Key.enter)
    limited_monkey.release(Key.enter)
    ranter_heading= str("Rant " + str(rant_count))
    limited_monkey.type(ranter_heading)
    limited_monkey.press(Key.enter)
    limited_monkey.release(Key.enter)

    random_rant_length=random.randint(20,100)#change this to change rant length
    monkey_limit=0
    rant_char_num=0
    
    #print("chap char number after 0", rant_char_num)

    limited_monkey.press(Key.enter)
    limited_monkey.release(Key.enter)
  
    
    while john_limit < random_rant_length:
        
        charnum=0
        random_monkey_word= random.randint(0,74)# The end number is the number of lines in shake.txt minus 1 line because of lists
        smallerword=randj[random_monkey_word]
        limited_monkey.press(Key.space)
        limited_monkey.release(Key.space)
        time.sleep(0.02)
        try:
            while smallerword[charnum] != ' ':
                
                limited_monkey.press(smallerword[charnum])
                limited_monkey.release(smallerword[charnum])
                #print("the random is: ", random_monkey_word, "the answer is ", random_monkey_word/2)
                
                #wordtwo= random_monkey_word%2
                #wordone= random_monkey_word%10
                #if wordtwo == 0 and wordone ==0 :
                 #   limited_monkey.press(Key.space)
                  #  limited_monkey.release(Key.space)
                charnum+=1
           # limited_monkey.press(Key.space)
            #limited_monkey.release(Key.space)
        except:
           # limited_monkey.press(Key.space)
            #limited_monkey.release(Key.space)
            continue
        john_limit+=1
    john_limit = 0
    rant_count+=1
    
    #print(charnum, "charnum")
