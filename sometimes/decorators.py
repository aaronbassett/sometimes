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
    
    wrapped.x = 0
    return wrapped

half_the_time = sometimes


"""
Has a 50/50 chance of calling a function
"""
def sometimesish(fn):

    def wrapped(*args, **kwargs):
        if random.randint(1,2) == 1:
            return fn(*args, **kwargs)
    
    return wrapped


"""
Function has a X percentage chance of running
"""
def percent_of_the_time(p):
    
    def decorator(fn):
        
        def wrapped(*args, **kwargs):
            if in_percentage(p):
                fn(*args, **kwargs)
        
        return wrapped
        
    return decorator

"""
Only 5% chance of happening
"""
def rarely(fn):
    def wrapped(*args, **kwargs):
        if in_percentage(5):
            fn(*args, **kwargs)
    return wrapped

"""
95% chance of happening
"""
def mostly(fn):
    def wrapped(*args, **kwargs):
        if in_percentage(95):
            fn(*args, **kwargs)
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

            # Reset for another go
            wrapped.min = wrapped.x
            wrapped.max = random.randint(wrapped.x, wrapped.y)

        wrapped.x = x
        wrapped.y = y
        wrapped.min = x
        wrapped.max = random.randint(x,y)
        
        return wrapped
    
    return decorator