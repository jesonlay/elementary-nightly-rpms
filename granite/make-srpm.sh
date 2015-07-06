#!/usr/bin/bash

VERSION=0.3.0

cd granite

OLD=$(bzr revno)
bzr pull --quiet
NEW=$(bzr revno)

if [ $OLD != $NEW ]; then
	echo 'Updates! Update revno in granite.spec file and run me again.'
	echo 'New revno:' $NEW
	exit
fi

bzr export ../granite-$VERSION~rev$NEW.tar.gz
cd ..

mkdir -p $HOME/rpmbuild/SPECS
mkdir -p $HOME/rpmbuild/SOURCES

mv granite*.tar.gz $HOME/rpmbuild/SOURCES/
cp make-srpm.sh $HOME/rpmbuild/SOURCES/
cp granite.spec $HOME/rpmbuild/SPECS/

cd $HOME/rpmbuild/SPECS

rpmbuild -bs granite.spec
mv ../SRPMS/* $HOME/

cd $HOME
rm -rf rpmbuild
