from bs4 import BeautifulSoup
import requests
import smtplib
from email.message import Message


URL = "url do produto"

headers = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"}

site = requests.get(URL, headers=headers )

soup = BeautifulSoup(site.content, 'html.parser')

title = soup.find('tag onde se encontra o titulo', class_ = 'nome da classe').get_text()
price = soup.find('tag onde se encontra o preço', class_ = 'nome da classe').get_text()

priceInt = float(price)

def sendEmail(title, price, url):
    email_content = f"""
    Confira o produto em oferta:
   {url}
    """
    msg = Message()
    msg['Subject'] = f'Preço de {title} está R${price}'
    msg['From'] = 'seu email'
    msg['To'] = 'email que deseja enviar a mensagem'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_content)

    senha = 'senha de app' 

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(msg['From'], senha)
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()

    print("Email enviado com sucesso!")

if priceInt < 400:
    sendEmail(title, price, URL)