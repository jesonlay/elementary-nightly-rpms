#!/usr/bin/bash

VERSION=0.1.2

mkdir -p $HOME/rpmbuild/SPECS
mkdir -p $HOME/rpmbuild/SOURCES

cp sqlheavy-0.1.2~git.tar.gz $HOME/rpmbuild/SOURCES/
cp make-srpm.sh $HOME/rpmbuild/SOURCES/
cp sqlheavy2.spec $HOME/rpmbuild/SPECS/

cd $HOME/rpmbuild/SPECS

rpmbuild -bs sqlheavy2.spec
mv ../SRPMS/* $HOME/

cd $HOME
rm -rf rpmbuild
