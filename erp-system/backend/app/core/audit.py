# audit.py: Utilitário para logs de auditoria do ERP

import logging
from datetime import datetime

logger = logging.getLogger("audit")
handler = logging.FileHandler("audit.log")
formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

def registrar_acao(usuario, acao, detalhes=None):
    msg = f"Usuário: {usuario} | Ação: {acao}"
    if detalhes:
        msg += f" | Detalhes: {detalhes}"
    logger.info(msg)
