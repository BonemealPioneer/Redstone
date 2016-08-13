from twisted.internet.task import LoopingCall

class World(object):

    def __init__(self):
        super(World, self).__init__()

        self.players = {}
        self.world_name = ''
        self.world_time_max = 24000
        self.world_time_delay = 0.05
        self.world_time = 0
        self.world_age = 0

    def add_player(self, player):
        pass

    def remove_player(self, player):
        pass

    def set_world_name(self, world_name):
        self.world_name = world_name

    def get_world_name(self):
        return self.world_name

    def set_world_time(self, world_time):
        self.world_time = world_time

    def get_world_time(self):
        return self.world_time

    def set_world_age(self, world_age):
        self.world_age = world_age

    def get_world_age(self):
        return self.world_age

    def startup(self):
        # begin world time as ticks
        self.start_world_time()

    def shutdown(self):
        # stop world time.
        self.stop_world_time()

    def start_world_time(self):
        self.time_loop = LoopingCall(self.tick)
        self.time_loop.start(self.world_time_delay)

    def tick(self):
        if self.world_time >= self.world_time_max:
            # add a world day
            self.set_world_age(self.get_world_age() + 1)

            # reset the current tick time
            self.set_world_time(0)

        # update world time
        self.set_world_time(self.get_world_time() + 1)

    def stop_world_time(self):
        self.time_loop.stop()