class Device:
    def turn_on(self):
        pass
    
    def turn_off(self):
        pass

    def switch_channel(self, channel):
        pass

class Lamp(Device):
    def turn_on(self):
        print("Lamp turned on")

    def turn_off(self):
        print("Lamp turned off")

class TV(Device):
    def turn_on(self):
        print("TV turned on")

    def turn_off(self):
        print("TV turned off")

    def switch_channel(self, channel):
        print(f"Switched to channel {channel}")

    def turn_on_lamp(self):
        print("Lamp turned on by TV")

    def turn_off_lamp(self):
        print("Lamp turned off by TV")

tv = TV()
tv.turn_on()
tv.switch_channel(5)
tv.turn_off()
tv.turn_on_lamp()

#----------------------------------------------------------------------------

class Switchable:
    def turn_on(self):
        pass
    
    def turn_off(self):
        pass

class Controllable:
    def switch_channel(self, channel):
        pass

class Lamp(Switchable):
    def turn_on(self):
        print("Lamp turned on")

    def turn_off(self):
        print("Lamp turned off")

class TV(Switchable, Controllable):
    def turn_on(self):
        print("TV turned on")

    def turn_off(self):
        print("TV turned off")

    def switch_channel(self, channel):
        print(f"Switched to channel {channel}")
