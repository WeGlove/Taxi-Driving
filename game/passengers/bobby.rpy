define bobby = Character("Bobby")

label bobby:
    $current_passenger_stats["paid"] = base_fare
    $current_passenger_stats["status"] = {"drug_subscription" : False}
    "Ein kleinwüchsiger Mann mit langem Bart steigt in dein Taxi. Er schaut dich aus schmalen Augen an und fragt dich mit schwerem Akzent:"
    bobby "Weißt du warum man mich nennt Bobby die Ratte?"
    menu:
        "Ähhm... , nein?": 
            bobby "Weil ich will zur Bank"
            "Du verstehst nicht was Ratten und Bänke miteinander zu tun haben, aber fährst einfach mal los"
        "Mit den Augen rollen.":
            you "Können Sie mir einfach sagen wohin Sie wollen?"
            bobby"Weißt du warum man mich nennt Bobby die Ratte, weil ich will zur Bank"
            "Du verstehst nicht was Ratten und Bänke miteinander zu tun haben"
            
        "Weil Sie eine Diebesgilde in Flüderich leiten?":
            bobby"Weißt du warum man mich nennt Bobby die Ratte? Weil ich nicht mag insider Jokes!"
    bobby "Weißt du warum man mich nennt Bobby die Ratte, weil ich weiß wann ein Taxifahrer unter Drogen steht"
    menu:   
        "Ich nehme meinen Job sehr ernst, ich nehme keine Drogen!":
            bobby   "Weißt du warum man mich nennt Bobby die Ratte? Weil in diese Welt keiner aushält ohne ein paar Drogen!"
        "Nervös Lachen":
            bobby "Weißt du warum man mich nennt Bobby die Ratte? Weil ich weiß, dass du unter Drogen stehen aber es keinem verraten werde"
        "Da sie dann ja wissen, das ich grade unter keinem Einfluss stehe, können Sie mir dann sagen wo ich welche herbekomme?":
            bobby"Weißt du warum man mich nennt Bobby die Ratte? Weil ich wusste dass du interessiert sein würdest !"
    bobby "Weißt du warum man mich nennt Bobby die Ratte? Weil ich dich kann versorgen mit ein bisschen was!"
    menu: 
        "Gerne!":
            $drug_cost = 2*base_fare
            $subscription_cost = 5* base_fare
            bobby"Weißt du warum man mich nennt Bobby die Ratte? Weil das kosten [drug_cost] Cryptobucks"
            menu:
                "Das ist zu teuer, geht das auch noch billiger?":
                    bobby "Weißt du warum man mich nennt Bobby die Ratte? Weil ich nicht feilschen. 50 CRP oder keine Drogen"
                "Ihm das Geld geben":
                    bobby "Weißt du warum man mich nennt Bobby die Ratte? Weil es eine Freude ist mit dir Geschäfte zu machen"
                    $current_passenger_stats["paid"] -= drug_cost
                "Kann ich auch ein Abo abschließen?":
                    bobby "Weißt du warum man mich nennt Bobby die Ratte? Weil es das gibt natürlich kostet nur [subscription_cost] im Monat für eine Drogenflatrate. Ich das kann nur empfehlen"
                    menu:
                        "Ihn bezahlen":
                            $current_passenger_stats["paid"] -= subscription_cost
                            $current_passenger_stats["status"]["drug_subscription"] = True
                            bobby "Weißt du warum man mich nennt Bobby die Ratte? Weil es eine Freude ist mit dir Geschäfte zu machen. Ich werden für die nächste Lieferung wieder mit dir fahren"
                        "Dann doch lieber nur die einzelne Dosis nehmen":
                            bobby "Weißt du warum man mich nennt Bobby die Ratte? Weil es eine Freude ist mit dir Geschäfte zu machen"
                            $current_passenger_stats["paid"] -= drug_cost
                        "Dankend ablehnen":
                            bobby "Weißt du warum man mich nennt Bobby die Ratte? Weil ich auch anderen meine Ware verkaufen kann"

        "Nein, danke!":
            bobby "Weißt du warum man mich nennt Bobby die Ratte? Weil ich auch anderen meine Ware verkaufen kann"
        "Sie wissen, dass es strafbar ist Taxifahrern Drogen zu verkaufen?":
            bobby "Weißt du warum man mich nennt Bobby die Ratte? Weil mich keiner nennt Bobby die Ratte und du nicht können mich anzeigen!"
            menu: 
                "Auf dem ins Taxi integrierten Telefon die Polizei anrufen":
                    bobby"Weißt du warum man mich nicht nennt Bobby die Ratte? Weil ich jetzt einen Abgang mache"
                    "Er springt aus dem fahrenden Auto. Natürlich ohne zu zahlen"
                    $current_passenger_stats["paid"] = 0
                "Anhalten und ihn rauswerfen":
                    "Unter Protest hälst du an und wirfst ihn aus dem Auto."
                    $current_passenger_stats["paid"] = 0
                "Stöhnen, ihn ignorieren und ihn zur Bank fahren":
                    "Er ist auch still. Der Weg restliche Weg zur Bank verläuft reibungslos"
    return

    

