#!/usr/bin/bash

VERSION=0.3.1

cd noise

OLD=$(bzr revno)
bzr pull --quiet
NEW=$(bzr revno)

if [ $OLD != $NEW ]; then
	echo 'Updates! Update revno in noise.spec file and run me again.'
	echo 'New revno:' $NEW
	exit
fi

bzr export ../noise-$VERSION~rev$NEW.tar.gz
cd ..

mkdir -p $HOME/rpmbuild/SPECS
mkdir -p $HOME/rpmbuild/SOURCES

mv noise*.tar.gz $HOME/rpmbuild/SOURCES/
cp make-srpm.sh $HOME/rpmbuild/SOURCES/
cp noise.spec $HOME/rpmbuild/SPECS/
cp noise.conf $HOME/rpmbuild/SOURCES/

cd $HOME/rpmbuild/SPECS

rpmbuild -bs noise.spec
mv ../SRPMS/* $HOME/

cd $HOME
rm -rf rpmbuild
