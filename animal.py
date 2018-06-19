class animal:
    def __init__(self, name, breed, character):
        self.name = name 
        self.breed = breed
        self.character = character
        self.mood = 10
        self.hunger = 10
        self.health = 10
        self.respect = 10
        self.alive = True
        
    def feed(self):
        if self.hunger < 5:
            self.health = self.health - 1
        self.hunger = self.hunger - 1
        
        self.mood = self.mood + 10/self.mood

        self.checkLife()
        
    def exercise(self):
        if self.alive:
            if self.hunger > 10:
                self.mood = self.mood - 1
            else:
                self.mood = self.mood + 1
            self.health = self.health + 1
        self.checkLife ()
            
    def check(self):
        if self.alive:
            if self.health > 5:
                print (self.name + " is healthy")
            else:
                print (self.name + " is sick!")
                
        else: 
            print(self.name + " IS DEAD!!!")
            
        
        