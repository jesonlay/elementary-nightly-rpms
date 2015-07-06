#!/usr/bin/bash

VERSION=2.0.1

cd switchboard

OLD=$(bzr revno)
bzr pull --quiet
NEW=$(bzr revno)

if [ $OLD != $NEW ]; then
	echo 'Updates! Update revno in switchboard.spec file and run me again.'
	echo 'New revno:' $NEW
	exit
fi

bzr export ../switchboard-$VERSION~rev$NEW.tar.gz
cd ..

mkdir -p $HOME/rpmbuild/SPECS
mkdir -p $HOME/rpmbuild/SOURCES

mv switchboard*.tar.gz $HOME/rpmbuild/SOURCES/
cp make-srpm.sh $HOME/rpmbuild/SOURCES/
cp switchboard.spec $HOME/rpmbuild/SPECS/

cd $HOME/rpmbuild/SPECS

rpmbuild -bs switchboard.spec
mv ../SRPMS/* $HOME/

cd $HOME
rm -rf rpmbuild
