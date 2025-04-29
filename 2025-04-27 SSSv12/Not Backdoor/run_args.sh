#!/bin/bash

output_file="output.txt"

> "$output_file"

for i in {1..1000}; do
    echo "Running ./not_backdoor $i" >> "$output_file"
    ./not_backdoor "$i" >> "$output_file" 2>&1
    echo "--------------------------------------" >> "$output_file"
done