#!/bin/bash

# Script to build the Slacker package for an AWS Lambda function

shopt -s extglob # Enable extended pattern matching
zip -r Slacker.zip !(Slacker.zip|venv|build_package.sh)