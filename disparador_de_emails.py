import smtplib
import ssl
import email.message

enviar_email = 'Sim'
while enviar_email == 'Sim':
    message = email.message.Message()

    message['From'] = str(input('Digite o email do emissor: ')).strip()
    password = str(input('Digite a senha do email do emissor: ')).strip()

    message['To'] = str(input('Digite o email do receptor: ')).strip()
    message.add_header('Content-Type', 'text/html')

    message['Subject'] = str(input('Digite o assunto da mensagem: '))
    text_body = str(input('Digite a mensagem para o receptor: ')).strip()

    message.set_payload(text_body)

    context = ssl.create_default_context()
    with smtplib.SMTP('smtp.gmail.com', 587) as conexao:
        conexao.ehlo()
        conexao.starttls(context=context)
        conexao.login(message['From'], password)
        conexao.sendmail(message['From'], message['To'],message.as_string().encode('utf-8'))

    enviar_email = str(input('Deseja enviar um novo email? ')).strip().title()

print('Volte sempre ao sistema. . .')
exit(0)
