import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters("localhost")
)

channel = connection.channel()

channel.queue_declare(queue="fazer_limpeza", durable=True)

def receber_mensagem(ch, method, properties, body):
    situacao_limpeza = body.decode()
    print(f"Mensagem recebida: {situacao_limpeza}")

    if situacao_limpeza == "LIGA":
        print("Comando enviado com sucesso. Ligando o limpador.")
    elif situacao_limpeza == "DESLIGA":
        print("Comando enviado com sucesso. Parando limpeza.")
    else:
        print("Comando não existe.")

channel.basic_consume(
    queue="fazer_limpeza",
    on_message_callback=receber_mensagem,
    auto_ack=True
)

print("Aguardando mensagens para o limpador...")

channel.start_consuming()