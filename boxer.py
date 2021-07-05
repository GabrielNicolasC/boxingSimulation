
class Boxer:
    def __init__(self, name, stance, reach, chin, xLocation, yLocation, directionFacingInDegrees):
        self.name = name
        self.stance = stance
        self.reach = reach
        self.chin = chin
        self.xLocation = xLocation
        self.yLocation = yLocation
        self.directionFacingInDegrees = directionFacingInDegrees
        self.jabReach = reach
        self.crossReach = reach * 1.2
        self.hookReach = reach * 0.7
        self.uppercutReach = reach * 0.75

#Current Position and Angle
    def currentPosition(self):
        print(self.name, 'Current x coordinate:', self.xLocation,'Current y coordinate:', self.yLocation)
    def currentAngle(self):
        print(self.name, 'Current Angle', self.directionFacingInDegrees, 'degrees')
    def positionAndAngle(self):
        self.currentPosition()
        self.currentAngle()

#Movement
    def rotate(self, clockOrCounterClockWise, degrees):
        print('Old angle:',self.directionFacingInDegrees)
        if clockOrCounterClockWise == 'Clockwise':
            self.directionFacingInDegrees = self.directionFacingInDegrees + degrees
        elif clockOrCounterClockWise == 'Counter Clockwise':
            self.directionFacingInDegrees = self.directionFacingInDegrees - degrees
        print('New angle:',self.directionFacingInDegrees)
    def move(self, strideLength, direction):
        if direction == 'left':
            if self.xLocation - strideLength < 0:
                print('max movement not allowed, bounced onto the left ropes')
                self.xLocation = 0
                #self.positionAndAngle()
            else:
                self.xLocation = self.xLocation - strideLength
                #self.positionAndAngle()
        elif direction == 'right':
            if self.xLocation + strideLength > 10:
                print('max movement not allowed, bounced onto the right ropes')
                self.xLocation = 10
                #self.positionAndAngle()
            else:
                self.xLocation = self.xLocation + strideLength
                #self.positionAndAngle()
        elif direction == 'backward':
            if self.yLocation - strideLength < 0:
                print('max movement not allowed, bounced onto the back ropes')
                self.yLocation = 0
                #self.positionAndAngle()
            else:
                self.yLocation = self.yLocation - strideLength
                #self.positionAndAngle()
        elif direction == 'forward':
            if self.yLocation + strideLength > 10:
                print('max movement not allowed, bounced onto the front ropes')
                self.yLocation = 10
                #self.positionAndAngle()
            else:
                self.yLocation = self.yLocation + strideLength
                #self.positionAndAngle()

    def moveLeft(self, strideLength, direction="left"):
        self.move(strideLength, direction)
    def smallMoveLeft(self, strideLength=1):
        self.moveLeft(strideLength)
    def largeMoveLeft(self,strideLength=2):
        self.moveLeft(strideLength)

    def moveRight(self, strideLength, direction="right"):
        self.move(strideLength, direction)
    def smallMoveRight(self, strideLength=1):
        self.moveRight(strideLength)
    def largeMoveRight(self, strideLength=2):
        self.moveRight(strideLength)

    def moveForward(self, strideLength, direction="forward"):
        self.move(strideLength, direction)
    def smallMoveForward(self, strideLength=1):
        self.moveForward(strideLength)
    def largeMoveForward(self, strideLength=2):
        self.moveForward(strideLength)

    def moveBackward(self, strideLength, direction="backward"):
        self.move(strideLength, direction)
    def smallMoveBackward(self, strideLength=1):
        self.moveBackward(strideLength)
    def largeMoveBackward(self, strideLength=2):
        self.moveBackward(strideLength)
