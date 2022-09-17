#!/bin/sh

input_file="../ex02/hh_sorted.csv"
output_file="hh_positions.csv"

(head -n1 $input_file && tail -n+2 $input_file |
  awk 'BEGIN { FS="\",";OFS="\"," } ;
  {
    result=""
     column = tolower($3)
    if (column ~ /junior/) {
          result = result "Junior/";
    }
    if (column ~ /middle/) {
      result = result "Middle/";
    }
    if (column ~ /senior/) {
       result = result "Senior/";
    }
    result=substr(result, 0, length(result) - 1)
    if (column !~ /junior/ && column !~ /middle/ && column !~ /senior/) {
       result = "-";
    }
    $3 = "\"" result
    print
  }') > $output_file