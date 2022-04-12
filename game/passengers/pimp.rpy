define faustings = Character("Max Faustings")


label passenger_faustings_neutral_start:
    "Der Mann brummt als Einveständnis"
    faustings "Sagen Sie, ist Taxi fahren ein guter Job?"
    menu:
        "Komisch. Ich hatte neulich einen Clown mitgenommen der mich das auch gefragt hat." if has_clowned:
            faustings "Ah, das wird wohl mein Bruder gewesen sein."
            jump passenger_faustings_brother
        "Ich kann mich nicht beklagen":
            label passenger_faustings_no_job:
            faustings "Gut, gut, wissen sie, ich kann meinen Job nicht besonders gut leiden."
            menu:
                "Was ist falsch an ihrem Beruf?":
                    faustings "Ich bin Anführer einer Gang."
                "Haben Sie eine Mitlife Crisis?":
                    faustings "Kann man so sagen."
                    menu: 
                        "So was finde ich ja immer höchst peinlich.":
                            faustings "Ja, danke."
                            "Er wirkt jetzt etwas kühler dir gegenüber."
                            faustings "Fahr mich einfach wo ich hin will."
                            "Den Rest der Fahrt verbringt ihr schweigend."
                            return
                        "Das passiert jedem glaube ich.":
                            faustings "Ich glaube meine Situation ist da anders. Ich bin Anführer einer Gang."
                "Das wird schon wieder...":
                    faustings "Das sagt sich immer so leicht wissen Sie. Aber aus dem Ganggewerbe tritt man nicht so einfach aus."
            faustings "Sehen Sie es so. Wenn ich es mache kann ich sicher sein, dass Verbrechen so menschenrechtsachtend wie möglich begangen werden."
            faustings "Wenn ich nicht der Anführer wäre könnte ich das nicht mehr garantieren."
            faustings "Ich sehe das als meine Pflicht an."
            menu:
                "Das ergibt Sinn für mich":
                    jump passenger_faustings_neutral_start_out
                "Sie verstecken sich und ihre Verbrechen hinter einer Ausrede":
                    faustings "Ach ja, hätten Sie es lieber es wäre jetzt eine Pistole an ihrer Schläfe?"
                    menu:
                        "Das ist nicht der Punkt. Das Sie etwas schlechts tun wird doch nicht dadurch besser, dass jemand anderes etwas noch schlechteres getan hätte":
                            faustings "Ich glaube das führt zu nichts. Sie wollen nicht sehen wie ich denke."
                            "Ihr kommt an seinem Treffpunkt an."
                            faustings "Trotzdem Danke für die Unterhaltung"
                            return
                        "Ok, ich seh es ein, Sie haben ja recht.":
                            jump passenger_faustings_neutral_start_out
       
label passenger_faustings_neutral_start_out:
    faustings "Danke, ich glaube das musste ich mal hören."
    faustings "Hier etwas extra für die Mühen."
    return

label passenger_faustings_clown:
    faustings "Er war nicht zufällig ein Clown oder?"
    menu:
        "Ja war er!":
            faustings "Ah"
            faustings "Das war mein Bruder."
            jump passenger_faustings_brother
        "Sie kennen ihn?":
            "Er wirkt etwas angespannter als vorher."
            faustings "Ja, er ist mein Bruder."
            jump passenger_faustings_brother
        "Nein, er war kein Clown":
            faustings "Oh"
            "Er wirkt plötzlich etwas niedergeschlagen."
            faustings "Hätte ja sein können."
            menu:
                "Kennen Sie einen Clown?":
                    faustings "Ah nicht eirklich er ist nur ein Bekannter."
                    jump passenger_faustings_annoy_him
                    
                "Sie sind also der Anführer einer Gang...":
                    jump passenger_faustings_boss
                

label passenger_faustings_annoy_him:
    menu:
        "Sind Sie sich sicher? Es hat sich so angehört als ob sie einen Clown kennen.":
            faustings "Nein, nein, nicht wirklich, geht auch nur uns wirklich was an."
            menu:
                "Ah, der Clown den Sie nicht kennen, der aber auch nur Sie etwas angeht, natrürlich.":
                    faustings "Suchst du nach Ärger?"
                    menu:
                        "Suchst du nach einem Clow-":
                            "Die Verartzung deines Auges hat eine Weile gedauert. Du scheinst deinen nächsten Kunde dadurch verpasst zu haben."
                            return
                        "Nein, nein, es tut mir Leid. Vergessen wir das.":
                            jump passenger_faustings_annoy_him_abort
                "Ist auch nicht so wichtig.":
                    jump passenger_faustings_annoy_him_abort
        "Ist auch nicht so wichitg":
            jump passenger_faustings_annoy_him_abort
    label passenger_faustings_annoy_him_abort:
        faustings "na also. Sah auch grade schlecht für Sie aus."
        menu:
            "... Also Sie sind Gangboss, ja?":
                jump passenger_faustings_boss
            "Für den Rest der Fahrt die Klappen halten":
                faustings "Hier ihr Geld"
                return
            
                
label passenger_faustings_brother:
    menu:
        "Wissen Sie, dass ihr Bruder depressiv ist?":
            faustings "Ha, es ist wohl kaum zu übersehen oder?"
            label passenger_faustings_brother_state:
            faustings "Es tut mir wirklich Leid um ihn und ich glaube ich bin etwas mit Schuld an seinem Zustand."
            faustings "Er hat einen schlechten Job und sieht seinen erfolgreichen Bruder neben ihm. Dabei hasse ich meinen Job noch mehr als er seinen..."
            menu:
                "Sie wollen kein Gangmitglied sein?":
                    faustings "Wenn ich kein Gangboss bin, wird es jeamand anderes sein." 
                    faustings "So weiß ich immerhin, dass niemand der den Leuten ernsthaft schaden will an der Macht ist."
                    menu:
                        "Ich verstehe was Sie meinen":
                            faustings "Danke, es ist gut mal mit jemandem über meine Probleme reden zu können, wissen Sie."
                            faustings "Danke das Sie sich die Zeit genommen haben."
                            return
                        "Warum hören Sie nicht auf?":
                            faustings "Das kann ich nicht mit meinem Gewissen vereinbaren."
                            faustings "..."
                            faustings "Es tut mir Leid, lassen Sie mich bitte hier schon raus."
                            return
                "Es ist also ein Minderwertigkeitskomplex":
                    faustings "Kann man so sagen ja."
                    faustings "Er lässt mich einfach nicht an ihn ran."
                    menu:
                        "Wenn ich ihn das nächste mal sehe könnte ich ja mit ihm reden.":
                            faustings "Ich bin ihnen was schuldig."
                            faustings "Hier etwas extra, für die Mühen."
                            return
                        "Mit so Leuten würde ich auch nicht unbedingt was zu tun haben wollen":
                            "Er seutzt."
                            faustings "Ich kann es ja schon irgendwo nachvollziehen."
                            "Ihr habt nichts weiter zu bereden un kommt an seinem Trefpunkt an."
                            return
                "Wieso lassen sie ihn nicht einsteigen?":
                    faustings "Als ob ich meinen Bruder in solche Gefahren bringe, nein, nein, er hat etwas besseres verdient"
                    menu:
                        "Sie scheinen ihren Bruder beschützen zu wollen?":
                            faustings "Ja, das stimmt wohl, seid wir klein waren, hab ich mich immer um ihn gekümmert."
                            faustings "Hat ja weiß Gott sonst keiner für uns getan."
                            faustings "Hören Sie, wenn Sie meinen Bruder nochmal sehen, könnten Sie mit ihm über mich reden?"
                            faustings "Ich will ihm näher kommen und ihm helfen aber er weißt mich immer sofort ab."
                            menu: 
                                "Ja, wenn er nochmal mit mir fährt rede ich mit ihm":
                                    "Ihr kommt an seinem Treffpunkt an."
                                    faustings "Ich bin ihnen was schuldig."
                                    faustings "Hier etwas extra, für die Mühen."
                                    return
                                "Nein, ich habe besseres zu tun.":
                                    faustings "Oh..."
                                    "Peinlich schweigend, sitzt dein Fahrgast den Rest der Zeit ab."
                                    return
                        "Die Lusche?":
                            "Dein blaues Auge heilt nur langsam."
                            "Mit etwas salbe tut es nach einiger Zeit aber schon gar nicht mehr SO sehr weh."
                            return
        "Haben Sie ein gutes Verhältnis zu ihrem Bruder?":
            faustings "Es ist verhalten"
            jump passenger_faustings_brother_state
        "Das tut mir Leid":
            "Er lacht."
            faustings "Ist schon ok. Er ist nicht der umgänglichste, aber er ist auch in einer schlechten Situation."
            jump passenger_faustings_brother_state
        "Sie scheinen erfolgreicher zu sein als ihr Bruder":
            faustings "Ja das mag stimmen, ich verdiene mehr Geld als er."
            faustings "Allerdings..."
            jump passenger_faustings_brother_state
label passenger_faustings_unfriendly:
    "Er wirkt belustigt."
    faustings "Leute meiner Sorte sorgen dafür, dass Leute ihrer Sorte im Geschäft bleiben."
    faustings "Wo denken Sie, dass Sie die Leute die ganze Zeit hinbringen, nur zum Bäcker?"
    faustings "Nein, jede Hure, jeder Junk und jede Alokoholeiche muss ihren Fix haben. Dann bringst du Sie zu mir."
    faustings "Vergraulen Sie sich nicht ihre gute Kundschaft mein Lieber."
    menu:
        "Nein mit Ausbeutern mache ich keine Geschäfte":
            faustings "Ausbeuter?"
            faustings "Wie viel von ihren Einnahmen gehen denn an ihre Arbeitgeber?"
            menu: 
                "Stimmt schon":
                    faustings "Dachte ich mir"
                    menu:
                        "Kann ich bei ihnen einsteigen?":
                            faustings "Sie brauchen Geld?"
                            jump passenger_faustings_money
                "Meine Arbeit ist legal, ihre nicht":
                    faustings "Welche Arbeit legal ist und welche nicht macht keinen Unterschied."
                    faustings "Wir beide schließen eine Marktlücke!"
                    faustings "Wenn sie kein Taxifahrer wären, ist es jemand anderes. Wenn ich kein Ganboss wär, wär es auch jemand anderes."
                    faustings "Meine Taten sind nur verwerflich, wenn meine Sie böser sind als für einen Gangboss angemessen."
                    faustings "Nein, es is sogar meine Pflicht ein Gangboss zu sein und zu bleiben."
                    menu:
                        "Dann ist es auch meine Pflicht dem Bösen in ihnen entgegen zu stehen. Ich werde Sie nicht fahren.":
                            "Er zieht seine Knarre"
                            menu:
                                "Ein durchschlagendes Argument":
                                    faustings "Dachte ich mir."
                                    "Du fährst den Gangboss zu seinem Treffpunkt."
                                    faustings "Vielen Dank. Hier ihr Geld. Wie gesagt, nur so böse wie es sein muss."
                                    return
                                "Nein, ich bleibe dabei.":
                                    "Deinen toten Körper finden Polizeiroboter ein paar Monate später in einem Heizungskeller."
                                    "Die Verfolgung wurde aufgrund mangelnder Beweislage einegstellt."
                                    return # TODO make player die.
                        "Ok, ok, ich seh es ja ein.":
                            jump passenger_faustings_unfriendly_out
        "Na gut... Sie haben ja Recht.":
            label passenger_faustings_unfriendly_out:
            "Er brummt."
            faustings "Na also"
            faustings "Dann fahren Sie mich mal schön zu meinem Treffpunkt."
            "Ihr kommt an seinem Treffpunkt an."
            faustings "Hier etwas von deinem Geld."
            faustings "Überleg dir nächstes Mal besser mit wem du dich anlegst."
            return

label passenger_faustings_boss:
    faustings "Allerdings. Und meine Gang ist gut im Geschäft."
    menu: 
        "Kann man in ihrem Geschäft einsteigen?":
            faustings "Sie brauchen Geld?"
            jump passenger_faustings_money
        "Ich glaube ich könnte nicht in so einem Geschäft arbeiten.":
            faustings "Natürlich, dazu fehlt ihnen der Bizeps oder die Brüste."
            "Er lacht herzlich"
            faustings "Aber um erhlich zu sein gefällt mir mein Job auch nicht wirklich..."
            jump passenger_faustings_no_job
        "Interessant. Wie ist das Leben denn so als Gangboss?":
            faustings "Ich mag meinen Job nicht wirklich"
            jump passenger_faustings_no_job
       
        "Hm":
            faustings "Das stört sie oder?"
            menu:
                "Nein eigentlich nicht.":
                    faustings "Vielleicht stört es mich auch nur selber."
                    menu:
                        "Sie mögen ihren Job nicht?":
                            faustings "Nein nicht wirklich"
                            jump passenger_faustings_no_job
                "Mit dem Gangboss assoziiert man nicht grade ein positives Arbeitsumfeld.":
                    faustings "Ja ich weiß, deswegen gefällt mir mein Jib auch eigenltich nicht wirklich."
                    jump passenger_faustings_no_job
                
label passenger_faustings_money:
    menu:
        "Ja, deshalb auch die Frage":
            faustings "Hah, du denkst du bist tough genug dafür?"
            faustings "Was ist das härteste was du in deinem Leben je angestellt hast?"
            menu :
                "Vergiss es ich bin nicht hart.":
                    faustings "Natürlich, das sind die wenigsten"
                    faustings "Immerhin bist du ehrlich, das ist eine Qualität die ich sehr schätze."
                    faustings "Ok, du kannst in meiner Gang einsteigen, wenn du das wirklich willst?"
                    
                    menu: 
                        "Ja, ich brauche das Geld":
                            faustings "Sehr gut. Ich bleibe im Kontakt mit dir."
                            return
                        "Nein, ich hab es mir anders überlegt.":
                            faustings "Gut, du bist also bei Verstand"
                            "Er lacht"
                            faustings "Ich hatte schon daran gezweifelt."
                            faustings "Na dann danke für die Fahrt."
                            return
                "Ich habe falsche Routen abgefahren um bei Gästen mehr zu kassieren.":
                    faustings "Ahh. Ok. Nun da wir ja sowieso grade angekommen sind hier ist dein Geld."
                    "Er gibt dir nur die Hälfte deines Fahpreises"
                    return
                "Ich hab im Supertmakrt einen Loli gekauft versehentlich"
                "Ich habe Einrad fahrend ein Driveby gemacht und dabei 5 Menschen getötet":
                    "Er lacht."
                    faustings "Wow! Das ist spannend ezählen sie mehr!"
                    menu:
                        "Dann hab ich mir noch ein paar bitches gegönnt und hab mit meinen Homies Party auf einem Flugzeug im Flug gemacht":
                            faustings "So lob ich mir das! Wie geht's weiter"
                            menu:
                                "Ich bin Zuhälter geworden und hab bei den Mädels immer abkassiert":
                                    jump passenger_faustings_money_out
                                "Ich bin bei Leuten eingebrochen um Wertsachen zu stehlen.":
                                    jump passenger_faustings_money_out
                                "Ich hab die Liebe meines Lebens gefunden und eine glückliche Familie fernab jedes Verbrechens gegründet.":
                                    faustings "..."
                                    faustings "Nun, danke für die Fahrt"
                                    return
                                "Ich hab mit meiner Gang eine Rakete gekapert und bin damit bis zum Mars. Da haben wir die Marsmenschen tyranisiert.":    
                                    faustings "Du Tier! Du bist ein echter Gangbanger"
                                    menu:
                                        "Hab ich doch gesagt!":
                                            faustings "Ich werd an dich denken wenn ich mal einen echt harten Kerl brauche."
                                            faustings "Hier danke fürs fahren lass es dir gut gehen."
                                            return
                                        "Wirklich?":
                                            faustings "Nein, aber es war eine amüsante Geschichte."
                                            faustings "Hier danke fürs fahren lass es dir gut gehen."
                                            return
                        "Ich hab Drogen an Minderjährige verkauft":
                            jump passenger_faustings_money_out
                        "Ich hab beim Juwelier Schutzgeld erpresst und mir davon eine schicke Uhr gekauft":
                            jump passenger_faustings_money_out
        "Nein, es geht mir um den _FAME_":
            "Er zieht die Augenbrauen zusammen."
            fausings "Den _FAME_?"
            menu:
                "Ich will etwas coolers sein als nur so ein blöder Taxifahrer.":
                    "Er schaut dich bemitleidend an."
                    faustings "Ich glaube ihr Beruf ist genau der richtige für Sie."
                    faustings "Glauben Sie mir in einer Gang zu sein bringt weniger Prestige mit sich als man glaubt."
                    faustings "Ah, da sind wir ja auch schon. Vielen Dank für die Fahrt."
                    return
                "Ich will das mich Leute respektiern wie Sie":
                    "Er schaut dich bemitleidend an."
                    faustings "Glauben Sie mir. Ich respektiere Sie."
                    faustings "Die Taxifahrer sind das einzige was uns aus der alten Ordnung noch wirklich übrig geblieben ist."
                    faustings "Ich bin sehr dankbar dafür das Sie fahren."
                    faustings "Ah das sind wir ja auch schon."
                    faustings "Danke für das nette Gespräch."
                    return
    
label passenger_faustings_money_out:
    "Plötzlich versteift er sich."
    faustings "Naja, ja wie dem auch sei. Das wir nicht mit dem Einsteigen in meine Gang."
    faustings "Trotzdem danke für die Fahrt."
    return
 
label passenger_faustings:
    $ has_clowned = game.get_passenger("clown").has_driven
    "Ein bulliger Mann mit Tattoos und einer Sonnenbrille steigt in deinen Wagen."
    faustings "Hallo. Bitte bringen Sie mich zum Treffpunkt meiner Gang \"die leeren Flaschen\", ist im Stripclub Soleil."
    menu:
        "Alles klar":
            jump passenger_faustings_neutral_start
        "Sie sind Anführer einer Gang?":
            jump passenger_faustings_boss
        "Ich hatte neulich einen Gast den ich dort hinbringen sollte" if has_clowned:
            jump passenger_faustings_clown
        "Ich fahre keine Leute ihrer Sorte":
            jump passenger_faustings_unfriendly
    