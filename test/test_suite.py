from __future__ import unicode_literals, print_function
from nose.tools import assert_equal, assert_true, assert_false
import glob
import json
import mf2py
import os.path
import sys


assert_equal.__self__.maxDiff = None


def test_mf2tests():
    def check_mf2(htmlfile, p, s):
        assert_equal(p, s)

    allfiles = [
        os.path.join(dirpath, f)
        for dirpath, dirnames, files in os.walk('testsuite/tests')
        for f in files if f.endswith('.json')]

    for jsonfile in allfiles:
        htmlfile = jsonfile[:-4] + 'html'
        with open(htmlfile) as f:
            p = mf2py.parse(doc=f, url='http://example.com')
        with open(jsonfile) as g:
            s = json.load(g)
        yield check_mf2, htmlfile, p, s
