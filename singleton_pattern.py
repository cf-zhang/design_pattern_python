# 方法一　使用模块
# class Singleton(object):
#     def foo(self):
#         pass
# singleton = Singleton()

import threading

class Singleton:
    _instances = dict()
    lock = threading.Lock()
    def __init__(self, *args, **kwargs):
        pass

    def __new__(cls, *args, **kwargs):
        instance = kwargs['pair'] + '_instance'
        if not hasattr(cls, instance):
            with Singleton.lock:
                if not hasattr(cls, instance):
                    Singleton._instances[instance] = super().__new__(cls)
                    setattr(cls, instance, instance)
        return Singleton._instances[instance]



obj1 = Singleton(pair='eos')
obj2 = Singleton(pair='bsv')
print(obj1, obj2)


def task(arg):
    obj = Singleton(pair='eos')
    obj2 = Singleton(pair='bsv')
    obj3 = Singleton(pair='aaa')
    print(obj, obj2, obj3)



for i in range(10):
    t = threading.Thread(target=task, args=[i, ])
    t.start()
