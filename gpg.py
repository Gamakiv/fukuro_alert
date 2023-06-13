import gnupg

# публичный ключ получателя должен быть импортирован
# и добавлен в доверенные

def encrypt_message(message):
    gpg = gnupg.GPG()
    public_keys = gpg.list_keys()
    gpg.encoding = 'utf-8'

    encrypted_data = gpg.encrypt(message, recipients=['receprt@local.local'])

    if encrypted_data.ok:
        print(encrypted_data)  # Выводим зашифрованные данные
        return(encrypted_data)
    else:
        print('Encryption failed')
        return('')

