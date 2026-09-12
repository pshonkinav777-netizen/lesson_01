from address import Address
from mailing import Mailing

from_addr = Address('134500', 'Sochi', 'Verhniy Laz', '4', '14')
to_addr = Address('145600', 'Moscow', 'Nagatinskaya', '2', '144')
mail = Mailing(to_address=to_addr, from_address=from_addr,
               cost=1000, track='TRACK-123')

print(f'Отправление {mail.track} из {mail.from_address} в {mail.to_address}.'
      f' Стоимость {mail.cost} рублей')
