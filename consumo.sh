#!/bin/bash

BOLD=$(tput bold) #texto en negrita
NORMAL=$(tput sgr0) #restablece formato

while :
do
# Cambia el título de la terminal a "CONSUMO INQUILINO"
echo -ne "\033]0;CONSUMO INQUILINO\007"
echo " "
echo -e "===APLICACIÓN PARA CALCULAR CONSUMO ELECTRICO===\nEscoga una opción"
	echo "1.) Calcular"
	echo "0.) Salir"
	echo " "
	echo -n "Su opción elegida es: "
	read opcion
	clear
	case $opcion in

1)

echo " "
echo "${BOLD}=== CALCULADORA DE CONSUMO ELECTRICO ==="
echo " "
read -p "Ingresar el consumo electrico del inquilino: " consumo
read -p "Ingresar adicional (baño, hall, lavnaderia): " adicional
echo " "

# Costo por hora kilovatio-hora
kilowat="0.64" #comas
#kilowat="0.6583" #jesus maria

echo "Este es el precio de kilovatio-hora:         $kilowat"

# calcular el costo total de electricidad consumo mas kilovatio
costo_electricidad=$(echo "scale=2; $consumo * $kilowat" | bc)
echo "Resultado del consumo mas el kilovatio-hora: $costo_electricidad"

# calcular el costo del consumo electricidad mas el adicional
costo_electricidad_adicional=$(echo "scale=2; $consumo * $kilowat + $adicional" | bc)
echo "Resultado del kilovatio-hora mas adicional:  $costo_electricidad_adicional"

# Calcular el IGV del 18%
igv=$(echo "scale=2; $costo_electricidad_adicional * 0.18" | bc)
echo "El igv del (18%) es:                         $igv"

# Calcular el total  a pagar (costo de electricidad + IGV)
total=$(echo "scale=2; $costo_electricidad_adicional + $igv" | bc)
echo "El resultado a pagar es:                     $total"

# Redondeo
parte_entera=$(echo "scale=0; $total / 1" | bc)
parte_decimal=$(echo "scale=4; $total - $parte_entera" | bc)

#echo "Monto redondeado a pagar es: $redondeo"

if (( $(echo "$parte_decimal >= 0.5" | bc -l) )); then 
	redondeo=$((parte_entera + 1))
	echo " "
	echo -e "El resultado es mayor o igual a 5
se aplica el redondeo, total a pagar:        S/.$redondeo soles${NORMAL}"
else
	redondeo=$parte_entera
	echo " "
	echo -e "El resultado es menor a 5
no aplica redondeo, total a pagar:           S/.$redondeo soles${NORMAL}"
fi
echo "========================================================="
echo "${NORMAL}Creado por; Jenrry Soto Dextre${NORMAL}"
echo "---------------------------------------------------------"
echo -e "Quiere volver a calcular? entonces escribe 1\nsi quiere salir escribe cero "
echo -e " \n "

;;

0) echo -e "\nUsted a salido de la calculadora" ; exit 0

esac
done

