#!/usr/bin/python
# -*- coding: utf-8 -*-
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
import rg


def process_game(game, id):
    self = list()
    others = list()
    for key in game['robots'].keys():
        if game['robots'][key]['player_id'] == id:
            self.append(key)
        else:
            others.append(key)
    return self, others


def test_location(loc):
    if loc not in rg.settings.obstacles and loc not in rg.settings.spawn_coords:
        return True
    return False


class Robot:

    def __init__(self):
        pass

    def act(self, game):
        us, them = process_game(game, self.player_id)
        x = int(sum([x[0] for x in us])/len(us))
        y = int(sum([y[1] for y in us])/len(us))
        if self.location == (x, y):
            return ['guard']
        enemies_around = list()
        friends_around = list()
        for each in them:
            if rg.dist(self.location, each) == 1:
                enemies_around.append(each)
        for each in us:
            if rg.dist(self.location, each) == 1:
                friends_around.append(each)
        if len(friends_around) >= 3:
            return ['guard']
        distance_border = min([rg.wdist(place, self.location) for place in rg.settings.spawn_coords])
        if len(friends_around) >= 2 and distance_border > 3:
            return ['guard']
        if len(enemies_around) >= 2:
            return ['suicide']
        if self.hp < 8 and enemies_around:
            return ['suicide']
        for each in them:
            if rg.dist(self.location, each) == 1:
                if test_location(each):
                    return ['attack', each]
        if test_location((x, y)):
            return ['move', rg.toward(self.location, (x, y))]
        return ['guard']
