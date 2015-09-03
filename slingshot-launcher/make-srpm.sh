#!/usr/bin/bash

VERSION=0.8.1.1

cd slingshot-launcher

OLD=$(bzr revno)
bzr pull --quiet
NEW=$(bzr revno)

if [ $OLD != $NEW ]; then
	echo 'Updates! Update revno in slingshot-launcher.spec file and run me again.'
	echo 'New revno:' $NEW
	exit
fi

bzr export ../slingshot-launcher-$VERSION~rev$NEW.tar.gz
cd ..

mkdir -p $HOME/rpmbuild/SPECS
mkdir -p $HOME/rpmbuild/SOURCES

mv slingshot-launcher*.tar.gz $HOME/rpmbuild/SOURCES/
cp make-srpm.sh $HOME/rpmbuild/SOURCES/
cp slingshot-launcher.spec $HOME/rpmbuild/SPECS/
cp slingshot-launcher.conf $HOME/rpmbuild/SOURCES/

cd $HOME/rpmbuild/SPECS

rpmbuild -bs slingshot-launcher.spec
mv ../SRPMS/* $HOME/

cd $HOME
rm -rf rpmbuild

