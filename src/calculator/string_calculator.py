# src/calculator/string_calculator.py

from calculator.calculator import Calculator

class InvalidExpressionException(Exception):
    """Raised when the expression format is invalid."""
    pass

class StringCalculator:
    def __init__(self):
        self.calc = Calculator()

    def calculate(self, expression: str) -> float:
        """
        文字列の数式を受け取り、計算結果を返す
        Format: "Number Operator Number" (例: "10 + 2.5")
        """
        
        
        # Bug 1: 入力が空、あるいは区切り文字がない場合に IndexError (またはAttributeError) が発生する
        # Fuzzerは "123" や "" といった入力を生成し、ここでクラッシュさせる
        parts = expression.split(" ")
        
        # Bug 2: 数値変換失敗時に ValueError が発生する
        # calculator.py の仕様上、ValueError は「0除算」用．
        # ここでのパースエラー(ValueError)をキャッチしないと、
        # Fuzzerの設定(ValueErrorを無視)によってはバグが見過ごされる、
        # あるいは意図しないクラッシュとして扱われる可能性がある．
        val_a = float(parts[0])
        val_b = float(parts[2])
            
        op = parts[1]

        # 分かりやすい if-elif 構造に変更
        if op == '+':
            return self.calc.add(val_a, val_b)
        elif op == '-':
            return self.calc.subtract(val_a, val_b)
        elif op == '*':
            return self.calc.multiply(val_a, val_b)
        elif op == '/':
            return self.calc.divide(val_a, val_b)
        elif op == '%':
            return self.calc.modulo(val_a, val_b)
        else:
            # Bug 3: 未対応の演算子が来た場合に生の Exception を投げる
            # これは "Uncaught Exception" としてFuzzerにクラッシュ判定される．
            # 本来は InvalidExpressionException にラップすべき箇所．
            raise InvalidExpressionException(f"System Error: Unsupported operator '{op}'")