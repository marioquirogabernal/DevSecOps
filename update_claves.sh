#!/bin/bash

# Obtén la dirección IP pública de Terraform
MARIO_CLAVES=$(terraform output My_ip)

# Realiza la sustitución en el archivo de inventario
sed -i "s/my_ip/$my_ip/g" inventario
