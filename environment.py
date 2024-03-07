from browser import Browser
from pages.secret_garden_login import HomePage
from pages.secret_garden_search import Search


def before_all(context):
    context.browser = Browser()
    context.browser.maximise_window()
    context.secret_garden_login = HomePage()
    context.secret_garden_search = Search()


def after_all(context):
    context.browser.close_browser()
