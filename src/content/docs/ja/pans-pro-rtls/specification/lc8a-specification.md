---
title: "LC8A 仕様"
lang: ja
slug: "pans-pro-rtls/specification/lc8a-specification"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/specification/lc8a-specification/"
order: 28
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="lc8a-specification">
<span id="id1"></span><h1>LC8A 仕様</h1>
<p>このドキュメントでは、LC8A デバイスの技術的な詳細について説明します。LC8A デバイスは、リアルタイム ロケーション システム (RTLS) 内でタグ ノード (TN) またはアンカー ノード (AN) として機能するように設計された多用途のハードウェア ソリューションです。その柔軟性と適応性により、さまざまな追跡および監視アプリケーションに最適です。</p>
<blockquote>
<div></div></blockquote>
<div class="sd-card sd-sphinx-override sd-mb-3 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<p class="sd-card-text"><a class="reference external" href="/_static/_pdfversion/lc8a-datasheet-ja.pdf">PDF バージョンの技術仕様</a> も参照してください。</p>
</div>
</div>
<a class="reference internal image-reference" href="../../../_images/lc8a_front_view.png"><img alt="デバイスの正面図" class="align-center" src="/docs-assets/ja/_images/lc8a_front_view.png" style="width: 151.79999999999998px; height: 235.2px;"></a>
<div style="text-align: center; font-weight: bold;">
The Front view of the device.
</div><hr class="docutils">
<div class="section" id="key-features">
<h2>主な機能</h2>
<ul class="simple">
<li><p>Qorvo の <a class="reference external" href="https://www.qorvo.com/products/p/DWM1001C">DWM1001C</a> 超広帯域 (UWB) モジュール (<a class="reference external" href="https://www.qorvo.com/products/p/DW1000">DW1000</a> 超広帯域 (UWB) トランシーバー IC および Nordic Semiconductor nRF52832) に基づいています:</p>
<ul>
<li><p>測距精度は +-20cm 以内です。</p></li>
<li><p>UWB チャネル 5 プリント PCB アンテナ (6.5 GHz)</p></li>
<li><p>6.8 Mbps データレート IEEE 802.15.4-2011 UWB 準拠</p></li>
<li><p>UWB および Bluetooth® アンテナとすべての RF 回路を統合します。</p></li>
<li><p>統合モーションセンサー: 3 軸加速度センサー。</p></li>
<li><p>低電力スリープモード向けに最適化された消費電流: &lt;15μA</p></li>
</ul>
</li>
<li><p>3 つの機能ボタン。</p></li>
<li><p>1 つの RGB メイン LED と 2 つの側面の緑色 LED</p></li>
<li><p>触覚フィードバック</p></li>
<li><p>アラーム機能のブザー</p></li>
<li><p>無料のソフトウェア構成および視覚化ツール (iOS、Android、Windows、macOS、および Linux プラットフォームのソフトウェア サポート)。</p></li>
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
<tr class="row-odd"><th class="head"><p>パラメータ</p></th>
<th class="head"><p>値</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>USB (電源とデータ)</p></td>
<td><p>5V @ 500mA最大</p></td>
</tr>
<tr class="row-odd"><td><p>バッテリー</p></td>
<td><p>3.7V @ 1Ah</p></td>
</tr>
<tr class="row-even"><td><p>動作温度 (なし)バッテリー）</p></td>
<td><p>-40°C - +85°C</p></td>
</tr>
<tr class="row-odd"><td><p>動作温度 (バッテリーあり)</p></td>
<td><p>-20°C - +45°C</p></td>
</tr>
<tr class="row-even"><td><p>動作温度 (充電時)</p></td>
<td><p>0°C ˜ +40°C</p></td>
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
<tr class="row-odd"><th class="head"><p>パラメータ</p></th>
<th class="head"><p>値</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>サイズ</p></td>
<td><p>90 x 70 x 10 mm</p></td>
</tr>
<tr class="row-odd"><td><p>重量</p></td>
<td><p>80g</p></td>
</tr>
<tr class="row-even"><td><p>色</p></td>
<td><p>白</p></td>
</tr>
<tr class="row-odd"><td><p>マウント中</p></td>
<td><p>バッジクリップ (オプション)</p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="device-overview">
<h2>デバイスの概要</h2>
<a class="reference internal image-reference" href="../../../_images/lc8a_hardware_interfaces.png"><img alt="デバイスの正面図" class="align-center" src="/docs-assets/ja/_images/lc8a_hardware_interfaces.png" style="width: 346.40000000000003px; height: 293.6px;"></a>
<div style="text-align: center; font-weight: bold;">
The Hardware Interfaces of the device.
</div></div>
<hr class="docutils">
<div class="section" id="safety-instructions">
<h2>安全上の注意事項</h2>
<ul class="simple">
<li><p>動作中はデバイスを水や湿気にさらさないでください。</p></li>
<li><p>デバイスをいかなる熱源からも熱にさらさないでください。この製品は、工業用温度 <cite>1</cite> で信頼性の高い動作ができるように設計されています。製品にバッテリーが装備されている場合、通常の動作温度‘2’ で使用できます。バッテリーの充電中の温度‘3’ は内部で保護されています (温度が範囲外の場合、バッテリーの充電は開始されないか、延期されます)。</p></li>
</ul>
</div>
<div class="section" id="warnings">
<h2>警告</h2>
<ul class="simple">
<li><p>この製品は、USB 電源と 0.5 A の最小電流供給にのみ接続する必要があります。</p></li>
<li><p>この製品で使用される外部電源は、使用目的の国に適用される関連規制および規格に準拠する必要があります。</p></li>
<li><p>この製品は、結露のない換気された環境で操作する必要があり、操作中にカバーを掛けないでください。</p></li>
<li><p>製品内にはユーザーが修理できる部品はなく、ユニットを開けると製品が損傷し、保証が無効になる可能性があります。</p></li>
<li><p>この製品で使用されるすべての周辺機器のケーブルとコネクタは、関連する安全要件を満たす適切な絶縁を備えている必要があります。</p></li>
</ul>
</div>
<div class="section" id="order-information">
<h2>注文情報</h2>
<ul class="simple">
<li><p>品番: PP-LC8A</p></li>
<li><p>HS Code: 8517.69.9000</p></li>
<li><p>梱包: 10個入り紙箱、17 cm x 11 cm x 12 cm 0.8kg</p></li>
</ul>
</div>
</div>


           </div>
