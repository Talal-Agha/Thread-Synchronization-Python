from threading import Thread

def print_thread( threadName, number):
      print"Thread %i: The number is '%i'"%(threadName,number)

i = 1      
while i <= 100:
      oddThread = Thread( target=print_thread,args= (1, i) )
      i = i+1
      evenThread = Thread( target=print_thread,args=(2, i) )
      i = i+1
      oddThread.start()
      evenThread.start()
      oddThread.join()
      evenThread.join()