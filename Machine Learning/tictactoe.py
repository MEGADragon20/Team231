import arcade
import  time as t
import random as r

def easy_gamemode(field):
    ra = r.randint(0,9)
    za = ra%3 - 1
    zb = int(ra/3) - 1 
    j = field[zb][za]
    if j.owner == None:
        j.texture = arcade.load_texture("data/o.png")
        j.owner = "o"
        return field
    else:
        return easy_gamemode(field)
def medium_gamemode(field):
    j = ""
    for b in range(3):
        a = b-1
        if field[0][a].owner == field[1][a].owner != None and field[2][a].owner == None:
            j = field[2][a]
        elif field[0][a].owner == field[2][a].owner != None and field[1][a].owner == None:
            j = field[1][a]
        elif field[1][a].owner == field[2][a].owner != None and field[0][a].owner == None:
            j = field[0][a]
        elif field[a][0].owner == field[a][1].owner != None and field[a][2].owner == None:
            j = field[a][2]
        elif field[a][0].owner == field[a][2].owner != None and field[a][1].owner == None:
            j = field[a][1]
        elif field[a][1].owner == field[a][2].owner != None and field[a][0].owner == None:
            j = field[a][0]
    if j == "":
        if field[0][0].owner == field[1][1].owner != None and field[2][2].owner == None:
            j = field[2][2]
        elif field[0][0].owner == field[2][2].owner != None and field[1][1].owner == None:
            j = field[1][1]
        elif field[2][2].owner == field[1][1].owner != None and field[0][0].owner == None:
            j = field[0][0]

        elif field[2][0].owner == field[1][1].owner != None and field[0][2].owner == None:
            j = field[0][2]
        elif field[0][2].owner == field[1][1].owner != None and field[2][0].owner == None:
            j = field[2][0]
        elif field[2][0].owner == field[0][2].owner != None and field[1][1].owner == None:
            j = field[1][1]
    if j != "":
        j.texture = arcade.load_texture("data/o.png")
        j.owner = "o"
        print("e")
        return field
    else:
        print("s")
        return easy_gamemode(field)
        
def check_for_victory(gitter):
    for i in gitter:
        if i[0].owner == i[1].owner and i[1].owner == i[2].owner and i[2].owner != None:
            return True
    for i in range(3):
        if gitter[0][i].owner == gitter[1][i].owner and gitter[1][i].owner == gitter[2][i].owner and gitter[2][i].owner != None:
                return True
    if gitter[0][0].owner == gitter[1][1].owner and gitter[1][1].owner == gitter[2][2].owner and gitter[2][2].owner != None:
        return True
    if gitter[0][2].owner == gitter[1][1].owner and gitter[1][1].owner == gitter[2][0].owner and gitter[2][0].owner != None:
        return True
    return False

def check_if_full(gitter):
    for i in range(3):
        for j in range(3):
            if gitter[i][j].owner == None:
                return False
    return True
    
class Game(arcade.View):
    def __init__(self, bot):
        super().__init__()
        self.players= ["x","o"]
        self.activeplayer = self.players[0]
        self.gitter = [[None, None, None],[None, None, None],[None, None, None]]
        self.bot = bot
        for i in range(3):
            for j in range(3):
                self.gitter[i][j] = Field(position=(i+1, j+1))
    
    def on_draw(self):
        self.clear()
        for i in range(3):
            for j in range(3):
                self.gitter[i][j].draw()
    
    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        pseudosprite = arcade.Sprite()
        pseudosprite.center_x = x
        pseudosprite.center_y = y
        pseudosprite.set_hit_box([(1,1), (0,1), (0,0), (1,0)])
        if button == 1:
            for i in self.gitter:
                for j in i:
                    if arcade.check_for_collision(pseudosprite, j) and j.owner == None:
                        j.texture = arcade.load_texture("data/"+self.activeplayer+".png")
                        j.owner = self.activeplayer
                        a = self.players[0]
                        self.players.pop(0)
                        self.players.append(a)
                        self.activeplayer = self.players[0]
                        if check_for_victory(self.gitter):
                            if self.players[0] == "o":
                                l = ("Blue", "#00FFFF")
                            elif self.players[0] == "x":
                                l = ("Pink","#E80EFF")
                            self.on_draw()
                            self.end(l)
                        elif check_if_full(self.gitter):
                            self.end(("Nobody", "#FFFFFF"))
                        else:
                            if self.bot != "d":
                                if self.bot == "a":
                                    self.gitter = easy_gamemode(self.gitter)
                                elif self.bot == "b":
                                    self.gitter = medium_gamemode(self.gitter)
                                a = self.players[0]
                                self.players.pop(0)
                                self.players.append(a)
                                self.activeplayer = self.players[0]
                                if check_for_victory(self.gitter):
                                    if self.players[0] == "o":
                                        l = ("Blue", "#00FFFF")
                                    elif self.players[0] == "x":
                                        l = ("Pink","#E80EFF")
                                    self.on_draw()
                                    self.end(l)
                                elif check_if_full(self.gitter):
                                    self.end(("Nobody", "#FFFFFF"))


                        
        return super().on_mouse_press(x, y, button, modifiers)

    def end(self, l):
        game_view = Victory(l)
        t.sleep(0.1)
        self.window.show_view(game_view)
    
class Field(arcade.Sprite):
    def __init__(self, position: tuple):
        super().__init__(filename="data/empty.png",center_x=position[0]*200-100, center_y=position[1]*200-100)
        self.owner = None

class Victory(arcade.View):
    def __init__(self, winner: str):
        super().__init__()
        self.winner = winner

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        self.clear()
        arcade.start_render()
        arcade.draw_text("Victory for", 300, 400, arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text(self.winner[0], 300, 300, arcade.color_from_hex_string(self.winner[1]), font_size=50, anchor_x="center")
        arcade.draw_text("Klick to rematch", 300, 200, arcade.color.WHITE, font_size=25, anchor_x="center")

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        if button == 1:
            game = Home()
            self.window.show_view(game)
        return super().on_mouse_press(x, y, button, modifiers)
class Home(arcade.View):
    def __init__(self):
        super().__init__()
    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)
    def on_draw(self):
        self.clear()
        arcade.draw_line(0, 300, 600, 300, arcade.color_from_hex_string("#00ff00"), 4)
        arcade.draw_line(300, 0, 300, 900, arcade.color_from_hex_string("#00ff00"), 4)
    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        if x < 300 and y > 300:
            game = Game("a")
        elif x > 300 and y > 300:
            game = Game("b")
        elif x < 300 and y < 300:
            game = Game("c")
        elif x > 300 and y < 300:
            game = Game("d")
        self.window.show_view(game)
        

class W(arcade.Window):
    def __init__(self):
        super().__init__(width=600, height=600, title="TicTacToe")
        startscreen = Home()
        self.show_view(startscreen)


game = W()
arcade.run()
