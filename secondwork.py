# subjects=[]
# grades=[]
# ask1=input("Do want to add subject?(yes/no):")
# while(ask1=='yes'):
#      subject=input("Your subject:")
#      grade=int(input("Your grade:"))
#      subjects.append(subject)
#      grades.append(grade)
#      dict1=dict(zip(subjects,grades))
#      ask1=input("Do you want to add subject?(yes/no):")
#      print(dict1)
#      print("min",min(dict1,key=dict1.get))
#      print("max",max(dict1,key=dict1.get))
# ask2=input("Do you want to change your grade?(yes/no):")
# while(ask2=='yes'):
#      yoursubject=input("Which subject?:")
#      dict1['subject']=yoursubject
#      yournewgrade=int(input("Your new grade?:"))
#      dict1['grade']=yournewgrade
#      print(dict1['subject'])
#      print(dict1['grade'])
#      ask2=input("Do you want to change your grade?(yes/no):")

# items=[]
# mode=input("Enter mode(q-quit,b=booking,c=cancel,p=print booking):")
# while(mode!="q"):
#  if(mode=="b"):
#     name=input("Your name:")
#     checkin=int(input("enter checkin day:"))
#     checkout=int(input("enter checkout day:"))
#     if(checkin>checkout):
#      print("error")
#     hotel=input("your hotel's name ?:")
#     booknumber=hotel,checkin,checkout
#     smoke=input("free smoke ?:")
#     item={'booknumber':booknumber,'name':name,'checkin':checkin,'checkout':checkout,'hotel':hotel,'smoke':smoke}
#     items.append(item)
#  elif(mode=="c"):
#     yourbooknumber=int(input("Your book number ?:"))
#     for item in items:
#        if item['booknumber']==yourbooknumber:
#           items.remove(item)
#           print("cancel complete")
#  elif(mode=="p"):
#     print(item)
#  mode=input("Enter mode(q-quit,b=booking,c=cancel,p=print booking):")

# def first_last_same(numberList):
#     print("Given list:", numberList)
    
#     first_num = numberList[0]
#     last_num = numberList[-1]
    
#     if first_num == last_num:
#         return True
#     else:
#         return False

# numbers_x = [10, 20, 30, 40, 10]
# print("result is", first_last_same(numbers_x))

# numbers_y = [75, 65, 35, 75, 30]
# print("result is", first_last_same(numbers_y))

# str_x = "Emma is good developer. Emma is a writer"
# # use count method of a str class
# cnt = str_x.count("Emma")
# print(cnt)

# number=int(input("Your number?:"))
# lists=[]
# lists.reverse(number)
# print(lists)

income=int(input("Your income?:"))
tax=0
tax1=0
tax2=0
tax3=0
tax4=0
tax5=0
tax6=0
tax7=0
if(income<=150000):
    tax=0
elif(income<=300000):
    x=income-150000
    tax1=x*5/100
elif(income<=500000):
    x=500000-income
    tax2=x*10/100+7500
elif(income<=750000):
    x=750000-income
    tax3=x*15/100+50000
elif(income<=1000000):
    x=1000000-income
    tax4=x*20/100+112500
elif(income<=2000000):
    x=2000000-income
    tax5=x*25/100+200000
elif(income<=5000000):
    x=5000000-income
    tax6=x*30/100+500000
elif(income>5000000):
    x=income-5000000
    tax7=x*35/100+1500000
total=tax1+tax2+tax3+tax4+tax5+tax6+tax7
print(total)