# MBSE BBS in a Box

This project will build a Docker image that can be used to run an MBSE
BBS.  The image includes:

- MBSE
- xinetd for managing network services
- darkhttpd for serving web content
- supervisord as a process supervisor

## Basic usage

Create a data volume for hosting your BBS data:

    docker volume create mbse

Boot the BBS container:

    docker run -v mbse:/srv/mbse -it --name mbse oddbit/mbse

Configure the BBS:

    docker exec -it -u mbse mbse bin/mbsetup

Open the BBS:

    docker exec -it -u mbse mbse bin/mbstat open

At this point the BBS is running and you should be able to log in by
telneting to the container IP:

    $ telnet 172.17.02

Log in as `bbs` to create a new account.

## Managing the BBS

You can re-run `mbsetup` at any time to make configuration changes:

    docker exec -it -u mbse mbse bin/mbsetup
