import arcade
import  time as t
import random as r

import arcade.color
import arcade.color

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
        return field
    else:
        return easy_gamemode(field)

def hard_gamemode(field):
    
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
def sum(gitter):
    s = 0
    for i in gitter:
        for j in i:
            if j.owner != None:
                s += 1
    return s

def ev_sum(p):
    return "o" if p%2 == 0 else "x"
def check_if_full(gitter):
    for i in range(3):
        for j in range(3):
            if gitter[i][j].owner == None:
                return False
    return True
    
class Game(arcade.View):
    def __init__(self, bot, music):
        super().__init__()
        self.players= ["x","o"]
        self.activeplayer = self.players[0]
        self.gitter = [[None, None, None],[None, None, None],[None, None, None]]
        self.bot = bot
        self.music = music
        self.cursor_sprite = arcade.Sprite("data/cursor1.png")
        self.cursor_sprite.center_x = 50
        self.cursor_sprite.center_y = 50
        for i in range(3):
            for j in range(3):
                self.gitter[i][j] = Field(position=(i+1, j+1))
    def setup(self):
        self.set_mouse_visible(False)

    def on_mouse_motion(self, x, y, dx, dy):
        self.cursor_sprite.center_x = x
        self.cursor_sprite.center_y = y

    def on_draw(self):
        self.clear()
        self.cursor_sprite.draw()
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
        game_view = Victory(l, self.music)
        t.sleep(0.1)
        self.window.show_view(game_view)
    
class Field(arcade.Sprite):
    def __init__(self, position: tuple):
        super().__init__(filename="data/empty.png",center_x=position[0]*200-100, center_y=position[1]*200-100)
        self.owner = None

class Victory(arcade.View):
    def __init__(self, winner: str, music):
        super().__init__()
        self.winner = winner
        self.music = music

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
            game = Home(self.music,1)
            self.window.show_view(game)
        return super().on_mouse_press(x, y, button, modifiers)



class Home(arcade.View):
    def __init__(self, music, inition):
        super().__init__()
        self.inition = inition
        self.mode = 0
        self.music = music
        self.standsprlist = arcade.SpriteList()
        self.arrow = arcade.Sprite("data/ArrowL.png", 4)
        self.arrow.center_x = 550
        self.arrow.center_y = 300
        self.standsprlist.append(self.arrow)
        self.arrow = arcade.Sprite("data/ArrowR.png", 4)
        self.arrow.center_x = 50
        self.arrow.center_y = 300
        self.standsprlist.append(self.arrow)
        self.settings = arcade.Sprite("data/Settings.png", 2)
        self.settings.center_x = 550
        self.settings.center_y = 550
        self.standsprlist.append(self.settings)
        if  self.inition == 0:
            self.musik2 = arcade.load_sound("data/Entspannungsmusik-mit-5-Minuten-Ostseewellen.wav")
            self.musik1 = arcade.load_sound("data/5_-Extinction-Level-Event-Jingle-Punks.wav")
            self.musik0 = arcade.load_sound("data/DigBarGayRaps-4-BIG-GUYS.wav")
            self.musik3 = arcade.load_sound("data/Godzilla-Peter-Griffin-_feat.-Lois-Griffin_.wav")
            self.musiks = [self.musik0, self.musik1, self.musik2, self.musik3]

            self.musikplayer = arcade.play_sound(self.musiks[self.music])

        self.robotsprlist = arcade.SpriteList()

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)


    def on_draw(self):
        self.clear()
        self.robotsprlist.clear()
        self.robot = arcade.Sprite("data/Robot" + str(self.mode % 4) + ".png" , 10)
        self.robot.center_x = 300
        self.robot.center_y = 300
        self.robotsprlist.append(self.robot)

        arcade.set_background_color(arcade.color_from_hex_string("#303030"))

        self.robotsprlist.draw(pixelated=True)
        self.standsprlist.draw(pixelated=True)
        

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        if x < 600 and y > 200 and x > 500 and y < 400:
            self.mode += 1
        elif x < 100 and y > 200 and x > 0 and y < 400:
            self.mode -= 1
        elif x > 150 and x < 450:
            if self.mode == 0:
                game = Game("d",self.music)
            elif self.mode == 1:
                game = Game("a",self.music)
            elif self.mode == 2:
                game = Game("b",self.music)
            else:
                game = Game("c",self.music)

            self.window.show_view(game)
        elif x > 450 and y > 450:
            arcade.stop_sound(self.musikplayer)
            settings = Settings()
            self.window.show_view(settings)
        
class Settings(arcade.View):
    def __init__(self):
        super().__init__()
        self.music = 0 
        self.choosen_music = 0
        self.standardsprlist = arcade.SpriteList()
        self.arrow = arcade.Sprite("data/ArrowL.png", 2)
        self.arrow.center_x = 550
        self.arrow.center_y = 400
        self.standardsprlist.append(self.arrow)
        self.arrow = arcade.Sprite("data/ArrowR.png", 1)
        self.arrow.center_x = 50
        self.arrow.center_y = 400
        self.standardsprlist.append(self.arrow)
        self.settings = arcade.Sprite("data/Settings.png", 1)
        self.settings.center_x = 550
        self.settings.center_y = 550
        self.standardsprlist.append(self.settings)

    def on_draw(self):

        arcade.set_background_color(arcade.color_from_hex_string("#303030"))
        self.clear()
        self.standardsprlist.draw(pixelated=True)

        if self.choosen_music % 4 == 0:
            arcade.draw_text("Gayyy", 0, 392, arcade.color_from_hex_string("000000"), 12, 600, "center")
        elif self.choosen_music % 4 == 1:
            arcade.draw_text("Action", 0, 392, arcade.color_from_hex_string("000000"), 12, 600, "center")
        elif self.choosen_music % 4 == 2:
            arcade.draw_text("Chill", 0, 392, arcade.color_from_hex_string("000000"), 12, 600, "center") 
        elif self.choosen_music % 4 == 3:
            arcade.draw_text("M&Ms", 0, 392, arcade.color_from_hex_string("000000"), 12, 600, "center") 
        arcade.draw_text("Musik", 0, 420, arcade.color_from_hex_string("000000"), 12, 600, "center",bold=True)


    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        if x < 600 and y > 100 and x > 500 and y < 500:
            self.choosen_music += 1
        elif x < 100 and y > 100 and x > 0 and y < 400:
            self.choosen_music -= 1
        if x > 450 and y > 450:
            settings = Home(self.choosen_music % 4, 0)
            self.window.show_view(settings)
        


class W(arcade.Window):
    def __init__(self):
        super().__init__(width=600, height=600, title="TicTacToe")
        startscreen = Home(0, 0)
        self.show_view(startscreen)


game = W()
arcade.run()
