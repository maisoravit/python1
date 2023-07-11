# def data(num):
#     if num%2==0:
#         print(f"even number:")
#     else:
#         print(f"odd number:")
# num=int(input("number:"))
# data(num)

# def countword(word):
#     vowel=0
#     consonant=0
#     for i in range(len(word)):
#      if word[i] in ["a","e","i","o","u"]:
#         vowel=vowel+1
        
#      else:
#         consonant=consonant+1
#     print(f"vowel is {vowel}")
#     print(f"consonant is {consonant}")
# word=input("Your word:")
# countword(word)

# num=int(input("Your num?:"))

# factorial=1
# while num!=0:
#     factorial=factorial*num
#     num=num-1
    
# print(factorial)

# num = input("Enter a string ").split()
# search = input("Enter a word to search ")
# if search in num:
#     print(f"{search} exist in String")
# else:
#     print(f"{search} not exist in String")

# word=input("Enter sting:")
# if word.isupper():
#     print(word) 

# def totalamount(rate):
#     return 1+(rate/100)
# money=int(input("Enter initial amount in Baht:"))
# rate=int(input("Enter interest rate in percent:"))
# print(f'Total amount after 1 year is {money*totalamount(rate):.2f} Baht.')
# print(f'Total amount after 5 years is {money*(totalamount(rate)**5):.2f} Baht.')
# print(f'Total amount after 10 years is {money*(totalamount(rate)**10):.2f} Baht.')
# print(f'Total amount after 20 years is {money*(totalamount(rate)**20):.2f} Baht.')

import datetime
def has_friday_13(month,year):
    return datetime.date(year,month,13).strftime("%A")== "Friday"
month=int(input("month:"))
year=int(input("year:"))
print(has_friday_13(month,year))
