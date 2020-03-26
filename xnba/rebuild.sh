#!/bin/bash

cd xnba-1.0.3
cp -rL ../debian .
dpkg-buildpackage -uc -us  -aamd64 

echo "> efi binary:"
ls -l debian/xnba-undi/tftpboot/xcat/xnba.efi
