from trello import TrelloApi

api_key = '9fa85ba29c84957b202b64e3f0f89ac5'
token = 'f8a7814c5618425df77d8819dcea9ad3188e6be3604ca981a191be095afdf306'

trello = TrelloApi(api_key, token)
response = trello.boards.new('Created with API')
board_id = response['id']
for column in trello.boards.get_list(board_id):
    if 'Нужно' in column['name']:
        list_id = column['id']
        print(column['name'])

card = trello.cards.new('Научиться использовать Trello API', list_id)