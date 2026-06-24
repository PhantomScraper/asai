---
title: "LC4A仕様"
lang: ja
slug: "pans-pro-rtls/specification/lc4a-specification"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/specification/lc4a-specification/"
order: 102
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="lc4a-specification">
<span id="id1"></span><h1>LC4A仕様</h1>
<p>このドキュメントでは、LC4A デバイスの技術的な詳細について説明します。LC4A デバイスは、リアルタイム ロケーション システム (RTLS) 内でアンカー ノード (AN) またはタグ ノード (TN) として機能するように設計された多用途のハードウェア ソリューションです。その柔軟性と適応性により、さまざまな追跡および監視アプリケーションに最適です。</p>
<div class="sd-card sd-sphinx-override sd-mb-3 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<p class="sd-card-text"><a class="reference external" href="/_static/_pdfversion/lc4a-datasheet-ja.pdf">PDF バージョンの技術仕様</a> も参照してください。</p>
</div>
</div>
<a class="reference internal image-reference" href="../../../_images/lc4a_front_view.png"><img alt="デバイスの正面図" class="align-center" src="/docs-assets/ja/_images/lc4a_front_view.png" style="width: 190.32px; height: 273.39px;"></a>
<div style="text-align: center; font-weight: bold;">
The Front view of the device.
</div><hr class="docutils">
<div class="section" id="key-features">
<h2>主な機能</h2>
<ul class="simple">
<li><p>Qorvo の <a class="reference external" href="https://www.qorvo.com/products/p/DWM1001C">DWM1001C</a> モジュールに基づいており、<a class="reference external" href="https://www.qorvo.com/products/p/DW1000">DW1000</a> 超広帯域 (UWB) トランシーバー IC と Nordic Semiconductor MCU を Bluetooth nRF52832 と統合します。</p>
<ul>
<li><p>測距精度は +-20cm 以内です。</p></li>
<li><p>UWB チャネル 5 プリント PCB アンテナ (6.5 GHz)</p></li>
<li><p>6.8 Mbps データレート IEEE 802.15.4-2011 UWB 準拠</p></li>
<li><p>UWB および Bluetooth® アンテナとすべての RF 回路を統合します。</p></li>
<li><p>統合モーションセンサー: 3 軸加速度センサー。</p></li>
<li><p>低電力スリープモード向けに最適化された消費電流: &lt;15μA</p></li>
</ul>
</li>
<li><p>ステータス LED と UWB ステータス LED が含まれます。</p></li>
<li><p>USB ケーブル (5 VDC) または外部電源 (7 ～ 32 VDC) から電力を供給します。</p></li>
<li><p>ソフトウェア インフラストラクチャ、構成ツール、視覚化ツール (Android、Windows、macOS、Linux プラットフォームのさまざまなプラットフォームをサポート) を含む、無料の完全なソフトウェア パッケージ。</p></li>
<li><p>オープンな <a class="reference external" href="https://docs.leapslabs.com/">オンライン ドキュメント</a> および <a class="reference external" href="https://forum.leapslabs.com">コミュニティ フォーラム</a>。</p></li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="software-compatibility">
<h2>ソフトウェアの互換性</h2>
<p><a class="reference internal" href="/docs/ja/pans-pro-rtls#pans-pro-rtls"><span class="std std-ref">PANS PRO RTLS</span></a> および <a class="reference internal" href="/docs/ja/leaps-rtls#leaps-rtls"><span class="std std-ref">LEAPS RTLS</span></a> と互換性があります。デフォルトのファームウェアは、製造元から提供される <a class="reference internal" href="/docs/ja/pans-pro-rtls#pans-pro-rtls"><span class="std std-ref">PANS PRO RTLS</span></a> です。</p>
</div>
<div class="section" id="electrical-parameters">
<h2>電気パラメータ</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 46%">
<col style="width: 54%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>パラメータ</strong></p></th>
<th class="head"><p>値</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>VDC電源</p></td>
<td><p>7 〜 32 @3W 最大</p></td>
</tr>
<tr class="row-odd"><td><p>USB (電源とデータ)</p></td>
<td><p>5V @ 500mA最大</p></td>
</tr>
<tr class="row-even"><td><p>動作温度</p></td>
<td><p>-40°C - +85°C</p></td>
</tr>
<tr class="row-odd"><td><p>UWB がサポートするチャンネル</p></td>
<td><p>UWB-CH5 - 6240-6739.2 MHz</p></td>
</tr>
<tr class="row-even"><td><p>UWB 送信電力</p></td>
<td><p>ETSI、FCC: -41.3 dBm/MHz 最大</p></td>
</tr>
</tbody>
</table>
</div>
<div class="section" id="mechanical-parameters">
<h2>機械的パラメータ</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 46%">
<col style="width: 54%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>パラメータ</strong></p></th>
<th class="head"><p>値</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>サイズ</p></td>
<td><p>100 x 70 x 25 mm</p></td>
</tr>
<tr class="row-odd"><td><p>重量</p></td>
<td><p>110g</p></td>
</tr>
<tr class="row-even"><td><p>色</p></td>
<td><p>白</p></td>
</tr>
<tr class="row-odd"><td><p>マウント中</p></td>
<td><p>クランプ マウントを 1/4 インチ スクリュー ボールヘッドに接続します</p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="device-overview">
<h2>デバイスの概要</h2>
<a class="reference internal image-reference" href="../../../_images/lc4a_hardware_interfaces.png"><img alt="デバイスの正面図" class="align-center" src="/docs-assets/ja/_images/lc4a_hardware_interfaces.png" style="width: 652.8000000000001px; height: 373.6px;"></a>
<div style="text-align: center; font-weight: bold;">
The Hardware Interfaces of the device.
</div></div>
<hr class="docutils">
<div class="section" id="safety-instructions">
<h2>安全上の注意事項</h2>
<ul class="simple">
<li><p>動作中はデバイスを水や湿気にさらさないでください。</p></li>
<li><p>デバイスをいかなる熱源からも熱にさらさないでください。この製品は、工業用温度で信頼性の高い動作ができるように設計されています。</p></li>
</ul>
</div>
<div class="section" id="warnings">
<h2>警告</h2>
<ul class="simple">
<li><p>この製品は、定格 7 ～ 32DC、USB 電源、および最小電流供給 0.5 A の外部電源にのみ接続してください。</p></li>
<li><p>この製品で使用される外部電源は、使用目的の国に適用される関連規制および規格に準拠する必要があります。</p></li>
<li><p>製品内にはユーザーが修理できる部品はなく、ユニットを開けると製品が損傷し、保証が無効になる可能性があります。</p></li>
<li><p>この製品で使用されるすべての周辺機器のケーブルとコネクタは、関連する安全要件を満たす適切な絶縁を備えている必要があります。</p></li>
</ul>
</div>
<div class="section" id="order-information">
<h2>注文情報</h2>
<ul class="simple">
<li><p>品番: PP-LC4A/LR-LC4A</p></li>
<li><p>HS Code: 8517.69.9000</p></li>
<li><p>梱包: 紙箱、7 cm x 11 cm x 2.5 cm 0.09kg</p></li>
</ul>
</div>
</div>


           </div>
