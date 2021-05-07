class Television:
    def __init__(self):
        self.current_channel = 0
        self.current_volume = 0
        self.tv_on = False
        self.__max_volume = 50
        self.__max_channel = 999

    def get_max_volume(self):
        return self.__max_volume

    def get_max_channel(self):
        return self.__max_channel

    def tv_turn_on(self):
        self.tv_on = True

    def tv_turn_off(self):
        self.tv_on = False
        self.current_channel = 0
        self.current_volume = 0

    def tv_volume_up(self):
        if self.tv_on:
            if self.current_volume < self.__max_volume:
                self.current_volume += 1
            else:
                print(f'TV is at the maximum volume: {self.__max_volume}')

    def tv_volume_down(self):
        if self.tv_on:
            if self.current_volume > 0:
                self.current_volume -= 1
            else:
                print('TV current volume is 0')

    def tv_channel_up(self):
        if self.tv_on:
            if self.current_channel < self.__max_channel:
                self.current_channel += 1
            else:
                print(f'TV is at the maximum channel: {self.__max_channel}')

    def tv_channel_down(self):
        if self.tv_on:
            if self.current_channel > 0:
                self.current_channel -= 1
            else:
                print('TV current channel number is 0')


class RemoteControl:
    def __init__(self, tv_object):
        self.__tv_object = tv_object

    def rc_turn_tv_on(self):
        self.__tv_object.tv_turn_on()

    def rc_turn_tv_off(self):
        self.__tv_object.tv_turn_off()

    def rc_volume_up(self):
        if self.__tv_object.tv_on:
            if self.__tv_object.current_volume < \
                    self.__tv_object.get_max_volume():
                self.__tv_object.tv_volume_up()
            else:
                print(
                    f'TV is at the maximum volume: '
                    f'{self.__tv_object.get_max_volume()}')

    def rc_volume_down(self):
        if self.__tv_object.tv_on:
            if self.__tv_object.current_volume > 0:
                self.__tv_object.tv_volume_down()
            else:
                print('TV current volume is 0')

    def rc_channel_up(self):
        if self.__tv_object.tv_on:
            if self.__tv_object.current_channel < \
                    self.__tv_object.get_max_channel():
                self.__tv_object.tv_channel_up()
            else:
                print(
                    f'TV is at the maximum channel: '
                    f'{self.__tv_object.get_max_channel()}'
                )

    def rc_channel_down(self):
        if self.__tv_object.tv_on:
            if self.__tv_object.current_channel > 0:
                self.__tv_object.tv_channel_down()
            else:
                print('TV current channel number is 0')

    def rc_channel_dial(self, channel_number):
        if 0 <= channel_number <= self.__tv_object.get_max_channel():
            self.__tv_object.current_channel = channel_number
        else:
            print(f'Channel number must be between 0 and '
                  f'{self.__tv_object.get_max_channel()}')

    def rc_channel_display(self):
        if self.__tv_object.tv_on:
            return f'Selected channel: {self.__tv_object.current_channel}'

    def rc_volume_display(self):
        if self.__tv_object.tv_on:
            return f'Selected volume: {self.__tv_object.current_volume}'
