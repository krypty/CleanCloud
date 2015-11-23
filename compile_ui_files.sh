#!/usr/bin/env bash

cd res/gui/
for f in *.ui; do
    pyuic5 ${f} -o ../../gen/gui/$(echo ${f} | sed s/ui/py/) ;
done
