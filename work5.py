# num=8
# print('%o' % num)

# import os
# size=os.stat("work7.py").st_size
# if size==0:
#     print("empty")

# threevalues=input("three person:").split()
# print(threevalues)

# list=[]
# data=int(input("number of data to enter:"))
# for i in range(data):
#     x=input(f'data at index{i+1}:')
#     list.append(x)
# print(list)
   
# import os 
# from pathlib import Path

# def read_file(file_name):
#     file_handle = open(file_name,'w')
#     file_handle.write("kfc")
#     file_handle.close()

# file_dir = Path(r'D:/vs')
# print (file_dir)

# #For accessing the file in the same folder
# file_name = "mai.txt"
# #For accessing the file inside a sibling folder.
# joinpath = os.path.join(file_dir, file_name)
# absolutepath = os.path.abspath(os.path.realpath(file_name))
# print (file_name)
# print(joinpath)
# print(absolutepath)
# read_file(joinpath)    

# import datetime

# thaiyear=int(input("thaiyear:"))
# time=thaiyear-543
# x=datetime.datetime(time,2,29)
# print(time)
# print(x.strftime("%d"))
# if time%4==0 and time%100!=0 or time%400==0:
#     print("has leap year")
# else:
#     print("not has leap year")



from datetime import datetime, timedelta

def thailand_to_canada_th(time_in_thailand):
    thailand_offset = timedelta(hours=7)
    canada_offset = timedelta(hours=-5)
    thailand_time = datetime.strptime(time_in_thailand, "%Y-%m-%d %H:%M:%S")
    utc_time = thailand_time - thailand_offset
    canada_time = utc_time + canada_offset
    return canada_time
thailand_time_str = int(input("2023-07-16 12:34:56"))
canada_time = thailand_to_canada_th(thailand_time_str)
print("Thailand Time:", thailand_time_str)
print("Canada Time (ET):", canada_time.strftime("%Y-%m-%d %H:%M:%S"))
