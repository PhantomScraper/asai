---
title: "dwm_serial_cfg_get"
lang: ja
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-serial-cfg-get"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/api-commands/dwm-serial-cfg-get/"
order: 208
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-serial-cfg-get">
<span id="id1"></span><h1>dwm_serial_cfg_get</h1>
<p>このコマンドはイーサネットゲートウェイでのみ使用可能です。UART/USB インターフェースの設定を取得します。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_serial_cfg_get">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_serial_cfg_get</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">uint8_t</span></span><span class="w"> </span><span class="n"><span class="pre">mode</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">パラメータ</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> -- (<em>なし</em>)</p></li>
<li><p><strong>output</strong> -- status_code, mode</p></li>
<li><p><strong>mode</strong> -- '0' | '1' (<em>0 - バイナリーモード , 1 - シェルモード</em>)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>Cコード例</strong></p>
<p>モジュール上のユーザーアプリケーションでは利用できません。</p>
<p><strong>SPI/UART 例</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 50%">
<col style="width: 50%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="2"><p>TLV 要求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
</tr>
<tr class="row-odd"><td><p>0x39</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x39 (57) は、コマンド dwm_serial_cfg_get を意味する</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 20%">
<col style="width: 11%">
<col style="width: 10%">
<col style="width: 9%">
<col style="width: 11%">
<col style="width: 39%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="6"><p>TLV 応答</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td><p>値</p></td>
<td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td><p>値</p></td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>0x40</p></td>
<td rowspan="2"><p>0x01</p></td>
<td rowspan="2"><p>0x00</p></td>
<td rowspan="2"><p>0x61</p></td>
<td rowspan="2"><p>0x04</p></td>
<td><div class="line-block">
<div class="line">バイト 0:予約済み</div>
<div class="line">バイト1: UART/USB モード</div>
<div class="line">バイト2:予約</div>
<div class="line">バイト 3: 予約</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x00 0x10 0x00 0x00</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">タイプ 0x40 はステータスコード</div>
<div class="line">タイプ 0x61 (97) はシリアル設定を意味します</div>
</div>
</div>


           </div>
