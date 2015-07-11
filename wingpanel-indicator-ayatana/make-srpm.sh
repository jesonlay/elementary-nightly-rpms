#!/usr/bin/bash

NAME=wingpanel-indicator-ayatana
VERSION=0.1

cd $NAME

OLD=$(bzr revno)
bzr pull --quiet
NEW=$(bzr revno)

if [ $OLD != $NEW ]; then
	echo 'Updates! Update revno in $NAME.spec file and run me again.'
	echo 'New revno:' $NEW
	exit
fi

bzr export ../$NAME-$VERSION~rev$NEW.tar.gz
cd ..

mkdir -p $HOME/rpmbuild/SPECS
mkdir -p $HOME/rpmbuild/SOURCES

mv $NAME*.tar.gz $HOME/rpmbuild/SOURCES/
cp make-srpm.sh $HOME/rpmbuild/SOURCES/
cp $NAME.spec $HOME/rpmbuild/SPECS/

cd $HOME/rpmbuild/SPECS

rpmbuild -bs $NAME.spec
mv ../SRPMS/* $HOME/

cd $HOME
rm -rf rpmbuild
