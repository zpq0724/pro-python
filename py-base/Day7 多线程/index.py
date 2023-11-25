

'''
  python 是解释性语言，python 的解释器默认也是单线程的。
  但是提供了用于多线程编程的模块 threading。
  
  
  
'''


'''
  1. threading 基础使用
'''

import threading
import time

class myThreading(threading.Thread): # 继承父类 threading.Thread, 可以重写父类方法
  def __init__(self, name):
    threading.Thread.__init__(self)
    self.name = name
    
  def run(self):
    print('threadList:', len(threading.enumerate()))
    print("start:", self.name)
    
    # 线程休眠，执行耗时操作
    time.sleep(5)
    print("%s 时间：%s" % (self.name, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))))
    print("end:", self.name)
    

# 创建两个线程实例 
td1 = myThreading("threading1")
td2 = myThreading("threading2")

# start 方法启动线程，自动调用 run 方法
td1.start()
td2.start()
print('执行完了1')

# join 方法等待线程执行完毕，确保主线程在子线程完成之前不会继续执行
td1.join()
td2.join()
print('执行完了2')



'''
  2. threading 线程同步
      当多个线程同时访问共享资源时，可能会引发竞争条件。 
      threading 模块提供了线程同步机制。
'''

import threading
my_lock = threading.Lock() # 创建锁
my_lock.acquire() # 加锁
my_lock.release() # 释放

def my_function():
  # with 语句自动调用 my_lock.acquire() 和 my_lock.release(),确保在进入和退出临界区时自动获取和释放锁。
  # my_function 中的代码是个临界区，一次只能有一个线程运行
  with my_lock:
    print("hello world")
    
my_thread = threading.Thread(target=my_function)
my_thread.start()
# 主线程等待子线程完成
my_thread.join()


''''
  3. threading 线程间通信
    线程之间通信，使用队列 Queue, 或其他线程安全的数据结构。
'''

import threading
from queue import Queue

my_queue = Queue() # 创建队列

def producer():
  for i in range(5):
    my_queue.put(i)
    print("生产者生产了数据%d" % i)
    
    
def consumer():
  while True:
    if not my_queue.empty():
      data = my_queue.get()
      print("消费者消费了数据")
    else:
      break
    
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()




# 以下是一个简单的示例，演示了多个线程使用同步锁的情况：
import threading

# 共享资源
shared_resource = 0

# 创建锁
lock = threading.Lock()

# 线程函数
def update_shared_resource():
  '''
  在Python中，当你在一个函数内部修改一个全局变量时，
  如果你不使用global关键字，Python会将其视为局部变量，而不是全局变量。
  这意味着在函数内部创建了一个新的局部变量，而不是修改已经存在的全局变量。
  '''
  global shared_resource

  for _ in range(1000000):
    # 加锁
    with lock:
      shared_resource += 1
    # 释放锁

# 创建多个线程
threads = []
for _ in range(5):
  thread = threading.Thread(target=update_shared_resource)
  threads.append(thread)

# 启动所有线程
for thread in threads:
  thread.start()

# 等待所有线程完成
for thread in threads:
  thread.join()

# 打印最终结果
print("Final shared resource value:", shared_resource)

# 在这个例子中，有5个线程同时访问一个共享资源 shared_resource，这个资源是一个简单的计数器。
# 每个线程执行一个循环，将共享资源递增1000000次。
# 由于这是一个并发操作，如果不使用同步锁，可能会导致竞争条件，最终结果可能不是我们期望的值。
# 通过引入 with lock 语句，我们确保了对 shared_resource 的访问是原子的，即在同一时刻只有一个线程能够访问临界区。
# 这样可以确保数据的一致性，避免了竞争条件。

'''
  问题1：使用同步锁，意思是创建的这五个线程是同步，按顺序执行吗？
    
  答案1：
    不是的，使用同步锁（threading.Lock）确保在关键区域内只有一个线程能够执行，但并不保证线程的执行顺序。
    同步锁的目的是防止多个线程同时访问临界区，以避免数据竞争和不一致性。

    在你的示例中，你创建了5个线程，每个线程都会执行 update_shared_resource 函数，该函数包含一个循环来递增 shared_resource 变量的值。
    通过使用 with lock 语句，确保了在每个线程的循环内只有一个线程能够执行临界区（修改 shared_resource 的部分），这样就避免了竞争条件。

    然而，线程的执行顺序仍然是不确定的。
    线程的调度是由操作系统决定的，具体的执行顺序可能因为操作系统的调度策略、线程的优先级等因素而变化。

    如果你希望线程按照一定的顺序执行，你可能需要使用其他同步机制，
    比如信号量（threading.Semaphore）或者条件变量（threading.Condition），或者通过其他手段在线程之间进行协调。


  问题2：
  
'''


