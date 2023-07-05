import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def enviar_correo(remitente, destinatario, asunto, mensaje, contrasenia):
    """Envía un correo electrónico utilizando el servidor SMTP"""
    try:
        # Crea una conexión segura con el servidor SMTP
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()

        # Inicia sesión en la cuenta de correo del remitente
        servidor.login(remitente, contrasenia)

        # Crea un mensaje multipartito
        mensaje_correo = MIMEMultipart()
        mensaje_correo['From'] = remitente
        mensaje_correo['To'] = destinatario
        mensaje_correo['Subject'] = asunto

        # Adjunta el mensaje al correo
        mensaje_correo.attach(MIMEText(mensaje, 'plain'))

        # Envía el correo electrónico
        servidor.send_message(mensaje_correo)

        print("Correo electrónico enviado exitosamente.")
    except Exception as e:
        print("Ocurrió un error al enviar el correo electrónico:", str(e))
    finally:
        # Cierra la conexión con el servidor SMTP
        servidor.quit()
