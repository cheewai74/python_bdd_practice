pip install pytest</BR>

pytest tests/calculate_test.py
pytest --doctest-modules -v tests/calculate_test.py

```

textmy_project/
│
├── src/                          # Your production code
│   ├── __init__.py
│   ├── calculator.py
│   └── database.py
│
├── tests/                        # Your test suite folder
│   ├── __init__.py               # Required for test discovery
│   ├── test_calculator.py        # Tests matching calculator.py
│   └── test_database.py          # Tests matching database.py
│
├── README.md
└── requirements.txt

```