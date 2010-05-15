#!/bin/bash
cd /tmp/
hg clone https://bitbucket.org/Anay/buildnotify
cd buildnotify
hg archive -pbuildnotify-0.2.5 -ttgz $HOME/buildnotify.tar.gz
rm -rf /tmp/buildnotify
cd $HOME
rpmdev-setuptree
mv buildnotify.tar.gz rpmbuild/SOURCES/
mv buildnotify.spec rpmbuild/SPECS/
cd rpmbuild/SPECS/
rpmbuild -ba buildnotify.spec