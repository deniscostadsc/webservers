#!/bin/bash

# Para usar:
#
# ./siege.sh <numero de repetições> <opções do siege>
#

repeat=$1
shift

for i in $(seq $repeat); do
    siege $*
done