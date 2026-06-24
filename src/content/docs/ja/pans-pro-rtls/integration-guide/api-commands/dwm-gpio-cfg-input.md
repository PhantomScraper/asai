---
title: "dwm_gpio_cfg_input"
lang: ja
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-gpio-cfg-input"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/api-commands/dwm-gpio-cfg-input/"
order: 185
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-gpio-cfg-input">
<span id="id1"></span><h1>dwm_gpio_cfg_input</h1>
<p>GPIO ピンを入力として設定します。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_gpio_cfg_input">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_gpio_cfg_input</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">uint8_t</span></span><span class="w"> </span><span class="n"><span class="pre">gpio_idx</span></span>, <span class="n"><span class="pre">uint8_t</span></span><span class="w"> </span><span class="n"><span class="pre">gpio_pull</span></span><span class="sig-paren">)</span><span class="p"><span class="pre">;</span></span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">パラメータ</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>gpio_idx</strong> -- 8 ビット整数 (許可される値については gpio_idx セクションを参照してください)</p></li>
<li><p><strong>gpio_pull</strong> -- 8 ビット整数 (0 プルなし、1 プルダウン、3 プルアップ)。</p></li>
<li><p><strong>output</strong> -- <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">ステータスコード</span></a>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>Cコード例</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_gpio_cfg_input</span><span class="p">(</span><span class="n">DWM_GPIO_IDX_13</span><span class="p">,</span><span class="w"> </span><span class="n">DWM_GPIO_PIN_PULLUP</span><span class="p">);</span>
<span class="n">dwm_gpio_cfg_input</span><span class="p">(</span><span class="n">DWM_GPIO_IDX_9</span><span class="p">,</span><span class="w"> </span><span class="n">DWM_GPIO_PIN_NOPULL</span><span class="p">);</span>
<span class="n">dwm_gpio_cfg_input</span><span class="p">(</span><span class="n">DWM_GPIO_IDX_31</span><span class="p">,</span><span class="w"> </span><span class="n">DWM_GPIO_PIN_PULLDOWN</span><span class="p">);</span>
</pre></div>
</div>
<p><strong>SPI/UART 例</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="4"><p>TLV 要求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td colspan="2"><p>値</p></td>
</tr>
<tr class="row-odd"><td></td>
<td></td>
<td><p>ピンインデックス</p></td>
<td><p>設定をプルします</p></td>
</tr>
<tr class="row-even"><td><p>0x29</p></td>
<td><p>0x02</p></td>
<td><p>0x0D</p></td>
<td><p>0x03</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x29 はコマンド dwm_gpio_cfg_input を意味します</p>
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
<p>タイプ0x40は、直前のコマンドの <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">ステータスコード</span></a> を意味する</p>
</div>


           </div>
