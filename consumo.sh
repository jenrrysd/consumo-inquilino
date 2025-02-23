#!/bin/bash
clear
BOLD=$(tput bold) #texto en negrita
NORMAL=$(tput sgr0) #restablece formato

echo " "
echo "${BOLD}=== CALCULADORA DE CONSUMO ELECTRICO ==="
echo " "
read -p "Ingresar el consumo electrico del inquilino: " consumo
echo " "

# Costo por hora kilovatio-hora
kilowat="0.6742"
echo "Este es el precio de kilovatio-hora:         $kilowat"

# calcular el costo total de electricidad consumo mas kilovatio
costo_electricidad=$(echo "scale=2; $consumo * $kilowat" | bc)
echo "Resultado del consumo mas el kilovatio-hora: $costo_electricidad"


# Calcular el IGV del 18%
igv=$(echo "scale=2; $costo_electricidad * 0.18" | bc)
echo "El igv del (18%) es:                         $igv"

# Calcular el total  a pagar (costo de electricidad + IGV)
total=$(echo "scale=2; $costo_electricidad + $igv" | bc)
echo "El resultado total a pagar es:               $total"

# Redondeo
parte_entera=$(echo "scale=0; $total / 1" | bc)
parte_decimal=$(echo "scale=4; $total - $parte_entera" | bc)

#echo "Monto redondeado a pagar es: $redondeo"

if (( $(echo "$parte_decimal >= 0.5" | bc -l) )); then 
	redondeo=$((parte_entera + 1))
	echo " "
	echo -e "El resultado es mayor o igual a 5
se aplica el redondeo, total a pagar:        S/.$redondeo soles"
else
	redondeo=$parte_entera
	echo " "
	echo -e "El resultado es menor a 5
no aplica redondeo, total a pagar:           S/.$redondeo soles"
fi
echo " "
echo "${NORMAL}Creado por; Jenrry Soto Dextre${NORMAL}"

