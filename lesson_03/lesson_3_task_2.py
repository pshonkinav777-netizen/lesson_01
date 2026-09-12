from smartphone import Smartphone

catalog = [Smartphone('Samsung', 'A-54', '+79856664488'),
           Smartphone('Huaway', 'Pura', '+79854360488'),
           Smartphone('Apple I-Phone', '18 pro Max', '+79854456932'),
           Smartphone('Samsung', 'S25', '+79165589874'),
           Smartphone('Samsung', 'Galaxy S1', '+79160106890'),]

for smartphone in catalog:
    print(f'{smartphone.brand} - {smartphone.model}. {smartphone.number}')
