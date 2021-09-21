# NIA
Nature Inspired Optimization Algorithms
<a><img align="right" src="https://img.shields.io/github/license/salar-shdk/nia"/></a>
<a><img align="right" src="https://img.shields.io/pypi/v/nia"/></a>
<a><img align="right" src="https://img.shields.io/pypi/pyversions/nia"/></a>
<a><img align="right" src="https://img.shields.io/github/languages/code-size/salar-shdk/nia?color=blueviolet"/></a>

# Instalation
Check [NIA's PyPI page](https://pypi.org/project/nia/) or simply install it using pip:
<a><img align="right" src="https://pepy.tech/badge/nia"/></a>
```
pip install nia
```

# Usage
Solve Ackley problem using Genetic Algorithm:
``` python
from nia.algorithms import GeneticAlgorithm

def ackley(X):
    x = X[0]
    y = X[1]
    return -20 * np.exp(-0.2 * np.sqrt(0.5 * (x**2 + y**2))) - np.exp(0.5 *
        (np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y))) + np.e + 20

nia = GeneticAlgorithm(cost_function=ackley,
                       lower_bond=[-5,-5],
                       upper_bond=[5,5],
                                )
nia.run()
print(nia.message);
```
output:  

```
quit criteria reached best answer is: [-0.02618036 -0.03615453] and best fitness is: 0.0006327163637145361 iteration : 11
```  

Plot:  
<p align="center">
  <img alt="Result gif" align="center" src="https://user-images.githubusercontent.com/33146532/134220470-742ca835-2b9a-4d1d-9a87-76c337156823.gif"/>
</p>



## Customization:
``` python
from nia.algorithms import GeneticAlgorithm
# Specific selection, crossover and muttion algorithms are available under related sub-packages.
from nia.selections import Tournament
from nia.crossovers import RandomSBX
from nia.mutations import Uniform
import numpy as np

def ackley(X):
    x = X[0]
    y = X[1]
    return -20 * np.exp(-0.2 * np.sqrt(0.5 * (x**2 + y**2))) - np.exp(0.5 *
        (np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y))) + np.e + 20

def log(ga):
  print(ga.best)

lower = np.array([-5,-5])
upper = np.array([5,5])

nia = GeneticAlgorithm(cost_function=ackley,
                       iteration_function=log,
                       lower_bond=lower,
                       upper_bond=upper,
                       quit_criteria = 0.0001,
                       num_variable = 2,
                       num_population = 20,
                       max_iteration = 100,
                       crossover = RandomSBX(2),
                       mutation = Uniform(0.05),
                       selection = Tournament(20)
                                )
nia.run()
print(nia.message);
```  
output
```
max iteration reached best answer so far: [-0.02618036 -0.03615453] with best fitness: 0.1786046633597529 iteration : 99
```


# Supported Algorithms :  
- [x] Genetic algorithm (GeneticAlgorithm)
- [ ] Differential Evolution  
- [ ] Evolutionary Programming  
- [ ] Artificial Immune System  
- [ ] Clonal Selection Algorithm  
- [ ] Biogeography-based  
- [ ] Symbiotic Organisms Search  
- [ ] Ant Colony Optimization  
- [x] Artificial Bee Colony (ArtificialBeeColony)
- [ ] Moth Flame Optimization Algorithm  
- [ ] Cuckoo Search  
- [ ] Green Herons Optimization Algorithm  
- [ ] Bat Algorithm  
- [ ] Whale Optimization Algorithm  
- [ ] Krill Herd  
- [ ] Fish-swarm Algorithm  
- [ ] Grey Wolf Optimizer  
- [ ] Shuffle frog-leaping Algorithm  
- [ ] Cat Swarm Optimization  
- [ ] Flower Pollination Algorithm  
- [ ] Invasive Weed Optimization  
- [ ] Water Cycle Algorithm  
- [ ] Teaching–Learning-Based Optimization  
- [x] Particle Swarm Optimization (ParticleSwarmOptimization)
- [ ] Simulated Annealing Algorithm  
- [ ] Gravitational Search Algorithm  
- [ ] Big Bang - Big Crunch  

# Supported Selection Operators :  
- [x] Rank (Rank)
- [x] Tournament (Tournament)  

# Supported Cross Over Operators :  
- [x] K-Point (KPoint)
- [x] SBX (SBX)  
- [x] Random SBX (RandomSBX)

# Supported Mutation Operators :  
- [x] Uniform (Uniform) 

