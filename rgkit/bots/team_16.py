import random
import rg


class Robot:
    def act(self, game):
        if 'spawn' in rg.loc_types(self.location):
            return ['move', rg.toward(self.location, rg.CENTER_POINT)]

        my_friendly_neighbours = self.get_neighbours(game)
        if my_friendly_neighbours:
            return ['move', rg.toward(self.location, rg.CENTER_POINT)]

        bad_neighbours = self.get_neighbours(game, friendly=False,
                                             onlyspawn=False)
        # CAMP THE SPAWN! SHOOT NOW!
        shoot = 'attack'
        if bad_neighbours:
            if random.randint(0, 10) > 7:
                print('HAHAHA! DIE DIE DIE!')
            return [shoot, bad_neighbours[0]['location']]



        return ['guard']

    def get_neighbours(self, game, friendly=True, onlyspawn=True):
        if friendly:
            player_id = self.player_id
        else:
            player_id = (self.player_id + 1) % 2
        return  [
            bot for bot in game.robots.values()
            if bot['player_id'] == player_id
            and (
                not onlyspawn or
                'spawn' in rg.loc_types(bot.location)
            )
            and bot.location in rg.locs_around(self.location)
        ]
