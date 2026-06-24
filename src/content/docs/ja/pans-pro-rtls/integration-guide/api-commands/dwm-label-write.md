---
title: "dwm_label_write"
lang: ja
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-label-write"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/api-commands/dwm-label-write/"
order: 196
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-label-write">
<span id="id1"></span><h1>dwm_label_write</h1>
<p>ラベルをノードに書き込みます。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_label_write">
<span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_label_write</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">uint8_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">label</span></span>, <span class="n"><span class="pre">uint8_t</span></span><span class="w"> </span><span class="n"><span class="pre">len</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">パラメータ</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> -- ラベル、長さ</p></li>
<li><p><strong>data</strong> -- 最大 16 バイト (<em>書き込まれるラベルのバイト数</em>)</p></li>
<li><p><strong>len</strong> -- 1 バイト (<em>ラベルの長さ、最大 16</em>)</p></li>
<li><p><strong>output</strong> -- <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">ステータスコード</span></a></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>Cコード例</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="kt">uint8_t</span><span class="w"> </span><span class="n">len</span><span class="p">,</span><span class="w"> </span><span class="n">label</span><span class="p">[</span><span class="n">DWM_LABEL_LEN_MAX</span><span class="p">];</span>
<span class="kt">int</span><span class="w"> </span><span class="n">rv</span><span class="p">;</span>
<span class="n">len</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">DWM_LABEL_LEN_MAX</span><span class="p">;</span>
<span class="n">rv</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">dwm_label_write</span><span class="p">(</span><span class="n">label</span><span class="p">,</span><span class="w"> </span><span class="n">len</span><span class="p">);</span>
<span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="w"> </span><span class="n">len</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="n">rv</span><span class="w"> </span><span class="p">)</span>
<span class="w"> </span><span class="n">printf</span><span class="p">(</span><span class="s">"ok</span><span class="se">\n</span><span class="s">"</span><span class="p">);</span>
<span class="k">else</span>
<span class="w"> </span><span class="n">printf</span><span class="p">(</span><span class="s">"error, %d"</span><span class="p">,</span><span class="w"> </span><span class="n">rv</span><span class="p">);</span>
</pre></div>
</div>
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
<td><p>値</p></td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>0x1D</p></td>
<td rowspan="2"><p>0x10</p></td>
<td><p>ラベル - 最大 16 バイト</p></td>
</tr>
<tr class="row-even"><td><p>0x01 0x02 0x03
…. 0x0F 0x10</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x1D はコマンド dwm_label_write を意味します</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
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
<td><p>値（エラーコードを参照）</p></td>
</tr>
<tr class="row-odd"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x40 はコマンドの <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">ステータスコード</span></a> を意味します</p>
</div>


           </div>
