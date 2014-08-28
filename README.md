reddit-to-Kindle
================

[![Flattr reddit-to-Kindle](http://api.flattr.com/button/flattr-badge-large.png)](https://flattr.com/submit/auto?user_id=Antrikshy&url=github.com/Antrikshy/reddit-to-Kindle&title=reddit-to-Kindle&language=English&tags=github&category=software)

Compiles text posts from reddit into an HTML file, ready to convert to the popular .mobi format readable on Kindle devices and apps. The HTML file can be pumped into a converter such as KindleGen, a free, simple command-line tool from Amazon, which compiles it into the e-book format.

Now you can read long text posts from /r/talesfromtechsupport, /r/talesfromretail, /r/tifu or a story-based subreddit of your choice with the comfort of your e-reader.

Usage
-----
1. Install using `pip install reddit-to-Kindle`.
2. `cd` to a directory of your choice (this is where the HTML file will be generated).
3. Use `reddit-to-Kindle talesfromtechsupport month 15` or similar, which compiles the top 15 stories of the month from /r/talesfromtechsupport.
4. Convert HTML to .mobi format and send it to your Kindle (see the 'Converting to .mobi' section below).

You can pick any public subreddit. Only top posts can be compiled. Time period can be hour, day, week, month or year.

You can also use this program, in part or otherwise, in your own creations as long as it is attributed properly. It's MIT-licensed. Simply download the .tar.gz source distribution package from the `/dist` folder.

Converting to .mobi
-------------------
You can use a variety of methods to convert the HTML file into .mobi, and possibly other ebook formats such as .ePub, although only Kindle compatibility is guaranteed for now. [KindleGen](http://www.amazon.com/gp/feature.html/?ie=UTF8&camp=1789&creative=390957&docId=1000765211&linkCode=ur2&pf_rd_i=1000729511&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=1343256962&pf_rd_r=1PVPS0HAD6ZBTADSD8SA&pf_rd_s=center-6&pf_rd_t=1401&tag=rinointe-20&linkId=3VCDXGTPPQQH3TX5), a command-line tool available from Amazon for free is a quick and painless way to convert the HTML file.

Due to licensing reasons, I cannot include a copy of KindleGen and automate the entire process. But you can download it yourself and manually convert. To do this, just `cd` to the directory where KindleGen is saved and use `./kindlegen /path/to/FileToConvert.htm` to create a .mobi file in the same directory as the HTML. You can simply transfer this file to your Kindle using Amazon's email service or by a USB cable.

reddit-to-Kindle's UTF-8 encoded HTML is best converted by KindleGen.

[Calibre](http://calibre-ebook.com) may also convert the generated HTML, but I haven't tested it yet. If you have confirmed that everything converts properly, you can fork this repo, edit this message and send a pull request. Maybe throw in some code as well? 

Amazon's email service does not seem to use the same conversion algorithms as KindleGen, because some non-ASCII Unicode characters like smart-quotes don't show up properly. Perhaps compatibility will be improved in later versions of reddit-to-Kindle.

Donate
------
* [Flattr](https://flattr.com/submit/auto?user_id=Antrikshy&url=github.com/Antrikshy/reddit-to-Kindle&title=reddit-to-Kindle&language=English&tags=github&category=software)
* via Bitcoin at 1Aqvg4zVrdskeaS4dVjSGK7eHavSoEbB7V

Contributing
------------
Contributing is super easy. Simply fork, clone and edit the Python code in the `/reddit-to-Kindle` folder. Test using `python reddit-to-Kindle.py [args]`. Once you're done, just commit and send me a pull request. Don't worry about `setup.py`, version numbers and other stuff. I'll handle that.

**Things to do:**

* Add a way to convert single posts from URL (should be _very_ easy)
* Integrate some conversion functionality into the app using parts (or all) of the GPL-licensed Calibre
* Fix some encoding issues so the HTML converts cleanly using Amazon's email service (perhaps replace all Unicode characters)
* Expand compatibility with other ebook formats (I don't know how well it converts at the moment)
* Also add compatibility for hot posts?
