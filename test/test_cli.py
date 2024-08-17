import pytest as pt
import os


test_data = [
    '--version',
    'iciktArray /mlab/data/psbhatt/projects/icikt/test/bigTest.csv --data-format=csv',
    'iciktArray /mlab/scratch/rmflight/praneeth/largish_sample.tsv --data-format=tsv --replace= --output=test',
    'iciktArray /mlab/data/psbhatt/projects/icikt/test/bigTest.csv --replace=0 --mode=local --scale=False --diag=False --chunk=5',
    'leftCensor /mlab/scratch/rmflight/praneeth/largish_sample.tsv --data-format=tsv',
    'leftCensor /mlab/scratch/rmflight/praneeth/largish_sample.tsv --data-format=tsv --replace=0,inf',
    'leftCensor /mlab/data/psbhatt/projects/icikt/test/bigTest.csv --data-format=csv --replace=None',

]


@pt.mark.parametrize('argv', test_data)
def test_cli(argv: list[str]):
    argv = 'icikt ' + argv
    assert os.system(argv) == 0


error_data = [
    'iciktArray /mlab/data/psbhatt/projects/icikt/test/bigTest.csv --data-format=error',
    'iciktArray /mlab/data/psbhatt/projects/icikt/test/bigTest.csv --replace=error',
    'iciktArray /mlab/data/psbhatt/projects/icikt/test/bigTest.csv --mode=error',
    'iciktArray /mlab/data/psbhatt/projects/icikt/test/bigTest.csv --scale=error',
    'iciktArray /mlab/data/psbhatt/projects/icikt/test/bigTest.csv --diag=error',
    'iciktArray /mlab/data/psbhatt/projects/icikt/test/bigTest.csv --chunk=error',
    'leftCensor /mlab/data/psbhatt/projects/icikt/test/bigTest.csv --data-format=error',
    'leftCensor /mlab/data/psbhatt/projects/icikt/test/bigTest.csv --replace=error',
    'leftCensor /mlab/data/psbhatt/projects/icikt/test/bigTest.csv --sample=error',
]


@pt.mark.parametrize('argv', error_data)
def test_cli_error(argv: list[str]):
    argv = 'icikt ' + argv
    assert os.system(argv) != 0
