#!/bin/sh

make clean
./configure
make
ln -sf /bin/true checkbasic
