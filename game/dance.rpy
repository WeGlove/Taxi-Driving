define dance = Character("Dance Dancington")

label dance:
    "Ein Mann in Discokleidung steigt ein"
    dance "Bitte zur Discothek 90. Wenn du dich beeilen könntest {i}babygirl{/i}? Der Danceter ist {i}late{/i}."
    dance "Go, go, step it up!"
    
    you "Sind Sie beruflich unterwegs?"
    dance "Nein, {i}baby{/i}!"
    dance "Dance Dancington tanzt {b}nur{/b} aus reiner... {i}Passion{/i}!"
    dance "Schwingen Sie ihre Hüften auch mal aufs Parkett?"
    menu:
        "Nein, Disco geht mir gar nicht ab":
            dance "Ich bin {i}schocked{/i}!"
            dance "Wenn Dance Dancington dir mal ein paar seiner {i}Moves{/i} zeigt wirst du anders thinken!"
            jump dance_rude
        "Jeden Freitag, baby!":
            dance "{i}Uhhhhhhhhhh{/i}, ein Bruder. Du musst mir umbedingt mal ein paar deiner Moves zeigen."
            dance "Wir sind ja auch schon an der {i}location{/i}"
            dance "Time to, {i}step it up{/i}!"
            jump dance_out
        "Ich habe kein besonderes Interesse. Nach einer Weile ist der ganze Disco Zug für mich abgefharen":
            dance "Ich bin {i}schocked{/i}!"
            dance "Naja, eigenltich..."
            dance "*er seuftzt*"
            dance "Sie haben ja recht. Der Discohype ist schon lange um."
            dance "Aber was soll ich auch machen. Meine Dancemoves sind doch alles was ich hab..."
            jump dance_honest
    label dance_rude:
        menu:
            "Wie lange wollen Sie eigentlich noch einer Vergangenheit nachstellen, die Sie nie hatten?":
                dance "Der Dancter ist nicht nur {i}shocked{/i}, er ist {b}ULTRA SHOCKED{/b}"
                dance "Disco wird {i}für immer{/i} die {i}Steps{/i} auf den {i}Floor{i} bringen"
                dance "Genau das werd ich jetzt zeigen gehen. Time to, {i}step it up{/i}!"
                jump dance_out
            "Na gut, vielleicht kann Disco manchmal doch interssant sein":
                dance "Na also, so wie Dance steppt, steppt die Welt."
                dance "Komm doch mal vorbei!"
                jump dance_out
            "Wenn Sie das sagen":
                dance "Der Danceter {i}tellt{/i} es wie es ist!"
    label dance_honest:
        menu:
            "Naja, Tanzfertigkeit ist ja schon mal was. Werden Sie doch Tanzlehrer":
                dance "Vielleicht hast du recht. Ich leg noch eine mal ein heißes Solo aufs Parkett und dann zeig ich anderen wie man es tut."
                dance "Danke, Mann!"
                jump dance_out
            "Wie wär's denn mit einer anderen Musikrichtung?":
                jump dance_music
                
    label dance_music:
        dance "Eine neue Msikrichtung, huh?"
        dance "An was hast du denn gedacht?"
        menu:
            "Rap":
                dance "Das ist es. Das war es mit Dance Dancington. Es ist Zeit für Rap Rapington, Brother!"
            "Klassik":
                dance "Das ist es. Das war es mit Dance Dancington. Es schlägt die Stund der Geburt, des ehrenwerten Class Classingtons. Cahpeau, Monsieur!"
    label dance_out:
        "Dance Dancington steigt aus."
    return

