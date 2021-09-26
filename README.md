図書館の返却日チェックスクリプト
=====================================

利用している近隣の図書館から借りた本の返却日調べて読み上げたりするスクリプト

# 使い方

```
cd src
python3 main.py
```

# セットアップ

* chrome 入れとく
* brew 入れとく
* ターミナルで
  ```
  pip3 install --upgrade pip
  pip3 install --upgrade setuptools
  pip3 install selenium
  pip3 install chromedriver-binary==93.0.4577.63 # 適切なバーションを入れる
  ```
* ```src/secret.py``` を作る。中はこんな感じにする。
  ```
  accountData = {
      "杉並区立図書館" : {
          "user" : "your id",
          "password" : "your password"
      }
  }
  ```
    * plain textで行けてないけどとりあえず。
