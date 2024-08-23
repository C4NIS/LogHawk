import logging
from logging.handlers import RotatingFileHandler

def setup_logging():
    # Configuração do logger
    logger = logging.getLogger("LogHawk")
    logger.setLevel(logging.DEBUG)

    # Formato dos logs
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Console handler (exibe logs no terminal)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # File handler (salva logs em arquivo)
    file_handler = RotatingFileHandler("loghawk.log", maxBytes=5000000, backupCount=5)
    file_handler.setFormatter(formatter)

    # Adicionando os handlers ao logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
