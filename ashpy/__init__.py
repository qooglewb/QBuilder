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

"""ASHPY Package."""

from . import contexts
from . import datasets
from . import layers
from . import losses
from . import metrics
from . import models
from . import trainers
from . import types
from .modes import LogEvalMode

__version__ = "1.0.2"
__url__ = "https://github.com/zurutech/ashpy"
__author__ = "Machine Learning Team @ Zuru Tech"
__email__ = "ml@zuru.tech"
