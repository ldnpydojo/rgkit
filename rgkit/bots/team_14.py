import rg


class Robot:
    def act(self, game):
        # if there are enemies around, attack them
        enemies = list(self.generate_adjacent_enemies(game))
        if self.hp <= sum([min(enemy.hp, 15) for enemy in enemies]):
            return ['suicide']

        if enemies:
            return ['attack', enemies[0].location]

        # if we're in the center, stay put
        if self.location == rg.CENTER_POINT:
            return ['guard']

        # move toward the center
        return ['move', rg.toward(self.location, rg.CENTER_POINT)]

    def generate_adjacent_enemies(self, game):
        for loc, bot in game.robots.items():
            if bot.player_id != self.player_id:
                if rg.dist(loc, self.location) <= 1:
                    yield bot
