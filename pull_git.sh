#!/bin/bash

echo "Pulling main repository"
git pull

# Checkout the latest version of the submodules
echo "Checking out latest version of submodules"
git submodule update --recursive --remote

# This hopefully forces them to be on the branch, not detached HEAD
echo "Checkout branches on submodules"
git submodule foreach --recursive 'branch="$(git config -f $toplevel/.gitmodules submodule.$path.branch)"; git checkout $branch'

# And pull them if needed
echo "Pull submodules"
git submodule foreach --recursive git pull
