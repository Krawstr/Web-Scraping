<h1 align="left">Web Scraping para Monitoramento de Preços</h1>

###

<p align="left">Este é um projeto simples de Web Scraping desenvolvido em Python, utilizando as bibliotecas BeautifulSoup, requests, smtplib e email.message. O objetivo desta aplicação é monitorar o preço de um determinado produto em algum site e enviar uma notificação por e-mail quando o preço atingir um valor desejado.</p>

###

<h2>Funcionalidades</h2>
<ul>
    <li>🔎 Monitoramento de Preços: Extrai informações como título e preço de um produto em uma página específica.</li>
    <li>✅ Comparar Preços: Compara o preço atual com um limite definido pelo usuário.</li>
    <li>✉️ Envio de Notificações: Envia um e-mail notificando quando o produto está abaixo do preço estabelecido.</li>
</ul>

###

<h2>Tecnologias Utilizadas</h2>
<ul>
    <li>Python 3</li>
    <li>BeautifulSoup: Para extrair informações do HTML.</li>
    <li>Requests: Para realizar as requisições HTTP e obter o conteúdo da página.</li>
    <li>smtplib: Para configurações e envio de e-mails.</li>
    <li>email.message: Para criar a estrutura da mensagem de e-mail.</li>
</ul>

###
<h2>Requisitos</h2>
<p>Certifique-se de ter as seguintes bibliotecas instaladas:</p>

```bash
pip install beautifulsoup4 requests
```
###

<h2>Como Utilizar</h2>
<ol>
<li>Configure a URL do Produto: Altere a variável URL no código para o link do produto desejado.</li>
<li>Atualize o User-Agent: O código usa um User-Agent para evitar bloqueios. Certifique-se de que ele está atualizado e é compatível com seu navegador.</li>
<li>Configure o E-mail: Substitua os valores de msg['From'], msg['To'] e senha no método sendEmail com suas informações.</li>
<li>Defina o Preço Alvo: Altere o valor na condição if priceInt < 400 para o preço que deseja monitorar.</li>
</ol>

<h3>Exemplo de código</h2>

```python
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
```


###

<h2>Possíveis Modificações</h2>
<ul>
    <li>Monitoramento de Múltiplos Produtos: Adicione uma lista de URLs e implemente um loop para analisar vários produtos.</li>
    <li>Envio por Outras Plataformas: Configure o envio de notificações através de SMS ou Telegram.</li>
    <li>Integração com Banco de Dados: Salve históricos de preços para futuras análises.</li>
</ul>

###
<h2>Observação</h2>
<ul>
    <li>Certifique-se de que o site que você está analisando permite Web Scraping para evitar violações de termos de uso.</li
</ul>

###
<h3>Obrigado por ler ate aqui! <3</h3>
