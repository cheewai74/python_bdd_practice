https://behave.readthedocs.io/en/latest/tutorial/</BR>

python3 -m venv .venv</BR>
source .venv/bin/activate</BR>
pip install virtualenvwrapper</BR>
python3 -m pip install --upgrade pip</BR>

pip install behave</BR>

pip install pytest</BR>
pip install pytest-cov</BR>
pip install --upgrade unittest-xml-reporting</BR>
pip install mock</BR>
pip install requests</BR>
pip install webtest</BR>
pip install pylint</BR>
pip install coverage</BR>
pip install paver</BR>


```
pip install pynose
nosetests test/calculate_test.py
nosetests --with-doctest -v
nosetests
nosetests --with-coverage
nosetests --with-coverage --cover-erase --cover-xml
nosetests --with-coverage --cover-erase --cover-html

pip install rednose
nosetests --rednose
py.test
py.test -v
py.test -r f
py.test --pdb
py.test --cov app/ tests/
```


sudo apt install python3-pytest</BR>
sudo apt-get install jmeter</BR>
sudo apt-get install jenkins</BR>

pip freeze > requirements.txt</BR>
pip install -r requirements.txt</BR>


Note: To run the test case,we input behave in run command section.</BR>

Syntax: behave -i filename.feature</BR>
Syntax: behave</BR>


https://flask.palletsprojects.com/en/stable/</BR>

Using Gherkin Syntax</BR>
```
Feature:
Scenario:
Scenario Outline:
Given
When
Then
And
```

TDD Concept:</BR>
```
"Arrange, Act, Assert"

def test_something(self):
    # Arrange phase, nothing to prepare here.
    
    # Act phase, call do_something
    result = do_something()

    # Assert phase, verify do_something did what we expect.
    assert result == "did something"
```

https://www.selenium.dev/</BR>


https://github.com/PacktPublishing/Crafting-Test-Driven-Software-with-Python</BR>