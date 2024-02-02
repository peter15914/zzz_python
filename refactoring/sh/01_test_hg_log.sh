#!/bin/sh
#hg log -r 'adds("/media/diskwin10/zzz/dev/oisterra/terra_20191213/src/OISTerraManager/rpath.pri")'
#hg log -r 'file("/media/diskwin10/zzz/dev/oisterra/terra_20191213/src/OISTerraManager/rpath.pri")'
hg log -r 'file("/media/diskwin10/zzz/dev/oisterra/terra_20191213/src/OISTerraManager/main.cpp")' | grep "user"
