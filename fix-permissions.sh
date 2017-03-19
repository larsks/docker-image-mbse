#!/bin/sh

: ${MBSE_ROOT=/opt/mbse}

chown -R mbse:bbs $MBSE_ROOT/ftp
chmod 775 $MBSE_ROOT/home/bbs
