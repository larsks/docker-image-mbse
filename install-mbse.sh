#!/bin/sh

: ${MBSE_ROOT=/opt/mbse}

make install
mkdir $MBSE_ROOT/template

chown -R mbse:bbs $MBSE_ROOT/ftp
chmod 775 $MBSE_ROOT/home/bbs

for dir in share home etc var log tmp ftp; do
	mv $MBSE_ROOT/$dir $MBSE_ROOT/template
	ln -s /srv/mbse/$dir $MBSE_ROOT/$dir
done

install -m 755 -o mbse -g bbs -d /srv/mbse/www/htdocs
ln -s /srv/mbse/www /var/www
ln -s /opt/mbse/html /srv/mbse/www/htdocs/docs
