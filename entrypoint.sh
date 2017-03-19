#!/bin/sh

: ${MBSE_ROOT=/opt/mbse}

PATH=$MBSE_ROOT/bin:$PATH
export PATH

if [ ! -d "/srv/mbse/etc" ]; then
	echo "* Installing MBSE data files into /srv/mbse"
	cp -a $MBSE_ROOT/template/* /srv/mbse
fi

rm -f /srv/mbse/var/sema/*

chown -R mbse:bbs /srv/mbse

HOME=$MBSE_ROOT exec runuser --preserve-environment -u mbse -- "$@"
