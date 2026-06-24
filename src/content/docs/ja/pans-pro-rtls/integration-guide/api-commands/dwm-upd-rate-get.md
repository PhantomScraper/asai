---
title: "dwm_upd_rate_get"
lang: ja
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-upd-rate-get"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/api-commands/dwm-upd-rate-get/"
order: 214
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-upd-rate-get">
<span id="id1"></span><h1>dwm_upd_rate_get</h1>
<p>位置の更新レートを取得します。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_upd_rate_get">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_upd_rate_get</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">uint16_t</span></span><span class="p"><span class="pre">*</span></span>, <span class="n"><span class="pre">uint16_t</span></span><span class="p"><span class="pre">*</span></span><span class="sig-paren">)</span><span class="p"><span class="pre">;</span></span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">パラメータ</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>output</strong> -- <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">ステータスコード</span></a>, update_rate, update_rate_stationary</p></li>
<li><p><strong>update_rate</strong> -- 16ビット整数（<em>100ミリ秒の倍数での位置公表レート、最大は1分、最小は100ミリ秒</em>)</p></li>
<li><p><strong>update_rate_stationary</strong> -- 16ビット整数（<em>ノードが100ミリ秒の倍数で移動していないときの位置公開レート、最大は1分、最小は100ミリ秒</em>）</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>Cコード例</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="kt">uint16_t</span><span class="w"> </span><span class="n">ur</span><span class="p">,</span><span class="w"> </span><span class="n">urs</span><span class="p">;</span>
<span class="n">dwm_upd_rate_get</span><span class="p">(</span><span class="o">&amp;</span><span class="n">ur</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">urs</span><span class="p">);</span>
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
<tr class="row-odd"><td><p>0x04</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x04 は、コマンド dwm_upd_rate_get を意味する</p>
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
<td><p>値（エラーコードを参照）</p></td>
<td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td><p>値</p></td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>0x40</p></td>
<td rowspan="2"><p>0x01</p></td>
<td rowspan="2"><p>0x00</p></td>
<td rowspan="2"><p>0x45</p></td>
<td rowspan="2"><p>0x04</p></td>
<td><p>最初の2バイトはリトルエンディアンで16ビット値を表し、100msの倍数で更新レートを表す（例えば、0x0A 0x00は1秒を意味する）。2番目の2バイトはリトルエンディアンで16ビット値を表し、100msの倍数で定常更新レートを表す（例えば、0x16 0x00は2.2秒を意味する）。</p></td>
</tr>
<tr class="row-even"><td><p>0x0A 0x00
0x16 0x00</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">タイプ 0x45 は、更新レート（通常、定常）を意味する</div>
<div class="line">タイプ0x40は、直前のコマンドの <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">ステータスコード</span></a> を意味する</div>
</div>
</div>


           </div>
