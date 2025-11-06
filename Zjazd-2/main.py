"""
==========================================================
FUZZY INVENTED PENDULUM CONTROL SYSTEM (Odwrócone wahadło)
==========================================================

Autorzy:
---------
- Klaudia Denert (s29276)

Opis problemu:
---------------
Odwrócone wahadło (CartPole) to klasyczny problem sterowania.
Celem jest utrzymanie wahadła w pozycji pionowej poprzez odpowiednie sterowanie siłą działającą na wózek.

W tym projekcie zastosowano *logikę rozmytą (fuzzy logic)* do określenia siły sterującej na podstawie trzech parametrów:
1. Kąt wahadła (angle)
2. Prędkość kątowa (angular_velocity)
3. Pozycja wózka (position)

Na wyjściu system generuje siłę (force), którą należy zastosować, aby utrzymać równowagę.

Środowisko i przygotowanie:
----------------------------
1. Wymagane pakiety:
   pip3 install -r requirements.txt

2. Uruchomienie programu:
   python3 main.py

3. Wymagane biblioteki:
   - numpy
   - skfuzzy
   - matplotlib

-----------------------------------------------------------
"""

import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl

angle = ctrl.Antecedent(np.arange(-15, 16, 1), 'angle')
angular_velocity = ctrl.Antecedent(np.arange(-10, 11, 1), 'angular_velocity')
position = ctrl.Antecedent(np.arange(-5, 6, 1), 'position')

force = ctrl.Consequent(np.arange(-10, 11, 1), 'force')

angle['left'] = fuzz.trimf(angle.universe, [-15, -15, 0])
angle['center'] = fuzz.trimf(angle.universe, [-5, 0, 5])
angle['right'] = fuzz.trimf(angle.universe, [0, 15, 15])

angular_velocity['negative'] = fuzz.trimf(angular_velocity.universe, [-10, -10, 0])
angular_velocity['zero'] = fuzz.trimf(angular_velocity.universe, [-3, 0, 3])
angular_velocity['positive'] = fuzz.trimf(angular_velocity.universe, [0, 10, 10])

position['left'] = fuzz.trimf(position.universe, [-5, -5, 0])
position['center'] = fuzz.trimf(position.universe, [-2, 0, 2])
position['right'] = fuzz.trimf(position.universe, [0, 5, 5])

force['left'] = fuzz.trimf(force.universe, [-10, -10, 0])
force['none'] = fuzz.trimf(force.universe, [-2, 0, 2])
force['right'] = fuzz.trimf(force.universe, [0, 10, 10])

"""
Reguły są definiowane intuicyjnie:
- Jeśli kąt jest "right" i prędkość kątowa jest "positive", to trzeba działać siłą w lewo (żeby skorygować).
- Jeśli kąt jest "left" i prędkość kątowa jest "negative", to działamy siłą w prawo.
- Jeśli kąt i pozycja są blisko środka, to siła ≈ zero.
"""

rule1 = ctrl.Rule(angle['right'] & angular_velocity['positive'], force['left'])
rule2 = ctrl.Rule(angle['left'] & angular_velocity['negative'], force['right'])
rule3 = ctrl.Rule(angle['center'] & angular_velocity['zero'], force['none'])
rule4 = ctrl.Rule(position['left'], force['right'])
rule5 = ctrl.Rule(position['right'], force['left'])
rule6 = ctrl.Rule(angle['right'] & position['right'], force['left'])
rule7 = ctrl.Rule(angle['left'] & position['left'], force['right'])

pendulum_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7])
pendulum = ctrl.ControlSystemSimulation(pendulum_ctrl)

pendulum.input['angle'] = 8
pendulum.input['angular_velocity'] = 4
pendulum.input['position'] = 2

pendulum.compute()

print(f"Obliczona siła sterująca: {pendulum.output['force']:.2f}")

force.view(sim=pendulum)

angle.view()
angular_velocity.view()
position.view()

plt.show()
