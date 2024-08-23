import pandas as pd

def import_logs(file_path):
    """
    Importa logs de um arquivo e os retorna como um DataFrame do pandas.
    
    Args:
        file_path (str): Caminho para o arquivo de logs a ser importado.
    
    Returns:
        pd.DataFrame: DataFrame contendo os logs importados.
    """
    try:
        if file_path.endswith('.csv'):
            logs = pd.read_csv(file_path)
        elif file_path.endswith('.json'):
            logs = pd.read_json(file_path)
        else:
            raise ValueError("Formato de arquivo não suportado. Use .csv ou .json.")
        
        return logs
    except Exception as e:
        print(f"Erro ao importar logs: {e}")
        return None
