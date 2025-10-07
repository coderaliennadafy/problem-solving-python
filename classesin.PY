class point:
    def move (self):
        print("move")
        
    def draw (self):
        print("draw")
        
pt1 = point()
pt1.x = 10
pt1.y = 20

print(pt1.x)
print(pt1.y)
pt1.move()
pt1.draw()

