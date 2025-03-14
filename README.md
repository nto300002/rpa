# データ入力業務自動化スクリプト

このスクリプトは、Google Maps を使用して市役所の近くにある B 型事業所を自動的に検索する RPA（Robotic Process Automation）ツールです。

## 動作内容

1. Google Maps をブラウザで開く
2. `shiyakusyo.txt`ファイルから最初の行（市名）を読み取る
3. 読み取った市名に「市役所」を追加して Google Maps で検索
4. 表示されたピンを右クリック
5. 「付近を検索」をクリック
6. 「B 型事業所」と検索
7. 検索後、`shiyakusyo.txt`の最初の行を削除

## セットアップ

1. 必要なパッケージをインストール：

   ```
   pip install -r requirements.txt
   ```

2. `shiyakusyo.txt`ファイルに検索したい市名を 1 行ずつ記入してください：
   ```
   東京
   大阪
   名古屋
   ...
   ```

## 使用方法

ブラウザをデバッグモードで起動
Windows

```bash
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222
```

Mac

```bash
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
```

スクリプトを実行：

```
python data_entry_open_map.py
```

処理が完了すると、ブラウザに Google Maps が表示され、指定された市役所の近くにある B 型事業所の検索結果が表示されます。
Enter キーを押すとブラウザが閉じ、`shiyakusyo.txt`の最初の行が削除されます。

## 注意点

- このスクリプトを実行するには Chrome ブラウザがインストールされている必要があります
- Google Maps の UI が変更された場合、スクリプトが動作しなくなる可能性があります
