class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels_list = []
        self.volume = 0

    def turn_off(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def show_status(self):
        if self.is_on:
            if 1 <= self.channel_no <= len(self.channels_list):
                channel_name = self.channels_list[self.channel_no - 1]
                print(f"TV is on, channel {self.channel_no} ({channel_name}). Volume: {self.volume}")
            else:
                print(f"TV is on, channel {self.channel_no} (No channel available). Volume: {self.volume}")
        else:
            print("TV is off.")

    def set_channel(self, new_channel_no):
        if 1 <= new_channel_no <= len(self.channels_list):
            self.channel_no = new_channel_no
        else:
            print(f"Invalid channel number: {new_channel_no}. Please select a valid channel.")

    def set_channels(self, channels_list):
        self.channels_list = channels_list

    def show_channels(self):
        if self.channels_list:
            print("Available channels:")
            for i, channel in enumerate(self.channels_list, start=1):
                print(f"{i}. {channel}")
        else:
            print("No channels are available. Please set the channels.")
    def volume_up(self):
        if 0 <= self.volume <= 10:
            self.volume +=1
        else:
            print('Volume out of range 1-10')
    def volume_down(self):
        if 1 <= self.volume <= 10:
            self.volume -=1
        else:
            print('Volume out of range 1-10')

def main():
    tv = TV()
    tv.turn_on()
    tv.show_status()  # Show status with no channels set
    tv.set_channels(['TVP1', 'TVN', 'Polsat', 'TVP2', 'Filmbox', 'TVP3'])
    tv.show_channels()  # Show available channels
    tv.set_channel(5)  # Set to a valid channel
    tv.show_status()  # Show updated status
    tv.set_channel(10)  # Attempt to set an invalid channel
    tv.turn_off()
    tv.show_status()  # Show status when TV is off
    for i in range(12):
        tv.volume_up()
    

if __name__ == "__main__":
    main()


    