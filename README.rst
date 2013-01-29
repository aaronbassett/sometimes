sometimes
======================

Stop being so black and white. Mix things up a bit and execute code sometimes.
This is a Python port of the `Ruby sometimes gem
<https://github.com/sudara/sometimes>`_.

Installation
------------

You can install via ``pip``::
    
    $ pip install sometimes
    
Or by cloning from Github::

    $ git clone git@github.com:aaronbassett/sometimes.git
    $ cd sometimes
    $ python setup.py install

Usage
--------

Say something every other time::

    >>> from sometimes import sometimes
    
    >>> @sometimes
    ... def hello():
    ...     print "Hey, you are awesome. You really are."  # executes warm fuzzies 50% of the time
    ...

Have a 50% chance of saying something::

    >>> from sometimes import sometimesish
    
    >>> @sometimesish
    ... def hello():
    ...     print "Hey, you are awesome. You really are."
    ...

Maybe you want to do something several times, but not always the exact same number of times::

    >>> from sometimes import times
    
    >>> @times(4,10)
    ... def pick_nose():
    ...     pass
    ...

Maybe you want to remind someone of something, but not toooo often (It gets annoying!)::

    >>> from sometimes import percent_of_the_time
    
    >>> @percent_of_the_time(15)
    ... def naughty():
    ...     print "Howdy, Don't forget to register!"  # be annoying, but only 15% of the time
    ...
    
    >>> @percent_of_the_time(33)
    ... def be_very_polite():
    ...     pass
    ...

Share a rare moment with your user::

    >>> from sometimes import rarely
    
    >>> @rarely()
    ... def spam():
    ...     print "How would you like some spammy spam spam!"  # be really annoying about 5% of the time
    ...

Do something most of the time::

    >>> from sometimes import mostly
    
    >>> @mostly()
    ... def be_awesome():
    ...     print "Want to see something really cool?"  # Be awesome about 95% of the time
    ...

Hold on a minute
-----------------

Why does it have ``@sometimes`` and ``@sometimesish``? I wanted ``sometimes`` to behave as described 
by the gem docs, not how it operates in the gem. I included ``sometimesish`` if anyone wanted the 
gem style functionality.

License
-------

MIT: http://aaron.mit-license.org