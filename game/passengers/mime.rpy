define mime = Character("Pantomime")

label mime:
    "Eine Pantomime öffnet die Tür zu deinem Wagen."
    "Sie will einsteigen aber scheint gegen eine unsichtbare Wand zu stoßen."
    menu:
        "Mimen ihr die Tür aufzumachen":
            "Die Pantomime nickt und lächelt dankbar"
            "Sie steigt ein."
        "Ihr Sagen, dass Sie gefälligst einsteigen soll":
            "Die Pantomime, rüttelt noch ein paar mal an einem wohl unischtbaren Schloss bevor sie aufgibt, mit den Shultern zuckt, und geht."
            $current_passenger_stats["paid"] = 0
            return
    you "Wo soll's denn hingehen?"
    "Die Pantomime blickt nervös durch die Gegend."
    "Schließlich, nimmt sie eine Pose ein die dich beim Fahren darstellen soll."
    menu:
        "So wird das nichts, wenn Sie mir nicht mal Sagen können wohin Sie wollen, kann ich Sie auch nirgendwo hinbringen.":
            "Die Pantomime wirkt enttäuscht und traurig. Sie öffnet den Wagen versucht auszusteigen und stößt gegen eine unsichtbare Mauer."
            "Sichtlich beschämt und mit Tränen in den Augen öffnet Sie die unsichtbare Tür verlässt den Wagen und rennt weg..."
            $current_passenger_stats["paid"] = 0
            return
        "Sie, ... wollen mimen wo es lang geht?":
            "Sie nickt und lächelt nervös"
    menu:
        "Das ist ein Risiko. Ich darf meinen Blick eigentlich nicht von der Straße nehmen":
            "Die Pantomieme sieht für einen Moment geschlagen aus, bevor sie ihren Kopf schüttelt und lächelt."
            "Offenbar hat sie eine Idee. Die Pantomime tippt dir Links und Rechts auf die Schultern."
            you "Sie geben mir so an wo ich abbiegen soll?"
            "Die Pantomime nickt eifrig."
            you "Das sollte funktionieren."
            "Die Fahrt verläuft ohne weitere Schweirgikeiten und ihr kommt an der von der Pantomime gewünschten Stelle an"
            $current_passenger_stats["paid"] += base_fare / 2
        "Na gut, das könnte funktionieren":
            "Die Pantomime strahlt dich an."
            "Du fährst los und die Pantomime lotst dich durch die Straßen, wobei du ihrer gemimten Lenkradbewegung folgst."
            "Du erhältst ein paar Strafpunkte des Verkhrsamts fürs Abiegen ohne bzw. mit zu spätem Blinker, aber ihr kommt wohlbehalten an"
            $current_passenger_stats["paid"] -= base_fare / 4
    "Die Pantomime zahlt, aber als Sie austeigen will stößt sie den Kopf wieder an einer unsichtbaren Wand"
    "Du reichst herüber und mimst wie du die Türe öffnest"
    "Die Pantomime küsst dich auf die Wange und verlässt den Wagen."
    return
    

