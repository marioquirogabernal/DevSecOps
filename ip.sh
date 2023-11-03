# Obtén la dirección IP pública de Terraform
my_ip=$(terraform output My_ip)

# Establece una variable de entorno con la dirección IP
export ARACHNI_IP=$my_ip
