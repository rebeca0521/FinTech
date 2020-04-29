
# HW2

## 分析資料來源

使用tweepy爬取twitter上的貼文，keyword設定為"Dow Jones Industrial Average"，並且用tweepy上情緒分數的欄位，將情緒為正的文章抓出來做分析。
![](https://i.imgur.com/1ALz0Fb.png)



## 斷詞 NER
使用nltk套件將貼文做斷詞，由於斷詞後太多無意義的詞，所以決定使用NER來找出有意義的詞。
![](https://i.imgur.com/P7aFoAD.png)

使用內建的NER功能將有意義的詞彙挑選出來。
![](https://i.imgur.com/NbibSKO.png)

大約算一下每個詞出現的次數
![](https://i.imgur.com/rYjUyFN.png)


## 稀疏矩陣
用NER後找出來的詞和每一則貼文做出稀疏矩陣
![](https://i.imgur.com/G585nzp.png)
(最左邊的index為每一則貼文)


## Co-Occurrence Matrix
將每個詞轉向算出同時出現的次數，呈現共線矩陣。
![](https://i.imgur.com/IsUAN2x.png)


## 共現圖

以每則情緒為正向的貼文為單位
![](https://i.imgur.com/k3DyWzd.png)


## 熱度圖
![](https://i.imgur.com/3muV97M.png)


## 結論


## Reference
> * https://www.itread01.com/article/1529980432.html
> * https://networkx.github.io/documentation/networkx-1.7/tutorial/tutorial.html#drawing-graphs
* https://python-graph-gallery.com/network-chart/
* https://github.com/syuan0624/FinTech/blob/master/HW2/TDM%2C%20CO-occurrence%20Matrix%2C%20%E5%85%B1%E7%B7%9A%E5%9C%96%20.ipynb
