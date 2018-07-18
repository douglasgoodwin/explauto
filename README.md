# Explauto: A library to study, model and simulate intrinsically motivated multitask learning and exploration in virtual and robotic agents #

[![Build Status](https://travis-ci.org/flowersteam/explauto.svg?branch=master)](https://travis-ci.org/flowersteam/explauto)
[![codecov](https://codecov.io/gh/flowersteam/explauto/branch/master/graph/badge.svg)](https://codecov.io/gh/flowersteam/explauto)

Explauto is a framework developed in the [Inria FLOWERS](https://flowers.inria.fr/) research team which provides a common interface for the implementation and benchmarking of active and online sensorimotor learning algorithms. In particular, this framework considers algorithms where exploration is driven by models of intrinsic motivation/curiosity at multiple levels of abstraction (from the active choice of parameterized motor primitives to the choice of parameterized problems/goals to the choice of learning strategies - e.g. deciding when to self-explore or ask input from an external expert). It is designed and maintained by [Clément Moulin-Frier](https://flowers.inria.fr/clement_mf/), [Pierre Rouanet](https://github.com/pierre-rouanet), and [Sébastien Forestier](http://sforestier.com/).

Explauto provides a high-level API for an easy definition, use and evaluation of:

* Virtual and robotics setups (Environment level)
* Sensorimotor learning iterative models (Sensorimotor level)
* Active choice of sensorimotor experiments (Interest level)

It is crossed-platform and has been tested on Linux, Windows and Mac OS. Do not hesitate to contact us if you want to get involved! It has been released under the [GPLv3 license](http://www.gnu.org/copyleft/gpl.html).

## Documentation ##

### Scientific grounding ###


Explauto's scientific roots trace back from Intelligent Adaptive Curiosity algorithmic architecture [[Oudeyer, 2007]](http://hal.inria.fr/hal-00793610/en), which has been extended to a more general family of autonomous exploration architecture by [[Baranes, 2013]](http://www.pyoudeyer.com/ActiveGoalExploration-RAS-2013.pdf) and recently expressed as a compact and unified formalism [[Moulin-Frier, 2013]](http://hal.inria.fr/hal-00860641). We strongly recommend to read this [short introduction](http://flowersteam.github.io/explauto/about.html) into developmental robotics before going through the tutorials.

**If you use the library in a scientific paper, please cite** (follow the link for bibtex and pdf files):

Moulin-Frier, C.; Rouanet, P. & Oudeyer, P.-Y. [Explauto: an open-source Python library to study autonomous exploration in developmental robotics](http://hal.inria.fr/hal-01061708) *International Conference on Development and Learning, ICDL/Epirob, Genova, Italy*, 2014

### Tutorials ###

Most of Explauto's documentation is written as [IPython notebooks](http://ipython.org/notebook.html). If you do not know how to use them, please refer to the [dedicated section](http://flowersteam.github.io/explauto/notebook.html).

* [Full tutorial describing how to use the library](http://nbviewer.ipython.org/github/flowersteam/explauto/blob/master/notebook/full_tutorial.ipynb)

* More specific tutorials
    * [Setting environments](http://nbviewer.ipython.org/github/flowersteam/explauto/blob/master/notebook/setting_environments.ipynb)
    * [Learning sensorimotor models](http://nbviewer.ipython.org/github/flowersteam/explauto/blob/master/notebook/learning_sensorimotor_models.ipynb)
    * [Summary of available sensorimotor and interest models](http://nbviewer.ipython.org/github/flowersteam/explauto/blob/master/notebook/summary_available_models.ipynb)
    * [Learning sensorimotor models with sensorimotor context](http://nbviewer.ipython.org/github/flowersteam/explauto/blob/master/notebook/learning_with_sensorimotor_context.ipynb)
    * [Learning sensorimotor models with context provided by environment](http://nbviewer.ipython.org/github/flowersteam/explauto/blob/master/notebook/learning_with_environment_context.ipynb)
    * Comming soon: Autonomous exploration using interest models
    * [Setting a basic experiment](http://nbviewer.ipython.org/github/flowersteam/explauto/blob/master/notebook/setting_basic_experiment.ipynb)
    * [Comparing motor vs goal strategies](http://nbviewer.ipython.org/github/flowersteam/explauto/blob/master/notebook/comparing_motor_goal_stategies.ipynb)
    * [Running pool of experiments](http://nbviewer.ipython.org/github/flowersteam/explauto/blob/master/notebook/running_experiment_pool.ipynb)
    * [Introducing curiosity-driven exploration](http://nbviewer.ipython.org/github/flowersteam/explauto/blob/master/notebook/introducing_curiosity_learning.ipynb)
    * [Poppy environment](http://nbviewer.ipython.org/github/flowersteam/explauto/blob/master/notebook/poppy_environment.ipynb)
    * [Fast-forward a previous experiment](http://nbviewer.ipython.org/github/flowersteam/explauto/blob/master/notebook/fast_forward_experiment.ipynb)
    * [Tutorial on Active Model Babbling and a comparison with Motor Babbling and Goal Babbling](http://nbviewer.jupyter.org/github/sebastien-forestier/ExplorationAlgorithms/blob/master/main.ipynb)
    * [Goal Babbling with direct optimization](http://nbviewer.ipython.org/github/flowersteam/explauto/blob/master/notebook/goal_babbling_direct_optimization.ipynb)
    * [Learning to produce sounds with the DIVA vocal synthesizer and Dynamic Movement Primitives](http://nbviewer.jupyter.org/github/flowersteam/explauto/blob/master/notebook/DivaDMP.ipynb)


### API ###

Explauto's API can be found on a html format [here](http://flowersteam.github.io/explauto/).


## Installation ##

The best way to install Explauto at the moment is to clone the repo and use it in [development mode](http://flowersteam.github.io/explauto/installation.html#as-a-developer). It is also available as a [python package](https://pypi.python.org/pypi/explauto/). The core of explauto depends on the following packages:

* [python](http://www.python.org) 2.7 or 3.*
* [numpy](http://www.numpy.org)
* [scipy](http://www.scipy.org)
* [scikit-learn](http://scikit-learn.org/)

For more details, please refer to the [installation section](http://flowersteam.github.io/explauto/installation.html) of the documentation.
