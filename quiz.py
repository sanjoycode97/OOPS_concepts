import random
#############
class FlashCard:
    def __init__(self):
        self.__fruits = {'apple':'red', 'banana':'yellow','watermelon':'green','strawberries':'pink',
                         'guava':'green'}
    def quiz(self):
        print("Welcome to the Fruit Color Quiz!")
        while True:
            fruit,color=random.choices(list(self.__fruits.items()))[0]
            print(f'what is the color of {fruit} ?')
            user_input=input('guess the color: ').strip().lower()
            if color==user_input:
                print("picked the correct color")
            else:
                print('incorrect choice')
            try:
                option=input('enter 0 for continue and 1 for quit')
                if option==1:
                    print('thanks for playing')
                    break
            except ValueError:
                print('incorrect option exiting the quiz')
                break
card_game=FlashCard()
card_game.quiz()