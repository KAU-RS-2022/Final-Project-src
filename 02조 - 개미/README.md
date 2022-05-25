# 02조 : 개미

------------------------
# Stock predict with twitter sentiment analysis

**StockPredict.ipynb** is for stock prediction with twitter sentiment anaylsis.

The default sentiment analysis is PrepareData.getPreaparedData() with textblobs.

If you want to use custom text sentiment analysis (ex:SA_Word2Vec) Use PrepareDataWithSA_Word2Vec.getPreaperedData() instead of PrepareData.getPreaperedData()

* You can use **BertSentimentAnalysis.ipynb** to do sentiment analysis with BERT.

* You can use **Word2VecSentimentAnalysis.ipynb** to do sentiment analysis with Word2Vec and K-means algorithm.

  (**Word2VecSentimentAnalysis.ipynb** has been modularized and included in **StockPredict.ipynb**)
