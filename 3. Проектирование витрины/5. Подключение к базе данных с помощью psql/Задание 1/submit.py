#!/usr/bin/env python3

import os

from run_checker import submit

submit(os.path.dirname(os.path.abspath(__file__)), 'health')
