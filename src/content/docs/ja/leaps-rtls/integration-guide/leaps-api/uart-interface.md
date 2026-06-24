---
title: "UART インターフェース"
lang: ja
slug: "leaps-rtls/integration-guide/leaps-api/uart-interface"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/leaps-api/uart-interface/"
order: 132
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="uart-interface">
<h1>UART インターフェース</h1>
<hr class="docutils">
<p>ユーザーは、リセット後、UART API インターフェースを使用する前に少なくとも 1 秒待つ必要があります。UART はバイナリモードまたはシェルモードで動作できます。UART のリセット後、デフォルトモードは <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-serial-cfg-set#leaps-serial-cfg-set"><span class="std std-ref">leaps_serial_cfg_set</span></a> で設定できます。バイナリモードからシェルモードに切り替えるには、1秒以内に「ENTERを2回押します。シェルモードからバイナリモードに切り替えるには、シェルコマンド <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/base#quit"><span class="std std-ref">終了</span></a> を使用します。</p>
<a class="reference internal image-reference" href="../../../../_images/image8.png"><img alt="../../../../_images/image8.png" class="align-center" src="/docs-assets/ja/_images/image8.png" style="width: 384.0px; height: 265.0px;"></a>
<hr class="docutils">
<div class="section" id="example-leaps-gpio-cfg-output">
<h2>例leaps_gpio_cfg_output</h2>
<a class="reference internal image-reference" href="../../../../_images/image9.png"><img alt="../../../../_images/image9.png" class="align-center" src="/docs-assets/ja/_images/image9.png" style="width: 384.0px; height: 279.0px;"></a>
<hr class="docutils">
<div class="section" id="wakeup-via-uart">
<h3>UART経由のウェイクアップ</h3>
<p>モジュールがスリープ状態（低電力モード）の場合、SPI/UARTがコマンドの受信を開始する前にウェイクアップ手順を実行する必要があります。スリープ状態からウェイクアップするには、SPIのCSピンに少なくとも35マイクロ秒幅のパルスを生成するか、UARTインターフェースに少なくとも1バイトを送信する必要があります（低電力モードのみ）。</p>
</div>
</div>
</div>


           </div>
