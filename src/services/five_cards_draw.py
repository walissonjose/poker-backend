from src.domain.schemas.five_cards_draw import FirstRoundIn, FirstRoundOut, SecondRoundIn, SecondRoundOut
from sqlalchemy.orm import Session
from src.repositories import five_cards_draw as five_cards_draw_repository
from src.domain.models.game import Game
from typing import List
from collections import Counter


def first_round(match_in: FirstRoundIn, db: Session):
    game: Game = Game(
        id=match_in.match_id,
        opponent_mail=match_in.opponent_id,
    )

    cards_to_swap = choose_cards_to_swap(match_in.cards)

    bet: int = determine_first_bet(match_in.cards)

    first_round_out = FirstRoundOut(
        bet=bet,
        cards_to_swap=cards_to_swap
    )

    game.first_bet = bet

    # remove swapped cards from hand
    game.hand = [card for card in match_in.cards if card not in cards_to_swap]

    five_cards_draw_repository.create_game(game, db)

    return first_round_out


def second_round(match_in: SecondRoundIn, db: Session):
    game = five_cards_draw_repository.get_game(match_in.match_id, db)

    game.hand = match_in
    game.opponent_first_bet = match_in.match_bet - game.first_bet
    five_cards_draw_repository.update_game(game, db)

    bet = determine_second_bet(match_in.cards)


# Função para verificar o valor das cartas
def card_value(card: str) -> int:
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13,
              'A': 14}
    return values[card[0]]


# Função para verificar se as cartas são do mesmo naipe
def same_suit(cards: List[str]) -> bool:
    return all(card[-1] == cards[0][-1] for card in cards)


# Função para verificar se há uma sequência de cartas
def is_straight(cards: List[str]) -> bool:
    card_values = sorted(card_value(card) for card in cards)
    return card_values[-1] - card_values[0] == 4 and len(set(card_values)) == 5


def choose_cards_to_swap(cards: List[str]) -> List[str]:
    # Contar o número de ocorrências de cada naipe
    suit_counts = Counter(card[-1] for card in cards)

    print("Suit counts:", suit_counts)

    # Verificar se há quatro cartas do mesmo naipe
    for suit, count in suit_counts.items():
        if count == 4:
            print("Four of a kind detected. Suit:", suit)
            # Trocar apenas a carta de outro naipe e tentar obter um flush
            return [card for card in cards if card[-1] != suit]

    print("No four of a kind detected.")

    # Verificar se há uma mão muito fraca (por exemplo, sem pares, sem sequências, sem flush)
    if len(set(card[0] for card in cards)) >= 4:  # Se houver pelo menos 4 valores de cartas diferentes
        print("Weak hand detected.")
        return sorted(cards, key=card_value)[:2]  # Trocar apenas as duas cartas mais baixas

    if same_suit(cards) and is_straight(cards):  # Se houver um flush ou uma sequência
        print("Flush or straight detected.")
        return []  # Não trocar nenhuma carta

    print("No special condition detected.")

    # Trocar todas as cartas, exceto aquelas que já são parte de uma sequência alta ou de uma combinação de números iguais
    values_to_keep = set()
    card_counts = Counter(card[0] for card in cards)
    for value, count in card_counts.items():
        if count >= 2:
            values_to_keep.add(value)

    return [card for card in cards if card[0] not in values_to_keep]


# Função para determinar a aposta com base nas cartas atuais
def determine_first_bet(cards: List[str]) -> int:
    # Lógica para determinar a aposta, você pode personalizar conforme desejado
    return hand_score(cards)


# Função para calcular a pontuação da mão
def hand_score(cards: List[str]) -> int:
    # Contar o número de ocorrências de cada valor de carta
    card_counts = Counter(card[0] for card in cards)

    # Verificar se a mão é um Royal Flush
    if is_royal_flush(cards):
        return 200  # Pontuação alta para um Royal Flush
    # Verificar se a mão é um Straight Flush
    elif is_straight_flush(cards):
        return 150  # Pontuação alta para um Straight Flush
    # Verificar se a mão é um Four of a Kind
    elif is_four_of_a_kind(card_counts):
        return 120  # Pontuação alta para um Four of a Kind
    # Verificar se a mão é um Full House
    elif is_full_house(card_counts):
        return 120  # Pontuação média para um Full House
    # Verificar se a mão é um Flush
    elif is_flush(cards):
        return 120  # Pontuação média para um Flush
    # Verificar se a mão é um Straight
    elif is_straight(cards):
        return 120  # Pontuação média para um Straight
    # Verificar se a mão é um Three of a Kind
    elif is_three_of_a_kind(card_counts):
        return 120  # Pontuação baixa para um Three of a Kind
    # Verificar se a mão é um Two Pair
    elif is_two_pair(card_counts):
        return 60  # Pontuação baixa para um Two Pair
    # Verificar se a mão é um Pair
    elif is_pair(card_counts):
        return 20  # Pontuação baixa para um Pair
    else:
        return 10  # Pontuação mínima para uma High Card

    # Função auxiliar para verificar se todas as cartas têm o mesmo naipe


# Função para verificar se a mão é um Royal Flush
def is_royal_flush(cards: List[str]) -> bool:
    return same_suit(cards) and set(card[0] for card in cards) == {'T', 'J', 'Q', 'K', 'A'}


# Função para verificar se a mão é um Straight Flush
def is_straight_flush(cards: List[str]) -> bool:
    return same_suit(cards) and is_straight(cards)


# Função para verificar se a mão é um Four of a Kind
def is_four_of_a_kind(card_counts: dict) -> bool:
    return any(count >= 4 for count in card_counts.values())


# Função para verificar se a mão é um Full House
def is_full_house(card_counts: dict) -> bool:
    return any(count == 3 for count in card_counts.values()) and any(count == 2 for count in card_counts.values())


# Função para verificar se a mão é um Flush
def is_flush(cards: List[str]) -> bool:
    return same_suit(cards)


# Função para verificar se a mão é um Three of a Kind
def is_three_of_a_kind(card_counts: dict) -> bool:
    return any(count == 3 for count in card_counts.values())


# Função para verificar se a mão é um Two Pair
def is_two_pair(card_counts: dict) -> bool:
    return sum(1 for count in card_counts.values() if count == 2) >= 2


# Função para verificar se a mão é um Pair
def is_pair(card_counts: dict) -> bool:
    return any(count == 2 for count in card_counts.values())
