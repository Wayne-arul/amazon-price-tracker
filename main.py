from bs4 import BeautifulSoup
import requests
import smtplib

# en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36

USER_EMAIL = "waynetest@gmail.com"
USER_PASS = "PASS"
URL = "https://www.amazon.in/dp/B09G9DBNNN?th=1"
header = {
    "Accept-Language" : "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"
}


response = requests.get(url=URL, headers=header)
product_page = response.text

soup = BeautifulSoup(product_page, "html.parser")
price_first = soup.find(name="span", class_="a-price-whole").getText().split('.')[0]
price_decimal = soup.find(name="span", class_="a-price-fraction").getText()

price_1 = ""
price_2 = price_1.join(price_first.split(','))
actual_price = float(price_2 + "." + price_decimal)

print(actual_price)

if actual_price < 200000:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=USER_EMAIL, password=USER_PASS)
        connection.sendmail(
            from_addr= USER_EMAIL,
            to_addrs= "wayne@gmail.com",
            msg=f"Subject: Amazon Price Alert\n\nApple iPhone 13 Pro Max (128GB) - Gold is now {actual_price}"

        )
