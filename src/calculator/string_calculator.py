# string_calculator.py

"""
A string-based calculator module that processes simple arithmetic expressions.
NOTE: This implementation is intentionally incomplete/buggy for educational purposes,
      specifically lacking robustness against Index/Type/Size errors.
"""
from .calculator import Calculator, InvalidInputException


class InvalidExpressionException(Exception):
    """Exception raised when the string expression is invalid."""
    pass


class StringCalculator:
    """Processes simple expressions like 'a + b', 'a - b', etc."""

    def __init__(self):
        self.calc = Calculator()

    def calculate(self, expression: str):
        """
        Parses and calculates a simple expression (e.g., "5 + 3").
        
        Args:
            expression: The arithmetic expression string.

        Returns:
            The result of the calculation.

        Raises:
            InvalidExpressionException: If the expression is not in a supported format, 
                                        or if operands are invalid.
            ValueError: For division by zero.
            IndexError: 配列アクセスに失敗した場合（意図的にチェックを省略）。
            InvalidInputException: If operands are outside the valid range.
        """
        
        
        # 意図的なバグ/チェック漏れ: .strip() を省略し、前後の空白に弱い
        # cleaned_expression = expression.strip() # ← 意図的に省略

        parts = expression.split()

        # fixed: 要素数チェックを追加
        if len(parts) != 3:
            raise InvalidExpressionException("Expression must be in the format: 'a op b'.")

        # オペランドの解析 (意図的な型チェック漏れ: float()でまとめて変換)
        try:
            
            a = float(parts[0]) 
            op = parts[1]
            b = float(parts[2])
        except ValueError:
            # 意図的な型チェック漏れ: 'a', 'b' のいずれかが float に変換できない場合に発生
            raise InvalidExpressionException("Operands must be valid numbers.")
        except IndexError:
            # parts の要素数が足りない場合に発生。本来なら InvalidExpressionException でラップすべき。
            raise InvalidExpressionException("Incomplete expression.")

        # 演算子の実行 (意図的な数値の大きさチェック漏れ: Calculator側に依存するが、
        # StringCalculator側でオペランドの妥当性（例: 巨大な数）をチェックすべき)
        if op == '+':
            return self.calc.add(a, b)
        elif op == '-':
            return self.calc.subtract(a, b)
        elif op == '*':
            return self.calc.multiply(a, b)
        elif op == '/':
            return self.calc.divide(a, b)
        elif op == '%':
            # 意図的な不完全性/バグ: モジュロ演算の引数に対する型チェック（整数であるべきかなど）を省略
            # また、Calculator側での実装が意図的に不完全である可能性も考慮する
            return self.calc.modulo(a, b)
        else:
            raise InvalidExpressionException(f"Unsupported operator: {op}")