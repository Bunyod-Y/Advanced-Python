class Jungle:
    def __init__(self, name="Unknown"):
        self.visitorName=name
    
    def welcomeMessage(self):
        print(f"Hello %s, Welcome to the Jungle" %self.visitorName)

j=Jungle("Bunyod")
j.welcomeMessage()
k=Jungle()
k.welcomeMessage()

# class Jungle:
#     def welcomeMessage(self):
#         print("Welcome to the Jungle")

# bunyod=Jungle()
# bunyod.welcomeMessage()
