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

for keytype in rsa ecdsa ed25519; do
	if [ ! -f /etc/ssh/ssh_host_${keytype}_key ]; then
		echo "* Generating ${keytype} ssh key"
		/usr/libexec/openssh/sshd-keygen ${keytype}
	fi
done

# clear out state and lockfiles from previous instance
rm -f /srv/mbse/var/sema/*
rm -f /srv/mbse/var/run/*
rm -f /srv/mbse/tmp/*

chown -R mbse:bbs /srv/mbse

#HOME=$MBSE_ROOT exec runuser --preserve-environment -u mbse -- "$@"
exec "$@"
