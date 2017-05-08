from selenium import webdriver
import pytest
import os

class TestCalculator():

    def push_button(self, button):
        self.browser.find_element_by_id(button).click()

    def get_display_content(self):
        return self.browser.find_element_by_xpath(
            '//div[@id="display"]/p').text

    @classmethod
    def setup_class(cls):
        cls.browser = webdriver.Chrome()
        cls.browser.get(
            'file://' + os.path.join(os.getcwd(), 'index.html')
        )

    @classmethod
    def teardown_class(cls):
        cls.browser.close()

    def setup(self):
        self.browser.refresh()

    def test_zero_displayed_when_loaded(self):
        assert self.get_display_content() == '0'

    def test_when_press_one_displays_one(self):
        self.push_button('1')
        assert self.get_display_content() == '1'

    def test_when_press_zero_zero_displays_zero(self):
        self.push_button('0')
        self.push_button('0')
        assert self.get_display_content() == '0'

    def test_when_press_zero_one_displays_one(self):
        self.push_button('0')
        self.push_button('1')
        assert self.get_display_content() == '1'

    def test_two_digit_input(self):
        self.push_button('1')
        self.push_button('2')
        assert self.get_display_content() == '12'

    def test_when_load_and_press_clear_displays_zero(self):
        self.push_button('clear')
        assert self.get_display_content() == '0'

    def test_clear_input_digit(self):
        self.push_button('1')
        self.push_button('clear')
        assert self.get_display_content() == '0'

    def test_when_press_one_then_plus_displays_one(self):
        self.push_button('1')
        self.push_button('+')
        assert self.get_display_content() == '1'

    def test_when_press_one_plus_two_displays_two(self):
        self.push_button('1')
        self.push_button('+')
        self.push_button('2')
        assert self.get_display_content() == '2'

    def test_addition(self):
        self.push_button('1')
        self.push_button('+')
        self.push_button('1')
        self.push_button('=')
        assert self.get_display_content() == '2'

    def test_chained_addition(self):
        self.push_button('1')
        self.push_button('+')
        self.push_button('2')
        self.push_button('=')
        self.push_button('+')
        self.push_button('3')
        self.push_button('=')
        assert self.get_display_content() == '6'

    def test_when_press_equals_displays_zero(self):
        self.push_button('=')
        assert self.get_display_content() == '0'

    def test_multiplication(self):
        self.push_button('2')
        self.push_button('*')
        self.push_button('4')
        self.push_button('=')
        assert self.get_display_content() == '8'

    def test_addition_then_multiplication(self):
        self.push_button('2')
        self.push_button('+')
        self.push_button('5')
        self.push_button('=')
        self.push_button('*')
        self.push_button('3')
        self.push_button('=')
        assert self.get_display_content() == '21'

    def test_subtraction(self):
        self.push_button('5')
        self.push_button('-')
        self.push_button('2')
        self.push_button('=')
        assert self.get_display_content() == '3'

    def test_subtraction_with_negative_result(self):
        self.push_button('7')
        self.push_button('-')
        self.push_button('1')
        self.push_button('2')
        self.push_button('=')
        assert self.get_display_content() == '-5'

    def test_input_after_zero_result(self):
        self.push_button('1')
        self.push_button('-')
        self.push_button('1')
        self.push_button('=')
        self.push_button('3')
        assert self.get_display_content() == '3'

    def test_integer_division(self):
        self.push_button('4')
        self.push_button('/')
        self.push_button('2')
        self.push_button('=')
        assert self.get_display_content() == '2'

    def test_float_division(self):
        self.push_button('5')
        self.push_button('/')
        self.push_button('2')
        self.push_button('=')
        assert self.get_display_content() == '2.5'

    def test_float_division_rounding(self):
        self.push_button('1')
        self.push_button('/')
        self.push_button('3')
        self.push_button('=')
        assert self.get_display_content() == '0.33333'

    def test_zero_divided(self):
        self.push_button('/')
        self.push_button('1')
        self.push_button('=')
        assert self.get_display_content() == '0'

    def test_zero_division(self):
        self.push_button('1')
        self.push_button('/')
        self.push_button('0')
        self.push_button('=')
        assert self.get_display_content() == 'ERROR'

    def test_input_after_clear(self):
        self.push_button('9')
        self.push_button('clear')
        self.push_button('1')
        assert self.get_display_content() == '1'

    def test_input_non_integer(self):
        self.push_button('1')
        self.push_button('.')
        self.push_button('2')
        assert self.get_display_content() == '1.2'

    def test_input_non_integer_with_zero_int_part(self):
        self.push_button('.')
        self.push_button('3')
        assert self.get_display_content() == '0.3'

    def test_cannot_input_more_than_one_dot(self):
        self.push_button('1')
        self.push_button('.')
        self.push_button('.')
        assert self.get_display_content() == '1.'
