Feature: Test calculator functionalities.

Scenario: Addition
  Given Calculator app runs
  When I input '5' and '3'
  Then I get result '8'

Scenario: Addition Negative
  Given Calculator app runs
  When I input '-5' and '3'
  Then I get result '-2'
  