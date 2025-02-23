#!/bin/bash

icono=$PWD/consumo.svg
ejecutable=$PWD/consumo.sh
cat > ~/.local/share/applications/consumo.desktop << EOF
[Desktop Entry]
Type=Application
Categories=Office;
Name=Consumo
Comment=Calcular Consumo de Electricida del Inquilino
Icon=$icono
Exec=$ejecutable
MimeType=image/jpeg;image/png;image/svg;
Terminal=true
EOF

echo "Listo!!!!"
