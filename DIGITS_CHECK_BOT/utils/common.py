import re


def find_users_id_from_log():
    with open('../log.log', 'r') as f:
        text = f.read()
        a = re.findall(r'USER \d+', text)
    return [x.split()[1] for x in list(set(a))]


def get_users_from_txt():
    with open('DATA/active_users_for_attention.txt', 'r') as fu:
        users = fu.read().split('\n')
    return users


def add_user_in_txt(user):
    user = str(user)
    with open('DATA/active_users_for_attention.txt', 'r') as fu:
        users = fu.read().split('\n')
        if user not in users:
            users.append(user)
    with open('DATA/active_users_for_attention.txt', 'w') as fu:
        fu.write('\n'.join(users))


if __name__ == '__main__':
    with open('../DATA/active_users_for_attention.txt', 'r') as fu:
        users = fu.read().split('\n')
        for user in find_users_id_from_log():
            if user not in users:
                users.append(user)
    with open('../DATA/active_users_for_attention.txt', 'w') as fu:
        fu.write('\n'.join(users))
