Title: About 
Date: 2017-08-17 16:31

# Who am I

I have been system administrator for over 15 years and I am strong
supporter of open source software. I started playing around with
various Linux distributions(Red Hat, Mandrake, Gentoo, etc) in High
School. I was fortunate that my High School offered a [Cisco Networking
Academy](https://www.netacad.com/) that prepared students to take the
Cisco Certified Network Associate(CCNA) exam, which I did. With that
certification and the experience I had gained I was able to get some
summer jobs as an IT Assistant(mainly for MS Windows) and gain more
experience as a system administrator. I studied Computer Science at the
University of Tennessee and at the same time work as a Student System
Administrator in the Computer Science department on Labstaff. Labstaff
was a game changing experience which allowed students to get real world
linux/unix system administration experience running the departments
servers(web, email, file servers, workstations, etc). This oppurtunity,
along with the CS and coding knowlege I got from classes, allowed me
combine my basic system administration skills and my linux hobby into a
career as a Linux System Administrator. 

I am currently employed as a HPC System Administrator at [Oak
Ridge National Laboratory](http://www.ornl.gov) in Oak Ridge,
TN(near Knoxville). I work in the [Oak Ridge Leadership Computing
Facility](http://www.olcf.ornl.gov) where our mission is to deploy the
some of the worlds largest supercomputers to help solve some of the
worlds hardest scientific problems. Most of the research done on our
HPC resources is considered open science, where anyone from around the
world(mainly universities and other national laboratories) who has a big
problem to solve can use our computers for free as long as they publish
their work in the public domain.

As time allows I also enjoy the occasional programming project and
contributing to open source software.  My non-computer hobbies consist
of Swimming, Biking, Running, and doing long-distance triathlons.

# Why did I create this site

The purpose of this site is to give me place to share useful information
and work that I have done related to system administration, linux, open
source software, and technology in general for the benifit of others in
the field to learn from.

# How did I create this site

After many failed attempts of trying to customize and manage popular
content management systems such as Wordpress and Drupal to my liking,
I wanted to try a different approach that would lead to more easily
usable and maintainable site. So my requirements were this:
- Able to write/store/manage site content via a git repository and text editor. No more database backends or CMS administration web GUIs.
- A templating language that can generate static content. No more deluge of security updates for features I never use.
- Ability to easily customize, theme, structure the site to my liking.

Given all that I decided to use [Pelican](http://docs.getpelican.com/en/stable/index.html) as my static site generator,
becuase it seemed to have all the features I needed, was based on
python(which I like to code in), and was actively maintained. I am
currently using the [pelican-bootstrap3 theme](https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3).

# How do I host this site

For simplicity sake, I am currently using [github.io or Github
Pages](https://pages.github.com/) to host the static content for
my site. The source code for my site is in a seperate github repo
<https://github.com/scootersmk/scott-koch.com>. This allows me to host the
site entirely for free, easily share the source and content for the site,
and not have to maintain my own web server.
