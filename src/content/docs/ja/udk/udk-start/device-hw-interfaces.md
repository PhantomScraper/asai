---
title: "ハードウェアインターフェイス"
lang: ja
slug: "udk/udk-start/device-hw-interfaces"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/ja/udk/udk-start/device-hw-interfaces/"
order: 35
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="hardware-interfaces">
<span id="hardware-interface"></span><h1>ハードウェアインターフェイス</h1>
<p>デモを進める前に、ハードウェア インターフェイス、特に <span class="red-text">ボタン A、B、および C</span>、<span class="red-text">2 つの USB-C ポート</span>、<span class="red-text">前面の RGB LED</span>、および <span class="green-text">2 つの側面の GREEN LED</span> に重点を置くことが重要です。これらの要素を理解すると、各デモンストレーションを効果的に設定するのに非常に役立ちます。</p>
<hr class="docutils">
<blockquote id="uihwinterfaces">
<div><a class="reference internal image-reference" href="../../../_images/for-buttons.png"><img alt="../../../_images/for-buttons.png" class="align-right" src="/docs-assets/ja/_images/for-buttons.png" style="width: 260.0px; height: 226.3px;"></a>
</div></blockquote>
<p><strong>ボタン、LED、およびユーザー操作</strong></p>
<blockquote>
<div><ul class="simple">
<li><p>ボタン A: 電源オン/オフ ボタン (長押し)。</p>
<ul>
<li><p><span class="green-text">緑色のLED</span>: 電源ステータス</p></li>
</ul>
</li>
<li><p>ボタン B: Qorvo NI / UCI モードと LEAPS UWBS モードを切り替えます (長押し)。</p>
<ul>
<li><p><span class="green-text">緑の LED</span>: UWB ステータス</p></li>
</ul>
</li>
<li><p>ボタン C: N/A (将来の使用のため)。</p>
<ul>
<li><p>RGB LED: 電源投入時のデバイス モードを示します。</p>
<ul>
<li><p><span class="red-text">RED</span> は LEAPS UWBS です</p></li>
<li><p><span class="blue-text">BLUE</span> は Qorvo NI です</p></li>
<li><p><span class="green-text">GREEN</span> は Qorvo UCI です</p></li>
</ul>
</li>
</ul>
</li>
<li><p>ブザー: アラームに使用されます。</p></li>
<li><p>ハプティックモーター: アラームに使用されます。</p></li>
</ul>
</div></blockquote>
<hr class="docutils">
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/for-usb-type-c.png"><img alt="../../../_images/for-usb-type-c.png" class="align-right" src="/docs-assets/ja/_images/for-usb-type-c.png" style="width: 275.44px; height: 259.16px;"></a>
</div></blockquote>
<p><strong>データ インターフェイス</strong></p>
<blockquote>
<div><ul class="simple">
<li><p>USB-C データ ポート 1: USB コマンド ラインとバイナリ API。</p></li>
<li><p>USB-C データ ポート 2: DAPLink + USB/UART コマンド ラインおよびバイナリ API。</p></li>
<li><p>統合された UWB アンテナ。</p></li>
<li><p>統合された Bluetooth アンテナ。</p></li>
</ul>
</div></blockquote>
<hr class="docutils">
<p><strong>開発インターフェイス</strong></p>
<blockquote>
<div><ul class="simple">
<li><p>SWD デバッガーおよび USB/UART コンバーターを備えた統合 DAPLink: プログラミング、デバッグ目的、およびデバイス構成に使用されます。</p></li>
<li><p>外部 J-Link デバッガ用の 6 ピン Tag Connect 互換コネクタ。</p></li>
<li><p>PCB ジャンパー パッド: SWD_RST、SWD_DIO、SWD_CLK、DBG_TXD、DBG_RXD。</p></li>
<li><p>GPIOs: J11 (P0.21, P0.24, DW_GP0, DW_GP1, DW_GP2, DW_GP3, DW_GP4, DW_GP5, DW_GP6), J12 (P0.11, P0.12, P0.13, P0.14, P0.29, P0.31, P1.14, P1.07).</p></li>
<li><p>NFC アンテナ パッド: P0.09/NFC1、P0.10/NFC2。</p></li>
<li><p>3.7V バッテリー コネクタ。</p></li>
</ul>
<a class="reference internal image-reference" href="../../../_images/lc14_b2-top-view.png"><img alt="../../../_images/lc14_b2-top-view.png" class="align-center" src="/docs-assets/ja/_images/lc14_b2-top-view.png" style="width: 452.5px; height: 561.5px;"></a>
</div></blockquote>
<hr class="docutils">
<p><strong>ポートピンのマッピング</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 51%">
<col style="width: 24%">
<col style="width: 24%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>代替関数</p></th>
<th class="head"><p><a class="reference internal" href="/docs/ja/leaps-rtls#leaps-rtls"><span class="std std-ref">LEAPS RTLS</span></a></p></th>
<th class="head"><p><a class="reference internal" href="/docs/ja/pans-pro-rtls#pans-pro-rtls"><span class="std std-ref">PANS PRO RTLS</span></a></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>UART TX</p></td>
<td><p>P1.13</p></td>
<td><p>P1.13</p></td>
</tr>
<tr class="row-odd"><td><p>UART RX</p></td>
<td><p>P1.15</p></td>
<td><p>P1.15</p></td>
</tr>
<tr class="row-even"><td><p>UWB SPI CS</p></td>
<td><p>P0.20</p></td>
<td><p>P0.20</p></td>
</tr>
<tr class="row-odd"><td><p>UWB SPI CLK</p></td>
<td><p>P0.16</p></td>
<td><p>P0.16</p></td>
</tr>
<tr class="row-even"><td><p>UWB SPI SDO</p></td>
<td><p>P0.17</p></td>
<td><p>P0.17</p></td>
</tr>
<tr class="row-odd"><td><p>UWB SPI SDI</p></td>
<td><p>P0.23</p></td>
<td><p>P0.23</p></td>
</tr>
<tr class="row-even"><td><p>UWB IRQ</p></td>
<td><p>P0.25</p></td>
<td><p>P0.25</p></td>
</tr>
<tr class="row-odd"><td><p>UWB リセット</p></td>
<td><p>P0.15</p></td>
<td><p>P0.15</p></td>
</tr>
<tr class="row-even"><td><p>LED RED</p></td>
<td><p>P0.27</p></td>
<td><p>P0.27</p></td>
</tr>
<tr class="row-odd"><td><p>LED BLUE</p></td>
<td><p>P0.4</p></td>
<td><p>P0.4</p></td>
</tr>
<tr class="row-even"><td><p>LED GREEN</p></td>
<td><p>P0.5</p></td>
<td><p>P0.5</p></td>
</tr>
<tr class="row-odd"><td><p>LED 外部 0</p></td>
<td><p>P1.12</p></td>
<td><p>P1.12</p></td>
</tr>
<tr class="row-even"><td><p>LED 外部 1</p></td>
<td><p>P0.30</p></td>
<td><p>P0.30</p></td>
</tr>
<tr class="row-odd"><td><p>ボタンメイン</p></td>
<td><p>P0.26</p></td>
<td><p>P0.26</p></td>
</tr>
<tr class="row-even"><td><p>ボタン外部 0</p></td>
<td><p>P1.11</p></td>
<td><p>P1.11</p></td>
</tr>
<tr class="row-odd"><td><p>ボタン外部1</p></td>
<td><p>P0.28</p></td>
<td><p>P0.28</p></td>
</tr>
<tr class="row-even"><td><p>ACC I2C SDA</p></td>
<td><p>P0.22</p></td>
<td><p>P0.22</p></td>
</tr>
<tr class="row-odd"><td><p>ACC I2C SCL</p></td>
<td><p>P0.19</p></td>
<td><p>P0.19</p></td>
</tr>
<tr class="row-even"><td><p>ACC IRQ</p></td>
<td><p>P1.1</p></td>
<td><p>P1.1</p></td>
</tr>
<tr class="row-odd"><td><p>ブザー</p></td>
<td><p>P0.2</p></td>
<td><p>P0.2</p></td>
</tr>
<tr class="row-even"><td><p>モーター</p></td>
<td><p>P1.10</p></td>
<td><p>P1.10</p></td>
</tr>
<tr class="row-odd"><td><p>バッテリー ADC ピン</p></td>
<td><p>P0.3</p></td>
<td><p>P0.3</p></td>
</tr>
<tr class="row-even"><td><p>DCDC3V3 制御ピン</p></td>
<td><p>該当なし</p></td>
<td><p>該当なし</p></td>
</tr>
<tr class="row-odd"><td><p>充電器ステータスピン</p></td>
<td><p>該当なし</p></td>
<td><p>該当なし</p></td>
</tr>
<tr class="row-even"><td><p>USB 検出器ピン</p></td>
<td><p>P1.9</p></td>
<td><p>該当なし</p></td>
</tr>
<tr class="row-odd"><td><p>API SPI CS</p></td>
<td><p>P0.29</p></td>
<td><p>P0.12</p></td>
</tr>
<tr class="row-even"><td><p>API SPI CLK</p></td>
<td><p>P0.12</p></td>
<td><p>P0.11</p></td>
</tr>
<tr class="row-odd"><td><p>API SPI SDO</p></td>
<td><p>P0.11</p></td>
<td><p>P0.14</p></td>
</tr>
<tr class="row-even"><td><p>API SPI SDI</p></td>
<td><p>P0.14</p></td>
<td><p>P0.31</p></td>
</tr>
<tr class="row-odd"><td><p>API IRQ</p></td>
<td><p>P0.31</p></td>
<td><p>P0.29</p></td>
</tr>
</tbody>
</table>
</div>


           </div>
