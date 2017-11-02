class Robot:
    def act(self, game):
        neighbour_loc = [
                (self.location[0] - 1, self.location[1] - 1),
                (self.location[0] - 1, self.location[1] + 1),
                (self.location[0] + 1, self.location[1] - 1),
                (self.location[0] + 1, self.location[1] + 1)
        ]

        for n in neighbour_loc:
            if n not in game['robots']:
                # neighbour location is empty
                is_surrounded = False
                break
            else:
                # n is not empty
                is_surrounded = game['robots'][n].player_id == self.player_id
                break
        else:
            is_surrounded = True

        if is_surrounded:
            return ['suicide']

        for loc in game.robots:
            bot = game.robots.get(loc)
            if bot.player_id != self.player_id:
                if rg.dist(loc, self.location) <= 1:
                    return ['attack', loc]
        return ['move', rg.toward(self.location, rg.CENTER_POINT)]
