mport queue
a=queue.queue()
b=queue.queue()
for i in range(5):
    b.put(x)
print(a.empty())
print(b.empty())
import queue
l=queue.queue(maxsize=5)
l.put(10)
l.put(20)
print(type(l))
