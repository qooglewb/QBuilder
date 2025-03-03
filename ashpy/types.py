"""
Custom Type-Aliases. Mostly here for brevity in documentation.

TScalar = :py:obj:`typing.Union` [:obj:`int`, :obj:`float`]

TWeight = :py:obj:`typing.Union` [TScalar, :py:class:`tf.Tensor`,
:obj:`typing.Callable` [..., TScalar]]

"""

from typing import Union, Callable

import tensorflow as tf


TScalar = Union[int, float]
TWeight = Union[TScalar, tf.Tensor, Callable[..., TScalar]]
