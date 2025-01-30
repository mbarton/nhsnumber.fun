#!/bin/bash -e

# Looks like UV can't bundle into the stupid ZIP file format that AWS Lambda expects.
# So fine... I'll do it myself.

rm -rf dist
uv pip install nhs_number --target dist
cp app.py dist
cd dist
zip -r nhsnumber_fun.zip .