#!/bin/bash

for id in {1..100}
do
        curl "http://141.85.224.70:8088/my-special-name?name-id=${id}";
        echo
done