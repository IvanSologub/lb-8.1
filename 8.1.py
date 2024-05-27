def process_anfisa(query):
    if query == 'Сколько у меня друзей?':
        count = len(DATABASE)
        return 'У тебя ' + str(count) + ' друзей.'
    elif query == 'Кто все мои друзья?':
        friends_string = ''
        for friend in DATABASE.keys():
            friends_string += friend + ' '
        return 'Твои друзья: ' + friends_string
    else:
        return '<неизвестный запрос>'