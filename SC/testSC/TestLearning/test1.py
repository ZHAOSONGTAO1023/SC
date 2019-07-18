#并发
# import urllib.request
# import time
# ts = time.time()
# #urloepn():https://www.imooc.com/article/49788
# req = urllib.request.urlopen('http://www.baidu.com')        #req为对象
# print('req:', req)
# pageHtml = req.read()
# print('pageHtml:' , pageHtml)
# te = time.time()
# print("Page Fetching Time : {} Seconds".format (te-ts))

# !/usr/bin/python3

import _thread
import time

# # _thread.start_new_thread ( function, args[, kwargs] )     函数调用方法
#
# def print_time(threadName, delay):
#     print("%s" % (time.ctime(time.time())))
#     count = 0
#     while count < 5:
#         time.sleep(delay)
#         count += 1
#         print("%s: %s,count = %s" % (threadName, time.ctime(time.time()),count))
#     print("%s is over" %(threadName))
#
# try:
#     _thread.start_new_thread(print_time, ("Thread-1", 2,))
#     _thread.start_new_thread(print_time, ("Thread-2", 4,))
# except:
#     print("Error: unable to start thread")
#
# while 1:
#     pass

# 要使用threading模块实现新线程，必须执行以下操作：
# 定义Thread类的新子类。覆盖__init __(self [，args])方法添加其他参数。然后，重写run(self [，args])方法来实现线程在启动时应该执行的操作。
# 当创建了新的Thread的子类之后，就可以创建一个实例，然后调用start()方法来调用run()方法来启动一个新的线程。

import threading
import time

exitFlag = 0

class MyThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print ("Starting " + self.name)
      print_time(self.name, self.counter, 5)
      print ("Exiting " + self.name)

def print_time(threadName, delay, counter):
   while counter:
      if exitFlag:
         threadName.exit()
      time.sleep(delay)
      print ("%s: %s,counter = %s" % (threadName, time.ctime(time.time()),counter))
      counter -= 1

# Create new threads
thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print ("Exiting Main Thread")

