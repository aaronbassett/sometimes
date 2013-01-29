import random


in_percentage = lambda x: random.randint(1,100) <= x


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
Has a 50/50 chance of calling a function
"""
def sometimesish(fn):

    def wrapped(*args, **kwargs):
        if random.randint(1,2) == 1:
            return fn(*args, **kwargs)
        return
    
    return wrapped


"""
Function has a X percentage chance of running
"""
def percent_of_the_time(p):
    
    def decorator(fn):
        
        def wrapped(*args, **kwargs):
            if in_percentage(p):
                fn(*args, **kwargs)
            return
        
        return wrapped
        
    return decorator


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