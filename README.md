## Descriere proiect

Proiectul este un set de teste pentru website-ul Secret Garden, care este un magazin online specializat în produse pentru grădinărit, inclusiv plante, decoruri pentru grădină și accesorii pentru plante.

## Framework-ul folosit

Framework-ul utilizat este BDD (Behavior Driven Development), care se concentrează pe descrierea comportamentului dorit al sistemului într-un mod ușor de înțeles atât de către dezvoltatori, cât și de către persoanele non-tehnice, cum ar fi managerii de produs sau clienții.

## Instrumente și limbaje utilizate

- Proiectul a fost scris în [PyCharm](https://www.jetbrains.com/pycharm/) folosind limbajul Python.
- Am folosit limbajul Gherkin pentru scrierea fișierelor de tip feature, care descriu comportamentul sistemului.
- Testele au acoperit funcționalități precum logarea pe pagină, recuperarea parolei, acceptarea cookie-urilor, căutarea de produse, adăugarea în coșul de cumpărături, sortarea după preț, etc.

## Librării utilizate și instalare

- [Selenium](https://www.selenium.dev/): Librărie pentru automatizarea testelor web.
  - Instalare: `pip install selenium`
- [Behave](https://behave.readthedocs.io/en/latest/): Framework BDD pentru Python.
  - Instalare: `pip install behave`
- [WebDriver Manager](https://pypi.org/project/webdriver-manager/): Librărie pentru gestionarea și instalarea automată a WebDriver-elor necesare pentru Selenium.
  - Instalare: `pip install webdriver-manager`

## Rularea testelor

Pentru a rula testele și a genera un raport de execuție HTML, utilizați următoarea comandă în terminal:

```
behave -f behave_html_formatter:HTMLFormatter -o behave-report.html
```


