# Base class
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.battery = battery  # in mAh
        self.is_on = False

    def power_on(self):
        if not self.is_on:
            self.is_on = True
            print(f"{self.brand} {self.model} is now ON 🔋")
        else:
            print(f"{self.brand} {self.model} is already ON.")

    def power_off(self):
        if self.is_on:
            self.is_on = False
            print(f"{self.brand} {self.model} is now OFF 📴")
        else:
            print(f"{self.brand} {self.model} is already OFF.")

    def take_picture(self):
        if self.is_on:
            print(f"{self.model} 📸: Picture taken!")
        else:
            print("Please power on the phone first.")

    def charge(self):
        print(f"{self.model} is charging... 🔌")

# Inherited class
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery, gpu_power):
        super().__init__(brand, model, storage, battery)
        self.gpu_power = gpu_power  # Performance rating

    def play_game(self, game_name):
        if self.is_on:
            print(f"Launching {game_name} on {self.model} 🎮 with GPU power: {self.gpu_power}")
        else:
            print("Power on the phone to play games.")

# Another Inherited class
class CameraPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, camera_quality):
        super().__init__(brand, model, storage, battery)
        self.camera_quality = camera_quality  # MP or rating

    def take_picture(self):
        if self.is_on:
            print(f"{self.model} 📷: Snapped a {self.camera_quality}MP photo!")
        else:
            print("Power on the phone to use the camera.")

# Example usage
phone1 = Smartphone("Samsung", "Galaxy A10", 64, 4000)
phone2 = GamingSmartphone("Asus", "ROG Phone 5", 256, 6000, "Ultra")
phone3 = CameraPhone("Google", "Pixel 7", 128, 5000, 50)

phone1.power_on()
phone1.take_picture()
phone2.power_on()
phone2.play_game("PUBG Mobile")
phone3.power_on()
phone3.take_picture()