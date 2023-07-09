from unittest import TestCase

import pytest
from assertpy import assert_that
from hypothesis import given
from hypothesis import strategies as st

from src.nestea import do_we_have_nestea


class TestDoWeHaveNestea(TestCase):
    def test__do_we_have_nestea_for_test_the_test_case(
        self,
    ):
        assert_that(
            do_we_have_nestea("Yes, we have Nestea for TestCase! 🤙")
        ).is_equal_to("Yes, we have Nestea for TestCase! 🤙")


@pytest.mark.parametrize(
    "message,expected",
    [
        pytest.param(
            "Yes, we have Nestea for Pytest! 🤙", "Yes, we have Nestea for Pytest! 🤙"
        ),
        pytest.param(
            "No, we don't have Nestea for Pytest! 😭",
            "No, we don't have Nestea for Pytest! 😭",
        ),
    ],
)
def test__do_we_have_nestea_for_test_the_pytest_discovery(
    message,
    expected,
):
    assert_that(do_we_have_nestea(message)).is_equal_to(expected)


@given(st.text())
def test__do_we_have_nestea_for_test_the_hypothesis_discovery(message):
    assert_that(do_we_have_nestea(message)).is_equal_to(message)
