import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters("localhost")
)

channel = connection.channel()

channel.queue_declare(queue="sensor_umidade_chuva", durable=True)

UMIDADE_IDEAL = 50.0

def receber_mensagem(ch, method, properties, body):
    mensagem_recebida = body.decode() 
    print(f"Mensagem recebida: {mensagem_recebida}")

    sensor = mensagem_recebida.split(',')
    chuva = sensor[0]
    umidade = float(sensor[1])

    if chuva=='s' and umidade < UMIDADE_IDEAL:
        print("Jardim ativado. Liberando chuva para o solo.")
    else:
        print("Condições não atingidas. Não liberar água para o solo.")

channel.basic_consume(
    queue="sensor_umidade_chuva",
    on_message_callback=receber_mensagem,
    auto_ack=True
)


print("Aguardando mensagens para o Jardim...")

channel.start_consuming()