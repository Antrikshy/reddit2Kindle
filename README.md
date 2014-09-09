reddit2Kindle (beta)
====================

[![Flattr reddit2Kindle](http://api.flattr.com/button/flattr-badge-large.png)](https://flattr.com/submit/auto?user_id=Antrikshy&url=github.com/Antrikshy/reddit2Kindle&title=reddit2Kindle&language=English&tags=github&category=software)

Conveniently compiles text posts from reddit into a .mobi book, readable by all Kindle devices and apps.

Now you can read long text posts from /r/talesfromtechsupport, /r/talesfromretail, /r/tifu or a story-based subreddit of your choice with the comfort of your e-reader.

Usage
-----
1. Install using `pip install reddit2Kindle`.
2. `cd` to a directory of your choice (this is where the HTML file will be generated).
3. Download and place the [KindleGen](http://www.amazon.com/gp/feature.html/?ie=UTF8&camp=1789&creative=390957&docId=1000765211&linkCode=ur2&pf_rd_i=1000729511&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=1343256962&pf_rd_r=1PVPS0HAD6ZBTADSD8SA&pf_rd_s=center-6&pf_rd_t=1401&tag=rinointe-20&linkId=3VCDXGTPPQQH3TX5) executable from Amazon into the current directory to automate conversion to .mobi OR convert the .htm result manually.
4. Use `reddit2Kindle talesfromtechsupport month 15` or similar, which compiles the top 15 stories of the month from /r/talesfromtechsupport.

You can pick any public subreddit. Only top posts can be compiled. Time period can be hour, day, week, month or year.

You can also use this program, in part or otherwise, in your own creations as long as it is attributed properly. It's MIT-licensed. Simply download the .tar.gz source distribution package from the `/dist` folder.

Converting to .mobi
-------------------
Amazon has a command line tool called [KindleGen](http://www.amazon.com/gp/feature.html/?ie=UTF8&camp=1789&creative=390957&docId=1000765211&linkCode=ur2&pf_rd_i=1000729511&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=1343256962&pf_rd_r=1PVPS0HAD6ZBTADSD8SA&pf_rd_s=center-6&pf_rd_t=1401&tag=rinointe-20&linkId=3VCDXGTPPQQH3TX5), which quickly and painlessly convert some file formats for Kindle.

Due to licensing reasons, I cannot include a copy of KindleGen and automate the entire process. But you can download it yourself. Just place this executable into the directory you are working in. r2K will automatically create a .mobi file. You can simply transfer this file to your Kindle using Amazon's email service or by a USB cable.

If KindleGen is not found in the current directory at runtime, an HTML file is created. This can be manually converted to .mobi using KindleGen, Calibre or some other solution.

Donate
------
* [Flattr](https://flattr.com/submit/auto?user_id=Antrikshy&url=github.com/Antrikshy/reddit2Kindle&title=reddit2Kindle&language=English&tags=github&category=software)
* via Bitcoin at 1Aqvg4zVrdskeaS4dVjSGK7eHavSoEbB7V

Contributing
------------
If you cannot code, you can create a new issue in this project and I should get back to you quickly.

Contributing code is super easy. Simply fork, clone and edit the r2K script and/or code in the `/redditKindleLib` folder using your favorite text editor. Test using `python ./r2K [args]`. Once you're done, just commit and send me a pull request. Don't worry about `setup.py`, version numbers and other stuff. I'll handle that.

**Things to do:**

* Add a way to convert single posts from URL (should be _very_ easy)
* Fix some encoding issues so the HTML converts cleanly using Amazon's email service (perhaps replace all Unicode characters)
* Expand compatibility with other ebook formats (I don't know how well it converts at the moment)
* Also add compatibility for hot posts?
