#! /bin/bash

for i in {1..4000}
do
        curl -s "http://141.85.224.70:8082/colors/index.php?index=$i" | grep SSS
done
