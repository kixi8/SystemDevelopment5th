import sys
import os

# srcディレクトリへのパスを通す
sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))

import atheris
# プロジェクトのディレクトリ構成に合わせてインポート
from calculator.calculator import Calculator, InvalidInputException

def TestOneInput(data):
    # ランダムなデータを生成するプロバイダを作成
    fdp = atheris.FuzzedDataProvider(data)
    
    # ランダムな整数を2つ取得
    val_a = fdp.ConsumeInt(4)
    val_b = fdp.ConsumeInt(4)
    # 0~3のランダムな数値で操作(足し算、引き算など)を決める
    op = fdp.ConsumeIntInRange(0, 3)
    
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
            
    except (ValueError, InvalidInputException):
        # 0除算や入力範囲外のエラーは仕様通りなので無視
        pass
    except Exception as e:
        # それ以外の予期せぬエラーは「クラッシュ」として報告
        raise e

if __name__ == "__main__":
    # 計測の設定をしてFuzzerを起動
    atheris.instrument_all()
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()