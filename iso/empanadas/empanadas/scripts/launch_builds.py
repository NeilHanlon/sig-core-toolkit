# Launches the builds of ISOs

import argparse

from empanadas.common import *
from empanadas.common import _rootdir

from jinja2 import Environment, FileSystemLoader

parser = argparse.ArgumentParser(description="ISO Compose")

parser.add_argument('--release', type=str, help="Major Release Version", required=True)
parser.add_argument('--isolation', type=str, help="mock isolation mode")
parser.add_argument('--rc', action='store_true', help="Release Candidate")
parser.add_argument('--local-compose', action='store_true', help="Compose Directory is Here")
parser.add_argument('--logger', type=str)
results = parser.parse_args()
rlvars = rldict[results.release]
major = rlvars['major']

def run():
    file_loader = FileSystemLoader(f"{_rootdir}/templates")
    tmplenv = Environment(loader=file_loader)
    job_template = tmplenv.get_template('kube/Job.tmpl')
    out = ""
    for arch in ["amd64", "arm64"]: 
        out += job_template.render(
            architecture=arch,
            backoffLimit=4,
            command=["build-iso", "--release", "9", "--rc", "--isolation", "simple"],
            containerName="buildiso",
            imageName="ghcr.io/neilhanlon/sig-core-toolkit:latest",
            jobName=f"build-iso-{arch}",
            namespace="empanadas",
            restartPolicy="Never",
        )
    for arch in ["s390x", "ppc64le"]: 
        out += job_template.render(
            architecture=arch,
            backoffLimit=4,
            command=["build-iso", "--release", "9", "--rc", "--isolation", "simple"],
            containerName="buildiso",
            imageName="ghcr.io/neilhanlon/sig-core-toolkit:latest",
            jobName=f"build-iso-{arch}",
            namespace="empanadas",
            restartPolicy="Never",
        )

    print(out)
