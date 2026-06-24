---
title: "dwm_cfg_get"
lang: ja
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-cfg-get"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/api-commands/dwm-cfg-get/"
order: 174
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-cfg-get">
<span id="id1"></span><h1>dwm_cfg_get</h1>
<p>ノードの現在の構成オプションを取得します。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_cfg_get">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_cfg_get</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">dwm_cfg_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">cfg</span></span><span class="sig-paren">)</span><span class="p"><span class="pre">;</span></span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">パラメータ</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>output:</strong> -- <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">ステータスコード</span></a>, mode, initiator, gateway, low_power_en, meas_mode, loc_engine_en, led_en, ble_en, uwb_mode, fw_update_en, enc_en,</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<div class="admonition note">
<p class="admonition-title">注釈</p>
<p>ファームウェアが UWB ルーティング バックホールでコンパイルされている場合にのみ使用可能: cfg.uwb_bh_routing</p>
</div>
<p><strong>Cコード例</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_cfg_t</span><span class="w"> </span><span class="n">cfg</span><span class="p">;</span>
<span class="n">dwm_cfg_get</span><span class="p">(</span><span class="o">&amp;</span><span class="n">cfg</span><span class="p">);</span>
<span class="n">printf</span><span class="p">(</span><span class="s">"mode %u </span><span class="se">\n</span><span class="s">”, cfg.mode);</span>
<span class="n">printf</span><span class="p">(</span><span class="s">"initiator %u </span><span class="se">\n</span><span class="s">”, cfg.initiator);</span>
<span class="n">printf</span><span class="p">(</span><span class="s">"gateway %u </span><span class="se">\n</span><span class="s">”, cfg.gateway);</span>
<span class="cm">/*[Available only when the firmware is compiled with UWB routing backhaul:* **printf("UWB mode %u \n”, cfg.uwb_bh_routing); */</span>
<span class="n">printf</span><span class="p">(</span><span class="s">"motion detection enabled %u </span><span class="se">\n</span><span class="s">”, cfg.stnry_en);</span>
<span class="n">printf</span><span class="p">(</span><span class="s">"measurement mode %u </span><span class="se">\n</span><span class="s">”, cfg.meas_mode);</span>
<span class="n">printf</span><span class="p">(</span><span class="s">"low-power enabled %u </span><span class="se">\n</span><span class="s">”, cfg.low_power_en);</span>
<span class="n">printf</span><span class="p">(</span><span class="s">"internal location engine enabled %u </span><span class="se">\n</span><span class="s">”, cfg.loc_engine_en);</span>
<span class="n">printf</span><span class="p">(</span><span class="s">"encryption enabled %u </span><span class="se">\n</span><span class="s">”, cfg.common.enc_en);</span>
<span class="n">printf</span><span class="p">(</span><span class="s">"LED enabled %u </span><span class="se">\n</span><span class="s">”, cfg.common.led_en);</span>
<span class="n">printf</span><span class="p">(</span><span class="s">"BLE enabled %u </span><span class="se">\n</span><span class="s">”, cfg.common.ble_en);</span>
<span class="n">printf</span><span class="p">(</span><span class="s">"firmware update enabled %u </span><span class="se">\n</span><span class="s">”, cfg.common.fw_update_en);</span>
<span class="n">printf</span><span class="p">(</span><span class="s">"UWB mode %u </span><span class="se">\n</span><span class="s">”, cfg.common.uwb_mode);</span>
</pre></div>
</div>
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
<tr class="row-odd"><td><p>0x08</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x08 はコマンド <a class="reference internal" href="#dwm-cfg-get"><span class="std std-ref">dwm_cfg_get</span></a> を意味します</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 9%">
<col style="width: 9%">
<col style="width: 9%">
<col style="width: 9%">
<col style="width: 9%">
<col style="width: 55%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="6"><p>TLV 応答</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td><p>値（エラーコードを参照）</p></td>
<td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td><p>値</p></td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>0x40</p></td>
<td rowspan="2"><p>0x01</p></td>
<td rowspan="2"><p>0x00</p></td>
<td rowspan="2"><p>0x46</p></td>
<td rowspan="2"><p>0x02</p></td>
<td><p><em>BYTE 1:</em> ファームウェアが UWB ルーティング バックホールでコンパイルされている場合にのみ使用可能: (ビット 6 ～ 7) uwb_bh_routing : 0 - オフ、1 - オン、2 -オート</p>
<ul class="simple">
<li><p>ビット 0 ～ 1: meas_mode: 0 ～ TWR、1 ～ 3 はサポートされていません</p></li>
<li><p>ビット2:stnry_en</p></li>
<li><p>bit 3: ゲートウェイ</p></li>
<li><p>bit 4: イニシエーター</p></li>
<li><p>bit 5: mode : 0 - タグ、1 -アンカー</p></li>
</ul>
<p><em>BYTE 0</em></p>
<ul class="simple">
<li><p>bits 0-1: uwb_mode</p></li>
<li><p>ビット2: fw_update_en</p></li>
<li><p>ビット3: ble_en</p></li>
<li><p>ビット4: led_en</p></li>
<li><p>ビット5: enc_en</p></li>
<li><p>ビット6: loc_engine_en</p></li>
<li><p>ビット7: low_power_en</p></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p>0x1C 0x20 (アンカー、LED、ble、fwup、uwb モードオフ)</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">タイプ0x40は、直前のコマンドの <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">ステータスコード</span></a> を意味する</div>
<div class="line">タイプ 0x46 はノード構成を意味します</div>
</div>
</div>


           </div>
