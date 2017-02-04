#!/bin/sh

set -e

# start from scratch
rm -rf build dist

# build
python setup.py sdist bdist_wheel

# upload
twine upload \
  --skip-existing \
  --sign \
  --sign-with gpg2 \
  --identity self@allon.nyc \
  --username allonhadaya \
  --password `pass show pypi` \
  dist/*
