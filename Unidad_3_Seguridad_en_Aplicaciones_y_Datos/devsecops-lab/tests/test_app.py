import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))

def test_placeholder():
    assert 1 + 1 == 2

def test_app_importable():
    import app
    assert app.app is not None
