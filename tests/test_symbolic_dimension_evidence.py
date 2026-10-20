"""Preserved authored terms must retain their dimensional constraints."""

import pytest
import sympy as sp

from bridgman import DimensionalError, dims_of_expr, explain_expr, verify_expr


F, m, t, r, n, missing = sp.symbols("F m t r n missing")
DIMS = {"F": {"M": 1, "L": 1, "T": -2}, "m": {"M": 1}, "t": {"T": 1}, "r": {}, "n": {}}


@pytest.mark.parametrize("base", [sp.Integer(2), r, sp.Integer(0)])
def test_dimensionful_exponent_is_rejected_before_base_shortcut(base):
    expr = sp.Pow(base, m, evaluate=False)
    with pytest.raises(DimensionalError, match="exponent.*dimensionless"):
        dims_of_expr(expr, DIMS)


def test_unknown_exponent_is_not_assumed_dimensionless():
    with pytest.raises(KeyError, match="missing"):
        dims_of_expr(sp.Pow(sp.Integer(2), missing, evaluate=False), DIMS)


def test_dimensionless_symbolic_exponent_remains_supported():
    assert dims_of_expr(sp.Pow(r, n, evaluate=False), DIMS) == {}
    assert dims_of_expr(sp.Pow(0, n, evaluate=False), DIMS) == {}


@pytest.mark.parametrize("zero", [sp.Integer(0), sp.Float(0)])
@pytest.mark.parametrize("reverse", [False, True])
def test_literal_zero_can_instantiate_force_dimensions(zero, reverse):
    lhs, rhs = (zero, F) if reverse else (F, zero)
    relation = sp.Eq(lhs, rhs, evaluate=False)
    assert verify_expr(relation, DIMS)
    result = explain_expr(relation, DIMS)
    assert result.ok
    assert result.lhs_dimensions == result.rhs_dimensions == DIMS["F"]


@pytest.mark.parametrize("zero_term", [
    sp.Integer(0),
    sp.Mul(0, m, evaluate=False),
    sp.Pow(0, 2, evaluate=False),
    sp.Abs(0, evaluate=False),
])
def test_zero_remains_polymorphic_in_addition_and_relations(zero_term):
    expr = sp.Add(F, zero_term, evaluate=False)
    assert dims_of_expr(expr, DIMS) == DIMS["F"]
    assert verify_expr(sp.Eq(F, zero_term, evaluate=False), DIMS)


@pytest.mark.parametrize("expr,error", [
    (sp.Mul(0, missing, evaluate=False), KeyError),
    (sp.Mul(0, sp.Add(m, t, evaluate=False), evaluate=False), DimensionalError),
    (sp.Add(0, m, t, evaluate=False), DimensionalError),
    (sp.Mul(0, sp.Pow(2, m, evaluate=False), evaluate=False), DimensionalError),
])
def test_zero_does_not_hide_unchecked_authored_operands(expr, error):
    with pytest.raises(error):
        verify_expr(sp.Eq(F, expr, evaluate=False), DIMS)


def test_nonzero_constants_remain_dimensionless():
    assert not verify_expr(sp.Eq(F, 1, evaluate=False), DIMS)


def test_zero_does_not_hide_missing_relation_binding():
    with pytest.raises(KeyError):
        verify_expr(sp.Eq(missing, 0, evaluate=False), DIMS)


@pytest.mark.parametrize("power", [
    sp.Mul(2, sp.Pow(2, -1, evaluate=False), evaluate=False),
    sp.Add(2, -1, evaluate=False),
])
def test_preserved_exact_numeric_exponent_arithmetic(power):
    assert dims_of_expr(sp.Pow(m, power, evaluate=False), DIMS) == DIMS["m"]


def test_preserved_square_root_exponent_arithmetic():
    power = sp.Mul(1, sp.Pow(2, -1, evaluate=False), evaluate=False)
    expr = sp.Pow(sp.Pow(m, 2, evaluate=False), power, evaluate=False)
    assert verify_expr(sp.Eq(m, expr, evaluate=False), DIMS)
