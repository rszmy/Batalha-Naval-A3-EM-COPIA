# Batalha-Naval-A3-EM
Jogo de batalha naval desenvolvido para o projeto A3 da Unidade Curricular de Estruturas Matemáticas.

- Para começarmos é preciso dar o comando para instalar a VENV (python.exe -m venv .venv) logo após é preciso acessar ela com o comando (..venv\Scripts\Activate.ps1) que acessa e entra na venv.

- Agora é possivel instalar os requirements com os comandos (pip install fastapi, pip install "uvicorn[standard]") ou apenas (-r requirements.txt).

- Para finalizar é preciso sair da pasta src e entrar na pasta database e executar o arquivo python (\database\init_db.py) que gera um arquivo onde esta localizada o nosso banco de dados, com ele pronto é só arrastar ele para a root do código e esta pronto para rodar.

- Para rodar basta entrar na pasta \src e utilizar o comando "uvicorn.exe URLs:app --reload".
