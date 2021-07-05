from exchange import Exchange
from boxer import Boxer
import inquirer
class Decision:
    def askContinueQuestion():
        continueQuestion = [
            inquirer.List('continueQuestion',
                        message="Do you wish to continue? ",
                        choices=['Yes', 'No'],
                    ),
        ]
        return(inquirer.prompt(continueQuestion)['continueQuestion'])

    def askQuestion(boxer1, boxer2, bout):
        initialQuestion = [
            inquirer.List('initialDecision',
                        message="Move, Pivot or Punch? ",
                        choices=['Move', 'Pivot', 'Punch'],
                    ),
        ]

        movementDirectionQuestions = [
            inquirer.List('movementDecision',
                          message="Left, Right, Forward or Backward? ",
                          choices=['Left', 'Right', 'Forward', 'Backward'],
                      )
            ]

        lengthDirectionQuestion = [
            inquirer.List('strideDecision',
                          message="Short or Long Move? ",
                          choices=['Short','Long'],
                      )
        ]

        strikeQuestions = [
            inquirer.List('strikeDecision',
                          message="jab, cross, hook or uppercut? ",
                          choices=['jab','cross', 'hook', 'uppercut'],
                      )
        ]

        pivotDirectionQuestion = [
            inquirer.List('directionDecision',
                          message="Clockwise or Counter Clockwise? ",
                          choices=['Clockwise','Counter Clockwise'],
                      )
                      ]
        pivotDegreeQuestion = [
            inquirer.List('degreesDecision',
                          message="Number of Degrees",
                          choices=[0,15,30,45,60,75,90,105,120,135,150,165,180],
                      )
        ]

        decisionMade = inquirer.prompt(initialQuestion)['initialDecision']
        if decisionMade == "Move":
            print('Decided to Move')
            movementDecision = inquirer.prompt(movementDirectionQuestions)['movementDecision']
            strideDecision = inquirer.prompt(lengthDirectionQuestion)['strideDecision']
            if movementDecision == "Left":
                if strideDecision == "Short":
                    boxer1.smallMoveLeft()
                elif strideDecision == "Long":
                    boxer1.largeMoveLeft()
            elif movementDecision == "Right":
                if strideDecision == "Short":
                    boxer1.smallMoveRight()
                elif strideDecision == "Long":
                    boxer1.largeMoveRight()
            elif movementDecision == "Forward":
                if strideDecision == "Short":
                    boxer1.smallMoveForward()
                elif strideDecision == "Long":
                    boxer1.largeMoveForward()
            elif movementDecision == "Backward":
                if strideDecision == "Short":
                    boxer1.smallMoveBackward()
                elif strideDecision == "Long":
                    boxer1.largeMoveBackward()
            bout.ringSetup()
        elif decisionMade == "Punch":
            strikeDecision = inquirer.prompt(strikeQuestions)['strikeDecision']
            exchange = Exchange(boxer1, boxer2, bout.pythagDistance(boxer1.xLocation, boxer2.xLocation, boxer1.yLocation, boxer2.yLocation), strikeDecision)
            exchange.strikeThrown(boxer1, boxer2, bout.pythagDistance(boxer1.xLocation, boxer2.xLocation, boxer1.yLocation, boxer2.yLocation), strikeDecision)
        elif decisionMade == "Pivot":
            directionDecision = inquirer.prompt(pivotDirectionQuestion)['directionDecision']
            degreesDecision = inquirer.prompt(pivotDegreeQuestion)['degreesDecision']
            boxer1.rotate(directionDecision,degreesDecision)
        else:
            print('redo')
