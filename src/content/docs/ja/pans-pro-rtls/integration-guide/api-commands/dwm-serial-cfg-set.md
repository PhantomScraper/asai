---
title: "dwm_serial_cfg_set"
lang: ja
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-serial-cfg-set"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/api-commands/dwm-serial-cfg-set/"
order: 209
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-serial-cfg-set">
<span id="id1"></span><h1>dwm_serial_cfg_set</h1>
<p>このコマンドは、イーサネット ゲートウェイでのみ使用できます。 UART/USBなどのシリアルインターフェースの設定を行います。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_serial_cfg_set">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_serial_cfg_set</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">uint8_t</span></span><span class="w"> </span><span class="n"><span class="pre">mode</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">パラメータ</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> -- モード</p></li>
<li><p><strong>mode</strong> -- '0' | '1' (<em>0 - バイナリーモード , 1 - シェルモード</em>)</p></li>
<li><p><strong>output</strong> -- <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">ステータスコード</span></a></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>Cコード例</strong></p>
<p>モジュール上のユーザーアプリケーションでは利用できません。</p>
<p><strong>SPI/UART 例</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 29%">
<col style="width: 16%">
<col style="width: 55%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV 応答</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td><p>値</p></td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>0x38</p></td>
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
<div class="line">タイプ 0x38 はコマンド dwm_serial_cfg_set を意味します</div>
</div>
</div>


           </div>
