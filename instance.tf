resource "aws_instance" "MyInstancia" {
  ami           = "ami-0fc5d935ebf8bc3bc"
  instance_type = "t3.micro"
  key_name = "mario_claves"
  security_groups = [aws_security_group.allow_ssh_http.id]
  subnet_id = "subnet-0a5ddfb50c67b40ea"
  tags = {
    Name = "MyInstancia"
  }
}

output "My_ip"{
  value = aws_instance.MyInstancia.public_ip
}

resource "aws_security_group" "allow_ssh_http" {
  name        = "allow_ssh_http"

  ingress {
    description      = "ssh"
    from_port        = 22
    to_port          = 22
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  ingress {
    description      = "http"
    from_port        = 80
    to_port          = 80
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  ingress {
    description      = "webgoat"
    from_port        = 8080
    to_port          = 8080
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  ingress {
    description      = "webgoat"
    from_port        = 9090
    to_port          = 9090
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  tags = {
    Name = "allow_ssh_http"
  }
}
