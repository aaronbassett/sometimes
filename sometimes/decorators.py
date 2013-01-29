import random


"""
They've done studies, you know. 50% of the time,
it works every time.
"""
def sometimes(fn):
    
    def wrapped(*args, **kwargs):
        wrapped.x += 1
        if wrapped.x % 2 == 1:
            return fn(*args, **kwargs)
        return
    
    wrapped.x = 0
    return wrapped


"""
Do something a random amount of times
between x & y
"""
def times(x,y):
    
    def decorator(fn):
        
        def wrapped(*args, **kwargs):
            while wrapped.min <= wrapped.max:
                wrapped.min += 1
                fn(*args, **kwargs)
            return

        wrapped.min = x
        wrapped.max = random.randint(x,y)
        
        return wrapped
    
    return decorator