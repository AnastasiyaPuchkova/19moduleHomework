import requests
import json

class PetFriends:
    def __init__(self):
        self.base_url = 'https://petfriends.skillfactory.ru/'

    def get_api_key(self, email, password):
        '''Метод делает запрос к API сервера и возвращает статус запроса и результат в формате JSON
        с уникальным ключом пользователя, найденного по указанным email и паролем'''
        headers = {
            'email': email,
            'password': password
        }
        res = requests.get(self.base_url+'api/key', headers=headers)
        status = res.status_code  #Получение статуса запроса
        result = ''
        try:
            result = res.json()  #Результат в json
        except:
            result = res.text
        return  status, result

    def get_list_of_pets(self, auth_key, filter):
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате JSON
        со списком наденных питомцев, совпадающих с фильтром. На данный момент фильтр может иметь
        либо пустое значение - получить список всех питомцев, либо 'my_pets' - получить список
        собственных питомцев"""
        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}

        res = requests.get(self.base_url+'api/pets', headers=headers, params=filter)
        status = res.status_code  # Получение статуса запроса
        result = ''
        try:
            result = res.json()  # Результат в json
        except:
            result = res.text
        return status, result

    def add_new_pet_with_photo(self, auth_key, name, animal_type, age, pet_photo):
        """Метод отправляет (постит) на сервер данные о добавляемом питомце и возвращает статус
        запроса на сервер и результат в формате JSON с данными добавленного питомца"""

        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age,
                'pet_photo': (pet_photo, open(pet_photo, 'cat1'), 'image/jpeg')
            })
        headers = {'auth_key': auth_key['key']}

        res = requests.post(self.base_url + 'api/pets', headers=headers, data=data)
        status = res.status_code  # Получение статуса запроса
        result = ''
        try:
            result = res.json()  # Результат в json
        except:
            result = res.text
        print(result)
        return status, result

    def delete_pet(self, auth_key, pet_id):
        """Метод отправляет на сервер запрос на удаление питомца по указанному ID и возвращает
        статус запроса и результат в формате JSON с текстом уведомления о успешном удалении."""
        headers = {'auth_key': auth_key['key']}

        res = requests.delete(self.base_url + 'api/pets/' + pet_id, headers=headers)
        status = res.status_code  # Получение статуса запроса
        result = ''
        try:
            result = res.json()  # Результат в json
        except:
            result = res.text
        return status, result

    def update_pet_info(self, auth_key, pet_id, name, animal_type, age):
        """Метод отправляет запрос на сервер о обновлении данных питомуа по указанному ID и
        возвращает статус запроса и result в формате JSON с обновлённыи данными питомца"""
        headers = {'auth_key': auth_key['key']}
        data = {
            'name': name,
            'age': age,
            'animal_type': animal_type
        }
        res = requests.put(self.base_url + 'api/pets/' + pet_id, headers=headers, data=data)
        status = res.status_code  # Получение статуса запроса
        result = ''
        try:
            result = res.json()  # Результат в json
        except:
            result = res.text
        return status, result

    def add_new_pet_without_photo(self, auth_key, name, animal_type, age):
        """Метод отправляет (постит) на сервер данные о добавляемом питомце и возвращает статус
        запроса на сервер и результат в формате JSON"""
        headers = {'auth_key': auth_key['key']}
        data = {
            'name': name,
            'age': age,
            'animal_type': animal_type
        }
        res = requests.post(self.base_url + 'api/create_pet_simple', headers=headers, data=data)
        status = res.status_code  # Получение статуса запроса
        result = ''
        try:
            result = res.json()  # Результат в json
        except:
            result = res.text
        print(result)
        return status, result

    def add_photo_of_pet(self, auth_key, pet_id, pet_photo):
        """Метод отправляет (постит) на сервер данные в видео фото и возвращает статус
        запроса на сервер и результат в формате JSON"""
        data = MultipartEncoder(
            fields={
                'pet_photo': (pet_photo, open(pet_photo, 'cat2'), 'image/jpeg')
            })
        headers = {'auth_key': auth_key['key']}

        res = requests.post(self.base_url + 'api/pets/set_photo/' + pet_id, headers=headers, data=data)
        status = res.status_code  # Получение статуса запроса
        result = ''
        try:
            result = res.json()  # Результат в json
        except:
            result = res.text
        print(result)
        return status, result

