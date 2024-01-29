import json
import sys
import os

papernumber = sys.argv[1]

fonts ='''<style>
        ol {
            font-size: 22px;
        }

        ul {
            font-size: 22px;
        }
    </style>'''

papernumber=14

# Opening JSON file
with open("json/paperinfo.json", 'r') as openfile:
 
    # Reading from json file
    json_object = json.load(openfile)

# inputs:
date = json_object['date']
title = json_object['title']
author= json_object['author']
introduction = json_object['introduction']
conclusion = json_object['conclusion']

keys = ['date', 'title', 'author', 'introduction', 'conclusion']

for key in keys:
    json_object.pop(key, None)

body = ''

for section in json_object:
    content = json_object[section]

    isection = f"""
    <h2>{section}:</h2>

    <p class="lead"><span class="drop-cap"></span>
    {content}
    </p>
    """

    body = body + isection


paperbody = f"""
<!DOCTYPE html>
<html class="no-js" lang="en">
<head>
    <!-- Your AdSense code: -->
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3982955326140985"
     crossorigin="anonymous"></script>
    <!--- basic page needs
    ================================================== -->
    <meta charset="utf-8">
    <title>{title}</title>
    <meta name="description" content="">
    <meta name="author" content="">

    <!-- mobile specific metas
    ================================================== -->
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- CSS
    ================================================== -->
    <link rel="stylesheet" href="css/base.css">
    <link rel="stylesheet" href="css/vendor.css">
    <link rel="stylesheet" href="css/main.css">

    <!-- script
    ================================================== -->
    <script src="js/modernizr.js"></script>

    <!-- favicons
    ================================================== -->
    <link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="favicon-16x16.png">
    <link rel="manifest" href="site.webmanifest">

    <!-- Font size list enumerate -->
    {fonts}
</head>

<body class="ss-bg-white">

    <!-- preloader
    ================================================== -->
    <div id="preloader">
        <div id="loader" class="dots-fade">
            <div></div>
            <div></div>
            <div></div>
        </div>
    </div>

    <div id="top" class="s-wrap site-wrapper">

        <!-- site header
        ================================================== -->
        <header class="s-header header">

            <div class="header__top">
                <div class="header__logo">
                    <a class="site-logo" href="index.html">
                        <img src="images/logo.svg" alt="Homepage">
                    </a>
                </div>
            </div> <!-- end header__top -->

            <nav class="header__nav-wrap">

                <ul class="header__nav">
                    <li class="current"><a href="index.html" title="">Home</a></li>
                    <!--
                    <li class="has-children">
                        <a href="#0" title="">Categories</a>
                        <ul class="sub-menu">
                        <li><a href="category.html">Lifestyle</a></li>
                        <li><a href="category.html">Health</a></li>
                        <li><a href="category.html">Family</a></li>
                        <li><a href="category.html">Management</a></li>
                        <li><a href="category.html">Travel</a></li>
                        <li><a href="category.html">Work</a></li>
                        </ul>
                         -->
                    </li>
                    <li class="has-children">
                        <!-- 
                        <a href="#0" title="">Blog Posts</a>
                        <ul class="sub-menu">
                        <li><a href="single-video.html">Video Post</a></li>
                        <li><a href="single-audio.html">Audio Post</a></li>
                        <li><a href="single-gallery.html">Gallery Post</a></li>
                        <li><a href="single-standard.html">Standard Post</a></li>
                        </ul>
                    </li>
                    <li><a href="styles.html" title="">Styles</a></li>
                    -->
                    <li><a href="page-about.html" title="about">About</a></li>
                    <li><a href="page-contact.html" title="contact">Contact</a></li>
                    </ul>  <!-- end header__nav -->

                <ul class="header__social">
                    <li class="ss-facebook">
                        <a href="https://facebook.com/">
                            <span class="screen-reader-text">Facebook</span>
                        </a>
                    </li>
                    <li class="ss-twitter">
                        <a href="#0">
                            <span class="screen-reader-text">Twitter</span>
                        </a>
                    </li>
                    <li class="ss-dribbble">
                        <a href="#0">
                            <span class="screen-reader-text">Instagram</span>
                        </a>
                </ul>

            </nav> <!-- end header__nav-wrap -->

            <!-- menu toggle -->
            <a href="#0" class="header__menu-toggle">
                <span>Menu</span>
            </a>

        </header> <!-- end s-header -->


        <!-- search
        ================================================== -->
        <div class="s-search">

            <div class="search-block">
    
                <form role="search" method="get" class="search-form" action="#">
                    <label>
                        <span class="hide-content">Search for:</span>
                        <input type="search" class="search-field" placeholder="Type Keywords" value="" name="s" title="Search for:" autocomplete="off">
                    </label>
                    <input type="submit" class="search-submit" value="Search">
                </form>
    
                <a href="#0" title="Close Search" class="search-close">Close</a>
    
            </div>  <!-- end search-block -->

            <!-- search modal trigger -->
            <a href="#0" class="search-trigger">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" style="fill:rgba(0, 0, 0, 1);transform:;-ms-filter:"><path d="M10,18c1.846,0,3.543-0.635,4.897-1.688l4.396,4.396l1.414-1.414l-4.396-4.396C17.365,13.543,18,11.846,18,10 c0-4.411-3.589-8-8-8s-8,3.589-8,8S5.589,18,10,18z M10,4c3.309,0,6,2.691,6,6s-2.691,6-6,6s-6-2.691-6-6S6.691,4,10,4z"></path></svg>
                <span>Search</span>
            </a>
            <span class="search-line"></span>

        </div> <!-- end s-search -->


        <!-- site content
        ================================================== -->
        <div class="s-content content">
            <main class="row content__page">
                
                <article class="column large-full entry format-standard">

                    <div class="media-wrap entry__media">
                        <div class="entry__post-thumb">
                            <img src="images/finance/tamb{papernumber}paper.png" 
                                 srcset="images/finance/tamb{papernumber}paper.png 2000w, 
                                         images/finance/tamb{papernumber}paper.png 1000w, 
                                         images/finance/tamb{papernumber}paper.png 500w" sizes="(max-width: 2000px) 100vw, 2000px" alt="" class="center">
                        </div>
                    </div>

                    <div class="content__page-header entry__header">
                        <h1 class="display-1 entry__title">
                        {title}
                        </h1>
                        <ul class="entry__header-meta">
                            <li class="author">By <a href="#0">{author}</a></li>
                            <li class="date">{date}</li>
                            <li class="cat-links">
                                <a href="#0">Finance</a><a href="#0">Financial Education</a>
                            </li>
                        </ul>
                    </div> <!-- end entry__header -->

                    <div class="entry__content">

                        <p class="lead drop-cap">
                        {introduction}
                        </p>

                        {body}

                        <h2>Conclusion:</h2>

                        <p class="lead"><span class="drop-cap"></span>
                        {conclusion}
                        </p>
                        

                        <p class="lead"><span class="drop-cap"></span>
                        That's it for now. Thank you very much for read the article!
                        </p>

                        <h3>I wish you All the best in life!</h3>


                        <p class="entry__tags">
                            <span>Post Tags</span>
        
                            <span class="entry__tag-list">
                                <a href="#finance">finance</a>
                                <a href="#financialeducation">Financial Education</a>
                                <a href="#money">Money</a>
                                <a href="#investing">Investing</a>
                                <a href="#financialfreedom">Financial Freedom</a>
                                <a href="#minsetfinance">Mindset Finance</a>
                                <a href="#lifechanging">Life Changing</a>

                            </span>
            
                        </p>
                    </div> <!-- end entry content -->
                </article> <!-- end column large-full entry-->
            </main>

        </div> <!-- end s-content -->


        <!-- footer
        ================================================== -->
        <footer class="s-footer footer">
            <div class="row">
                <div class="column large-full footer__content">
                    <div class="footer__copyright">
                        <span>© Copyright 2023</span> 
                        <span>Design by andrevsilva.com<a href="https://andrevsilva.com"></a></span>
                    </div>
                </div>
            </div>

            <div class="go-top">
                <a class="smoothscroll" title="Back to Top" href="#top"></a>
            </div>
        </footer>

    </div> <!-- end s-wrap -->


    <!-- Java Script
    ================================================== -->
    <script src="js/jquery-3.2.1.min.js"></script>
    <script src="js/plugins.js"></script>
    <script src="js/main.js"></script>

</body>
"""

# Creating the HTML file
file_html = open(f"papertopage/{papernumber}paper.html", "w")

# Adding the input data to the HTML file
file_html.write(paperbody)

# Saving the data into the HTML file
file_html.close()

os.system(f'mv papertopage/{papernumber}paper.html ../../')

print('Paper in html ready to publish in my page.')