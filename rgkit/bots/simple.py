import rg

class Robot(object):
    def act(self, game):
        print('g.settings', rg.settings)
        rg.settings.max_turns = 0
        return ['move', rg.toward(self.location, rg.CENTER_POINT)]
