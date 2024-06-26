"""EduuRobot core package."""
# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2024 Amano LLC

from subprocess import run

__commit__ = (
    run(["git", "rev-parse", "--short", "HEAD"], capture_output=True, check=False)
    .stdout.decode()
    .strip()
    or "None"
)

__version_number__ = (
    run(["git", "rev-list", "--count", "HEAD"], capture_output=True, check=False)
    .stdout.decode()
    .strip()
    or "0"
)
