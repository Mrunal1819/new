#importing Library

import pandas as pd  #pandas are used data handling


#open log file operation
file=open("access_log","a+")
file.seek(0)
r=file.readlines()
file.close()

#hello i m using git
#operation of the lists 
f_list=[]////
s_list=[]
for line in  r:
    if "404" in line:
        position=r.index(line)
        f_list.append(position)
    else:
        s_list.append(line)

len(f_list)
len(s_list)dgsjhdjshjhsajdhsaj
s_list


hjxsbjxbjhsbxhjsb
#used for finding status codes in the log file
f_list=[]
s_list=[]
t1 = []
no_hhtp = []
for line in  r:
    if "HTTP/1.1" in line:
        position=r.index(line)
        t=r[position]
        if "HTTP/1.1" in t:
            ind = t.index("HTTP/1.1")
            ind = ind+10
            #print(ind)
            data = t[ind :ind+3]
            #print(data)
            t1.append(data)
    else:
        no_hhtp.append(line)

#operations to find total number of success and failure code
        
failure_404 = t1.count('404')
failure_403 = t1.count('403')
failure_400 = t1.count('400')

set_1 = set(t1)
print(f"Different Status Code in log file{set_1}")

print(f"Failure 404 = {failure_404}")

print(f"Failure 403 = {failure_403}")

print(f"Failure 400 = {failure_400}")

successful_200=t1.count('200')
print(f"Successful 200 = {successful_200}")

redirect_301=t1.count('301')
print(f"Redirect 301 = {redirect_301}")

redirect_302=t1.count('302')
print(f"Redirect 302 = {redirect_302}")

redirect_304=t1.count('304')
print(f"Redirect 304 = {redirect_304}")

print(f"Total Successfull {successful_200}")
print(f"Total Failures {16+failure_400+failure_403+failure_404+redirect_302+redirect_304}")



