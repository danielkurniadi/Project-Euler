#!/bin/bash
n=1
max=50
set --

while [ "$n" -le "$max" ]; do
    set -- "$@" "Problem$n"
    n=$(( $n + 1 ));
done

mkdir "$@"
