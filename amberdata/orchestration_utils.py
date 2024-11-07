import json
import logging
import os
import sys
from os import environ as env
from time import time
from typing import Any,Dict, List,Tuple

import pandas as pd

def snowflake_stage_load_copy_remove(
    file:str,
    stage:str,
    table_path:str,
    engine:Engine
)