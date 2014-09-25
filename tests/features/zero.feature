Feature: Go to google  

Scenario: Visit google
    Given I go to "http://www.google.com/"  
  	When I fill in field with class "gbqfif" with "testingbot"
  	Then I should see "testingbot.com" within 2 second  

Scenario: Visit google
    Given I go to "http://www.youtube.com/"      
