import random
from pynput.keyboard import Key,Controller
import time 
import math

limited_monkey=Controller()

chapter_name=["Chapter 0","Chapter 1,", "Chapter 2,","Chapter 3, "," Chapter 4,"]
randj = []
f = open('shake.txt','r')

for line in f:
    randj.append(line.strip()) # We don't want newlines in our list, do we?
#print(randj)
f.close()

#newshakeopen= open('new_shake.txt', 'w')
#newshakeopen.writelines(randj)
#newshakeopen.close()

print(randj[0])
print(len(randj))
monkey_limit=0
#If harold starts typing nonesense, give him more bananas and less coffee 
chapter_count=1
time.sleep(3)
while chapter_count <= 4:
    #print(chapter_count,"chap count")
    random_chapter_length=random.randint(100,750)
    monkey_limit=0
    chapter_char_num=0
    which_chapter=chapter_name[chapter_count]
    print("chap char number after 0", chapter_char_num)

    limited_monkey.press(Key.enter)
    limited_monkey.release(Key.enter)
    limited_monkey.press(Key.enter)
    limited_monkey.release(Key.enter)

    while which_chapter[chapter_char_num] != ',':

        limited_monkey.press(which_chapter[chapter_char_num])
        limited_monkey.release(which_chapter[chapter_char_num])
        print(which_chapter[chapter_char_num])
        chapter_char_num+=1
    print(chapter_char_num,"chap char num")
    chapter_char_num=0
    print("chap char num after second 0", chapter_char_num)
    
    limited_monkey.press(Key.enter)
    limited_monkey.release(Key.enter)
    limited_monkey.press(Key.enter)
    limited_monkey.release(Key.enter)
    limited_monkey.press(Key.enter)
    limited_monkey.release(Key.enter)
    
    while monkey_limit < random_chapter_length:
        charnum=0
        random_monkey_word= random.randint(0,15093)
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
        except:
           # limited_monkey.press(Key.space)
            #limited_monkey.release(Key.space)
            continue
        monkey_limit+=1
    chapter_count+=1
    #print(charnum, "charnum")
    