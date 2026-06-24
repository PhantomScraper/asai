---
title: "dwm_backhaul_xfer"
lang: ja
slug: "pans-pro-rtls/integration-guide/api-commands/dwm_backhaul_xfer"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/api-commands/dwm_backhaul_xfer/"
order: 222
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-backhaul-xfer">
<span id="id1"></span><h1>dwm_backhaul_xfer</h1>
<p>ダウンリンク データを書き込み、アップリンク データ チャンクを読み取ります。 DWM モジュールはゲートウェイとして設定する必要があります。アップリンク データとダウンリンク データは TLV フレームにエンコードされ、SPI インターフェイスによって説明されているように転送されます。SPI マスターは、<strong>downlink_byte_cnt</strong> によってスレーブに転送するダウンリンク バイト数を伝えます。<strong>downlink_byte_cnt</strong> は、最初の SPI 転送でスレーブによって読み取られます。スレーブは、ダウンリンクを読み取るときに、マスターに転送するアップリンク データを用意しています。マスターからスレーブへのダウンリンクとスレーブからマスターへのアップリンクの両方を転送するには、スレーブは必要なバイト数と SPI 転送数を計算する必要があります。マスターは、2 番目の SPI 転送でバイト数と転送数を読み取ります。最後に、転送が実行され、アップリンクとダウンリンクの両方が転送されます。現在サポートされている転送の最大数は 5 で、最大ペイロードは 253 バイト (255 - TLV ヘッダーのサイズ) です。 <a class="reference internal" href="#dwm-backhaul-xfer"><span class="std std-ref">dwm_backhaul_xfer</span></a> への 1 回の呼び出しで最大 5 つのアップリンク フレームと 2 つのダウンリンク フレームがサポートされます。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_backhaul_xfer">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_backhaul_xfer</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">uint16_t</span></span>, <span class="n"><span class="pre">uint8_t</span></span><span class="p"><span class="pre">*</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">パラメータ</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> -- downlink_byte_cnt, {downlink_chunk}</p></li>
<li><p><strong>downlink_byte_cnt</strong> -- 16 ビット符号なし整数 (<em>TLV を含まないダウンリンク データ バイト数)ヘッダー、最大 506 バイト</em>)</p></li>
<li><p><strong>downlink_chunk</strong> -- 最大 253 バイト (<em>不透明なデータはダウンリンクとしてスレーブに送信され、最大 2 チャンク</em>)</p></li>
<li><p><strong>output</strong> -- {uplink_chunk} (<em>アップリンク データの最大 5 チャンク</em>)</p></li>
<li><p><strong>uplink_chunk</strong> -- 最大 253 バイト (<em>不透明なデータはマスターへのアップリンクとして送信</em>)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>Cコード例</strong></p>
<p>ユーザー アプリケーションでは使用できません。</p>
<p><strong>UARTの例</strong></p>
<p>UART インターフェイスでは使用できません。</p>
<p><strong>ゲートウェイ以外の SPI の例</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV 要求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td><p>値</p></td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>0x37</p></td>
<td rowspan="2"><p>0x02</p></td>
<td><p>downlink_byte_cnt = ダウンリンク データのサイズ (244 バイト)</p></td>
</tr>
<tr class="row-even"><td><p>0xF4 0x00</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x37 はコマンド dwm_backhour_xfer を意味します</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV 応答</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td><p>値（エラーコードを参照）</p></td>
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
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV 要求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td><p>値</p></td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>0x37</p></td>
<td rowspan="2"><p>0x02</p></td>
<td><p>downlink_byte_cnt = ダウンリンク データのサイズ (244 バイト)</p></td>
</tr>
<tr class="row-even"><td><p>0xF4 0x00</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">タイプ 0x37 はコマンド dwm_backhour_xfer を意味します</div>
</div>
<p>この呼び出しには、TLV リクエストに続く可変数の連続転送があります。 API over SPI インターフェイスの説明を参照してください。</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p><strong>TLVダウンリンク番号1,2,3,4,5</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ <strong>(244 バイト)</strong></p></td>
<td><p>値</p></td>
</tr>
<tr class="row-odd"><td><p>0x64</p></td>
<td><p>0xF4 (244)</p></td>
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
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p><strong>TLV アップリンク番号 1,2,3,4,5</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ <strong>(980 バイト)</strong></p></td>
<td><p>値</p></td>
</tr>
<tr class="row-odd"><td><p>0x6E</p></td>
<td><p>0xFD (253)</p></td>
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
<td><p>0xDD (22#.</p></td>
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


           </div>
