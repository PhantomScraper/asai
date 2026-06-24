---
title: "dwm_loc_get"
lang: ja
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-loc-get"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/api-commands/dwm-loc-get/"
order: 197
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-loc-get">
<span id="id1"></span><h1>dwm_loc_get</h1>
<p>測距アンカーまでの最新の距離を取得し、位置を取得します。イベントが生成され、すべてのTWR測定が完了するとステータスが変更され、新しい位置データがユーザーに提供されます。低電力モードを使用している場合も、同様に動作します。</p>
<p>アンカー ノードの場合、位置と距離は、自動位置決め手順が完了している場合にのみ使用できます。自動位置決め手順は、BLE インターフェイス経由で実行されます。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_loc_get">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_loc_get</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">dwm_loc_data_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">loc</span></span><span class="sig-paren">)</span><span class="p"><span class="pre">;</span></span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">パラメータ</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>output</strong> -- <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">ステータスコード</span></a>, [position], [cnt, {an_pos, addr, distance, pqf}]</p></li>
<li><p><strong>cnt</strong> -- 0,1,2,3,4 (<em>アンカーまでの距離</em>)</p></li>
<li><p><strong>an_pos</strong> -- 位置 (<em>距離に対応するアンカーの位置</em>)</p></li>
<li><p><strong>addr</strong> -- 16 ビット整数 (<em>特定のアンカーの UWB アドレス/ID</em>)</p></li>
<li><p><strong>distance</strong> -- 32 ビット整数 (<em>特定のアンカーまでの距離 (ミリメートル)</em>)</p></li>
<li><p><strong>pqf</strong> -- 8 ビット整数 (<em>品質係数</em>)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<div class="admonition note">
<p class="admonition-title">注釈</p>
<p>パラメータ <strong>an_pos</strong> は <strong>タグ ノード</strong> にのみ適用されます</p>
</div>
<p><strong>Cコード例</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_loc_data_t</span><span class="w"> </span><span class="n">loc</span><span class="p">;</span>
<span class="kt">int</span><span class="w"> </span><span class="n">rv</span><span class="p">,</span><span class="w"> </span><span class="n">i</span><span class="p">;</span>
<span class="cm">/* if pos_available is false, position data are not read, and the function returns without error */</span>
<span class="nl">rv</span><span class="p">:</span><span class="w"> </span><span class="n">dwm_loc_get</span><span class="p">(</span><span class="o">&amp;</span><span class="n">loc</span><span class="p">);</span>

<span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="mi">0</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="n">rv</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">loc</span><span class="p">.</span><span class="n">pos_available</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">             </span><span class="n">printf</span><span class="p">(</span><span class="s">"[%ld,%ld,%ld,%u] "</span><span class="p">,</span><span class="w"> </span><span class="n">loc</span><span class="p">.</span><span class="n">pos</span><span class="p">.</span><span class="n">x</span><span class="p">,</span><span class="w"> </span><span class="n">loc</span><span class="p">.</span><span class="n">pos</span><span class="p">.</span><span class="n">y</span><span class="p">,</span><span class="w"> </span><span class="n">loc</span><span class="p">.</span><span class="n">pos</span><span class="p">.</span><span class="n">z</span><span class="p">,</span>
<span class="w">                     </span><span class="n">loc</span><span class="p">.</span><span class="n">pos</span><span class="p">.</span><span class="n">qf</span><span class="p">);</span>
<span class="p">}</span>
<span class="w">     </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="n">i</span><span class="o">:</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">loc</span><span class="p">.</span><span class="n">anchors</span><span class="p">.</span><span class="n">dist</span><span class="p">.</span><span class="n">cnt</span><span class="p">;</span><span class="w"> </span><span class="o">++</span><span class="n">i</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">             </span><span class="n">printf</span><span class="p">(</span><span class="s">"%u)"</span><span class="p">,</span><span class="w"> </span><span class="n">i</span><span class="p">);</span>
<span class="w">             </span><span class="n">printf</span><span class="p">(</span><span class="s">"0x%04x"</span><span class="p">,</span><span class="w"> </span><span class="n">loc</span><span class="p">.</span><span class="n">anchors</span><span class="p">.</span><span class="n">dist</span><span class="p">.</span><span class="n">addr</span><span class="p">[</span><span class="n">i</span><span class="p">]);</span>
<span class="w">             </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">loc</span><span class="p">.</span><span class="n">anchors</span><span class="p">.</span><span class="n">an_pos</span><span class="p">.</span><span class="n">cnt</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="n">printf</span><span class="p">(</span><span class="s">"[%ld,%ld,%ld,%u]"</span><span class="p">,</span><span class="w"> </span><span class="n">loc</span><span class="p">.</span><span class="n">anchors</span><span class="p">.</span><span class="n">an_pos</span><span class="p">.</span><span class="n">pos</span><span class="p">[</span><span class="n">i</span><span class="p">].</span><span class="n">x</span><span class="p">,</span>
<span class="w">                                     </span><span class="n">loc</span><span class="p">.</span><span class="n">anchors</span><span class="p">.</span><span class="n">an_pos</span><span class="p">.</span><span class="n">pos</span><span class="p">[</span><span class="n">i</span><span class="p">].</span><span class="n">y</span><span class="p">,</span>
<span class="w">                                     </span><span class="n">loc</span><span class="p">.</span><span class="n">anchors</span><span class="p">.</span><span class="n">an_pos</span><span class="p">.</span><span class="n">pos</span><span class="p">[</span><span class="n">i</span><span class="p">].</span><span class="n">z</span><span class="p">,</span>
<span class="w">                                     </span><span class="n">loc</span><span class="p">.</span><span class="n">anchors</span><span class="p">.</span><span class="n">an_pos</span><span class="p">.</span><span class="n">pos</span><span class="p">[</span><span class="n">i</span><span class="p">].</span><span class="n">qf</span><span class="p">);</span>
<span class="w">             </span><span class="p">}</span>
<span class="w">             </span><span class="n">printf</span><span class="p">(</span><span class="s">"=%lu,%u "</span><span class="p">,</span><span class="w"> </span><span class="n">loc</span><span class="p">.</span><span class="n">anchors</span><span class="p">.</span><span class="n">dist</span><span class="p">.</span><span class="n">dist</span><span class="p">[</span><span class="n">i</span><span class="p">],</span><span class="w"> </span><span class="n">loc</span><span class="p">.</span><span class="n">anchors</span><span class="p">.</span><span class="n">dist</span><span class="p">.</span><span class="n">qf</span><span class="p">[</span><span class="n">i</span><span class="p">]);</span>
<span class="w">     </span><span class="p">}</span>
<span class="w">     </span><span class="n">printf</span><span class="p">(</span><span class="s">"</span><span class="se">\n</span><span class="s">"</span><span class="p">);</span>
<span class="p">}</span><span class="w"> </span><span class="k">else</span><span class="w"> </span><span class="p">{</span>
<span class="w">     </span><span class="n">printf</span><span class="p">(</span><span class="s">"err code: %d</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">rv</span><span class="p">);</span>
<span class="p">}</span>
</pre></div>
</div>
<p><strong>SPI/UART の例 1 (タグ ノード)</strong></p>
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
<tr class="row-odd"><td><p>0x0C</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x0C はコマンド loc_get を意味します</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 3%">
<col style="width: 3%">
<col style="width: 3%">
<col style="width: 3%">
<col style="width: 3%">
<col style="width: 7%">
<col style="width: 7%">
<col style="width: 0%">
<col style="width: 7%">
<col style="width: 0%">
<col style="width: 8%">
<col style="width: 3%">
<col style="width: 3%">
<col style="width: 7%">
<col style="width: 7%">
<col style="width: 0%">
<col style="width: 7%">
<col style="width: 0%">
<col style="width: 8%">
<col style="width: 13%">
<col style="width: 8%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="21"><p>TLV 応答</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td><p>値</p></td>
<td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td colspan="6"><p>値</p></td>
<td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td colspan="8"><p>値</p></td>
</tr>
<tr class="row-odd"><td rowspan="3"><p>0x40</p></td>
<td rowspan="3"><p>0x01</p></td>
<td rowspan="3"><p>0x00</p></td>
<td rowspan="3"><p>0x41</p></td>
<td rowspan="3"><p>0x0D</p></td>
<td rowspan="2"><p>int32 - ミリメートル単位の x 座標</p></td>
<td colspan="2" rowspan="2"><p>int32 - ミリメートル単位の y 座標</p></td>
<td colspan="2" rowspan="2"><p>int32 - ミリメートル単位の Z 座標</p></td>
<td rowspan="2"><p>uint8 - 位置品質係数 (パーセント単位)</p></td>
<td rowspan="3"><p>0x49</p></td>
<td rowspan="3"><p>0x51</p></td>
<td rowspan="2"><p>uint8 -距離の数</p></td>
<td colspan="6"><p>位置と距離番号。 1</p></td>
<td><p>位置と距離 nr.2、3、4</p></td>
</tr>
<tr class="row-even"><td colspan="2"><p>int16 - UWB アドレス</p></td>
<td colspan="2"><p>uint32 - ミリメートル単位の距離</p></td>
<td><p>uint8 - パーセント単位の距離品質係数</p></td>
<td><p>3 x int32 + uint8 - x、y、z (ミリメートル) + 品質係数 (パーセント)</p></td>
<td><p>...</p></td>
</tr>
<tr class="row-odd"><td colspan="6"><p>0x4b
0x0a
0x00
0x00
0x1f
0x04
0x00
0x00         0x9c
0x0e         0x00
0x00         0x64</p></td>
<td><p>0x04</p></td>
<td colspan="2"><p>0xab 0xbc</p></td>
<td colspan="2"><p>0x0e 0x03
0x00 0x00</p></td>
<td><p>0x64</p></td>
<td><p>...</p></td>
<td><p>...</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">タイプ 0x40 は、前のコマンドの <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">ステータスコード</span></a> を意味します</div>
<div class="line">タイプ 0x41 は位置を意味します</div>
<div class="line">タイプ 0x49 は測距アンカーの位置と距離を意味します</div>
</div>
<p><strong>SPI/UART の例 2 (アンカー ノード)</strong></p>
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
<tr class="row-odd"><td><p>0x0C</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x0C はコマンド loc_get を意味します</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 4%">
<col style="width: 4%">
<col style="width: 4%">
<col style="width: 4%">
<col style="width: 4%">
<col style="width: 8%">
<col style="width: 8%">
<col style="width: 0%">
<col style="width: 8%">
<col style="width: 0%">
<col style="width: 9%">
<col style="width: 4%">
<col style="width: 4%">
<col style="width: 8%">
<col style="width: 8%">
<col style="width: 0%">
<col style="width: 8%">
<col style="width: 0%">
<col style="width: 9%">
<col style="width: 11%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="20"><p>TLV 応答</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td><p>値</p></td>
<td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td colspan="6"><p>値</p></td>
<td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td colspan="7"><p>値</p></td>
</tr>
<tr class="row-odd"><td rowspan="3"><p>0x40</p></td>
<td rowspan="3"><p>0x01</p></td>
<td rowspan="3"><p>0x00</p></td>
<td rowspan="3"><p>0x41</p></td>
<td rowspan="3"><p>0x0D</p></td>
<td rowspan="2"><p>int32 - ミリメートル単位の x 座標</p></td>
<td colspan="2" rowspan="2"><p>int32 - ミリメートル単位の y 座標</p></td>
<td colspan="2" rowspan="2"><p>int32 - ミリメートル単位の Z 座標</p></td>
<td rowspan="2"><p>uint8 - 位置品質係数 (パーセント単位)</p></td>
<td rowspan="3"><p>0x48</p></td>
<td rowspan="3"><p>0x63</p></td>
<td rowspan="2"><p>uint8 -距離の数</p></td>
<td colspan="5"><p>距離番号。 1</p></td>
<td><p>距離 nr.2,..., nr. 14</p></td>
</tr>
<tr class="row-even"><td colspan="2"><p>int16 - UWB アドレス</p></td>
<td colspan="2"><p>uint32 - ミリメートル単位の距離</p></td>
<td><p>uint8 - パーセント単位の距離品質係数</p></td>
<td><p>...</p></td>
</tr>
<tr class="row-odd"><td colspan="6"><p>0x4b
0x0a
0x00
0x00
0x1f
0x04
0x00
0x00         0x9c
0x0e         0x00
0x00         0x64</p></td>
<td><p>0x0E</p></td>
<td colspan="2"><p>0xab 0xbc</p></td>
<td colspan="2"><p>0x0e 0x03
0x00 0x00</p></td>
<td><p>0x64</p></td>
<td><p>...</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">タイプ 0x40 は、前のコマンドの <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">ステータスコード</span></a> を意味します</div>
<div class="line">タイプ 0x41 は位置を意味します</div>
<div class="line">タイプ 0x48 は測距アンカーの距離を意味します</div>
</div>
</div>


           </div>
