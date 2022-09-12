import sys


def get_people():
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com', 'john@snow.is', 'bill_gates@live.com',
               'mark@facebook.com', 'elon@paypal.com', 'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
                    'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']
    return clients, participants, recipients


def for_promotion_email():
    clients, participants, recipients = get_people()
    return list(set(clients + participants).difference(recipients))


def potential_clients_list():
    clients, participants, recipients = get_people()
    return list(set(participants).difference(clients))


def for_loyalty_program():
    clients, participants, recipients = get_people()
    return list(set(clients).difference(participants))


def start(arg):
    if arg == 'call_center':
        return for_promotion_email()
    elif arg == 'potential_clients':
        return potential_clients_list()
    elif arg == 'loyalty_program':
        return for_loyalty_program()
    else:
        raise Exception("Wrong argument. Enter as argument: \'call_center\' or \'potential_clients\' or "
                        "\'loyalty_program\'")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        data = start(sys.argv[1])
        print(data)
    else:
        raise Exception("Wrong argument. Enter as argument: \'call_center\' or \'potential_clients\' or "
                        "\'loyalty_program\'")