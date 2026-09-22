import pytest
from string_utils import StringUtils


str_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize('input_text, expected_output', [
                          ('stripe', 'Stripe'),
                          ('hello kitty', 'Hello kitty')
])
def test_capitalize_positive(input_text, expected_output):
    assert str_utils.capitalize(input_text) == expected_output


@pytest.mark.negative
@pytest.mark.parametrize('input_text, expected_output',
                         [('@#$', '@#$'), (' ', ' '), ('', '')])
def test_capitalize_negative(input_text, expected_output):
    assert str_utils.capitalize(input_text) == expected_output


@pytest.mark.positive
@pytest.mark.parametrize('with_a_space, without_a_space',
                         [(' sun', 'sun'),
                          ('  1234', '1234'),
                          (' earth ', 'earth ')])
def test_trim_positive(with_a_space, without_a_space):
    assert str_utils.trim(with_a_space) == without_a_space


@pytest.mark.negative
@pytest.mark.parametrize('with_a_space, without_a_space',
                         [(' ', ''),
                          ('', ''),
                          (None, 'expected_output_for_None')])
# Баг репорт
def test_trim_negative(with_a_space, without_a_space):

    if with_a_space is None:
        with pytest.raises(TypeError):
            str_utils.trim(with_a_space)
    else:
        assert str_utils.trim(with_a_space) == without_a_space


@pytest.mark.positive
@pytest.mark.parametrize('string_input, symbol, expected',
                         [('word', 'w', True),
                          ('jocker', 's', False),
                          ('04 апреля 2023', '4', True)])
def test_contains_positive(string_input, symbol, expected):
    assert str_utils.contains(string_input, symbol) == expected


# Баг-репорт
@pytest.mark.negative
@pytest.mark.parametrize('string_input, symbol, expected',
                         [('', '', False),
                          ('jocker', '', False),
                          ('04 апреля 2023', '04', False)])
def test_contains_negative(string_input, symbol, expected):
    assert str_utils.contains(string_input, symbol) == expected


@pytest.mark.positive
@pytest.mark.parametrize('string_input, symbol, expected',
                         [('SkyPro', 'P', 'Skyro'),
                          ('SkyPro', 'Sky', 'Pro'),
                          ('04 april 2026', ' 20', '04 april26')])
def test_delsymb_positive(string_input, symbol, expected):
    assert str_utils.delete_symbol(string_input, symbol) == expected


# Баг-репорт
@pytest.mark.negative
@pytest.mark.parametrize('string_input, symbol, expected',
                         [('SkyPro', 'p', 'SkyPro'),
                          ('SkyPro', 'Sky', 'SkyPro'),
                          ('04 april 2026', None, '04 april 2026')])
def test_delsymb_negative(string_input, symbol, expected):
    assert str_utils.delete_symbol(string_input, symbol) == expected
