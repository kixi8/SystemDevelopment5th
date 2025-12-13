# Calculator

A Python calculator implementation with comprehensive test coverage and input validation.
This Calculator can handle the values up to 1000000 (Not implemented yet on purpose)

## Features

- **Basic Operations**: Addition, subtraction, multiplication, division

## Installation

1. Fork the repository:
<!-- ```bash
git clone https://github.com/Yutaro-Kashiwa/SystemDevelopment5th.git
cd SystemDevelopment5th
``` -->
Fork


2. Actionsに移動して実行してみよう
画像が出ると思うので，「I understand my workflows, go ahead and enable them」を選んでください．

「Python Atheris Fuzzing」をクリックし，「Run workflow」を押してActionsを手動実行

<!--  -->


# おまけ
## カバレッジレポートの生成方法
ここでのカバレッジは新しいコードパスを取得した際の入力値のみを表示している．
<!-- Yamlの追記コードを説明 -->
```yaml
      # 2. カバレッジ計測
      - name: Coverage Collection
        run: |
          mkdir -p crashes
          # クラッシュファイルを退避
          mv crash-* crashes/ || true
          mv leak-* crashes/ || true
          mv timeout-* crashes/ || true
          
          export PYTHONPATH=$PYTHONPATH:$(pwd)
          # Calculatorのコーパスでカバレッジ計測
          coverage run --source=src fuzz/repro_coverage.py corpus_calc crashes
          # StringCalculatorのコーパスでカバレッジ計測 (既存の結果に追加 -a)
          # coverage run -a --source=src fuzz/repro_coverage.py corpus_str_calc crashes

      # 3. HTMLレポート生成
      - name: Generate Report
        run: coverage html -d coverage-report



```



## コーパスの取得
ここでのコーパスは，新しいコードパスを取得した際の入力値のみが保存される．そのため，実際にはもっとたくさんの入力値が実行されている．
```yaml
      # 4. 成果物をまとめる
      - name: Bundle Artifacts
        run: |
          mkdir -p fuzzing_results
          mv coverage-report fuzzing_results/
          # 両方のコーパスを成果物に含める
          cp -r corpus_calc fuzzing_results/
          # cp -r corpus_str_calc fuzzing_results/
          cp -r crashes fuzzing_results/

      # 5. アップロード (ZIPでダウンロード可能になります)
      - name: Upload All Artifacts
        uses: actions/upload-artifact@v4
        with:
          name: all-fuzzing-results
          path: fuzzing_results/


```

## Usage

### Basic Usage

```python
from src.calculator.calculator import Calculator

# Create calculator instance
calc = Calculator()

# Basic operations
result = calc.add(5, 3)         # 8
result = calc.subtract(10, 3)   # 7
result = calc.multiply(4, 5)    # 20
result = calc.divide(10, 2)     # 5.0

# Advanced operations
result = calc.power(2, 3)       # 8
result = calc.square_root(16)   # 4.0
result = calc.modulo(10, 3)     # 1
```


## Testing

### Run All Tests

```bash
pytest tests/
```

### Run Tests with Verbose Output

```bash
pytest tests/test_calculator.py -v
```

### Generate Coverage Report

```bash
pytest --cov=src --cov-report=html tests/
```

View the HTML report:
```bash
open htmlcov/index.html
```

## Project Structure

```
SystemDevelopment5th/
├── src/
│   └── calculator/
│       ├── __init__.py
│       └── calculator.py          # Calculator implementation
├── tests/
│   ├── __init__.py
│   └── test_calculator.py         # Test suite (67 tests)
├── .gitignore
├── .coveragerc                    # Coverage configuration
├── setup.cfg                      # Project configuration
└── README.md
```

## API Documentation

### Calculator Class

#### Methods

**`add(a, b)`**
- Adds two numbers
- Raises `InvalidInputException` if inputs are outside valid range
- Returns: Sum of a and b

**`subtract(a, b)`**
- Subtracts b from a
- Raises `InvalidInputException` if inputs are outside valid range
- Returns: Difference of a and b

**`multiply(a, b)`**
- Multiplies two numbers
- Raises `InvalidInputException` if inputs are outside valid range
- Returns: Product of a and b

**`divide(a, b)`**
- Divides a by b
- Raises `InvalidInputException` if inputs are outside valid range
- Raises `ValueError` if b is zero
- Returns: Quotient of a and b

### Constants

- `MAX_VALUE = 1000000`: Maximum allowed input value
- `MIN_VALUE = -1000000`: Minimum allowed input value

### Exceptions

**`InvalidInputException`**
- Raised when input values are outside the valid range [-1000000, 1000000]
- Inherits from `Exception`


### Code Quality

The project follows Python best practices:
- Comprehensive docstrings for all methods
- Type hints where applicable
- Error handling for edge cases
- Input validation
- AAA test pattern

## Requirements

- Python 3.12+
- pytest 9.0+
- pytest-cov 7.0+

## License

This project is for educational purposes.

## Contributing

Contributions are welcome! Please ensure:
1. All tests pass
2. New features include tests
3. Tests follow AAA pattern
4. Code includes proper documentation

## Author

Yutaro Kashiwa


