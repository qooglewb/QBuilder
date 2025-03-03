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

"""Various modalities used to configure certain ash behaviours."""

from enum import Enum


class LogEvalMode(Enum):
    """Mode to use when logging end evaluating a model.
    Models often have the same behaviour (or very similar) when evaluated
    in trainable and non trainable setting.

    There are some other models, see pix2pix, that instead require to be tested
    and trained in TRAIN mode (Model with trainable=True)."""

    TEST = 0
    TRAIN = 1
