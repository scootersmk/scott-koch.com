Title: Using the Strace Rule for quicker troubleshooting on Linux
Date: 2018-12-01 11:00
Category: Sysadmin

Over the years troubleshooting many different problems on Linux/UNIX
I have developed a personal rule of sorts to help me troubleshoot
problems faster and avoid loosing time by going down the wrong path.
I had a bad habit of after doing some basic troubleshooting of a
problem and not seeing any indication of cause, I would all of a
sudden jump to using strace to troubleshoot the problem further.
Sometimes I would get lucky and the root-cause of the problem would
be revealed by the strace output. While other times it would lead
to sometimes an hour or more of wadeing through output, reading man
pages of system calls, and chasing down things that looked like
they may be errors but either weren't or were unrelated to the
problem at hand.

So one day when I would lost in strace output, this rule occured to me:

If I am using strace to troubleshoot a problem, then the chances
are I'm in too deep and need to take a step back and re-evaluate
the problem and my toubleshooting options.

The power and usefulness of strace are also the reasons its shouldn't
be your goto tool for troubleshooting. You can easily miss the exact
cause of your problem in all the output. You can notice another
error or strange behavior and get distracted trying to understand
that scenario. You can get a false sense of making progress or
gaining understanding about a problem, which isn't really leading
to solving the problem.

Now when I catch myself breaking or about to break my rule, I stop
and re-evaluate the problem and start asking myself some questions
like the following:.
  - Do I understand the problem correctly, its impact, and its full scope(when, where, how, etc)

  - Have I exausted all non-strace methods in troubleshoot especially
  basic things like resource contraints, permissions issues, log
  file output, problems with dependent systems, information from
  monitoring/metrics systems, etc.

  - Can I change something about the problem to understand the scope
  of the problem(different user, different OS version, different
  software version, different network, etc)

  - Is there another resource I can utilize to ensure I'm on the
  right course, such as a co-worker, online community, etc. Sometimes
  the act of preparing to describe the problem(by writing it down) to
  someone helps you realize that missing piece of knowledge that you
  needed.

This is not to say that you should be discouraged from using strace
to help you solve your problems. I would just recommend you try to
only use strace when you have a specific aspect to examine that you
can target your attention to. This way you figure out exactly what
you wanted to know without getting distracted or wasting time dealing
with a ton of output. Some recomendations here:

  - Does the problem still occur when you strace it. Do the following
  to grab the strace output into a file, but ensure the problem
  still actually occurs before you spend time looking at the data.
```
$ strace -f -o strace.out /usr/bin/ps
```
  - Are you interested in a certain type of system call, such as
  network activity(connect/send/recv) or file
  I/O(stat,open,read,write,close), that you can filter your search
  on.
```
$ strace -f -o telnet.out -e connect /usr/bin/telnet www.google.com 80
#OR
$ strace -f -o cat.out -e open,read,close /usr/bin/cat /etc/resolv.conf
```
  - Are you interested in the timeing of the problem or understanding what part of the problem is taking so long
```
#Shows how long each system call took
$ strace -f -T -o cat.out /usr/bin/cat /etc/resolv.conf
#Shows statistics of each system call including times called, average time, and percent of total time
$ strace -f -cw -o cat.out /usr/bin/cat /etc/resolv.conf
```

I think a similar rule could be stated for other debugging tools that have
the potential to present you with a overwelming amount of data that
you are then left to sort through or visually parse. Some other instances that I can think of:
- TCPdump network packet traces on high traffic systems/networks
- Opting to turn on as much debugging output as possible from a program
- Log output from one of more busy services or systems

Remember there is nothing wrong with any of these tools as they are
great ways to get more information about what is going on. However
proceed cautiously on how and when you choose to use them such that
you don't waste valueble time dealing with the flood of data these
tools can produce. 

I hope sharing this rule will help others troubleshoot and debug
problems more efficiently.

