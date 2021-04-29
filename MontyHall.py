import numpy as np
#%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

N_TRIALS = 1000

prizes = np.random.randint(0,3, size=(N_TRIALS)) #choosing randomly the winning door 
first_choices = np.random.randint(0,3, size=(N_TRIALS)) #choosing randomly the player's choice

switching_player_gains = (prizes!=first_choices).astype(int)
keeping_player_gains = (prizes==first_choices).astype(int)

plot = plt.bar([1,2],[switching_player_gains.sum(),keeping_player_gains.sum()],tick_label=["Change","Keep"])

figure = plt.figure()
plot = plt.scatter(range(N_TRIALS), switching_player_gains.cumsum())
plot = plt.scatter(range(N_TRIALS), keeping_player_gains.cumsum())