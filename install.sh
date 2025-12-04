#!/bin/bash

set -e  # Exit immediately if any command fails

# Get the latest release zip URL and download
ZIP_URL=$(curl -s "https://api.github.com/repos/akash73/arduino-uno-q-apps/releases/latest" | \
grep '"browser_download_url": "[^"]*\.zip"' | \
cut -d'"' -f4 | head -n1)

if [ -z "$ZIP_URL" ]; then
    echo "Error: No zip file found in latest release"
    exit 1
fi

ZIP_NAME=$(basename "$ZIP_URL")
echo "Downloading: $ZIP_NAME"

# Download to /tmp directory
cd /tmp
curl -sL "$ZIP_URL" -o app.zip

unzip -q app.zip
#rm -rf /home/arduino/ArduinoApps/arduino-uno-q-apps-main
mv -f arduino-uno-q-apps-main $HOME/ArduinoApps/
rm -f app.zip

echo "Installed $ZIP_NAME  at $HOME/ArduinoApps"
