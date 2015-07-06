#!/usr/bin/bash

VERSION=2.1.0

cd libgsignon-glib

OLD=$(bzr revno)
bzr pull --quiet
NEW=$(bzr revno)

if [ $OLD != $NEW ]; then
	echo 'Updates! Update revno in libgsignon-glib.spec file and run me again.'
	echo 'New revno:' $NEW
	exit
fi

bzr export ../libgsignon-glib-$VERSION~rev$NEW.tar.gz
cd ..

mkdir -p $HOME/rpmbuild/SPECS
mkdir -p $HOME/rpmbuild/SOURCES

mv libgsignon-glib*.tar.gz $HOME/rpmbuild/SOURCES/
cp make-srpm.sh $HOME/rpmbuild/SOURCES/
cp libgsignon-glib.spec $HOME/rpmbuild/SPECS/

cd $HOME/rpmbuild/SPECS

rpmbuild -bs libgsignon-glib.spec
mv ../SRPMS/* $HOME/

cd $HOME
rm -rf rpmbuild
