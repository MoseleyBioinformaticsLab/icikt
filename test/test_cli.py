import pytest as pt
import os
import typing as t


test_data = [
    '--version',
    'iciktArray ./test/bigTest.csv --data-format=csv',
    'iciktArray ./test/largish_sample.tsv --data-format=tsv --replace= --output=test',
    'iciktArray ./test/bigTest.csv --replace=0 --mode=local --scale=False --diag=False --chunk=5',
    'leftCensor ./test/largish_sample.tsv --data-format=tsv',
    'leftCensor ./test/largish_sample.tsv --data-format=tsv --replace=0,inf',
    'leftCensor ./test/bigTest.csv --data-format=csv --replace=None',

]


@pt.mark.parametrize('argv', test_data)
def test_cli(argv: t.List[str]):
    argv = 'icikt ' + argv
    assert os.system(argv) == 0


error_data = [
    'iciktArray ./test/bigTest.csv --data-format=error',
    'iciktArray ./test/bigTest.csv --replace=error',
    'iciktArray ./test/bigTest.csv --mode=error',
    'iciktArray ./test/bigTest.csv --scale=error',
    'iciktArray ./test/bigTest.csv --diag=error',
    'iciktArray ./test/bigTest.csv --chunk=error',
    'leftCensor ./test/bigTest.csv --data-format=error',
    'leftCensor ./test/bigTest.csv --replace=error',
    'leftCensor ./test/bigTest.csv --sample=error',
]


@pt.mark.parametrize('argv', error_data)
def test_cli_error(argv: t.List[str]):
    argv = 'icikt ' + argv
    assert os.system(argv) != 0
