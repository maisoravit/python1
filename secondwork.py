subjects=[]
grades=[]
ask1=input("Do want to add subject?(yes/no):")
while(ask1=='yes'):
     subject=input("Your subject:")
     grade=int(input("Your grade:"))
     subjects.append(subject)
     grades.append(grade)
     dict1=dict(zip(subjects,grades))
     ask1=input("Do you want to add subject?(yes/no):")
     print(dict1)
     print("min",min(dict1,key=dict1.get))
     print("max",max(dict1,key=dict1.get))
ask2=input("Do you want to change your grade?(yes/no):")
while(ask2=='yes'):
     yoursubject=input("Which subject?:")
     dict1['subject']=yoursubject
     yournewgrade=int(input("Your new grade?:"))
     dict1['grade']=yournewgrade
     print(dict1['subject'])
     print(dict1['grade'])
     ask2=input("Do you want to change your grade?(yes/no):")
     