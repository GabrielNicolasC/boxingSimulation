from boxer import Boxer
from bout import Bout
import numpy as np
from exchange import Exchange
from decision import Decision


class Main():
    boxer1 = Boxer("Gabe", "southpaw", 1.7, 10, 3,3,135)
    boxer2 = Boxer("Jerry", "orthodox", 1.6, 7, 7,7,315)
    boxer3 = Boxer("Tom", "orthodox", 1.65, 3, 7,7,315)
    bout = Bout(boxer1, boxer2)

    #Initial Commentary
    print("Welcome to tonight's fight between", boxer1.name, "(" + boxer1.stance + ")",'and', boxer2.name, "(" + boxer2.stance + ")")
    bout.determineLongerReach()
    bout.determineStrongerChin()
    print("The fighters have taken their positions and are ready to go")
    bout.ringSetup()

    userWantsToContinue = True
    while userWantsToContinue:
        Decision.askQuestion(boxer1, boxer2, bout)
        continueDecision = Decision.askContinueQuestion()
        if continueDecision == "No":
            userWantsToContinue = False
