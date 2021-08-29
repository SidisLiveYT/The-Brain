class Distributor:
    def __init__(this, RobotName):
        this.RobotName = RobotName,

    ##def chat(this, UserInput):



RobotEntity = Distributor('Jericho')

while(True):
    UserReply = input()
    RobotEntity.chat(UserReply)
    if(UserReply == 'exit'):
        break
