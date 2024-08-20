# LangChain-python-study

- こちらのリポジトリ-は [langchain](https://github.com/langchain-ai/langchain) のパッケージを利用して勉強を進める。

## 技術選定

go で実装可能な [langchaingo](https://github.com/tmc/langchaingo) や java で実装可能な[langchain4j](https://github.com/langchain4j/langchain4j)や javascriot[langchainjs](https://github.com/langchain-ai/langchainjs)がある。しかし、package によっては、メンテナンスがされていないものがある。AI は、移り変わりが激しい分野であるため、メンテナンスがされている package を選択する必要がある。今回は、メンテナンスの観点に,javascriot[langchainjs](https://github.com/langchain-ai/langchainjs)と [langchain](https://github.com/langchain-ai/langchain) の 2 つに絞り込んだ。今回はフロントエンドを作成しない、LangChain(python)の方がドキュメントやサンプルコードも充実、機械学習やデータサイエンスにおいて python のライブラリーが豊富であることを踏まえて LangChain を選定した。

## インデックス

- [環境構築](./docs/construction.md)
- langChain について
  - [langChain とは]()
  - [model について]()
