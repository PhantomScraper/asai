---
title: "dwm_boot_cfg_set"
lang: ja
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-boot-cfg-set"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/api-commands/dwm-boot-cfg-set/"
order: 170
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-boot-cfg-set">
<span id="id1"></span><h1>dwm_boot_cfg_set</h1>
<p>この呼び出しは、イーサネット・ゲートウェイでのみ利用可能です。リセット後にデバイスがブートローダ・モードにとどまる時間を設定します。ブートローダ・モードは、シリアル・インタフェースを使用してファームウェア・アップデートを行うときに使用されます。時間経過後、モジュールは通常動作にジャンプします。ファームウェア・アップデートはジャンプの前に開始することができ、時間は0から4294967295ミリ秒まで設定できます。ただし、有効にするにはリセットする必要があります。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_boot_cfg_set">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_boot_cfg_set</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">パラメータ</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> -- boot_delay</p></li>
<li><p><strong>boot_delay</strong> -- 32ビット符号なし整数 (<em>ミリ秒単位の遅延時間</em>)</p></li>
<li><p><strong>output</strong> -- status_code</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>SPI/UART 例</strong></p>
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
<td><p>値 1000ミリ秒</p></td>
</tr>
<tr class="row-odd"><td><p>0x26</p></td>
<td><p>0x04</p></td>
<td><p>0xE8 0x03 0x00 0x00</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x26 (38 dec) は、コマンド <a class="reference internal" href="#dwm-boot-cfg-set"><span class="std std-ref">dwm_boot_cfg_set</span></a> を意味する</p>
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
<td><p>値</p></td>
</tr>
<tr class="row-odd"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x40 はステータスコード</p>
</div>


           </div>
