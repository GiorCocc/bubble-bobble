from bubble_bobble import Arena, Platform, Enemy, Dragon, Bubble, Bonus
from time import time

# variabili globali
W, H = 480, 420
PLAY_TIME = 120
TOTAL_POINTS = 0

class BubbleGame:
    def __init__(self):
        self._arena=Arena((W, H))
        self._platform = []
        self._bubble = []
        self._bonus = []
        self._enemy = []
        self._playtime = PLAY_TIME  # seconds

        global TOTAL_POINTS

        with open ("platform.txt") as f:
            for line in f:
                x, y, w, h = line.split(",")
                self._platform.append(Platform(self._arena, (int(x),int(y)), int(w), int(h)))
            f.close()

        with open ("dragon.txt") as f:
            line = f.readline()
            x, y = line.split(",")
            self._dragon = Dragon(self._arena, (int(x),int(y)))
            line = f.readline()
            x, y = line.split(",")
            self._dragon1 = Dragon(self._arena, (int(x),int(y)))
            f.close()

        with open ("enemy.txt") as f:
            for line in f:
                x, y = line.split(",")
                self._enemy.append(Enemy((int(x),int(y)),self._arena))
            f.close()

        with open ("bonus.txt") as f:
            for line in f:
                x, y = line.split(",")
                self._bonus.append(Bonus(self._arena, (int(x),int(y))))
                TOTAL_POINTS +=5
            f.close()

    def arena(self) -> Arena:
        return self._arena

    def hero(self) -> Dragon:
        return self._dragon
    
    def hero1(self) -> Dragon:
        return self._dragon1

    def enemy(self) -> Enemy:
        return self._enemy
    
    def enemy_lives (self):
        total_lives = 0
        for enemy in self._enemy:
            total_lives += enemy.lives()
        return total_lives

    def bubble(self) -> Bubble:
        return self._bubble
    
    def platform(self) -> Platform:
        return self._platform

    def game_over(self) -> bool:
        return (self._dragon.lives() <= 0 or self._dragon1.lives() <= 0) or self.remaining_time() <= 0 and self.enemy_lives() > 0

    def game_won(self) -> bool:
        return  self.enemy_lives() == 0 and (self.hero().points() + self.hero1().points()) == TOTAL_POINTS

    def remaining_time(self) -> int:
        return (self._playtime - self._arena.count() // 30)