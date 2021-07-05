from bout import Bout

class Exchange:
    def __init__(self,thrower, receiver, pythagDistance, punchType):
        self.thrower = thrower
        self.receiver = receiver
        self.pythagDistance = pythagDistance
        self.punchType = punchType

    def strikeThrown(self,thrower, receiver, pythagDistance, punchType):
        print(thrower.name, 'throws a', punchType, '...')
        print(self.receiver.name + "'s current health:", end= '')
        for i in range(self.receiver.chin):
            print('|', end= '')
        print('\n')
        print('Current Angle:', thrower.directionFacingInDegrees)
        print('Angle Required:',"{:.0f}".format(Bout.getAngleOfLineBetweenTwoPoints(self,thrower, receiver)))
        if (thrower.directionFacingInDegrees > Bout.getAngleOfLineBetweenTwoPoints(self,thrower, receiver) + 10 or thrower.directionFacingInDegrees < Bout.getAngleOfLineBetweenTwoPoints(self,thrower, receiver) - 10):
            print('It misses, not the right angle and may be out of range')
        else:
            if punchType == 'jab':
                 if thrower.jabReach >= pythagDistance:
                     self.receiver.chin = receiver.chin - 1
                     print('it lands!')
                     if receiver.chin == 0:
                         print(receiver.name, 'is knocked out!')
                     else:
                         print(receiver.name[0], "health:", end= '')
                         for i in range(receiver.chin):
                             print('|', end= '')
                         print('\n')

                 else:
                     print('it misses, out of range')

            if punchType == 'cross':
                 if thrower.crossReach >= pythagDistance:
                     self.receiver.chin = receiver.chin - 2
                     print('it lands!')
                     if receiver.chin == 0:
                         print(receiver.name, 'is knocked out!')
                     else:
                         print(receiver.name[0], "health:", end= '')
                         for i in range(receiver.chin):
                             print('|', end= '')
                         print('\n')
                 else:
                     print('it misses, out of range')
            if punchType == 'hook':
                 if thrower.hookReach >= pythagDistance:
                     self.receiver.chin = receiver.chin - 4
                     print('it lands!')
                     if receiver.chin == 0:
                         print(receiver.name, 'is knocked out!')
                     else:
                         print(receiver.name[0], "health:", end= '')
                         for i in range(receiver.chin):
                             print('|', end= '')
                         print('\n')
                 else:
                     print('it misses, out of range')
            if punchType == 'uppercut':
                 if thrower.uppercutReach >= pythagDistance:
                     self.receiver.chin = receiver.chin - 3
                     print('it lands!')
                     if receiver.chin == 0:
                         print(receiver.name, 'is knocked out!')
                     else:
                         print(receiver.name[0], "health:", end= '')
                         for i in range(receiver.chin):
                             print('|', end= '')
                         print('\n')
                 else:
                     print('it misses, out of range')

        print(self.thrower.name[0], "health:", end= '')
        for i in range(self.thrower.chin):
            print('|', end= '')
        print('\n')
