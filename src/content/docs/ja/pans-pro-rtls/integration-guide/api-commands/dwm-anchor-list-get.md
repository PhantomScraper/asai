---
title: "dwm_anchor_list_get"
lang: ja
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-anchor-list-get"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/api-commands/dwm-anchor-list-get/"
order: 167
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-anchor-list-get">
<span id="id1"></span><h1>dwm_anchor_list_get</h1>
<p>周囲のアンカーのリストを読み込み、アンカーに対してのみ動作する。リスト内のアンカーは、同じネットワークのものでも、近隣のネットワークのものでもよい。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_anchor_list_get">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_anchor_list_get</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">dwm_anchor_list_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">list</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">パラメータ</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> -- (SPI/UART) '0' | '1'(<em>ページ番号（SPI/UARTのみ、ユーザーアプリケーションは1回の呼び出しでリスト全体を読み込む）、有効な番号は0,1</em>)</p></li>
<li><p><strong>input</strong> -- (ユーザーアプリケーション) (<em>なし</em>)</p></li>
<li><p><strong>output</strong> -- <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">ステータスコード</span></a>, cnt, {node_id, position, rssi, seat, neighbor_network}</p></li>
<li><p><strong>cnt</strong> -- 1バイト? (<em>要素数。SPI/UARTでは最大15、ユーザーアプリケーションでは最大30</em>)</p></li>
<li><p><strong>node_id</strong> -- 2バイト（<em>アンカーID</em>）</p></li>
<li><p><strong>position</strong> -- 12 バイト？</p></li>
<li><p><strong>rssi</strong> -- 1バイト符号付き？（<em>信号強度インジケーター</em>）</p></li>
<li><p><strong>seat</strong> -- 5ビット（<em>アンカーの座席番号</em>）</p></li>
<li><p><strong>neighbor_network</strong> -- 1ビット（<em>アンカーが現在のネットワークからのものか、近隣ネットワークからのものかを示すステータスフラグ</em>）</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>Cコード例</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_anchor_list_t</span><span class="w"> </span><span class="n">list</span><span class="p">;</span>
<span class="kt">int</span><span class="w"> </span><span class="n">i</span><span class="p">;</span>
<span class="n">dwm_anchor_list_get</span><span class="p">(</span><span class="o">&amp;</span><span class="n">list</span><span class="p">);</span>
<span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="n">i</span><span class="o">:</span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">list</span><span class="p">.</span><span class="n">cnt</span><span class="p">;</span><span class="w"> </span><span class="o">++</span><span class="n">i</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">     </span><span class="n">printf</span><span class="p">(</span><span class="s">"%d. id=0x%04X pos=[%ld,%ld,%ld] rssi=%d seat=%u neighbor=%d</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">i</span><span class="p">,</span>
<span class="w">                     </span><span class="n">list</span><span class="p">.</span><span class="n">v</span><span class="p">[</span><span class="n">i</span><span class="p">].</span><span class="n">node_id</span><span class="p">,</span>
<span class="w">                     </span><span class="n">list</span><span class="p">.</span><span class="n">v</span><span class="p">[</span><span class="n">i</span><span class="p">].</span><span class="n">x</span><span class="p">,</span>
<span class="w">                     </span><span class="n">list</span><span class="p">.</span><span class="n">v</span><span class="p">[</span><span class="n">i</span><span class="p">].</span><span class="n">y</span><span class="p">,</span>
<span class="w">                     </span><span class="n">list</span><span class="p">.</span><span class="n">v</span><span class="p">[</span><span class="n">i</span><span class="p">].</span><span class="n">z</span><span class="p">,</span>
<span class="w">                     </span><span class="n">list</span><span class="p">.</span><span class="n">v</span><span class="p">[</span><span class="n">i</span><span class="p">].</span><span class="n">rssi</span><span class="p">,</span>
<span class="w">                     </span><span class="n">list</span><span class="p">.</span><span class="n">v</span><span class="p">[</span><span class="n">i</span><span class="p">].</span><span class="n">seat</span><span class="p">,</span>
<span class="w">                     </span><span class="n">list</span><span class="p">.</span><span class="n">v</span><span class="p">[</span><span class="n">i</span><span class="p">].</span><span class="n">neighbor_network</span><span class="p">);</span>
<span class="p">}</span>
</pre></div>
</div>
<p><strong>SPI/UART 例 1</strong></p>
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
<tr class="row-odd"><td><p>0x0B</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x0B は、コマンド dwm_an_list_get を意味する</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 5%">
<col style="width: 5%">
<col style="width: 9%">
<col style="width: 5%">
<col style="width: 5%">
<col style="width: 9%">
<col style="width: 9%">
<col style="width: 11%">
<col style="width: 5%">
<col style="width: 19%">
<col style="width: 17%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="11"><p>TLV 応答</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="3"><p>タイプ</p></td>
<td rowspan="3"><p>長さ</p></td>
<td><p>値</p></td>
<td rowspan="3"><p>タイプ</p></td>
<td rowspan="3"><p>長さ</p></td>
<td colspan="6"><p>値</p></td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>uint8 - エラーコード</p></td>
<td rowspan="2"><p>uint8 - 符号化要素数</p></td>
<td rowspan="2"><p>uint16 - リトルエンディアンのUWBアドレス</p></td>
<td colspan="3"><p>アンカーnr.1</p></td>
<td><p>アンカーnr. 2 ... nr.15</p></td>
</tr>
<tr class="row-even"><td><p>3 x int32 - リトルエンディアンの位置座標 x, y, z</p></td>
<td><p>int8 -
RSSI</p></td>
<td><div class="line-block">
<div class="line">uint8 - フラッグ</div>
</div>
<div class="line-block">
<div class="line">(ビット 0-4) 座席番号</div>
<div class="line">(ビット5) 近隣ネットワーク</div>
<div class="line">(ビット 6-7) 予約</div>
</div>
</td>
<td><p>...</p></td>
</tr>
<tr class="row-odd"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x56</p></td>
<td><p>0xE1</p></td>
<td><p>0x0F</p></td>
<td colspan="4"><p>0xAB 0x1E ...</p></td>
<td><p>...</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">タイプ0x40は、直前のコマンドの <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">ステータスコード</span></a> を意味する</div>
<div class="line">タイプ0x56はアンカーリストを意味する</div>
</div>
<p><strong>SPI/UART 例 2</strong></p>
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
<tr class="row-odd"><td><p>0x0B</p></td>
<td><p>0x01</p></td>
<td><p>0x01</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x0B は、コマンド dwm_an_list_get を意味する</p>
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
<tr class="row-odd"><th class="head" colspan="6"><p>TLV 応答（アンカーリストは空です）</p></th>
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
<td rowspan="2"><p>0x56</p></td>
<td rowspan="2"><p>0x01</p></td>
<td><p>uint8 - 値にエンコードされている要素数</p></td>
</tr>
<tr class="row-even"><td><p>0x00</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">タイプ0x40は、直前のコマンドの <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">ステータスコード</span></a> を意味する</div>
<div class="line">タイプ0x56はアンカーリストを意味する</div>
</div>
</div>


           </div>
