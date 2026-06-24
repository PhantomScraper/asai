---
title: "dwm_pos_set"
lang: ja
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-pos-set"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/api-commands/dwm-pos-set/"
order: 206
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-pos-set">
<span id="id1"></span><h1>dwm_pos_set</h1>
<p>ノードのデフォルト位置を設定する。デフォルトの位置はタグモードでは使用されないが、いずれにせよ保存される。これにより、モジュールをアンカー・モードで設定し、以前に dwm_pos_set で設定した値を使用することができる。通常、この呼び出しは新しい値を設定するときに内部フラッシュに書き込む。したがって、頻繁に使うべきでない。レスポンスは最悪の場合数百ミリ秒かかる！</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_pos_set">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_pos_set</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">dwm_pos_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">pos</span></span><span class="sig-paren">)</span><span class="p"><span class="pre">;</span></span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">パラメータ</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>pos-&gt;x</strong> -- 32ビット整数（ミリメートル単位の位置座標）</p></li>
<li><p><strong>pos-&gt;y</strong> -- 32ビット整数（ミリメートル単位の位置座標）</p></li>
<li><p><strong>pos-&gt;z</strong> -- 32ビット整数（ミリメートル単位の位置座標）</p></li>
<li><p><strong>output</strong> -- <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">ステータスコード</span></a></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C コード例 1</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_pos_t</span><span class="w"> </span><span class="n">pos</span><span class="p">;</span>
<span class="n">pos</span><span class="p">.</span><span class="n">qf</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">100</span><span class="p">;</span>
<span class="n">pos</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">121</span><span class="p">;</span>
<span class="n">pos</span><span class="p">.</span><span class="n">y</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">50</span><span class="p">;</span>
<span class="n">pos</span><span class="p">.</span><span class="n">z</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">251</span><span class="p">;</span>
<span class="n">dwm_pos_set</span><span class="p">(</span><span class="o">&amp;</span><span class="n">pos</span><span class="p">);</span>
</pre></div>
</div>
<p><strong>SPI/UART 例 1</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 13%">
<col style="width: 13%">
<col style="width: 19%">
<col style="width: 19%">
<col style="width: 19%">
<col style="width: 18%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="6"><p>TLV 要求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td><p>値</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>0x01</p></td>
<td><p>0x0D</p></td>
<td><p>int32_tリトルエンディアン - x 座標ミリメートル単位</p></td>
<td><p>int32_tリトルエンディアン - y 座標ミリメートル単位</p></td>
<td><p>int32_tリトルエンディアン – ｚ 座標ミリメートル単位</p></td>
<td><p>uint8_t -</p>
<p>パーセント単位の品質係数 (0-100)</p>
</td>
</tr>
<tr class="row-even"><td></td>
<td></td>
<td colspan="4"><p>0x4b
0x0a
0x00
0x00
0x1f
0x04
0x00
0x00
0x9c
0x0e
0x00
0x00
0x64</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x01 はコマンド dwm_pos_set を意味します</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 31%">
<col style="width: 31%">
<col style="width: 39%">
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
<p>** Cコード例2**</p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="kt">int32_t</span><span class="w"> </span><span class="n">x</span><span class="p">,</span><span class="n">z</span><span class="p">;</span>
<span class="n">x</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">121</span><span class="p">;</span>
<span class="n">z</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">251</span><span class="p">;</span>
<span class="n">dwm_pos_set_xyz</span><span class="p">(</span><span class="o">&amp;</span><span class="n">x</span><span class="p">,</span><span class="w"> </span><span class="nb">NULL</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">z</span><span class="p">);</span>
</pre></div>
</div>
<p><strong>SPI/UART 例 2</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 20%">
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 20%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="8"><p>TLV 要求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td><p>値</p></td>
<td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td><p>値</p></td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>0x80</p></td>
<td rowspan="2"><p>0x0C</p></td>
<td rowspan="2"><p>0x42</p></td>
<td rowspan="2"><p>0x04</p></td>
<td><p>int32_tリトルエンディアン - x 座標ミリメートル単位</p></td>
<td rowspan="2"><p>0x44</p></td>
<td rowspan="2"><p>0x04</p></td>
<td><p>int32_tリトルエンディアン – ｚ 座標ミリメートル単位</p></td>
</tr>
<tr class="row-even"><td><p>0x4b
0x0a
0x00
0x00
0x1f
0x04
0x00
0x00</p></td>
<td><p>0x9c
0x0e
0x00
0x00
0x00
0x64
0x00
0x00</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">タイプ 0x80 は、コマンド dwm_pos_set_xyz を意味する</div>
<div class="line">タイプ0x42は位置座標xを意味する</div>
<div class="line">タイプ0x44は位置座標zを意味します</div>
</div>
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
</div>


           </div>
