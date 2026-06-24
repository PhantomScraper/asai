---
title: "dwm_alarm_start"
lang: ja
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-alarm-start"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/api-commands/dwm-alarm-start/"
order: 166
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-alarm-start">
<span id="id1"></span><h1>dwm_alarm_start</h1>
<p>指定された期間、ボード アラームをアクティブにします。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_alarm_start">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_alarm_start</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">dwm_alarm_start_t</span></span><span class="p"><span class="pre">*</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">パラメータ</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> -- led_0、led_1、led_2、モーター、ブザー、時間、強度</p></li>
<li><p><strong>input</strong> -- led_0、led_1、led_2、モーター、ブザー:​​ ‘0’ | ‘1’ (<em>1 は特定のアラームを有効にします</em>)</p></li>
<li><p><strong>duration</strong> -- 8 ビット符号なし整数 (200 ミリ秒の倍数のアラーム期間)</p></li>
<li><p><strong>intensity</strong> -- 8 ビット符号なし整数 (<em>アラーム強度</em>)</p></li>
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
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 50%">
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
<tr class="row-odd"><td rowspan="2"><p>0x85</p></td>
<td rowspan="2"><p>0x04</p></td>
<td><ul class="simple">
<li><p>バイト 0: アラーム設定:</p>
<ul>
<li><p>ビット 0 - LED 0 を有効にする、</p></li>
<li><p>ビット1 - LED1 を有効にし、</p></li>
<li><p>ビット 2 - LED 2 を有効にする、</p></li>
<li><p>ビット 3 - ブザーを有効にする、</p></li>
<li><p>ビット 4 - モーターを有効にする</p></li>
</ul>
</li>
<li><p>バイト 1: 予約済み</p></li>
<li><p>バイト 2: 100 ミリ秒の倍数の継続時間</p></li>
<li><p>バイト 3: 強​​度</p></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p>0x19 0x00 0x05 0xff</p></td>
</tr>
</tbody>
</table>
<p>0x85 と入力すると、コマンド <a class="reference internal" href="#dwm-alarm-start"><span class="std std-ref">dwm_alarm_start</span></a> を意味します</p>
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
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">タイプ0x40は、直前のコマンドの <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">ステータスコード</span></a> を意味する</div>
</div>
</div>


           </div>
