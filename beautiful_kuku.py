"""
スラスラ読めるPythonふりがなプログラミング P115

https://www.relief.jp/docs/python-make-multiplication-table.html
を参照した。
"""

for cnt1 in range(1, 10):
    for cnt2 in range(1, 10):
        print( cnt1, "✗", cnt2, "＝", f'{cnt1 * cnt2 :3d}' ,"｜", end=" ")
    print()
