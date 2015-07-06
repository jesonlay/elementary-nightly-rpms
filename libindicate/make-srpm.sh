#!/usr/bin/bash

VERSION=12.10.1

mkdir -p $HOME/rpmbuild/SPECS
mkdir -p $HOME/rpmbuild/SOURCES

cp libindicate-$VERSION.tar.gz $HOME/rpmbuild/SOURCES/
cp make-srpm.sh $HOME/rpmbuild/SOURCES/
cp libindicate.spec $HOME/rpmbuild/SPECS/

cd $HOME/rpmbuild/SPECS

rpmbuild -bs libindicate.spec
mv ../SRPMS/* $HOME/

cd $HOME
rm -rf rpmbuild
