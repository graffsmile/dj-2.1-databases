from dotenv import load_dotenv
import os.path

# Загрузка переменных окружения из файла .env
dotenv_path = 'config-example.env'
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
LOGIN = os.getenv('LOGIN')
PASSWORD_PSQ = os.getenv('PASSWORD_PSQ')
NAME_DB = os.getenv('NAME_DB')
