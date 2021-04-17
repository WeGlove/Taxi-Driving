define clown = Character("Clown")

label clown:
    "[current_passenger_stats]"
    "Ein Clown steigt in dein Taxi. Er wirkt niedergeschlagen."
    clown "Zum Stripclub Soleil, bitte."
    menu:
        "Alles klar.":
            clown "Danke."
        "Das Geschäft läuft nicht so?":
            clown "100 Auftritte und nicht ein Kunde der mich 2 mal gebucht hat."
            clown "Ich bin vielleicht ein Clown, aber mir wäre es lieber meine Karriere wäre kein Witz."
            clown "Ich hab morgen nochmal einen Gig, aber mir fällt um Himmels Willen kein gute Witz ein um meine Vorführung zu eröffnen."
            clown "Fällt dir was ein?"
            menu:
                "Du":
                    clown "Vielleicht, aber immerhin bin ich ein Witz mit 20 CRP."
                    clown "20 CRP von denen du jetzt nichts sehen wirst."
                    "Der Clown steigt aus deinem Taxi ohne zu bezahlen."
                    return
                "Was ist gelb und fährt auf der Straße":
                    clown "Ich weiß es nicht."
                    you "Ein Taxi."
                    "Der Clown fängt an zu lachen"
                    clown "Wow, danke. Den werd ich mir merken"
                    clown "Der ist tasächlich besser als die Witze die ich normalerweise erzähle."
                "Klopf, klopf":
                    clown "Wer ist da?"
                    you "Mag mich"
                    clown "Mag mich wer?"
                    you "Nein"
                    "Dem Clown schießen die Tränen in die Augen und er fängt an zu schreien"
                    clown "ICH WEIß, ICH WEIß ES DOCH. MEINE MUTTER HATTE RECHT, ICH HÄTTE WEITER WIRTSCHAFT STUDIEREN SOLLEN..."
                    "Der Clown flüchtet sich aus deinem Wagen, aber nicht ohne dir etwas Wasser aus einer Plastikblume ins Gesicht zu spritzen"
                    return
        "Bekommen Sie da keine rote Nase?":
            clown "Haben wir ein Problem?"
            clown "Es ist Samstagabend und bei meinem letzten Auftritt, hab ich den Zuschauern ausversehen statt Wasser, {i}Alkohol{/i} ins Gesicht gespritzt."
            clown "Kleinkindergeburtstage kann ich glaube ich für die nächste Zeit vergessen."
            clown "Fahren Sie einfach los."
    clown "Verdient man eigentlich gut als Taxifahrer?"
    menu:
        "Kommt auf die Kundschaft an":
            clown "Verständlich. Heutzutage, dreht ja jeder am Rad."
            clown "Naja, was erwarte ich auch."
        "Ich komm kaum über die Runden":
            clown "Immerhin bin ich nicht der einzige."
            clown "Wir Wracks müssen ja zusammenhalten."
        "Eigentlich schon":
            clown "Wenn mir die Sonne auch mal so aus dem Arsch scheinen Würde."
            clown "Das würden sich die Leute dann auch eher ansehen wollen."
        "Sind die lachenden Gesichter der Kunden nicht der beste Verdienst":
            clown "Nein. Essen, Wasser, ein Platz zum Schlafen der nicht in der Gasse neben dem letzten Gig ist, {b}das{/b} ist ein guter Verdienst."
    you "Hier wären wir"
            
    
    return
    

