import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters("localhost")
)

channel = connection.channel()

channel.queue_declare(queue="sensor_luminosidade", durable=True)

def receber_mensagem(ch, method, properties, body):
    mensagem_recebida = body.decode()
    print(f"Mensagem recebida: {mensagem_recebida}")

    luminosidade = float(mensagem_recebida)

    if float(luminosidade) < 100:
        print("Baixa luminosidade. Ativando lâmpada do poste.")
    else:
        print("Ainda há luz natural suficiente. Não ativar lâmpada.")

channel.basic_consume(
    queue="sensor_luminosidade",
    on_message_callback=receber_mensagem,
    auto_ack=True
)

print("Aguardando mensagens para a lâmpada...")

channel.start_consuming()