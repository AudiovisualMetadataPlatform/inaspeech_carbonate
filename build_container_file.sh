#!/bin/bash

SCRIPTDIR="$(cd $(dirname ${BASH_SOURCE[0]}) >/dev/null 2>&1 && pwd)"
TMPDIR=$SCRIPTDIR/tmpdir.$$

# make sure we clean up.
function cleanup {
    echo "Removing $TMPDIR"
    rm -rf $TMPDIR
}
trap cleanup EXIT

echo "Temporary data in $TMPDIR"
mkdir $TMPDIR


SINGULARITY_TMPDIR=$TMPDIR singularity build --fakeroot inaspeech.sif inaspeech.def
