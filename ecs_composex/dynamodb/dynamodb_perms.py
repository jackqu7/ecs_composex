#  -*- coding: utf-8 -*-
# SPDX-License-Identifier: MPL-2.0
# Copyright 2020-2021 John Mille <john@compose-x.io>

"""
Set of functions to generate permissions to access queues
based on pre-defined TABLE policies for consumers
"""

from os import path
from json import loads
from ecs_composex.iam.import_sam_policies import import_and_cleanse_policies


def get_access_types():
    sam_policies = import_and_cleanse_policies()
    with open(
        f"{path.abspath(path.dirname(__file__))}/dynamodb_perms.json",
        "r",
        encoding="utf-8-sig",
    ) as perms_fd:
        dyn_policies = loads(perms_fd.read())
    sam_policies.update(dyn_policies)
    return sam_policies


ACCESS_TYPES = get_access_types()
