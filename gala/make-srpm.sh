#!/usr/bin/bash

VERSION=0.2.0

cd gala

OLD=$(bzr revno)
bzr pull --quiet
NEW=$(bzr revno)

if [ $OLD != $NEW ]; then
	echo 'Updates! Update revno in gala.spec file and run me again.'
	echo 'New revno:' $NEW
	exit
fi

bzr export ../gala-$VERSION~rev$NEW.tar.gz
cd ..

mkdir -p $HOME/rpmbuild/SPECS
mkdir -p $HOME/rpmbuild/SOURCES

mv gala*.tar.gz $HOME/rpmbuild/SOURCES/
cp make-srpm.sh $HOME/rpmbuild/SOURCES/
cp gala.spec $HOME/rpmbuild/SPECS/

cd $HOME/rpmbuild/SPECS

rpmbuild -bs gala.spec
mv ../SRPMS/* $HOME/

cd $HOME
rm -rf rpmbuild
