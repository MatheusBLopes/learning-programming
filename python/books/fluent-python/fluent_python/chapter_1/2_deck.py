import collections

# collctions.namedtuple existe dês do Python 2.6 e é utilizado para criar classes de objetos que sejam apenas grupos de atributos
Card = collections.namedtuple('Card', ['rank', 'suit'])

new_card = Card("7", "diamonds")

# print([str(n) for n in range(2,11)] + list('JQKA'))

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]

deck = FrenchDeck()

# print(len(deck))
# print(deck[0])

# from random import choice

# Com a implementação acima conseguimos utilizar o método choice pra pegar uma carta aleatória sem precisar implementar novos métodos
# print(choice(deck))


# E utilizando o getitem nosso baralho já suporta fatiamento
# print(deck[:3])

# print(deck[12::13])
# print(Card('Q', 'hearts') in deck)

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

# Com essa função é retornado o peso da carta através de um index
def spades_high(card):
    # Pega o index da carta passada como parâmetro de dentro da classe FrenckDeck
    rank_value = FrenchDeck.ranks.index(card.rank)
    # print(card)
    # print("Index da carta dentro do baralho: " + str(rank_value))
    # print("Quantidade de naipes: " + str(len(suit_values)))
    # print("Peso do naipe da carta em questão: " + str(suit_values[card.suit]))

    # Pega o index e multiplica por 4 já que existem 4 naipes
    # Somando o peso do naipe ao valor multiplicado nós temos qual a posicação da carta dentro do seu grupo
    return rank_value * len(suit_values) + suit_values[card.suit]

# print(deck[1])
print(spades_high(deck[0]))

# print(sorted(deck, key=spades_high))

for card in sorted(deck, key=spades_high):
    print(card)