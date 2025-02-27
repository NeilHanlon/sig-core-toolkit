# builds ISO's

import argparse

from empanadas.common import *
from empanadas.util import Checks
from empanadas.util import IsoBuild

parser = argparse.ArgumentParser(description="ISO Compose")

parser.add_argument('--release', type=str, help="Major Release Version", required=True)
parser.add_argument('--isolation', type=str, help="mock isolation mode")
parser.add_argument('--rc', action='store_true', help="Release Candidate")
parser.add_argument('--local-compose', action='store_true', help="Compose Directory is Here")
parser.add_argument('--logger', type=str)
results = parser.parse_args()
rlvars = rldict[results.release]
major = rlvars['major']

a = IsoBuild(
        rlvars,
        config,
        major=major,
        rc=results.rc,
        isolation=results.isolation,
        compose_dir_is_here=results.local_compose,
        logger=results.logger,
)

def run():
    a.run()
