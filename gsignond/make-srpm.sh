#!/usr/bin/bash

VERSION=1.0.4

cd gsignond

OLD=$(bzr revno)
bzr pull --quiet
NEW=$(bzr revno)

if [ $OLD != $NEW ]; then
	echo 'Updates! Update revno in gsignond.spec file and run me again.'
	echo 'New revno:' $NEW
	exit
fi

bzr export ../gsignond-$VERSION~rev$NEW.tar.gz
cd ..

mkdir -p $HOME/rpmbuild/SPECS
mkdir -p $HOME/rpmbuild/SOURCES

mv gsignond*.tar.gz $HOME/rpmbuild/SOURCES/
cp make-srpm.sh $HOME/rpmbuild/SOURCES/
cp gsignond.spec $HOME/rpmbuild/SPECS/

cd $HOME/rpmbuild/SPECS

rpmbuild -bs gsignond.spec
mv ../SRPMS/* $HOME/

cd $HOME
rm -rf rpmbuild
