---
title: "dwm_loc_get"
lang: zh
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-loc-get"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/api-commands/dwm-loc-get/"
order: 197
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-loc-get">
<span id="id1"></span><h1>dwm_loc_get</h1>
<p>获取到测距锚的最后距离并获取位置。 当完成所有 TWR 测量后，事件生成，状态改变，用户可获得新的位置数据。 当使用低功耗模式时，也会以同样的方式工作。</p>
<p>对于锚节点，只有在完成自动定位程序后，才能获得位置和距离数据。 自动定位程序是通过 BLE 接口执行的。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_loc_get">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_loc_get</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">dwm_loc_data_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">loc</span></span><span class="sig-paren">)</span><span class="p"><span class="pre">;</span></span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">参数</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a>, [position], [cnt, {an_pos, addr, distance, pqf}]</p></li>
<li><p><strong>cnt</strong> – 0,1,2,3,4 (<em>与锚点的距离</em>)</p></li>
<li><p><strong>an_pos</strong> – 位置 (<em>与距离相对应的锚点位置</em>)</p></li>
<li><p><strong>addr</strong> – 16位整数 (<em>特定锚点的UWB地址/ID</em>)</p></li>
<li><p><strong>distance</strong> – 32 位整数（<em>到特定锚点的距离，以毫米为单位</em>）</p></li>
<li><p><strong>pqf</strong> – 8位整数 (<em>质量因子</em>)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<div class="admonition note">
<p class="admonition-title">注解</p>
<p>参数**an_pos**仅适用于**标签节点**</p>
</div>
<p><strong>C代码示例</strong></p>
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
<p><strong>SPI/UART 示例 1 (标签节点)</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 50%">
<col style="width: 50%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="2"><p>TLV 请求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度</p></td>
</tr>
<tr class="row-odd"><td><p>0x0C</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>类型0x0C 表示 loc_get 命令</p>
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
<tr class="row-odd"><th class="head" colspan="21"><p>TLV 响应</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度</p></td>
<td><p>价值</p></td>
<td><p>类型</p></td>
<td><p>长度</p></td>
<td colspan="6"><p>价值</p></td>
<td><p>类型</p></td>
<td><p>长度</p></td>
<td colspan="8"><p>价值</p></td>
</tr>
<tr class="row-odd"><td rowspan="3"><p>0x40</p></td>
<td rowspan="3"><p>0x01</p></td>
<td rowspan="3"><p>0x00</p></td>
<td rowspan="3"><p>0x41</p></td>
<td rowspan="3"><p>0x0D</p></td>
<td rowspan="2"><p>int32 - x坐标，单位为毫米</p></td>
<td colspan="2" rowspan="2"><p>int32 - y坐标，单位为毫米</p></td>
<td colspan="2" rowspan="2"><p>int32 - z坐标，单位为毫米</p></td>
<td rowspan="2"><p>uint8 - 以百分数为单位的位置质量因子</p></td>
<td rowspan="3"><p>0x49</p></td>
<td rowspan="3"><p>0x51</p></td>
<td rowspan="2"><p>uint8 -距离数</p></td>
<td colspan="6"><p>位置和距离 nr.2,3,4</p></td>
<td><p>位置和距离 nr. 2,3,4</p></td>
</tr>
<tr class="row-even"><td colspan="2"><p>int16 - UWB 地址</p></td>
<td colspan="2"><p>uint32 - 距离，以毫米为单位</p></td>
<td><p>uint8 - 距离质量因子（百分比）</p></td>
<td><p>3 x int32 + uint8 - 以毫米为单位的 x, y, z + 以百分数为单位的质量系数</p></td>
<td><p>…</p></td>
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
<td><p>…</p></td>
<td><p>…</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">类型0x40 表示前一个命令的 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a></div>
<div class="line">类型0x41表示位置</div>
<div class="line">类型0x49表示测距锚的位置和距离</div>
</div>
<p><strong>SPI/UART 示例 2（锚节点）</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 50%">
<col style="width: 50%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="2"><p>TLV 请求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度</p></td>
</tr>
<tr class="row-odd"><td><p>0x0C</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>类型0x0C 表示 loc_get 命令</p>
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
<tr class="row-odd"><th class="head" colspan="20"><p>TLV 响应</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度</p></td>
<td><p>价值</p></td>
<td><p>类型</p></td>
<td><p>长度</p></td>
<td colspan="6"><p>价值</p></td>
<td><p>类型</p></td>
<td><p>长度</p></td>
<td colspan="7"><p>价值</p></td>
</tr>
<tr class="row-odd"><td rowspan="3"><p>0x40</p></td>
<td rowspan="3"><p>0x01</p></td>
<td rowspan="3"><p>0x00</p></td>
<td rowspan="3"><p>0x41</p></td>
<td rowspan="3"><p>0x0D</p></td>
<td rowspan="2"><p>int32 - x坐标，单位为毫米</p></td>
<td colspan="2" rowspan="2"><p>int32 - y坐标，单位为毫米</p></td>
<td colspan="2" rowspan="2"><p>int32 - z坐标，单位为毫米</p></td>
<td rowspan="2"><p>uint8 - 以百分数为单位的位置质量因子</p></td>
<td rowspan="3"><p>0x48</p></td>
<td rowspan="3"><p>0x63</p></td>
<td rowspan="2"><p>uint8 -距离数</p></td>
<td colspan="5"><p>距离 nr. 1</p></td>
<td><p>距离 nr.2,…, nr. 14</p></td>
</tr>
<tr class="row-even"><td colspan="2"><p>int16 - UWB 地址</p></td>
<td colspan="2"><p>uint32 - 距离，以毫米为单位</p></td>
<td><p>uint8 - 距离质量因子（百分比）</p></td>
<td><p>…</p></td>
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
<td><p>…</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">类型0x40 表示前一个命令的 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a></div>
<div class="line">类型0x41表示位置</div>
<div class="line">类型0x48表示测距锚的距离</div>
</div>
</div>


           </div>
