#!/usr/bin/bash

NAME=ido
VERSION=12.10.2

mkdir -p $HOME/rpmbuild/SPECS
mkdir -p $HOME/rpmbuild/SOURCES

cp $NAME-$VERSION.tar.gz $HOME/rpmbuild/SOURCES/
cp make-srpm.sh $HOME/rpmbuild/SOURCES/
cp $NAME.spec $HOME/rpmbuild/SPECS/

cd $HOME/rpmbuild/SPECS

rpmbuild -bs $NAME.spec
mv ../SRPMS/* $HOME/

cd $HOME
rm -rf rpmbuild
