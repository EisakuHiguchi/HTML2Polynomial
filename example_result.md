# example の処理の流れと結果

今回使用したhtmlは

```
<html>
<body>
<p>ここに文章</p>
<i>たとえばイタリックにしたり？</i>
<p><strong>文章を強調</strong>してみたり！</p>
</body>
</html>
```

と，

```
<html>
<body>
<p>ここに文章</p>
<p><strong>文章を強調</strong>してみたり！</p>
</body>
</html>
```

タグ（変数）と文章（定数）は次．

```
x1 = "<html>"
x2 = "<body>"
x3 = "<p>"
x4 = "<strong>"
x5 = "</html>"
x6 = "</body>"
x7 = "</p>"
x8 = "</strong>"

a1 = "ここに文章"
a2 = "<i>"
a3 = "たとえばイタリックにしたり？"
a4 = "</i>" 
a5 = "文章を強調"
a6 = "してみたり！"
```

このとき，htmlを変換（タグを記号に置き換えるだけ）すると

```
x1 + x2 + x3*a1*x7 + a2*a3*a4 + x3*x4*a5*x8*a6*x7 + x6 + x5 ,
x1 + x2 + x3*a1*x7 + x3*x4*a5*x8*a6*x7 + x6 + x5
```

となる．

この2つの多項式でグレブナ基底を計算すると

```
a4*a3*a2, x1+x2+(a6*a5*x8*x4+a1)*x7*x3+x6+x5
```

これをhtmlに戻すと

```
<!-- a4*a3*a2 の結果 -->
</i>たとえばイタリックにしたり？<i>
```

```
<!-- x1+x2+(a6*a5*x8*x4+a1)*x7*x3+x6+x5 の結果 -->
<html>
<body>
してみたり！文章を強調</strong><strong></p><p>
ここに文章</p><p>
</body>
</html>
```

となる．
