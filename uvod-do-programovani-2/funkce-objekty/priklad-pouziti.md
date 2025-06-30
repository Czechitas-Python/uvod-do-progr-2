## Čtení na doma: Příklad použití OOP

Objektově orientované programování používá řada různých knihoven v nejrůznějších jazycích. Jedním z nich je například Django, které slouží k vývoji webu. Uvažujme, že bychom chtěli náš personální systém vytvořit jako webovou aplikaci. K tomu bychom potřebovali tzv. model, který v Django reprezentuje nějakou datovou entitu. Pokud vytvoříme model, Django nám pro něj automaticky vygeneruje tabulku v databázi. Drobný rozdíl je, že atributy píšeme rovnou ke třídě (je to podobné datovým třídám) a kvůli tabulce v databázi musíme použít nějaké specifické parametry (např. maximální délka řetězce v textovém sloupci, výchozí hodnota atd.). U `car_license_plate` je nastaveno, že ve sloupci může být prázdná hodnota

Naše třída `Employee` dědí od třídy `models.Model` a díky tomu zdědíme metody, které se starají o práci s daty. Například metoda `.save()` slouží k uložení nového nebo úpravě stávajícího záznamu, metody `filter()` pro výběr záznamů na základě podmínky a metoda `.delete()` pro smazání záznamu.

```py
class Employee(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    holiday_entitlement = models.PositiveIntegerField(default=25)
    car_license_plate = models.CharField(max_length=20, null=True, blank=True)
```

Dále vytvoříme stránku (v Django se používá termín *View*) pro přidání nového zaměstnance. Dědíme od třídy `CreateView`, aby bylo jasné, že jde o stránku pro vytvoření záznamu. Poté přidáme atributy `model` (k vytvoření kterého modelu stránka slouží), `template_name` (šablona v jazyce HTML, která určuje, jak bude stránka vypadat), `fields` (která pole mají na stránce být pro vyplnění), `success_url` (kam má být uživatel přesměrován po úspěšném uložení záznamu).

```py
class EmployeeCreateView(CreateView):
    model = Employee
    template_name = 'employee_create.html'
    fields = ['name', 'position', 'holiday_entitlement', 'car_license_plate']
    success_url = reverse_lazy('index')
```

Tím je stránka hotová. Díky dědičnosti se nám Django postará o vytvoření formulářových políček a zařídí uložení nového záznamu po uložení formuláře.
