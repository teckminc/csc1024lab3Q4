import lab3q4
from io import StringIO
from sys import stderr
def test_case1(monkeypatch, capsys):
    number_inputs = StringIO('56\n34\n78\nDONE')

    monkeypatch.setattr('sys.stdin', number_inputs)
    lab3q4.main()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert captured_stdout.strip().find(f'168') != -1

def test_case2(monkeypatch, capsys):
  with open(f"lab3q4.py") as tf:
    head = [next(tf) for _ in range(10)]
    s = tf.read()
    assert(s.find("while") != -1 )
