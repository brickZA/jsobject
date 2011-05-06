
from distutils.core import setup

DESCRIPTION = """Python objects that act like JavaScript objects. Based on James Robert blog entry http://jiaaro.com/making-python-objects-that-act-like-javascrip
"""

setup(
    name = 'jsobject',
    version = '0.1',
    description = DESCRIPTION,
    author = 'nojaku',
    author_email = 'n ( at ) nojaku ( dot ) com',
    url = 'https://github.com/nojaku/jsobject',
    license = 'Public Domain',
    py_modules = ['jsobject',],
    scripts = ['jsobject.py'],
    platforms = 'any',
    classifiers = [
        'License :: Public Domain',
        'Programming Language :: JavaScript',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)

