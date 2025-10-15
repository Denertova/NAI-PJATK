"""
Gra w Podział (Division Game) - deterministyczna gra dwuosobowa o sumie zerowej.

Autorzy: Krystyna Tokarska, Klaudia Denert

Instrukcja przygotowania środowiska:
1. Utwórz wirtualne środowisko Python
2. Zainstaluj wymagania: pip3 install -r requirements.txt
3. Uruchom grę: python3 main.py
"""

from easyAI import TwoPlayerGame, Human_Player, AI_Player, Negamax
import numpy as np

class DivisionGame(TwoPlayerGame):
    """
    Klasa implementująca grę w Podział.

    Zasady:
    - Na początku mamy liczbę startową `n`.
    - Gracze na zmianę dzielą liczbę przez dowolny dzielnik > 1.
    - Gracz, któremu zostanie 1, przegrywa.
    """

    def __init__(self, players, n=20):
        self.players = players
        self.n = n
        self.current_player = 1

    def possible_moves(self):
        """Zwraca listę możliwych dzielników liczby `n` (większych niż 1)."""
        divisors = [i for i in range(2, self.n + 1) if self.n % i == 0]
        return [str(d) for d in divisors]

    def make_move(self, move):
        """Wykonanie ruchu - dzielenie liczby przez wybrany dzielnik."""
        self.n = self.n // int(move)

    def win_condition(self):
        """Wygrywa przeciwnik, jeśli zostanie 1 po ruchu aktualnego gracza."""
        return self.n == 1

    def is_over(self):
        return self.win_condition()

    def show(self):
        print(f"\nAktualna liczba: {self.n}")

    def scoring(self):
        """Wartość stanu dla AI (1 jeśli wygrana obecnego gracza, -1 jeśli przegrana)."""
        if self.is_over():
            return -1
        else:
            return 0

if __name__ == "__main__":
    ai_algo = Negamax(6)
    players = [Human_Player(), AI_Player(ai_algo)]

    game = DivisionGame(players, n=20)
    game.play()
