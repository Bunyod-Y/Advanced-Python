class Jungle:
    def __init__(self, name="Unknown"):
        self.visitorName= name

    def welcomeMessage(self):
        print("Hello %s, Welcometo the Jungle" % self.visitorName)

def main():
    # createobject of class Jungle
    j = Jungle("Bunyod")
    j.welcomeMessage() # Hello Bunyod, Welcome to the Jungle

    # if noname is passed, thedefault value i.e. Unknown will be used
    k = Jungle()
    k.welcomeMessage() # Hello Unknown, Welcome to the Jungle

# standardboilerplate to set 'main' as startingfunction
if __name__=='__main__':
    main()
