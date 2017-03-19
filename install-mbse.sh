#!/bin/sh

: ${MBSE_ROOT=/opt/mbse}

make install
mkdir $MBSE_ROOT/template

for dir in etc var log tmp ftp; do
	mv $MBSE_ROOT/$dir $MBSE_ROOT/template
	ln -s /srv/mbse/$dir $MBSE_ROOT/$dir
done
