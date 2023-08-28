import pytest
from pyplate.pyplate import Substance, Plate


@pytest.fixture
def salt() -> Substance:
    return Substance.solid('NaCl', 58.4428)


@pytest.fixture
def water() -> Substance:
    return Substance.liquid('H2O', mol_weight=18.0153, density=1)


@pytest.fixture
def dmso() -> Substance:
    return Substance.liquid('DMSO', 78.13, 1.1004)


@pytest.fixture
def sodium_sulfate() -> Substance:
    return Substance.solid('Sodium sulfate', 142.04)


@pytest.fixture
def lipase() -> Substance:
    return Substance.enzyme('lipase')
