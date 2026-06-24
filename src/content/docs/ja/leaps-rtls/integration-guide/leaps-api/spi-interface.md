---
title: "SPI インターフェイス"
lang: ja
slug: "leaps-rtls/integration-guide/leaps-api/spi-interface"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/leaps-api/spi-interface/"
order: 131
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="spi-interface">
<h1>SPI インターフェイス</h1>
<hr class="docutils">
<p>モジュールはアイドル状態では 0xFF で応答します。SPI トランザクション間の最小遅延は 5 ミリ秒以上である必要があります。モジュールは SPI バス上で SPI スレーブとして動作します。スレーブが 1 回の転送でサポートする最大バイト数は 255 です。SPI API インターフェースを使用する前に、リセット後少なくとも 1 秒待つ必要があります。</p>
<hr class="docutils">
<div class="section" id="using-polling">
<h2>ポーリングの使用</h2>
<a class="reference internal image-reference" href="../../../../_images/image3.png"><img alt="../../../../_images/image3.png" class="align-center" src="/docs-assets/ja/_images/image3.png" style="width: 615.0px; height: 352.0px;"></a>
</div>
<hr class="docutils">
<div class="section" id="example-polling-leaps-gpio-cfg-output">
<h2>leaps_gpio_cfg_output ポーリングの例</h2>
<a class="reference internal image-reference" href="../../../../_images/image4.png"><img alt="../../../../_images/image4.png" class="align-center" src="/docs-assets/ja/_images/image4.png" style="width: 614.0px; height: 312.0px;"></a>
</div>
<hr class="docutils">
<div class="section" id="using-interrupt-gpio-when-command-is-issued-from-the-master">
<h2>マスターからコマンドが発行された際に割り込み（GPIO）を使用する</h2>
<a class="reference internal image-reference" href="../../../../_images/image5.png"><img alt="../../../../_images/image5.png" class="align-center" src="/docs-assets/ja/_images/image5.png" style="width: 615.0px; height: 464.0px;"></a>
</div>
<hr class="docutils">
<div class="section" id="using-core-int-gpio-pin-to-notify-master-about-the-status-change">
<h2>CORE_INT GPIOピンを使用して、マスターにステータス変更を通知する</h2>
<p>この割り込みは、上記のTLV要求応答手順中に発生した場合、延期されます。</p>
<a class="reference internal image-reference" href="../../../../_images/image6.png"><img alt="../../../../_images/image6.png" class="align-center" src="/docs-assets/ja/_images/image6.png" style="width: 614.0px; height: 291.0px;"></a>
</div>
<hr class="docutils">
<div class="section" id="example-interrupt-leaps-bh-xfer">
<h2>leaps_bh_xfer 割り込みの例</h2>
<p>1つのTLVフレームの最大ペイロードサイズは253バイトです（スレーブがサポートする最大TLVフレーム - TLVヘッダー = 255 - 2 = 253）。マスターが leaps_bh_xfer コマンドを使用してスレーブ（ダウンリンク）に転送するバイト数は、コマンドの引数にエンコードされます。スレーブは、マスターへの転送準備が整ったダウンリンクデータとアップリンクデータの数を取得し、SPI転送シーケンスにおいてダウンリンクとアップリンクの両方を転送するためのトランザクションのサイズと数を決定します。</p>
<p>マスターが299バイトのダウンリンクデータを転送しようとしており、スレーブが1124バイトのアップリンクデータを準備しているとします。</p>
<ul class="simple">
<li><p>ダウンリンクバイト: 299 (少なくとも 2 TLV フレーム)</p></li>
<li><p>アップリンクバイト数：1124（少なくとも5つのTLVフレーム）</p></li>
</ul>
<p>マスターは引数 == 299 でコマンド leaps_bh_xfer を実行します。スレーブはサイズ == 255、トランザクション数 == 5 (5 * 253 = 1265) で応答します。ダウンリンクとアップリンクの両方の TLV データチャンクは、複数の TLV フレームにエンコードされたデータをシリアル化するために使用できる予約済みの TLV タイプを使用してエンコードされます。現在、最大 5 つの TLV フレームがサポートされています。TLV タイプ 100～104 (0x64～0x68) はアップリンクデータチャンク用に予約されています。TLV タイプ 110～114 (0x6E～0x72) はダウンリンクデータチャンク用に予約されています。</p>
<a class="reference internal image-reference" href="../../../../_images/image7.png"><img alt="../../../../_images/image7.png" class="align-center" src="/docs-assets/ja/_images/image7.png" style="width: 615.0px; height: 440.0px;"></a>
<hr class="docutils">
<div class="section" id="wakeup-via-spi">
<h3>SPI 経由のウェイクアップ</h3>
<p>モジュールがスリープ状態 (低電力モード) の場合、SPI/UART がコマンドの受信を開始する前にウェイクアップ手順を実行する必要があります。スリープ状態から復帰するには、SPIのCSピンに少なくとも35マイクロ秒幅のパルスを生成するか、UARTインターフェースに少なくとも1バイトを送信する必要があります（低電力モードのみ）。</p>
</div>
</div>
</div>


           </div>
