USD_TO_RUB = 95.50
def convert_usd(usd):
    """
    Конвертирует сумму из долларов США в рубли по фиксированному курсу.
     usd: Сумма в долларах США
    """
    return usd * USD_TO_RUB
USD = float(input("Введите кол-во $:"))
print(f"Коп во рублеи: {convert_usd(USD):.2f}")
