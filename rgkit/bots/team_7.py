import rg

class Robot:
    bait = False
    last_turns_hp = 50
    def act(self, game):

        # check if being attacked
        if self.last_turns_hp < self.hp:
            self.bait = True
        last_turns_hp = self.hp

        # guard if attacked
        if self.bait:
            return ['guard']

        closest_bot_loc = None
        closest_bot_distance = 50000
        for loc, bot in game.robots.items():
            if bot.player_id != self.player_id:
                if rg.dist(loc, self.location) <= 1:
                    if self.hp < 11:
                        return ['suicide']
                    else:
                        return ['attack', loc]
                if rg.dist(loc, self.location) < closest_bot_distance:
                    closest_bot_distance = rg.dist(loc, self.location)
                    closest_bot_loc = loc

        # move towards an enemy
        if closest_bot_loc:
            move_loc = rg.toward(self.location, closest_bot_loc)
            if move_loc not in game['robots']:
                return ['move', move_loc]
        return ['guard']

