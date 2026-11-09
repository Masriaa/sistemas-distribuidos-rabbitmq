# Simulador de Cidade Inteligente (RabbitMQ)

[Vídeo explicativo](https://drive.google.com/drive/folders/16prMGaYBCrK0FFAH3dHWeAaGT-sht3qM?usp=sharing)

Projeto prático de Sistemas Distribuídos que utiliza o padrão Pub/Sub com RabbitMQ para comunicação entre sensores (produtores) e objetos inteligentes (consumidores).

## Requisitos
* Python 3.x
* Docker
* Biblioteca Pika

## Configuração do Ambiente e Execução

1. Inicie o servidor RabbitMQ via Docker:
```bash
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:4-management
```
2. Crie e ative o ambiente virtual no terminal do projeto (Windows):
```dos
python -m venv venv
.\venv\Scripts\activate
```
3. Instale as dependências:
```dos
pip install pika
```
4. Inicie os Consumidores (Objetos Inteligentes):
   
(Abra terminais separados e execute os scripts que ficarão aguardando mensagens:)
```
python obj_jardim.py

python obj_lampada.py

python obj_semaforo.py

python obj_limpador.py
```
5. Inicie os Produtores (Sensores e Comandos):
   
(Em outro terminal, execute os sensores para enviar dados e verificar a reação dos consumidores:)
```
python sensor_umidade_chuva.py

python sensor_luminosidade.py

python prod_semaforo.py

python prod_limpeza.py
```
