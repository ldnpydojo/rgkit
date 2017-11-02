import rg

class Robot:
    def act(self, game):
        # if we're in the center, stay put
        # if rg.dist(self.location, rg.CENTER_POINT) > 5:
        #     return ['move', rg.toward(self.location, rg.CENTER_POINT)]             
        # else:
        #     return ['guard']
        #     # places_to_go = rg.locs_around(self.location, filter_out=('invalid', 'obstacle'))
        #     # return ['move', places_to_go[-1]]

        if self.location == rg.CENTER_POINT:
            return ['guard']

        if self.hp < 15 and rg.dist(self.location, rg.CENTER_POINT) < 6:
            return ['guard']

        # if there are enemies around, attack them
        for loc, bot in game.robots.items():
            if bot.player_id != self.player_id:
                if rg.dist(loc, self.location) <= 1:
                    if self.hp < 15:
                        return ['guard']
                    else:
                        return ['attack', loc]

        # move toward the center
        return ['move', rg.toward(self.location, rg.CENTER_POINT)]
