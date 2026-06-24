---
title: "leaps_bh_xfer"
lang: ja
slug: "leaps-rtls/integration-guide/leaps-api/leaps-bh-xfer"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/leaps-api/leaps-bh-xfer/"
order: 148
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-bh-xfer">
<span id="id1"></span><h1>leaps_bh_xfer</h1>
<p>ダウンリンク データを書き込み、アップリンク データ チャンクを読み取ります。モジュールはゲートウェイ ノードとして設定する必要があります。</p>
<p><a class="reference external" href="#example-interrupt-leaps_bh_xfer">SPI を介した複数の TVL</a> で説明されているように、SPI インターフェイスによって転送されるとき、アップリンク データとダウンリンク データの両方が tlv フレームにエンコードされます。</p>
<p>SPI マスターは、<strong>downlink_byte_cnt</strong> によって転送したいダウンリンク バイト数をスレーブに伝えます。 <strong>downlink_byte_cnt</strong> は、最初の SPI 転送でスレーブによって読み取られます。スレーブには、ダウンリンクを読み取っているときにマスターに転送したいアップリンク データが準備されています。マスターからスレーブへのダウンリンクとスレーブからマスターへのアップリンクの両方を転送するには、スレーブは必要なバイト数と SPI 転送の数を計算する必要があります。マスターは、<a class="reference external" href="#example-interrupt-leaps_bh_xfer">SPI 経由の複数の TVL</a> で説明されているように、2 番目の SPI 転送でバイト数と転送数を読み取ります。最後に、転送が実行され、アップリンクとダウンリンクが転送されます。現在サポートされている転送の最大数は 5 で、最大ペイロードは 253 バイト (255 - (TLV ヘッダー) のサイズ) です。leaps_bh_xfer への 1 回の呼び出しで、最大 5 つのアップリンク フレームと最大 2 つのダウンリンク フレームがサポートされます。</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
入力</div>
<ul class="simple">
<li><p class="sd-card-text">downlink_byte_cnt: 16 ビット符号なし整数 (<em>TLV ヘッダーのないダウンリンク データ バイト数、最大 506 バイト</em>)</p></li>
</ul>
</div>
</div>
</div>
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
出力</div>
<ul class="simple">
<li><p class="sd-card-text">downlink_chunk: 最大 253 バイト (<em>スレーブへのダウンリンクとして送信される不透明なデータ</em>)</p></li>
<li><p class="sd-card-text">出力: 5 <em>[uplink_chunk]</em></p></li>
<li><p class="sd-card-text">uplink_chunk: 最大 253 バイト (<em>不透明なデータはマスターへのアップリンクとして送信</em>)</p></li>
</ul>
</div>
</div>
</div>
</div>
</div>
<hr class="docutils">
<p><strong>UARTの例</strong></p>
<p>UART インターフェイスでは使用できません。</p>
<p><strong>ゲートウェイ以外の SPI の例</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 15%">
<col style="width: 13%">
<col style="width: 72%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV 要求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td><p>値</p>
<p>downlink_byte_cnt = ダウンリンク データのサイズ (244 バイト)</p>
</td>
</tr>
<tr class="row-odd"><td><p>0x37</p></td>
<td><p>0x02</p></td>
<td><p>0xF4 0x00</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">0x37 と入力すると、コマンド Leaps_bh_xfer を意味します</div>
</div>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 34%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>TLV 応答</p></th>
<th class="head"></th>
<th class="head"></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td><p>値</p></td>
</tr>
<tr class="row-odd"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x02</p></td>
</tr>
</tbody>
</table>
<p><strong>SPI ゲートウェイの例</strong></p>
<div class="line-block">
<div class="line">ダウンリンクのバイト数: 244</div>
<div class="line">アップリンクバイト数: 980</div>
</div>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 15%">
<col style="width: 13%">
<col style="width: 72%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV リクエスト</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td><p>値 downlink_byte_cnt = ダウンリンク データのサイズ (244 バイト)</p></td>
</tr>
<tr class="row-odd"><td><p>0x37</p></td>
<td><p>0x02</p></td>
<td><p>0xF4 0x00</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">0x37 と入力すると、コマンド Leaps_bh_xfer を意味します</div>
</div>
<p>この呼び出しには、TLV リクエストに続く可変数の連続転送があります。<a class="reference external" href="#example-interrupt-leaps_bh_xfer">API over SPI インターフェイスの説明</a> を参照してください。</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 48%">
<col style="width: 15%">
<col style="width: 37%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV ダウンリンク nr.1、2、3、4、5</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ (244 バイト)</p></td>
<td><p>値</p></td>
</tr>
<tr class="row-odd"><td><p>0x64</p></td>
<td><p>0xF4
(244)</p></td>
<td><p>ダウンリンク データ チャンク nr.1</p></td>
</tr>
<tr class="row-even"><td><p>0x65</p></td>
<td><p>0x00</p></td>
<td><p>空</p></td>
</tr>
<tr class="row-odd"><td><p>0x66</p></td>
<td><p>0x00</p></td>
<td><p>空</p></td>
</tr>
<tr class="row-even"><td><p>0x67</p></td>
<td><p>0x00</p></td>
<td><p>空</p></td>
</tr>
<tr class="row-odd"><td><p>0x68</p></td>
<td><p>0x00</p></td>
<td><p>空</p></td>
</tr>
</tbody>
</table>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 48%">
<col style="width: 15%">
<col style="width: 37%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV アップリンク番号 1、2、3、4、5</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ (980 バイト)</p></td>
<td><p>値</p></td>
</tr>
<tr class="row-odd"><td><p>0x6E</p></td>
<td><p>0xFD
(253)</p></td>
<td><p>アップリンク データ チャンク nr.1</p></td>
</tr>
<tr class="row-even"><td><p>0x6F</p></td>
<td><p>0xFD</p></td>
<td><p>アップリンク データ チャンク nr.2</p></td>
</tr>
<tr class="row-odd"><td><p>0x70</p></td>
<td><p>0xFD</p></td>
<td><p>アップリンク データ チャンク nr.3</p></td>
</tr>
<tr class="row-even"><td><p>0x71</p></td>
<td><p>0xDD
(221)</p></td>
<td><p>アップリンクデータチャンク番号4</p></td>
</tr>
<tr class="row-odd"><td><p>0x72</p></td>
<td><p>0x00</p></td>
<td><p>空</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">タイプ 0x64 は、ダウンリンク データ チャンク nr.1 を意味します。</div>
<div class="line">タイプ 0x65 は、ダウンリンク データ チャンク nr.2 を意味します。</div>
<div class="line">...</div>
<div class="line">タイプ 0x68 は、ダウンリンク データ チャンク nr.5 を意味します。</div>
<div class="line">タイプ 0x6E はアップリンク データ チャンク nr.1 を意味します。</div>
<div class="line">タイプ 0x6F はアップリンク データ チャンク nr.2 を意味します。</div>
<div class="line">...</div>
<div class="line">タイプ 0x72 はアップリンク データ チャンク nr.5 を意味します。</div>
</div>
</div>
<div class="section" id="bh-transfer-over-usb">
<h1>USB 経由の BH 転送</h1>
<p>USB 経由の BH データ転送は SPI 経由の転送とは異なります。SPI データ転送は割り込みに基づいていますが、LEAPS RTLS デバイスと PC 間の USB 接続では割り込み ラインを使用できないため、USB インターフェイスでは、TLV_TYPE_CMD_BH_XFER TLV コマンドを使用した要求応答アプローチを使用する代わりに、LEAPS RTLS デバイスは通知 (TLV_TYPE_NOTIF_STATUS、TLV_TYPE_NOTIF_BH_STATUS) とアップリンク データ チャンクをゲートウェイ マスター (PC) にアクティブに送信します。通知とアップリンク データは、<a class="reference external" href="#leaps_int_cfg_set">leaps_int_cfg_set</a> を使用した割り込みと同様に、有効/無効にすることができます。</p>
</div>


           </div>
