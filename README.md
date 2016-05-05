# [EchelonPlanner](https://echelonplanner.noip.me)
SOEN341 Team Project for a Multiyear planner for Software Engineering Students

A Project made in Python's Django using MySQL
 
### Development

Project structure in this repository is split into two main directories under the "src" master directory:

1. ["app"](src/app) 

    This is the actual working EchelonPlanner app. Here you can see everything that pertains to the way the app was
    implemented and is working in the live site. This is the directory that should be used if the app ever need be 
    packaged.


2. ["echelon"](src/echelon)

    The 'echelon' directory deals mostly with our development specific setup. Most of it is deprecated since our initial
    deployment on [echelonplanner.me](echelonplanner.me) on April 8th, 2015. You should check this and make amendments if 
    you wish to start developing the app further.
    
    
To run the server, open a terminal prompt and change directory to "src" then input: "python manage.py runserver". 
This will create a basic web server for the Django app on localhost:8000
If you want to test a TLS server to test features, we recommend taking a look at [django-sslserver](https://github.com/teddziuba/django-sslserver).
It Really Helped :)

### The Team
Computer Engineering Students of Concordia University

####Team Leads
<ul>
<li>Nicole Cappadocia-Assaly</li>
<li>Javier E. Fajardo</li>
</ul>

####Front-End
<ul>
<li>Mario Felipe Muñoz Ferrante (Software Engineering Student)</li>
<li>Javier E. Fajardo</li>
<li>Arsalan Ali</li>
</ul>

####Back-End
<ul>
<li>Thinesh Thuraisingam</li>
<li>Ahmed Popal</li>
<li>Nauman Saeed Mirza</li>
</ul>

####Testing
<ul>
<li>Nicole Cappadocia-Assaly</li>
<li>Nitesh Arora</li>
<li>  Joseph Siouffi</li>
</ul>

####Internal Administration
<ul>
<li>  Philippe Sylvestre</li>
<li>  Dimitrios "James" Ziavras</li>
</ul>

### Licensing and Legal

This software is released under the GPL-Compatible [MIT License](/LICENSE.md).
 
The Licensing terms, however, do not make a user exempt from possible notices of academic fraud if part of this software
is used for Academic Purposes in secondary or post-secondary institutions.

In other words, **_The User is responsible for abiding academic code of conduct of the institution they are enrolled and,
respecting such, accepts full responsibility of what they made do with this code, freeing the original authors from any
consequences that may derive from such actions._** 

