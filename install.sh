#!/bin/sh
rm -rf build && python setup.py develop build_ext --inplace
