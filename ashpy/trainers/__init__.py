# Copyright 2019 Zuru Tech HK Limited. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Trainers help reducing boilerplate code by bootstrapping models training.

The module contains a primitive Interface and specific trainers that inherits from it.

.. currentmodule:: ashpy.trainers

.. rubric:: Classes

.. autosummary::
    :nosignatures:
    :toctree: trainers

    BaseTrainer
    AdversarialTrainer
    EncoderTrainer

----

.. rubric:: Modules

.. autosummary::
    :nosignatures:
    :toctree: trainers
    :template: autosummary/submodule.rst

    base_trainer
    classifier
    gan

"""

from ashpy.trainers.base_trainer import BaseTrainer
from ashpy.trainers.gan import AdversarialTrainer, EncoderTrainer
from ashpy.trainers.classifier import ClassifierTrainer

__ALL__ = ["BaseTrainer", "Adversarial", "AdversarialEncoder", "ClassifierTrainer"]
