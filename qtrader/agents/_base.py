from __future__ import absolute_import
from __future__ import division

import numpy as np


class Agent:
    """Base `Agent` Interface/Class."""

    def __init__(self, **kwargs):
        raise NotImplementedError

    def act(self, observation, reward, done):
        raise NotImplementedError
