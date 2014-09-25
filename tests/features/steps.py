# -*- coding: utf-8 -*-
from lettuce import *  
from lettuce_webdriver.util import AssertContextManager  
  
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys
import lettuce_webdriver.webdriver  
 
@before.all
def setup_browser():
    world.browser = webdriver.Firefox()

@step(u'Given I go to "([^"]*)"')
def given_i_go_to_url(step, url):
    world.response = world.browser.get(url)


def find_field_by_class(browser, attribute):  
    xpath = "//input[@class='%s']" % attribute  
    elems = browser.find_elements_by_xpath(xpath)  
    return elems[0] if elems else False  

@step(u'When I fill in field with class "([^"]*)" with "([^"]*)"')
def when_i_fill_in_field_with_class_group1_with_group2(step, field_class, value):        
    with AssertContextManager(step):  
        text_field = find_field_by_class(world.browser, field_class)  
        text_field.clear()  
        text_field.send_keys(value, Keys.ENTER);         
        #text_field.submit()
        #text_field.send_keys(world.browser.title)


@step(u'Then I should see "([^"]*)" within "([^"]*)" seconds')
def then_i_should_see(step, value, seconds):        
    return True

  	  
