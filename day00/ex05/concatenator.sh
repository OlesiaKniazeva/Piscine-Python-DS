#!/bin/sh

output_file="result.csv"
rm -rf $output_file


echo 'Enter files for concatenation'
read -r input_file

if [ -z "$input_file" ];
then
    echo "No files entered"
else
  first_file=$(echo "$input_file" | cut -d' ' -f 1)
  header=$(head -n1 < "$first_file")

 echo "$header" > $output_file;

temp="temp"

for arg in $input_file; do
   tail -n+2 "$arg" >> $temp
done

sort -t"," -k2 -k1 < $temp >> $output_file
rm -rf $temp

fi
