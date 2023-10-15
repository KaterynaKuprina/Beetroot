CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:
    def __init__(self, my_channel):
        self.my_channel = my_channel
        self.cur_channel = 0

    def first_channel(self):
        self.cur_channel = 1
        return self.my_channel[0]

    def last_channel(self):
        self.cur_channel = len(self.my_channel)
        return self.my_channel[-1]

    def turn_channel(self, some_channel):
        self.some_channel = some_channel
        self.cur_channel = some_channel
        return self.my_channel[some_channel - 1]

    def next_channel(self):
        if self.cur_channel == len(self.my_channel):
            self.cur_channel = 1
            return self.my_channel[0]
        self.cur_channel = self.cur_channel + 1
        return self.my_channel[self.cur_channel - 1]

    def previous_channel(self):
        if self.cur_channel == 1:
            self.cur_channel = len(self.my_channel)
            return self.my_channel[-1]
        self.cur_channel = self.cur_channel - 1
        return self.my_channel[self.cur_channel - 1]

    def current_channel(self):
        return self.my_channel[self.cur_channel - 1]

    def is_exist(self, channel_name):
        self.channel_name = channel_name

        if isinstance(channel_name, int):
            return "yes" if 1 <= channel_name <= len(self.my_channel) else "no"

        if isinstance(channel_name, str):
            return "yes" if channel_name in self.my_channel else "no"


controller = TVController(CHANNELS)

print(controller.first_channel())
print(controller.last_channel())
print(controller.turn_channel(1))
print(controller.next_channel())
print(controller.previous_channel())
print(controller.current_channel())
print(controller.is_exist(4))
print(controller.is_exist("BBC"))
