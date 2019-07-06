import time;

def print_time(str):
    localtime = time.asctime( time.localtime(time.time()) )
    print "Local current time :", localtime

