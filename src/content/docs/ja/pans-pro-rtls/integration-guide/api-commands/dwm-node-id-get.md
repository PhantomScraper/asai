---
title: "dwm_node_id_get"
lang: ja
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-node-id-get"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/api-commands/dwm-node-id-get/"
order: 201
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-node-id-get">
<span id="id1"></span><h1>dwm_node_id_get</h1>
<p>ノードの完全な UWB アドレスを取得します。アドレス/ID は固有の 64 ビット数値です。これは、固定プレフィックス 0xDECA、MCU 固有のチップ ID、および DW1000 固有のパーツ ID から次の形式で派生されます: 0xDECA + 28 ビット MCU 固有のチップ ID + 20 ビット DW1000 固有のパーツ ID。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_node_id_get">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_node_id_get</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">uint64_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">node_id</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">パラメータ</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> -- (<em>なし</em>)</p></li>
<li><p><strong>output</strong> -- <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">ステータスコード</span></a>, node_id</p></li>
<li><p><strong>node_id</strong> -- 64 ビット整数 (<em>UWB ノード アドレス/ID</em>)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>Cコード例</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="kt">uint64_t</span><span class="w"> </span><span class="n">node_id</span><span class="p">;</span>
<span class="n">dwm_node_id_get</span><span class="p">(</span><span class="o">&amp;</span><span class="n">node_id</span><span class="p">);</span>
<span class="n">printf</span><span class="p">(</span><span class="s">"node ID = 0x%llx </span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">node_id</span><span class="p">);</span>
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
<tr class="row-odd"><td><p>0x30</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>0x30 と入力すると、コマンド dwm_node_id_get を意味します</p>
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
<td rowspan="2"><p>0x4E</p></td>
<td rowspan="2"><p>0x08</p></td>
<td><p>リトルエンディアンで8バイト</p></td>
</tr>
<tr class="row-even"><td><p>0x99
0x0c
0x80
0x8d
0x63
0xef
0xca
0xde</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">タイプ0x40は、直前のコマンドの <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">ステータスコード</span></a> を意味する</div>
<div class="line">タイプ 0x4E はノード ID を表します。</div>
</div>
</div>


           </div>
