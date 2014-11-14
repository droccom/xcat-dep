#!/bin/bash

tar xvfj xnba-1.0.3.tar.bz2 
cd xnba-1.0.3
cp -rL ../debian .
dpkg-buildpackage -uc -us  -aamd64 
cd -
rm -rf xnba-1.0.3 
cp `pwd`/debian/`dh_listpackages`/tftpboot/xcat/xnba.kpxe `pwd`/binary/
cp `pwd`/debian/`dh_listpackages`/tftpboot/xcat/xnba.efi  `pwd`/binary/
