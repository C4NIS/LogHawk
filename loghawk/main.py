import argparse
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from loghawk import cli, logger, parser, analyzer, exporter

def main():
    # Configurações iniciais (ex: configuração de logs)
    log = logger.setup_logging()

    # Parsing de argumentos da linha de comando
    args = cli.parse_arguments()

    logs = None
    filtered_logs = None

    # Lógica de execução com base nos comandos
    if args.command == "import":
        logs = parser.import_logs(args.file)
        if logs is not None:
            log.info("Logs importados com sucesso.")
            print(f"Logs importados: {logs.shape[0]} entradas")
        else:
            log.error("Falha ao importar logs.")

    elif args.command == "filter":
        if logs is None:
            print("Nenhum log foi importado. Use o comando 'import' primeiro.")
        else:
            filtered_logs = analyzer.filter_logs(logs, args.criteria)
            if filtered_logs is not None:
                log.info("Logs filtrados com sucesso.")
                print(f"Logs filtrados: {filtered_logs.shape[0]} entradas")
            else:
                log.error("Falha ao filtrar logs.")

    elif args.command == "export":
        if filtered_logs is None:
            print("Nenhum log filtrado disponível. Use o comando 'filter' primeiro.")
        else:
            success = exporter.export_logs(filtered_logs, args.format, f"exported_logs.{args.format}")
            if success:
                log.info("Logs exportados com sucesso.")
            else:
                log.error("Falha ao exportar logs.")

    else:
        print("Comando não reconhecido. Use --help para ver as opções disponíveis.")
        log.error("Comando não reconhecido.")

if __name__ == "__main__":
    main()

