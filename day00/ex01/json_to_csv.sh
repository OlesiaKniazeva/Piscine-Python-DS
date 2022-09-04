#!/bin/bash

file="hh.csv"

chmod 777 filter.jq;
echo "\"id\"", "\"created_at\"", "\"name\"", "\"has_test\"", "\"alternate_url\"" > $file;
./filter.jq >> $file;