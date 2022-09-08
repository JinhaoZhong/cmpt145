import random as rand
class Card:
    cards={'A':1, '2':2, '3':3, '4':4,'5':5, '6':6, '7':7,
                '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13}

    def create():
        """
            Purpose:
                Create a list to store all the cards.
            Pre-conditions:
                all the vaues of cards
            Post-conditions:
                a list of cards is created
            Return:
                A list that contains all the cards
            """
        card_list=[]
        for suit in ["H", "D", "S", "C"]:
            for key in Card.cards.keys():
                card_list.append(key+suit)
        return  card_list

    def deal(num_cards, num_players, deck):
        """
                    Purpose:
                        Create a list to store every cards that players have
                    Pre-conditions:
                        Alist of cards
                    Post-conditions:
                        A list contains players cards
                    Return:
                        A list of cards that players have
                    """
        list=[]
        for num in range(num_players):
            list.append([])
        rand.shuffle(deck)

        return [[deck[i] for i in range(num_cards*num_players) if (i % num_players) == r]
            for r in range(num_players)]

    def value(card):
        if len(card)==2:
            return Card.dictionary[card[0]]
        return 0

    def maximum(list_cards=[]):
        """
                    Purpose:
                        Find which card has the largest value
                    Pre-conditions:
                        A list that contains players card
                    Post-conditions:
                        None
                    Return:
                        The maximum value
                    """
        max=0
        for card in list_cards:
            if Card.value(card)>max:
                max=Card.value(card)
        return  max

    def minimum(list_cards):
        """
                            Purpose:
                                Find which card has the smallest value
                            Pre-conditions:
                                A list that contains players card
                            Post-conditions:
                                None
                            Return:
                                The minimum value
                            """

        min = 100
        for card in list_cards:
            if Card.value(card) < min:
                min = Card.value(card)
        return  min

    def average(card_list):
        """
            Purpose:
                Find the average value of the card list
            Pre-conditions:
                A list that contains players card
            Post-conditions:
                 None
            Return:
                The average value
            """

        sum=0
        for card in card_list:
            sum+=Card.value(card)
        return sum/len(card_list)


##print out all the card
card_list=Card.create()
print(Card.create())

##print out all the card that players have
players_cards=Card.deal(5, 3, card_list)
print(players_cards)

###find maximum value
b=[]
for t in players_cards:
    a=max(t)
    b.append(a)
print('Maximun value:',max(b))

###find minimum value
z=[]
for x in players_cards:
    y=min(x)
    z.append(y)
print('minimum value:',min(z))



