---
title: Celkova cena
demand: 3
---

Uvažujme nyní, že chceme nabízet možnost koupit si dohromady jízdenky na vlak i letenky a naším úkolem je spočítat celkovou cenu. Vytovř si seznam `tickets`, kam vlož alespoň jednu letenku a jednu jízdenku na vlak. Dále vytvoř cyklus, který všechny položky v seznamu projde a vypočítá celkovou cenu.

Pokud bys chtěl(a) mít kód bezpečný, můžeš využít funkci `isinstance()`, která zkontroluje, zda se do seznamu nepřipletlo něco, co tam nemá být. Než použiješ metodu `total_price()`, zkontroluj pomocí `isinstance()`, zda aktuální objekt pochází ze třídy, která dědí od třídy `Ticket`. Zamysli se také nad tím, zda by bylo možné využít funkci `hasattr()`.

:::solution
```py
class Ticket:
    def __init__(self, basic_price, seat_number):
        self.basic_price = basic_price
        self.seat_number = seat_number

    def get_price(self):
        return self.basic_price

class TrainTicket(Ticket):
    def __init__(self, basic_price, seat_number, fare_class):
        super().__init__(basic_price, seat_number)
        self.fare_class = fare_class
    
    def get_price(self):
        if self.fare_class == "economy":
            return self.basic_price
        elif self.fare_class == "business":
            return self.basic_price * 1.3
        else:
            return self.basic_price

class PlaneTicket(TrainTicket):
    def __init__(self, basic_price, seat_number, fare_class, checkout_luggages):
        super().__init__(basic_price, seat_number, fare_class)
        self.checkout_luggages = checkout_luggages
    
    def get_price(self):
        if self.fare_class == "economy":
            base_price = self.basic_price
        else:
            base_price = self.basic_price * 1.5
        
        return base_price + (self.checkout_luggages * 2000)


train_economy = TrainTicket(150, "A12", "economy")
plane_business = PlaneTicket(6000, "3A", "business", 1)
tickets = [train_economy, plane_business]
total_price = 0
for item in tickets:
    if isinstance(item, Ticket):
        total_price = total_price + item.get_price()
print(total_price)
```
:::
