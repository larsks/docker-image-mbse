#!/bin/sh

: ${MBSE_ROOT=/opt/mbse}

groupadd -r bbs
useradd -c "MBSE BBS Admin" -d $MBSE_ROOT -g bbs mbse
install -d -m 755 -o mbse -g bbs $MBSE_ROOT/home
useradd -c "MBSE BBS Login" -d $MBSE_ROOT/home/bbs \
	-g bbs -s $MBSE_ROOT/bin/mbnewusr bbs

cat >> $MBSE_ROOT/.bash_profile <<EOF
export MBSE_ROOT=$MBSE_ROOT
export PATH=$MBSE_ROOT/bin:$PATH
EOF

chown mbse:bbs $MBSE_ROOT/.bash_profile
