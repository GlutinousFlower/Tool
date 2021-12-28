#!/usr/bin/env bash


a=`ls -l report/html/data/suites.csv | awk '{print $5}'`


if [[ $a == 0 ]];then
	echo "Exist failure cases" && exit 1
else
	echo "NOT exist failure cases" && exit 0
fi

