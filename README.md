## Project description

The project is a set of tests for the Secret Garden website, which is an online store specializing in gardening products, including plants, garden decorations, and plant accessories.
The tests covered functionalities such as logging in to the page, password recovery, accepting cookies, product search, adding to the shopping cart, sorting by price, etc.

## Framework Used

The framework used is BDD (Behavior Driven Development), which focuses on describing the desired behavior of the system in an easily understandable manner by both developers and non-technical individuals, such as product managers or clients.

## Tools

- The project was written in [PyCharm](https://www.jetbrains.com/pycharm/) using Python.
- I used the Gherkin language for writing the feature files, which describe the system's behavior.
- [Selenium](https://www.selenium.dev/): Library for web test automation.
  - Installation: `pip install selenium`
- [Behave](https://behave.readthedocs.io/en/latest/):  BDD framework for Python.
  - Installation: `pip install behave`
- [WebDriver Manager](https://pypi.org/project/webdriver-manager/): Library for managing and automatically installing the WebDriver needed for Selenium.
  - Instalare: `pip install webdriver-manager`

## Installing the project

* Open Git Bash
* Change the current working directory to the location where you want the cloned directory
* Type git clone and paste the URL link of the repository
```
git clone https://github.com/CameliaAM/Project_Secret_Garden.git
```
* Press Enter to create your local clone

## Running the tests
Use the following commands in the terminal:
1. Running tests
```
behave
```
2. Running tests and generating an HTML execution report
```
behave -f behave_html_formatter:HTMLFormatter -o behave-report.html
```
3. Running a feature file
```
behave -i file_name.feature
```
4. Running specific tests
```
behave --tags=tag_name (E.g. test1)
```
5. Running specific tests and generating an HTML execution report
```
behave -f html-o behave-report --tags=tag_name
```

