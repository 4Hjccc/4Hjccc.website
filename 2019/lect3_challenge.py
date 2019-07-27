

import datetime
date_time = datetime.datetime.now()
date = date_time.date()  # Gives the date
time = date_time.time()  # Gives the time
mstr = "Jan."
m = date.month
if (m==2):
    mstr = "Feb."
elif (m==3):
    mstr = "Mar."
elif (m==4):
    mstr = "Apr."
elif (m==5):
    mstr = "May"
elif (m==6):
    mstr = "Jun."
elif (m==7):
    mstr = "Jul."
elif (m==8):
    mstr = "Aug."
elif (m==9):
    mstr = "Sep."
elif (m==10):
    mstr = "Oct."
elif (m==11):
    mstr = "Nov."
elif (m==12):
    mstr = "Dec."
    
hstr = "AM"    
h = time.hour
if (h>12):
    h=h-12;
    hstr = "PM"
    
print("Today is: "+mstr+" "+str(date.day)+", "+str(date.year))
tmp = str(h)+":"+str(time.minute)+":"+str(time.second)+hstr
print("The current time is: "+tmp)