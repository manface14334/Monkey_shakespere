import random
from pynput.keyboard import Key,Controller
import time 


limited_monkey=Controller()

title=["My Shakespere Play"]
signature=["Written by: Harold"]
chapter_name=["Chapter 0","Chapter 1,", "Chapter 2,","Chapter 3, "," Chapter 4,","Chapter 5,", "Chapter 6,", "Chapter 7,", "Chapter 8,", "Chapter 9, ", "Chapter 10,","Chapter 11,","Chapter 12,","Chapter 13,","Chapter 14,","Chapter 15,", "Chapter 16,","Chapter 17,","Chapter 18,","Chapter 19,", "Chapter 20,","Chapter 21,","Chapter 22,","Chapter 23","Chapter 24","Chapter 25","Chapter 26","Chapter 27","Chapter 28","Chapter 29","Chapter 30","Chapter 31","Chapter 32","Chapter 33","Chapter 34","Chapter 35"]
randj = []
f = open('shake.txt','r')

for line in f:
    randj.append(line.replace('\n',' ')) # We don't want newlines in our list, do we?
#print(randj)
f.close()

#newshakeopen= open('new_shake.txt', 'w')
#newshakeopen.writelines(randj)
#newshakeopen.close()

print(randj[0])
print(len(randj))
monkey_limit=0
#If harold starts typing nonesense, give him more bananas and less coffee 
#current plays: Macbeth, Tempest, Hamlet, Othello, R&J
time.sleep(3)#3 seconds to get ready for a novel
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

how_many_chapters=random.randint(10,22)
chapter_count=1
time.sleep(3)
while chapter_count <= how_many_chapters:
    time.sleep(5)
    #print(chapter_count,"chap count")
    random_chapter_length=random.randint(300,1050)
    monkey_limit=0
    chapter_char_num=0
    which_chapter=chapter_name[chapter_count]
    #print("chap char number after 0", chapter_char_num)

    limited_monkey.press(Key.enter)
    limited_monkey.release(Key.enter)
    limited_monkey.press(Key.enter)
    limited_monkey.release(Key.enter)

    while which_chapter[chapter_char_num] != ',':

        limited_monkey.press(which_chapter[chapter_char_num])
        limited_monkey.release(which_chapter[chapter_char_num])
        print(which_chapter[chapter_char_num])
        chapter_char_num+=1
    #print(chapter_char_num,"chap char num")
    chapter_char_num=0
    #print("chap char num after second 0", chapter_char_num)
    
    limited_monkey.press(Key.enter)
    limited_monkey.release(Key.enter)
    limited_monkey.press(Key.enter)
    limited_monkey.release(Key.enter)
    limited_monkey.press(Key.enter)
    limited_monkey.release(Key.enter)
    
    while monkey_limit < random_chapter_length:
        charnum=0
        random_monkey_word= random.randint(0,21197)# The end number is the number of lines in shake.txt minus 1 line because of lists
        smallerword=randj[random_monkey_word]
        try:
            while smallerword[charnum] != ' ':
                
                limited_monkey.press(smallerword[charnum])
                limited_monkey.release(smallerword[charnum])
                #print("the random is: ", random_monkey_word, "the answer is ", random_monkey_word/2)
                
                wordtwo= random_monkey_word%2
                wordone= random_monkey_word%10
                if wordtwo == 0 and wordone ==0 :
                    limited_monkey.press(Key.space)
                    limited_monkey.release(Key.space)
                charnum+=1
           # limited_monkey.press(Key.space)
            #limited_monkey.release(Key.space)
        except:
           # limited_monkey.press(Key.space)
            #limited_monkey.release(Key.space)
            continue
        monkey_limit+=1
    chapter_count+=1
    #print(charnum, "charnum")
