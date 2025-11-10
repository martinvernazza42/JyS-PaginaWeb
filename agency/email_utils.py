from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def send_email_sendgrid(subject, message, from_email, to_emails):
    """
    Enviar email usando SendGrid Web API
    """
    try:
        # Crear el mensaje
        mail = Mail(
            from_email=from_email,
            to_emails=to_emails,
            subject=subject,
            plain_text_content=message
        )
        
        # Enviar usando SendGrid API
        sg = SendGridAPIClient(api_key=settings.SENDGRID_API_KEY)
        response = sg.send(mail)
        
        logger.info(f"Email enviado exitosamente. Status: {response.status_code}")
        return True
        
    except Exception as e:
        logger.error(f"Error enviando email: {str(e)}")
        return False