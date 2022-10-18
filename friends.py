from collections import defaultdict


def check_relation(net: tuple, first: str, second: str) -> bool:
    relations = create_communication_sets(net)
    checked_persons = set()
    queue_people = {first}

    while queue_people:
        friend = queue_people.pop()
        if second in relations[friend]:
            return True
        checked_persons.add(friend)
        new_people = relations[friend].difference(checked_persons)
        queue_people.update(new_people)
    return False


def create_communication_sets(net: tuple) -> defaultdict:
    """
    Creating a dictionary where the key is the name,
    and the value is a set of friends
    """
    relations = defaultdict(set)
    for friend_1, friend_2 in net:
        relations[friend_1].add(friend_2)
        relations[friend_2].add(friend_1)
    return relations


if __name__ == '__main__':
    net = (
        ("Ваня", "Лёша"), ("Лёша", "Катя"),
        ("Ваня", "Катя"), ("Вова", "Катя"),
        ("Лёша", "Лена"), ("Оля", "Петя"),
        ("Стёпа", "Оля"), ("Оля", "Настя"),
        ("Настя", "Дима"), ("Дима", "Маша")
    )

    assert check_relation(net, "Петя", "Стёпа") is True
    assert check_relation(net, "Маша", "Петя") is True
    assert check_relation(net, "Ваня", "Дима") is False
    assert check_relation(net, "Лёша", "Настя") is False
    assert check_relation(net, "Стёпа", "Маша") is True
    assert check_relation(net, "Лена", "Маша") is False
    assert check_relation(net, "Вова", "Лена") is True
