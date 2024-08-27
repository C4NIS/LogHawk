#!/bin/bash

# Nome do projeto
PROJECT_NAME="RealTimeLogMonitor"

# Função para criar diretórios e arquivos
create_structure() {
    echo "Criando diretório principal do projeto: $PROJECT_NAME"
    mkdir -p $PROJECT_NAME/{monitor,tests,data/sample_logs,docs,scripts}

    echo "Criando arquivos iniciais em $PROJECT_NAME/monitor"
    touch $PROJECT_NAME/monitor/__init__.py
    touch $PROJECT_NAME/monitor/main.py
    touch $PROJECT_NAME/monitor/log_collector.py
    touch $PROJECT_NAME/monitor/log_processor.py
    touch $PROJECT_NAME/monitor/log_viewer.py
    touch $PROJECT_NAME/monitor/alert_manager.py
    touch $PROJECT_NAME/monitor/exporter.py
    touch $PROJECT_NAME/monitor/config.py

    echo "Criando arquivos de testes em $PROJECT_NAME/tests"
    touch $PROJECT_NAME/tests/__init__.py
    touch $PROJECT_NAME/tests/test_log_collector.py
    touch $PROJECT_NAME/tests/test_log_processor.py
    touch $PROJECT_NAME/tests/test_log_viewer.py
    touch $PROJECT_NAME/tests/test_alert_manager.py
    touch $PROJECT_NAME/tests/test_exporter.py

    echo "Criando requirements.txt e setup.py em $PROJECT_NAME"
    touch $PROJECT_NAME/setup.py

    echo "Criando script de setup de ambiente em $PROJECT_NAME/scripts"
    cat <<EOL > $PROJECT_NAME/scripts/setup_env.sh
#!/bin/bash

echo "Configurando ambiente virtual..."
python3 -m venv venv
source venv/bin/activate

echo "Instalando dependências..."
pip install -r ../requirements.txt

echo "Ambiente configurado com sucesso!"
EOL

    chmod +x $PROJECT_NAME/scripts/setup_env.sh

    echo "Estrutura de diretórios e arquivos criada com sucesso em $PROJECT_NAME"
}

# Executa a função de criação
create_structure
