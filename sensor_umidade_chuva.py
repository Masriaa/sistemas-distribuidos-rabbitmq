import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters("localhost")
)

channel = connection.channel()

channel.queue_declare(queue="sensor_umidade_chuva", durable=True)

detectar_chuva = input("Está chovendo? (s/n)")
valor_umidade = input("Valor da Umidade do solo: ")

mensagem = f"{detectar_chuva},{valor_umidade}"

channel.basic_publish(
    exchange="",
    routing_key="sensor_umidade_chuva",
    body=mensagem
)

print(f"Mensagem enviada para o Jardim: {mensagem}")

connection.close()