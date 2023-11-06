#!/bin/bash

# Obtén la dirección IP pública de Terraform
my_ip=$(terraform output My_ip | sed 's/"//g')

# Establece una variable de entorno con la dirección IP
export ARACHNI_IP=$my_ip

# Realiza la sustitución en el archivo de inventario

sed -i "s/my_ip/$my_ip/g" inventario
