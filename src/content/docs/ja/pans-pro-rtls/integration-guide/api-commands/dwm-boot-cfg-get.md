---
title: "dwm_boot_cfg_get"
lang: ja
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-boot-cfg-get"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/api-commands/dwm-boot-cfg-get/"
order: 169
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-boot-cfg-get">
<span id="id1"></span><h1>dwm_boot_cfg_get</h1>
<p>この呼び出しはイーサネット ゲートウェイでのみ使用できます。ブートローダー構成を取得します。詳細については、<a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/api-commands/dwm-boot-cfg-set#dwm-boot-cfg-set"><span class="std std-ref">dwm_boot_cfg_set</span></a> を参照してください。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_boot_cfg_get">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_boot_cfg_get</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">dwm_mac_addr_list_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">mac_addr_list</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">パラメータ</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> -- (<em>なし</em>)</p></li>
<li><p><strong>output</strong> -- status_code, boot_delay</p></li>
<li><p><strong>boot_delay</strong> -- 32ビット符号なし整数 (<em>ミリ秒単位の遅延時間</em>)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

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
<tr class="row-odd"><td><p>0x27</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x27 (39) はコマンド <a class="reference internal" href="#dwm-boot-cfg-get"><span class="std std-ref">dwm_boot_cfg_get</span></a> を意味します</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 17%">
<col style="width: 17%">
<col style="width: 17%">
<col style="width: 17%">
<col style="width: 17%">
<col style="width: 17%">
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
<td rowspan="2"><p>0x60</p></td>
<td rowspan="2"><p>0x04</p></td>
<td><p>ミリ秒単位の起動遅延</p></td>
</tr>
<tr class="row-even"><td><p>0xB8 0x0B
0x00 0x00</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">タイプ 0x40 はステータスコード</div>
<div class="line">タイプ 0x60 (96) はブートローダー構成を意味します</div>
</div>
</div>


           </div>
