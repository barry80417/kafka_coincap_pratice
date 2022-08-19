# kafka_coincap_pratice

執行方式先用iTerm cd到kafka所在資料夾 cd /usr/local/Cellar/kafka/3.2.1
再進行指令./bin/zookeeper-server-start /usr/local/etc/kafka/zookeeper.properties
開啟zookeeper

在另開一個視窗一樣cd到kafka所在資料夾 cd /usr/local/Cellar/kafka/3.2.1
再進行指令./bin/kafka-server-start /usr/local/etc/kafka/server.properties

開啟kafka遇到一次錯誤 ERROR Exiting kafka due to fatal exception，最後發現是以前可能啟動過kafka要把它關閉，用brew services stop kafka關閉後就能正常再開

開啟zookeeper遇過一次錯誤錯誤碼如 https://stackoverflow.com/questions/67335702/zookeeper-gives-exiting-jvm-with-error-code-2-error
最後發現其實是我上方指令路徑打錯

執行玩上面兩者，再分別執行Producer及Consumer即可
