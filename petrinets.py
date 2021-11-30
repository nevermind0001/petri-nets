class Place:
    def __init__(self, name, token=0):
        self.name = name
        self.token = token
    
    # reverse token status
    def flipToken(self):
        if self.token == 1:
            self.token = 0
        else:
            self.token = 1

    def getTokenStatus(self):
        return self.token


class Transition:
    def __init__(self, name, preConditions, postConditions):
        self.name = name
        
        self.preConditions = preConditions
        self.postConditions = postConditions

        # initially set as false then check if that is true
        self.canActivate = self.check_if_can_activate()
    
    def check_if_can_activate(self):
        # return true if can activate false if cannot activate

        # check status of all preConditions
        for preCondition in self.preConditions:
            if preCondition.getTokenStatus() == 0:
                self.canActivate = False
                return False

        # check status of all postConditions
        for postCondition in self.postConditions:
            if postCondition.getTokenStatus() == 1:
                self.canActivate = False
                return False
        
        # condtions are not triggered transition in activable
        self.canActivate = True
        return True

    def activate(self):
        # remove token from all preconditions
        for preCondition in self.preConditions:
            preCondition.flipToken()
        
        # add token in all postconditions
        for postContition in self.postConditions:
            postContition.flipToken()

# defining my graph
p1 = Place("p1", 1)
p2 = Place("p2", 1)
p3 = Place("p3", 0)
p4 = Place("p4", 1)

p4.flipToken()


t1 = Transition("t1", [p1,p2], [p3,p4])
t1.check_if_can_activate()
t1.activate()

print(p1.getTokenStatus())
print(p2.getTokenStatus())
print(p3.getTokenStatus())
print(p4.getTokenStatus())