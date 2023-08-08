import requests


ENDPOINT = 'https://cl2u.ru/'


def test_connect_api():
    connect_response = connect()
    assert connect_response.status_code == 200


def test_create_url():
    payload = create_payload()
    create_url_response = create_url(payload)
    assert create_url_response.status_code == 200

    data = create_url_response.json()
    print(data)
    # task_id = data['id']['task_id']
    # get_task_response = get_task(task_id)
    # assert get_task_response.status_code == 200
    # get_task_data = get_task_response.json()
    # assert get_task_data['content'] == payload['content']
    # assert get_task_data['user_id'] == payload['user_id']


# def test_get_url():
#     payload = new_payload()
#     create_url_response = create_url(payload)
#     assert create_url_response.status_code == 201


def connect():
    return requests.get(ENDPOINT)


def create_url(payload):
    return requests.post(ENDPOINT + 'url', json=payload)


def get_url(short_url):
    return requests.get(ENDPOINT + f'{short_url}')


def create_payload():
    url = 'https://www.honeybadger.io/blog/django-test-github-actions/'
    return {
        'url': url,
    }


def get_payload():
    url = 'https://www.honeybadger.io/blog/django-test-github-actions/'
    return {
        'url': url,
        'short_url': '1a9e2d'
    }
