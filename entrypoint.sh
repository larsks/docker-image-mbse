#!/bin/sh

: ${MBSE_ROOT=/opt/mbse}

PATH=$MBSE_ROOT/bin:$PATH
export PATH

if [ ! -d "/srv/mbse/etc" ]; then
	echo "* Installing MBSE data files into /srv/mbse"
	cp -a $MBSE_ROOT/template/* /srv/mbse
fi

if [ -f "/srv/mbse/etc/users.data" ]; then
	echo "* Restoring passwords"
	mbse-pwfix
fi

# clear out state and lockfiles from previous instance
rm -f /srv/mbse/var/sema/*
rm -f /srv/mbse/var/run/*

chown -R mbse:bbs /srv/mbse

#HOME=$MBSE_ROOT exec runuser --preserve-environment -u mbse -- "$@"
exec "$@"
