import pandas as pd

def export_logs(logs, file_format, output_file):
    """
    Exporta os logs filtrados para um arquivo no formato especificado.
    
    Args:
        logs (pd.DataFrame): DataFrame contendo os logs filtrados.
        file_format (str): Formato de exportação ('csv' ou 'json').
        output_file (str): Nome do arquivo de saída.
    
    Returns:
        bool: True se a exportação for bem-sucedida, False caso contrário.
    """
    try:
        if file_format == "csv":
            logs.to_csv(output_file, index=False)
        elif file_format == "json":
            logs.to_json(output_file, orient='records', lines=True)
        else:
            raise ValueError("Formato de exportação não suportado. Use 'csv' ou 'json'.")
        
        print(f"Logs exportados com sucesso para {output_file}")
        return True
    except Exception as e:
        print(f"Erro ao exportar logs: {e}")
        return False
