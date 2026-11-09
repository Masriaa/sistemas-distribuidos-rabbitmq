import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters("localhost")
)

channel = connection.channel()

channel.queue_declare(queue="sensor_luminosidade", durable=True)

valor_luminosidade = input("Valor da Luminosidade: ")
mensagem = valor_luminosidade

channel.basic_publish(
    exchange="",
    routing_key="sensor_luminosidade",
    body=mensagem
)

print(f"Mensagem enviada para a lâmpada: {mensagem}")

connection.close()