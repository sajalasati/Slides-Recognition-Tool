#!/bin/bash
i=0
for file in Dataset/*/*.jpg
do
    cp "$file" slides/"$i".jpg
    i=$((i+1))
done