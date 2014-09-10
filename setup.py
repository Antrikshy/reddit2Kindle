from distutils.core import setup

setup(
    name='reddit2Kindle',
    scripts=['r2K'],
    packages=['redditKindleLib'],
    version='0.5.0',
    author='Antriksh Yadav',
    author_email='antrikshy@gmail.com',
    url='http://www.antrikshy.com/projects/reddit2Kindle.htm',
    description=(
        'Compiles top posts from a specified subreddit for a specified time'
        'period into a well-formatted Kindle book.'
    ),
    long_description=(
        'See http://www.github.com/Antrikshy/reddit2Kindle for instructions.'
        'Requires KindleGen from Amazon to convert HTML result to .mobi for'
        'Kindle.'
    ),
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License'
    ],
)
