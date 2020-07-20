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


class Robot:

    def act(self, game):
        # Borrowed sets of sets from github.com/ramk13
        all_locs = {(x, y) for x in xrange(19) for y in xrange(19)}
        spawn = {loc for loc in all_locs if 'spawn' in rg.loc_types(loc)}
        obstacle = {loc for loc in all_locs if 'obstacle' in rg.loc_types(loc)}
        team = {loc for loc in game.robots if game.robots[loc].player_id == self.player_id}
        enemy = set(game.robots) - team
        adjacent = set(rg.locs_around(self.location)) - obstacle
        adjacent_enemy = adjacent & enemy
        safe = adjacent - adjacent_enemy - spawn - team

        north = {loc for loc in team if loc[1] > 9 and loc[0] > 9}
        east = {loc for loc in team if loc[1] <= 9 < loc[0]}
        west = {loc for loc in team if loc[1] <= 9 and loc[0] <= 9}
        south = team - north - east - west

        x, y = int(sum(x for x, y in north if self)/len(north)), int(sum(y for x, y in north)/len(north))
        sx, sy = int(sum(x for x, y in south)/len(south)), int(sum(y for x, y in south)/len(south))
        if self.location in ((nx, ny), (sx, sy)) or rg.locs_around(self.location) in ((nx, ny), (sx, sy)):
            if self.location not in spawn:
                return ['guard']
        if len(adjacent_enemy) >= 3:
            return ['suicide']
        if self.hp < 9 and adjacent_enemy:
            return ['suicide']
        if adjacent_enemy:
            return ['attack', min(adjacent_enemy, key=lambda x: rg.dist(x, self.location))]
        if safe:
            if self.location in north:
                return ['move', rg.toward(self.location, (nx, ny))]
            else:
                return ['move', rg.toward(self.location, (sx, sy))]
        return ['guard']
