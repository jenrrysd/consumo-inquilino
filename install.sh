#!/bin/bash

icono=$PWD/consumo.svg
ejecutable=$PWD/consumo.sh
cat > ~/.local/share/applications/consumo.desktop << EOF
[Desktop Entry]
Type=Application
Categories=GNOME;GTK;AudioVideo;Audio;Player;
Name=Consumo
Comment=Consumo
Icon=$icono
Exec=$ejecutable
MimeType=image/jpeg;image/png;image/svg;
Terminal=true
EOF

echo "Listo!!!!"
