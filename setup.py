from distutils.core import setup

setup (
    name = 'reddit-to-Kindle',
    packages = ['reddit-to-Kindle'],
    version = '0.8.0',
    author = 'Antriksh Yadav',
    author_email = 'antrikshy@gmail.com',
    url = 'http://www.github.com/Antrikshy/reddit-to-Kindle',
    description = 'Compiles top posts from a specified subreddit for a specified\
                   time period into an HTML page that easily converts to Kindle format.',
    long_description = """\
                       See http://www.github.com/Antrikshy/reddit-to-Kindle for instructions. Requires KindleGen\
                       from Amazon to convert HTML result to .mobi for Kindle.
                       """,
    classifiers = ['Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities',
                   'Development Status :: 4 - Beta'
                   'Intended Audience :: End Users/Desktop',
                   'Natural Language :: English',
                   'License :: OSI Approved :: MIT License']
)