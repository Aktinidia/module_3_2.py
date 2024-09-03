def send_email(message, recipient, sender="university.help@gmail.com"):
    if "@" not in recipient and "@" not in sender or '.com' not in recipient and '.com' not in sender or '.ru' not in recipient and '.ru' not in sender or ".net" not in  recipient and ".net" not in sender:
        print('Невозможно отправить письмо с адреса <', sender, '> на адрес <', recipient, '>')
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender == 'university.help@gmail.com':
        print("Письмо успешно отправлено с адреса <", sender, "> на адрес <", recipient, ">.")
    else: print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <', sender, '> на адрес <', recipient, '>.')


send_email(1, 'university.help@gmail.com')