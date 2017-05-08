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
        
    def test_when_press_one_two_displays_twelve(self):
        self.push_button('1')
        self.push_button('2')
        assert self.get_display_content() == '12'

    def test_when_load_and_press_clear_displays_zero(self):
        self.push_button('clear')
        assert self.get_display_content() == '0'
        
    def test_when_press_one_then_clear_displays_zero(self):
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
        
    def test_when_press_one_plus_one_equals_display_two(self):
        self.push_button('1')
        self.push_button('+')
        self.push_button('1')
        self.push_button('=')
        assert self.get_display_content() == '2'
        
    def test_when_press_one_plus_two_equals_plus_three_equals_displays_six(self):
        self.push_button('1')
        self.push_button('+')
        self.push_button('2')
        self.push_button('=')
        self.push_button('+')
        self.push_button('3')
        self.push_button('=')
        assert self.get_display_content() == '6'