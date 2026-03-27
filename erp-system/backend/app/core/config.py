# Configurações globais do sistema ERP

import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "chave-padrao-insegura")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./app.db")
