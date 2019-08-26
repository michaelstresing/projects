from bs4 import BeautifulSoup
from crontab import CronTab
import requests
import smtplib

sauce = 'https://www.amazon.co.uk/Dell-S2419HGF-Anti-Glare-Gaming-Monitor/dp/B07HS7B1DC/ref=sr_1_16?keywords=monitor%2B144hz&pd_rd_r=6f0fb1ff-74d5-40ba-a080-ff418f0876a4&pd_rd_w=7O5Fm&pd_rd_wg=aRvdr&pf_rd_p=ff22d6ed-266b-4ba8-b66f-ddb8078b45c6&pf_rd_r=93SC9BZEPG795CMEWYQR&qid=1566848807&s=gateway&sr=8-16&th=1'
headers = {'User Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"}


def price_check():

    page = requests.get(sauce, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    # print(soup.prettify())

    product = soup.find(id="productTitle").get_text()

    # print(product.strip())

    price = soup.find(id="priceblock_ourprice").get_text()
    convertedprice = price[1:]
    floatprice = float(convertedprice)

    # print(floatprice)

    if floatprice <= 150.00:
        send_mail()
    else:
        pass


def send_mail():

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('mstresing@gmail.com', 'pass')

    subject = "Monitor price reduced!"
    body = "The price you were looking for is live!\n\n" \
           "LINK HERE: https://www.amazon.co.uk/Dell-S2419HGF-Anti-Glare-Gaming-Monitor/dp/B07HS7B1DC/ref=sr_1_16?keywords=monitor%2B144hz&pd_rd_r=6f0fb1ff-74d5-40ba-a080-ff418f0876a4&pd_rd_w=7O5Fm&pd_rd_wg=aRvdr&pf_rd_p=ff22d6ed-266b-4ba8-b66f-ddb8078b45c6&pf_rd_r=93SC9BZEPG795CMEWYQR&qid=1566848807&s=gateway&sr=8-16&th=1"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'mstresing@gmail.com',
        'mstresing@gmail.com',
        msg
    )

    print('Success!')


# cron = CronTab(user='')
# job = cron.new(command='python3 .py')
# job.minute.every(5)
#
# cron.write() - to create a log of each run.
#
#
# price_check()

# Should go in separate file which runs this file.