import json
from player import Player, Forward, MiddleField, DefenseField, GoalKeeper
from player_factory import register, create


def register_player() -> None:
    register('FW', Forward)
    register('MF', MiddleField)
    register('DF', DefenseField)
    register('GK', GoalKeeper)


def load_players():
    with open('player.json', 'r') as f:
        return json.load(f)


def main1():
    data = {
        'players': [
            {
                'name': 'Eruc Cantona',
                'role': 'FW'
            },
            {
                'name': 'David Beckham',
                'role': 'MF'
            },
            {
                'name': 'Steve Bruce',
                'role': 'DF'
            }
        ]
    }

    # 第一版
    # players = []
    # for player in data['players']:
    #     role = player['role']
    #     if role == 'FW':
    #         players.append(Forward(**player))
    #     elif role == 'MF':
    #         players.append(MiddleField(**player))
    #     elif role == 'DF':
    #         players.append(DefenseField(**player))

    # for player in players:
    #     print(player)
    #     player.action()

    # 第二版

    for args in data['players']:
        player = create(args)  # 从工厂获取实例
        # print(player)
        player.action()


def main2(data):
    players = data.copy()
    for args in players['players']:
        player = create(args)  # 从工厂获取实例
        # print(player)
        player.action()


if __name__ == '__main__':
    # 第一版
    # 注册player
    # register_player()
    # main1()

    # 第二版
    # 注册player
    register_player()
    # 加载数据
    data = load_players()
    print(data)
    # 处理数据
    main2(data)
