import pytest as pt
import os
import typing as t


test_data = [
    '--version',
    'iciktArray ./test/small_sample.csv --data-format=csv',
    'iciktArray ./test/small_sample.tsv --data-format=tsv --replace= --output=test',
    'iciktArray ./test/small_sample.csv --replace=0 --mode=local --scale=False --diag=False --chunk=5',
    'leftCensor ./test/small_sample.csv --data-format=csv',
    'leftCensor ./test/small_sample.csv --data-format=csv --replace=0,inf',
    'leftCensor ./test/small_sample.csv --data-format=csv --replace=None',

]


@pt.mark.parametrize('argv', test_data)
def test_cli(argv: t.List[str]):
    argv = 'icikt ' + argv
    assert os.system(argv) == 0


error_data = [
    'iciktArray ./test/small_sample.csv --data-format=error',
    'iciktArray ./test/small_sample.csv --replace=error',
    'iciktArray ./test/small_sample.csv --mode=error',
    'iciktArray ./test/small_sample.csv --scale=error',
    'iciktArray ./test/small_sample.csv --diag=error',
    'iciktArray ./test/small_sample.csv --chunk=error',
    'leftCensor ./test/small_sample.csv --data-format=error',
    'leftCensor ./test/small_sample.csv --replace=error',
    'leftCensor ./test/small_sample.csv --sample=error',
]


@pt.mark.parametrize('argv', error_data)
def test_cli_error(argv: t.List[str]):
    argv = 'icikt ' + argv
    assert os.system(argv) != 0
