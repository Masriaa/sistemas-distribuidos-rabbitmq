import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters("localhost")
)

channel = connection.channel()

channel.queue_declare(queue="fazer_limpeza", durable=True)

fazer_limpeza = input("Digite seu comando para limpeza: (LIGA/DESLIGA) ")

channel.basic_publish(
    exchange="",
    routing_key="fazer_limpeza",
    body=fazer_limpeza
)

print(f"Mensagem enviada para o limpador: {fazer_limpeza}")

connection.close()