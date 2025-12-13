import sys
import os

# srcディレクトリへのパスを通す
sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))

import atheris
# プロジェクトのディレクトリ構成に合わせてインポート
from calculator.calculator import Calculator, InvalidInputException

# 追記: 実行回数をカウントするためのグローバル変数
TEST_COUNT = 0

def TestOneInput(data):
   # 追記: グローバル変数にアクセスし、カウントをインクリメント
   global TEST_COUNT
   TEST_COUNT += 1
    
   # ランダムなデータを生成するプロバイダを作成
   fdp = atheris.FuzzedDataProvider(data)
    
   # ランダムな整数を2つ取得
   val_a = fdp.ConsumeInt(4)
   val_b = fdp.ConsumeInt(4)
   # 0~4のランダムな数値で操作(足し算、引き算など)を決める
   op = fdp.ConsumeIntInRange(0, 4)
    
   calc = Calculator()

   try:
      if op == 0:
         calc.add(val_a, val_b)
      elif op == 1:
         calc.subtract(val_a, val_b)
      elif op == 2:
         calc.multiply(val_a, val_b)
      elif op == 3:
         calc.divide(val_a, val_b)
      # TODO: Implement modulo operation
      elif op == 4:
         calc.modulo(val_a, val_b)

            
   except (ValueError, InvalidInputException):
      # 0除算や入力範囲外のエラーは仕様通りなので無視
      pass
   except Exception as e:
      # クラッシュ時の入力値を表示してから例外を再送出
      print(f"\n=== CRASH DETECTED ===")
      # 追記: 実行回数を出力
      print(f"Test Count: {TEST_COUNT}")
      print(f"val_a: {val_a}")
      print(f"val_b: {val_b}")
      print(f"op   : {op}")
      print(f"======================")
      print(f"Unexpected exception💥: {e} 😱")
        
      # それ以外の予期せぬエラーは「クラッシュ」として報告
      raise e
if __name__ == "__main__":
   # 計測の設定をしてFuzzerを起動
   atheris.instrument_all()
   atheris.Setup(sys.argv, TestOneInput)
   atheris.Fuzz()