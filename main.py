import requests


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
    assert parse('http://127.0.0.1:5000/?name=ferret&color=purple&age=17') == {'name': 'ferret', 'color': 'purple',
                                                                               'age': '17'}
    print('Test 6 Done')
    assert parse('http://127.0.0.1:5000/?name=ferret&color=purple&age=17&') == {'name': 'ferret', 'color': 'purple',
                                                                                'age': '17'}
    print('Test 7 Done')
    assert parse('http://127.0.0.1:5000/?name=ferret&age=17&') == {'name': 'ferret', 'age': '17'}
    print('Test 8 Done')
    assert parse('http://127.0.0.1:5000/?color=purple&age=17&') == {'color': 'purple', 'age':'17'}
    print('Test 9 Done')
    assert parse('http://127.0.0.1:5000/?color=purple&age=17') == {'color': 'purple', 'age':'17'}
    print('Test 10 Done')

print(' ')


def parse_cookie(query: str) -> dict:
    response = requests.get(query)
    return dict(response.cookies)


if __name__ == '__main__':
    assert parse_cookie('http://127.0.0.1:5000/?name=Dima') == {'name': 'Dima'}
    print('Test 1 Done')
    assert parse_cookie('http://127.0.0.1:5000/') == {}
    print('Test 2 Done')
    assert parse_cookie('http://127.0.0.1:5000/?name=Dima&age=28') == {'name': 'Dima', 'age': '28'}
    print('Test 3 Done')
    assert parse_cookie('http://127.0.0.1:5000/?name=Dima=User&age=28') == {'name': 'Dima=User', 'age': '28'}
    print('Test 4 Done')
    assert parse_cookie('http://127.0.0.1:5000/?name=Dima=User&age=28&') == {'name': 'Dima=User', 'age': '28'}
    print('Test 5 Done')
    assert parse_cookie('http://127.0.0.1:5000/?name=Alex&age=25') == {'name': 'Alex', 'age': '25'}
    print('Test 6 Done')
    assert parse_cookie('http://127.0.0.1:5000/?name=Alex&age=25&') == {'name': 'Alex', 'age': '25'}
    print('Test 7 Done')
    assert parse_cookie('http://127.0.0.1:5000/?password=1234') == {'password': '1234'}
    print('Test 8 Done')
    assert parse_cookie('http://127.0.0.1:5000/?password1=1234&password2=12345') == {'password1': '1234',
                                                                                     'password2': '12345'}
    print('Test 9 Done')
    assert parse_cookie('http://127.0.0.1:5000/?hobby=tennis&name=Jeff&age=40&nationality=ukrainian') == {'hobby': 'tennis',
                                                                                                          'name': 'Jeff',
                                                                                                          'age': '40',
                                                                                                          'nationality':
                                                                                                          'ukrainian'}
    print('Test 10 Done')




