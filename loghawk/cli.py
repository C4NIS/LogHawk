import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="LogHawk - Análise de Logs em Terminal")

    # Definição dos comandos suportados
    subparsers = parser.add_subparsers(dest="command", help="Comandos disponíveis")

    # Comando 'import'
    import_parser = subparsers.add_parser("import", help="Importa logs de um arquivo")
    import_parser.add_argument("--file", type=str, required=True, help="Caminho para o arquivo de logs a ser importado")

    # Comando 'filter'
    filter_parser = subparsers.add_parser("filter", help="Aplica filtros nos logs importados")
    filter_parser.add_argument("--criteria", type=str, required=True, help="Critérios para filtrar os logs (ex: palavras-chave, datas)")

    # Comando 'export'
    export_parser = subparsers.add_parser("export", help="Exporta logs filtrados para um arquivo")
    export_parser.add_argument("--format", type=str, choices=["csv", "json"], required=True, help="Formato de exportação (csv ou json)")

    # Parsing dos argumentos
    args = parser.parse_args()
    return args
