#!/usr/bin/env bash

test_dir=./tests

for t in $test_dir/*; do
  [ -f $t ] && [ ! -L $t ]  && {
    $t
  }
done

