import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters("localhost")
)

channel = connection.channel()

channel.queue_declare(queue="fechar_semaforo", durable=True)

def receber_mensagem(ch, method, properties, body):
    fechar_semanforo = body.decode()
    print(f"Mensagem recebida: {fechar_semanforo}")

    if fechar_semanforo == 's':
        print("Veículo de urgência detectado. Fechando o semáforo.")
    elif fechar_semanforo == 'n':
        print("Nenhum veículo de urgência. Abrindo semáforo.")
    else:
        print("Comando inexistente.")

channel.basic_consume(
    queue="fechar_semaforo",
    on_message_callback=receber_mensagem,
    auto_ack=True
)

print("Aguardando mensagens para o semáforo...")

channel.start_consuming()