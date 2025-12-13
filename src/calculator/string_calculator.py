# # src/calculator/string_calculator.py

# """
# A string-based calculator module that processes simple arithmetic expressions.
# """
# from .calculator import Calculator, InvalidInputException


# class InvalidExpressionException(Exception):
#     """Exception raised when the string expression is invalid."""
#     pass


# class StringCalculator:
#     """Processes simple expressions like 'a + b', 'a - b', etc."""

#     def __init__(self):
#         self.calc = Calculator()

#     def calculate(self, expression: str):
#         """
#         Parses and calculates a simple expression (e.g., "5 + 3").

#         Args:
#             expression: The arithmetic expression string.

#         Returns:
#             The result of the calculation.

#         Raises:
#             InvalidExpressionException: If the expression is not in a supported format.
#             ValueError: For division by zero.
#             InvalidInputException: If operands are outside the valid range.
#         """
#         # 入力文字列の先頭/末尾の空白を除去 (バグ修正)
#         cleaned_expression = expression.strip()
        
#         parts = cleaned_expression.split()

#         if len(parts) != 3:
#             raise InvalidExpressionException(f"Invalid expression format: {expression}")

#         a_str = parts[0]
#         op = parts[1]
#         b_str = parts[2]
        
#         # 演算によって適切な型に変換 (バグ修正)
#         try:
#             if op in ('+', '-', '*', '%'):
#                 # 整数演算
#                 a_val = int(a_str)
#                 b_val = int(b_str)
#             elif op == '/':
#                 # 浮動小数点数演算
#                 a_val = float(a_str)
#                 b_val = float(b_str)
#             else:
#                 a_val = float(a_str)
#                 b_val = float(b_str)

#         except ValueError:
#             raise InvalidExpressionException("Operands must be valid numbers matching the operation type.")

#         # 演算子の実行
#         if op == '+':
#             return self.calc.add(a_val, b_val)
#         elif op == '-':
#             return self.calc.subtract(a_val, b_val)
#         elif op == '*':
#             return self.calc.multiply(a_val, b_val)
#         elif op == '/':
#             return self.calc.divide(a_val, b_val)
#         elif op == '%':
#             # Modulo演算の不完全性を解消
#             return self.calc.modulo(a_val, b_val)
#         else:
#             raise InvalidExpressionException(f"Unsupported operator: {op}")


"""
A string-based calculator module that processes simple arithmetic expressions.
NOTE: This implementation is intentionally incomplete/buggy for educational purposes.
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
            もし エラーなら

        Raises:
            InvalidExpressionException: If the expression is not in a supported format.
            ValueError: For division by zero.
            InvalidInputException: If operands are outside the valid range.
        """
        # 式をスペースで区切ってオペランドと演算子を取得
        # 意図的なバグ: 複数のスペースや不正な形式に対する堅牢性が低い
        
        parts = expression.split()

        # if len(parts) != 3:
        #     raise InvalidExpressionException(f"Invalid expression format: {expression}")

        # オペランドの解析
        try:
            # ここではfloatで解析し、内部のCalculatorに渡す
            a = float(parts[0])
            op = parts[1]
            b = float(parts[2])
        except ValueError:
            raise InvalidExpressionException("Operands must be valid numbers.")

        # 演算子の実行
        if op == '+':
            return self.calc.add(a, b)
        elif op == '-':
            return self.calc.subtract(a, b)
        elif op == '*':
            return self.calc.multiply(a, b)
        elif op == '/':
            return self.calc.divide(a, b)
        elif op == '%':
            # 意図的な不完全性/バグ: modulo演算を実装していない
            raise InvalidExpressionException("Modulo operation (%) is not yet supported.")
        else:
            raise InvalidExpressionException(f"Unsupported operator: {op}")