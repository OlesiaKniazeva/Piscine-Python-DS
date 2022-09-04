#!/bin/bash

file=../ex01/hh.csv

(head -n1 $file && tail -n+2 $file | sort -t"," -k2 -k1) > hh_sorted.csv