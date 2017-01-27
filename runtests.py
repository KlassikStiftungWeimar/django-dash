#!/usr/bin/env python
import os
import sys
import pytest


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.django_1_8")
    sys.path.insert(0, "examples/example")
    sys.path.insert(0, "src")
    return pytest.main()


if __name__ == '__main__':
    sys.exit(main())
