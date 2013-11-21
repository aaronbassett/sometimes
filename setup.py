from distutils.core import setup

setup(
    name='sometimes',
    version='0.1.2',
    author='Aaron Bassett',
    author_email='me@aaronbassett.com',
    packages=['sometimes', ],
    url='https://github.com/aaronbassett/sometimes',
    license='LICENSE',
    description='Stop being so black and white. Mix things up a bit and execute code sometimes.',
    long_description=open('README.rst').read(),
)
