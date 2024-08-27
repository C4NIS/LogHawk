#!/bin/bash

echo "Configurando ambiente virtual..."
python3 -m venv venv
source venv/bin/activate

echo "Instalando dependências..."
pip install -r ../requirements.txt

echo "Ambiente configurado com sucesso!"
