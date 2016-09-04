# sycamore-page-extractor
This is a companion to [wikispot2dokuwiki](https://github.com/ychaouche/wikispot2dokuwiki). You can use it like this : 

    ychaouche@ychaouche-PC 12:46:07 ~/DOWNLOADS/DATA $ python sycamore-page-extractor.py wikispot.xml
    preparing the soup for wikispot.xml ...
    soup is ready ! 
    getting page vlcscreencapture
    writing the content to ./PAGES/vlcscreencapture
    getting page software
    writing the content to ./PAGES/software
    getting page emacsandkde
    writing the content to ./PAGES/emacsandkde
    [...]
    ychaouche@ychaouche-PC 12:46:42 ~/DOWNLOADS/DATA $ 

Then you can use [wikispot2dokuwiki](https://github.com/ychaouche/wikispot2dokuwiki) on each page to convert it to dokuwiki syntax.
