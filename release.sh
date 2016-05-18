#!/bin/sh

set -e

# start from scratch
rm -rf build dist

# build
python setup.py sdist bdist_wheel

# register
twine register \
  --username allonhadaya \
  --password `pass show pypi` \
  dist/*.tar.gz

# upload
twine upload \
  --skip-existing \
  --sign \
  --sign-with gpg2 \
  --identity self@allon.nyc \
  --username allonhadaya \
  --password `pass show pypi` \
  dist/*
