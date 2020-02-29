import matplotlib as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

fear = ctrl.Antecedent(np.arange(0, 11, 1), 'fear')
rage = ctrl.Antecedent(np.arange(0, 11, 1), 'rage')
joy = ctrl.Antecedent(np.arange(0, 11, 1), 'joy')
sadness = ctrl.Antecedent(np.arange(0, 11, 1), 'sadness')

fear.automf(5)
rage.automf(3)
joy.automf(3)
sadness.automf(3)

fear.view()
rage.view()
joy.view()
sadness.view()

volume = ctrl.Consequent(np.arange(0, 256, 1), 'volume')
pitch = ctrl.Consequent(np.arange(0, 256, 1), 'pitch')
velocity = ctrl.Consequent(np.arange(0, 256, 1), 'velocity')

volume.automf(3)
pitch.automf(3)
velocity.automf(3)

volume.view()
pitch.view()
velocity.view()

input()