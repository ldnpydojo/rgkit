import rg
class Robot:
    def act(self, game):
        if self.hp < 14:
            return ['suicide']

        # Calculate nearby bots
        nearby_bots = 0
        for loc, bot in game.robots.items():
            if bot.player_id!=self.player_id:
                if rg.dist(loc, self.location) <= 2:
                    nearby_bots += 1
                    enemy_loc = loc
        
        # Attack or suicide if bots nearby
        if nearby_bots == 1:
            if rg.dist(enemy_loc, self.location) == 1:
                return['attack', enemy_loc]
            else:
                return ['attack', rg.toward(self.location, enemy_loc)]
        elif nearby_bots > 2:
            return ['suicide']
        
        # If already at center, guard the center
        if self.location == rg.CENTER_POINT:    
            return ['guard']

        # Move to center
        next_move_to_center = rg.toward(self.location, rg.CENTER_POINT)

        #import pdb; pdb.set_trace()
        if next_move_to_center in game['robots']:
            return ['guard'] 

        return ['move', next_move_to_center]
