# fuzz/fuzz_string_calculator.py

import sys
import os

# srcディレクトリへのパスを通す
sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))

import atheris
# プロジェクトのディレクトリ構成に合わせてインポート
from calculator.string_calculator import StringCalculator, InvalidExpressionException
from calculator.calculator import InvalidInputException

# 実行回数をカウントするためのグローバル変数
TEST_COUNT = 0

def TestOneInput(data):
   global TEST_COUNT
   TEST_COUNT += 1
    
   # ランダムなデータを生成するプロバイダを作成
   fdp = atheris.FuzzedDataProvider(data)
    
   # 修正: ConsumeUnicodeString(1024) -> ConsumeString(1024)
   # ランダムな文字列（式）を取得 (最大1024バイトの文字列)
   expression = fdp.ConsumeString(1024)
    
   calc = StringCalculator()

   try:
      # StringCalculatorのcalculateメソッドを実行
      calc.calculate(expression)
            
   # except (InvalidInputException):
   # #    # 0除算、入力範囲外、不正な式形式のエラーは仕様通りなので無視
   #    pass
   except (InvalidExpressionException):
      pass
   except (ValueError):
      pass
   except Exception as e:
      # クラッシュ時の入力値（式）を表示してから例外を再送出
      print(f"\n=== CRASH DETECTED IN STRING_CALCULATOR ===")
      print(f"Test Count: {TEST_COUNT}")
      print(f"Expression: '{expression}'")
      print(f"=========================================")
        
      # それ以外の予期せぬエラーは「クラッシュ」として報告
      raise e

if __name__ == "__main__":
   # 計測の設定をしてFuzzerを起動
   atheris.instrument_all()
   atheris.Setup(sys.argv, TestOneInput)
   atheris.Fuzz()