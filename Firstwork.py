#count=0
# count1=0
# num_words=int(input("How many words to analyse?"))
# print("Ok-I will analyse",num_words,"words")
# words=[0 for i in range(num_words)]
# for i in range(num_words):
#   words[i]=input("words:")
# print(words)
# check=words[0]
# cnum=len(check)
# for j in range(cnum):
#    if(check[j]=="a"):
#     print("vowel")
#     count=count+1
#    elif(check[j]=="e"):
#     print("vowel")
#     count=count+1
#    elif(check[j]=="i"):
#     print("vowel")
#     count=count+1
#    elif(check[j]=="o"):
#     print("vowel")
#     count=count+1
#    elif(check[j]=="u"):
#     print("vowel")
#     count=count+1
    
#    else:
#     print("letter")
#     count1=count1+1
#     print("count letter:",count1)
#    print("count vowel:",count)

# from array import *
# arrey1 = array('i',[1,2,3,4,5,6,7,8,9,10])
# arrey2 = array('i',[0,0,0])
# arrey3 = array('i',[0,0,0])
# for i in range(3):
#  arrey2[i]=int(input("Your num:"))
#  arrey1.append(arrey2[i])
#  arrey3[i]=arrey1.index(arrey2[i])
# print(arrey1)
# print(arrey3)

# from array import *
# subject =(["english","math","science"])
# credit = array('i',[3,4,2])
# grade = array('i',[4,3,3])
# print(subject)
# print(credit)
# print(grade)
# ask=input("Do you want to change your grade?(yes/no)")
# while(ask=="yes"):
#     subject1=input("Which subjects?")
#     index = subject.index(subject1)
#     print('The index of',subject1,index)
#     newgrade=int(input("What is the new grade?"))
#     grade[index] = newgrade
#     print(subject1)
#     print(grade[index])
#     ask=input("Do you want to change your grade?(yes/no)")

list=[]
dict={'subject':'unknown','credit':0,'grade':0}
ask1=input("Do want to add subject?(yes/no):")
while(ask1=='yes'):
     subject=input("Your subject:")
     credit=int(input("Your credit:"))
     grade=int(input("Your grade:"))
     dict['subject']=subject
     dict['credit']=credit
     dict['grade']=grade
     lists={'subject':subject,'credit':credit,'grade':grade}
     list.append(lists)
     ask1=input("Do want to add subject?(yes/no):")
     print(list)
ask2=input("Do you want to change your grade?(yes/no):")
while(ask2=='yes'):
     yoursubject=input("Which subject?:")
     dict['subject']=yoursubject
     newgrade=int(input("Your new grade?:"))
     dict['grade']=newgrade
     print("'subject'",dict['subject'])
     print("'grade'",dict['grade'])
     ask2=input("Do you want to change your grade?(yes /no):")


    




    





