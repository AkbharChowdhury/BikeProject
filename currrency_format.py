import locale

locale.setlocale(locale.LC_MONETARY, 'en_GB')


def format_money(amount: float):
    return locale.currency(amount, grouping=True)
