---
title: "dwm_pos_get"
lang: ja
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-pos-get"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/api-commands/dwm-pos-get/"
order: 220
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-pos-get">
<span id="id1"></span><h1>dwm_pos_get</h1>
<p>ノードの位置を取得します。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_pos_get">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_pos_get</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">dwm_pos_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">pos</span></span><span class="sig-paren">)</span><span class="p"><span class="pre">;</span></span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">パラメータ</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>output</strong> -- <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">ステータスコード</span></a>, <strong>位置</strong></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>Cコード例</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_pos_t</span><span class="w"> </span><span class="n">pos</span><span class="p">;</span>
<span class="n">dwm_pos_get</span><span class="p">(</span><span class="o">&amp;</span><span class="n">pos</span><span class="p">);</span>
<span class="n">printf</span><span class="p">(</span><span class="s">"%ld </span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">pos</span><span class="p">.</span><span class="n">x</span><span class="p">);</span>
<span class="n">printf</span><span class="p">(</span><span class="s">"%ld </span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">pos</span><span class="p">.</span><span class="n">y</span><span class="p">);</span>
<span class="n">printf</span><span class="p">(</span><span class="s">"%ld </span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">pos</span><span class="p">.</span><span class="n">z</span><span class="p">);</span>
<span class="n">printf</span><span class="p">(</span><span class="s">"%u </span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">pos</span><span class="p">.</span><span class="n">qf</span><span class="p">);</span>
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
<tr class="row-odd"><td><p>0x02</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>0x02 と入力すると、コマンド pos_get</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 5%">
<col style="width: 6%">
<col style="width: 19%">
<col style="width: 6%">
<col style="width: 7%">
<col style="width: 15%">
<col style="width: 0%">
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 0%">
<col style="width: 14%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="11"><p>TLV 応答</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td><p>値（エラーコードを参照）</p></td>
<td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td colspan="6"><p>値</p></td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>0x40</p></td>
<td rowspan="2"><p>0x01</p></td>
<td rowspan="2"><p>0x00</p></td>
<td rowspan="2"><p>0x41</p></td>
<td rowspan="2"><p>0x0D</p></td>
<td><p>リトルエンディアンの int32_t -</p>
<p>x 座標 (ミリメートル単位)</p>
</td>
<td colspan="2"><p>リトルエンディアンの int32_t -</p>
<p>y 座標 (ミリメートル単位)</p>
</td>
<td colspan="2"><p>リトルエンディアンの int32_t -</p>
<p>ミリメートル単位の Z 座標</p>
</td>
<td><p>uint8_t -</p>
<p>品質係数 (パーセント単位) (0 ～ 100)</p>
</td>
</tr>
<tr class="row-even"><td colspan="6"><p>0x4b 0x0a 0x00 0x00 0x1f 0x04</p>
<p>0x00 0x00 0x9c 0x0e 0x00</p>
<p>0x00 0x64</p>
</td>
</tr>
</tbody>
</table>
<p>タイプ 0x40 は、前のコマンドの <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">ステータスコード</span></a> を意味します</p>
<p>タイプ 0x41 は位置 (x,y,z,pqf) を意味します</p>
</div>


           </div>
