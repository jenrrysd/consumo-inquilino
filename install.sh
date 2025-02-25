#!/bin/bash

icono=$PWD/consumo.svg
ejecutable=$PWD/consumo.py
cat > ~/.local/share/applications/consumo.desktop << EOF
[Desktop Entry]
Type=Application
Categories=Office;
Name=Consumo
Comment=Calcular Consumo de Electricidad del Inquilino
Icon=$icono
Exec=python3 $ejecutable
MimeType=image/jpeg;image/png;image/svg;
Terminal=false
EOF

echo "Listo!!!!"
