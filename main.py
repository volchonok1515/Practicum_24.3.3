import requests
import json

url='https://petstore.swagger.io/v2'

pet_1='Вениамин Бедросович'
pet_2='Босяк граф де Боскас'

data={
  "id": 0,
  "category": {"id": 0,"name": "string"},
  "name": pet_1,
  "photoUrls": ["string"],
  "tags": [{"id": 0,"name": "string"}],
  "status": "available"
}

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Host': 'petstore.swagger.io',
    'Content-Length': '236',
    'Cache-Control': 'no-cache'
}

res=requests.post(f"{url}/pet", headers=headers, data=json.dumps(data))
print(res.status_code)
print('Создан питомец:')
pet_id = dict(res.json())['id']

data["id"]=pet_id
data["name"]=pet_2
print(f'\nизменяем имя питомца на {pet_2}')

res_2=requests.put(f"{url}/pet", headers=headers,data=json.dumps(data))
print(res_2.status_code)
print('Внесены изменения:')

print('\nЗапрашиваем данные с сервера о питомце по id -'+str(pet_id))
res_3=requests.get( f"{url}/pet/{pet_id}", headers=headers)

print(res_3.status_code)
print('На сервере имеются такие данные:')

print('\nУдаляем данные о питомце по id -'+str(pet_id))
res_4=requests.delete( f"{url}/pet/{pet_id}", headers=headers)

print(res_4.status_code)
print('Данные о питомце удалены:')

res_5 = requests.get(f'{url}{pet_id}', headers=headers)
print(res_5.status_code)
print('Код ответа - 404 \nНа сервере нет данных о питомце')
