import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))
from fuzz_calculator import TestOneInput

def run_corpus(corpus_dir):
    if not os.path.exists(corpus_dir):
        print(f"Skipping {corpus_dir}")
        return

    files = os.listdir(corpus_dir)
    # ディレクトリ内の全ファイルを順に実行
    for fname in files:
        path = os.path.join(corpus_dir, fname)
        if not os.path.isfile(path) or fname.startswith("."):
            continue
            
        with open(path, "rb") as f:
            data = f.read()
        
        try:
            TestOneInput(data)
        except SystemExit:
            continue
        except:
            # 計測中はエラーが出ても止まらず次へ
            pass

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for d in sys.argv[1:]:
            run_corpus(d)