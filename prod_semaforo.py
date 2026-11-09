import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters("localhost")
)

channel = connection.channel()

channel.queue_declare(queue="fechar_semaforo", durable=True)

fechar_semaforo = input("Veículo em veículo de urgência? (s/n) ")

channel.basic_publish(
    exchange="",
    routing_key="fechar_semaforo",
    body=fechar_semaforo
)

print(f"Mensagem enviada para o semáforo: {fechar_semaforo}")

connection.close()