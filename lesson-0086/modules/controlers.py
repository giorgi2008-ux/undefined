

class Controller:
    def __init__(self):
        pass

    def jump(self):
        print("jump")

    def walk(self):
        print("walk")
        

    def run(self):
        print("run ")  
class Controllar:
    def __init__(self):
        pass

    def jump(self):
        print("jump")

    def walk(self):
        print("walk")
        

    def run(self):
        print("run ")


class MainController(Controller):
    def __init__(self):
        super().__init__()
         


class Main(Controllar):
    def __init__(self):
        super().__init__()

    def __str__(self):
        print("ar vici classebi kargad!")
        return ""

