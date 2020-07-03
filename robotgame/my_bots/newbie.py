"""

# ['move', (x, y)]
# ['attack', (x, y)]
# ['guard']
# ['suicide']

location — the robot's location as a tuple (x, y)
hp — the robot's health as an int
player_id — the robot's player_id (what "team" it belongs to)
robot_id — a unique number identifying each robot (only available for robots on your team)

(x, y) in game.robots False or True

rg.locs_around(self.location, filter_out=('invalid', 'obstacle'))

['move', rg.toward(self.location, rg.CENTER_POINT)]

method rg.wdist(loc1, loc2)

"""


def process_game(game):
    self = list()
    others = list()
    for key in game['robots'].keys():
        if game['robots'][key]['player_id'] == 0:
            self.append(key)
        else:
            others.append(key)
    return self, others


class Robot:

    def act(self, game):
        # TODO: quais as estratégias a serem considerar
        return ['guard']
