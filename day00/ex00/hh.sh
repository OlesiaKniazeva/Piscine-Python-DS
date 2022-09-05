#!/bin/sh

curl "https://api.hh.ru/vacancies?text='data%20scientist'&search_field=name&per_page=20&page=0" -k -H 'User-Agent: api-test-agent'|
jq '.' > hh.json;


#jq '.items | length'  hh.json;