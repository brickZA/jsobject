
"""

jsobject
=================

based on James Robert blog entry:

Making Python Objects that act like Javascript Objects
http://jiaaro.com/making-python-objects-that-act-like-javascrip

Usage:

    >>> from jsobject import JSObject
    >>> obj = JSObject()

    >>> obj1 = JSObject()
    >>> obj1.name = "JS Object"
    >>> print obj1.name
    JS Object
    >>> print obj1['name']
    JS Object

    >>> obj2 = JSObject()
    >>> obj2['msg'] = "Hello, JS Object!"
    >>> print obj2['msg']
    Hello, JS Object!
    >>> print obj2.msg
    Hello, JS Object!

    >>> from jsobject import JsObject
    >>> obj3 = JsObject()
    >>> obj3['msg'] = 'another name'
    >>> print obj3.msg
    another name

    >>> class MyClass(JSObject):
    ...
    ...     def __init__(self, **kwargs):
    ...         super(MyClass, self).__init__(**kwargs)
    ...         self.update(kwargs)
    ...
    >>> obj4 = MyClass(foo='bar', baz='zzz', hoge='fuga')
    >>> print obj4.foo
    bar
    >>> keys = obj4.keys()
    >>> keys.sort()
    >>> keys
    ['baz', 'foo', 'hoge']

"""

class JSObject(dict):
    """JSObject : Python Objects that act like Javascript Objects"""

    def __init__(self, *args, **kwargs):
        super(JSObject, self).__init__(*args, **kwargs)
        self.__dict__ = self 

JsObject = JSObject

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

