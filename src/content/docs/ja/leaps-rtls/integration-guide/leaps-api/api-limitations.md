---
title: "API の制限"
lang: ja
slug: "leaps-rtls/integration-guide/leaps-api/api-limitations"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/leaps-api/api-limitations/"
order: 116
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="api-limitations">
<h1>API の制限</h1>
<p>ノード構成が BLE インターフェース経由で変更されているときに、同時に SPI/UART インターフェースで API コマンドが実行されると、SPI/UART インターフェースの API が正しく動作しない可能性があります。潜在的なエラーを回避するために、現時点では BLE または SPI/UART のいずれかを使用する必要があります。特定のシェル コマンドは FLASH メモリにデータを書き込むため、これらのインターフェースを同時に使用すると、UART/SPI と BLE で問題が発生する可能性があります。これは、FLASH の消去または書き込み中に CPU が停止していることが原因です。</p>
</div>


           </div>
