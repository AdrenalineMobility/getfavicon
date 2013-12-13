#!/bin/bash
./pull_git.sh

echo "Do you want to push to app engine? You are responsible for any modified or odd files revealed above. Answer by number."

select yn in "Yes" "No"; do
    case $yn in
        Yes ) break;;
        No ) exit;;
    esac
done

appcfg.py update . --oauth2
