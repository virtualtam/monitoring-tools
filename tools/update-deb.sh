#!/bin/bash

# prevents grep from adding line numbers, etc
export GREP_OPTIONS=""

set -e

BUILD_PACKAGE="dpkg-buildpackage -us -uc -S --source-option=-Zgzip --source-option=--ignore-bad-version"

# library package
tar -czf shinkenplugins_0.1.orig.tar.gz shinkenplugins/ --exclude=$shinkenplugins/debian/*
cd shinkenplugins
$BUILD_PACKAGE
cd ..

# plugin packages
cd plugins
for plugin in `ls -d */ | tr -d '/'`
do 
    # We extract the last version from the changelog
    version=$(cat $plugin/debian/changelog  | grep 'check-' | head -n 1 | awk '{print $2}' | tr -d '()' | cut -d '-' -f 1)
    
    # We create the upstream source, foo.orig.tar.gz
    tar -czf ${plugin}_${version}.orig.tar.gz $plugin/ --exclude=${plugin}/debian/* --exclude=${plugin}/.git*
    
    # And let's build the source package
    cd $plugin
    # -S builds only the source package, the binary one is done by OpenBuildService
    # --ignore-bad-version skips the date check, because the files can be more recent
    # than the last debian/changelog entry
    $BUILD_PACKAGE
    cd ..
done
