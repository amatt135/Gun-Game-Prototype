def on_on_score():
    game.over(True, effects.confetti)
info.on_score(1000, on_on_score)

def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . 5 5 5 5 5 5 5 5 5 5 . . . 
                    . . 5 5 5 5 5 5 5 5 5 5 5 5 . . 
                    . 5 5 5 5 5 5 5 5 5 5 5 5 5 5 . 
                    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
                    . 5 5 5 5 5 5 5 5 5 5 5 5 5 5 . 
                    . . 5 5 5 5 5 5 5 5 5 5 5 5 . . 
                    . . . 5 5 5 5 5 5 5 5 5 5 . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        mySprite,
        100,
        0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    game.over(False, effects.dissolve)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.player, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    info.change_score_by(1)
    pause(300)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap2)

projectile: Sprite = None
mySprite: Sprite = None
scene.set_background_color(11)
mySprite = sprites.create(img("""
        ..................................................
            ..................................................
            ..................................................
            ..................................................
            ..................................................
            ..................................................
            ..................................................
            ..................................................
            ..................................................
            ......44444444444444444444444444444444444444444...
            ......45555555555555555555555555555555555555554...
            ......45444444444444444444444444444444444444454...
            ......45455555555555555555555555555555555555454...
            ......45454444444444444444444444444444444445454...
            ......45455555555555555555555555555555555555454...
            ......45444444444444444444444444444444444444454...
            ......45555555555555555555555555555555555555554...
            ......44444444444444444444444444444444444444444...
            ......4555554..4.....4............................
            ......4544454..4.....4............................
            ......4545454...4....4............................
            ......4545454....4...4............................
            ......4545454........4............................
            ......4545454444444444............................
            ......4545454.....................................
            ......4545454.....................................
            ......4545454.....................................
            ......4545454.....................................
            ......4545454.....................................
            ......4545454.....................................
            ......4545454.....................................
            ......4545454.....................................
            ......4545454.....................................
            ......4545454.....................................
            ......4544454.....................................
            ......4555554.....................................
            ......4444444.....................................
            ..................................................
            ..................................................
            ..................................................
            ..................................................
            ..................................................
            ..................................................
            ..................................................
            ..................................................
            ..................................................
            ..................................................
            ..................................................
            ..................................................
            ..................................................
    """),
    SpriteKind.player)
controller.move_sprite(mySprite)
myEnemy = sprites.create(assets.image("""
    Angry cube
"""), SpriteKind.enemy)
myEnemy.set_position(155, 50)
myEnemy.follow(mySprite, 30)
myEnemy.set_stay_in_screen(True)
mySprite.set_stay_in_screen(True)
info.set_score(0)