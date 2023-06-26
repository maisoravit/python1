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

items=[]
mode=input("Enter mode(q-quit,b=booking,c=cancel,p=print booking):")
while(mode!="q"):
 if(mode=="b"):
    name=input("Your name:")
    checkin=int(input("enter checkin day:"))
    checkout=int(input("enter checkout day:"))
    if(checkin>checkout):
     print("error")
    hotel=input("your hotel's name ?:")
    booknumber=hotel,checkin,checkout
    smoke=input("free smoke ?:")
    item={'booknumber':booknumber,'name':name,'checkin':checkin,'checkout':checkout,'hotel':hotel,'smoke':smoke}
    items.append(item)
 elif(mode=="c"):
    yourbooknumber=int(input("Your book number ?:"))
    for item in items:
       if item['booknumber']==yourbooknumber:
          items.remove(item)
          print("cancel complete")
 elif(mode=="p"):
    print(item)
 mode=input("Enter mode(q-quit,b=booking,c=cancel,p=print booking):")
       
       