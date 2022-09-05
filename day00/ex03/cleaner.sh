#!/bin/sh

input_file="../ex02/hh_sorted.csv"
output_file="hh_positions.csv"

(head -n1 $input_file && tail -n+2 $input_file |
  awk 'BEGIN { FS="\"*\"";OFS="\"" } ;
  {
    result=""
    if ($6 ~ /[jJ]unior/) {
          result = result "Junior/";
    }
    if ($6 ~ /[mM]iddle/) {
      result = result "Middle/";
    }
    if ($6 ~ /[sS]enior/) {
       result = result "Senior/";
    }
    result=substr(result, 0, length(result) - 1)
    if ($6 !~ /[jJ]unior/ && $6 !~ /[mM]iddle/ && $6 !~ /[sS]enior/) {
       result = "-";
    }
    $6 = result
    print
  }') > $output_file