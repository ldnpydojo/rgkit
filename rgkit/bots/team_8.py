import rg

class Robot:
    """Attack bot Mk 2"""
    def act(self, game):
        # Find nearest enemy
        enemies = {}
        nearest_enemy = (1000000, rg.CENTER_POINT)
        for loc, bot in game.robots.items():
            if bot.player_id != self.player_id:
                enemies[loc] = bot
                distance = rg.dist(loc, self.location)
                if distance < nearest_enemy[0]:
                    nearest_enemy = (distance, loc)

        # If nearest enemy is next to us, ATTACK or KABOOM!
        if nearest_enemy[0] <= 1:
            potential_suicide_damage = 0
            for loc in rg.locs_around(self.location):
                if loc in enemies:
                    potential_suicide_damage += min(15, enemies[loc].hp)
            if self.hp < potential_suicide_damage:
                return ['suicide']
            else:
                return ['attack', nearest_enemy[1]]

        # If we cannot move, defend.
        desired_move = rg.toward(self.location, nearest_enemy[1])
        if rg.loc_types(desired_move) in ['obstacle', 'invalid']:
            return['guard']
        
        # Otherwise, advance on the enemy without mercy
        return ['move', desired_move]
