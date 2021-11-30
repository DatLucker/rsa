class Somebody:
    def __init__(self, a=2, q=0, p=0):
        self.a = a
        self.q = q
        self.p = p
        self.said = ''
        self.listened = ''

    def say(self, lul):
        self.said = (self.q ** self.a) % self.p
        lul.listened = self.said
