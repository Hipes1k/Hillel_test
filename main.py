import requests, json

def parse(query: str) -> dict:
    response = requests.get(query)
    return response.json()


if __name__ == '__main__':
    assert parse('http://127.0.0.1:5000/?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    print('Test 1 Done')
    assert parse('http://127.0.0.1:5000/?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    print('Test 2 Done')
    assert parse('http://127.0.0.1:5000/') == {}
    print('Test 3 Done')
    assert parse('http://127.0.0.1:5000/?') == {}
    print('Test 4 Done')
    assert parse('http://127.0.0.1:5000/?name=Dima') == {'name': 'Dima'}
    print('Test 5 Done')
    assert parse('http://127.0.0.1:5000/?name=ferret&color=purple&age=17') == {'name': 'ferret', 'color': 'purple', 'age': '17'}
    print('Test 6 Done')
    assert parse('http://127.0.0.1:5000/?name=ferret&color=purple&age=17&') == {'name': 'ferret', 'color': 'purple', 'age': '17'}
    print('Test 7 Done')
    assert parse('http://127.0.0.1:5000/?name=ferret&age=17&') == {'name': 'ferret', 'age': '17'}
    print('Test 8 Done')
    assert parse('http://127.0.0.1:5000/?color=purple&age=17&') == {'color': 'purple', 'age':'17'}
    print('Test 9 Done')
    assert parse('http://127.0.0.1:5000/?color=purple&age=17') == {'color': 'purple', 'age':'17'}
    print('Test 10 Done')





