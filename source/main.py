from PyGE.Engine import side_scroller
from source.Objects.Bullet import Bullet
from source.Objects.Enemy import Enemy, EnemyHandler
from source.Objects.Player import Player
from source.Objects.Button import Button
from source.Objects.background import Background
from source.Objects.Gameover import Gameover



def run():
    side_scroller(
        xml=open("resources/xml/rooms.xml").read(),
        start_room="menu",
        images={
            "player1": {"path": "resources/images/player/player.png", "w": 32, "h": 32},
            "player2": {"path": "resources/images/player/player2.png", "w": 32, "h": 32},
            "bullet": {"path": "resources/images/bullet/bullet.png", "w": 32, "h": 32},
            "enemy": {"path": "resources/images/enemy/enemy.png", "w": 32, "h": 32},
            "background" : {"path": "resources/images/background/background.png", "w": 1000, "h": 700},
            "gameover" : {"path": "resources/images/gameover/gameover.png", "w": 1000, "h": 700}

        
        
          
        },
        sprite_sheets={

        },
        sounds={
        },
        font={
          "Querround16": {"path": "resources/font/querround/QUERROUND.TTF", "size": 16},
          "Title": {"path": "resources/font/querround/QUERROUND.TTF", "size": 50}
          
        },
        custom_objects=[
            Player, Bullet, Enemy, EnemyHandler, Button, Background, Gameover
        ],
        initial_variables={
        },
        development_screen_size=(1000, 700),
        fullscreen=False,
        auto_scale=False
        
    )