import tkinter as tk
import random

#jeu de combat entre deux monstre avec tkinter
class Monster:
      def __init__(self, name, health, power):
            self.name = name
            self.health = health
            self.power = power

      def attack(self, other):
            damage = random.randint(1, self.power)
            other.health -= damage
            print(f"{self.name} attacks {other.name} and deals {damage} damage.")

class Game:
      def __init__(self):
            self.root = tk.Tk()
            self.canvas = tk.Canvas(self.root, width=400, height=400)
            self.canvas.pack()

            self.monster1 = Monster("Monster 1", 100, 10)
            self.monster2 = Monster("Monster 2", 100, 10)

            self.canvas.create_text(200, 50, text=self.monster1.name)
            self.canvas.create_text(200, 350, text=self.monster2.name)

            self.canvas.create_rectangle(50, 100, 350, 150, fill="red")
            self.canvas.create_rectangle(50, 250, 350, 300, fill="red")

            self.canvas.create_rectangle(50, 100, 50, 150, fill="green", tags="health1")
            self.canvas.create_rectangle(50, 250, 50, 300, fill="green", tags="health2")

            self.canvas.bind("<Button-1>", self.on_click)

      def update_health_bar(self):
            self.canvas.coords("health1", 50, 100, 50 + self.monster1.health, 150)
            self.canvas.coords("health2", 50, 250, 50 + self.monster2.health, 300)

      def on_click(self, event):
            self.monster1.attack(self.monster2)
            self.monster2.attack(self.monster1)
            self.update_health_bar()

            if self.monster1.health <= 0:
                  print(f"{self.monster2.name} wins!")
                  self.root.quit()
            elif self.monster2.health <= 0:
                  print(f"{self.monster1.name} wins!")
                  self.root.quit()

game = Game()
game.root.mainloop()