Testar em todos os hosts:
pytest -v --connection=ansible teste.py

Selecionar hosts para executar
pytest -v --connection=ansible --hosts=frontend,backend  teste.py
