---
title: "dwm_anchor_list_get"
lang: zh
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-anchor-list-get"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/api-commands/dwm-anchor-list-get/"
order: 167
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-anchor-list-get">
<span id="id1"></span><h1>dwm_anchor_list_get</h1>
<p>读取周围锚点的列表，仅对锚点有效。 列表中的锚点可以来自同一网络或邻居网络。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_anchor_list_get">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_anchor_list_get</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">dwm_anchor_list_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">list</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">参数</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> – (SPI/UART) ‘0’ | ‘1’(<em>页码（仅在 SPI/UART 上，用户应用程序在一次调用中读取整个列表），有效数字为 0,1</em>)</p></li>
<li><p><strong>input</strong> – (用户应用程序) (<em>无</em>)</p></li>
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a>, cnt, {node_id, position, rssi, seat, neighbor_network}</p></li>
<li><p><strong>cnt</strong> – 1 字节？(<em>元素计数，对于 SPI/UART 最大为 15，对于用户应用程序最大为 30</em>)</p></li>
<li><p><strong>node_id</strong> – 2 字节（<em>锚点 ID</em>）</p></li>
<li><p><strong>position</strong> – 12 字节？</p></li>
<li><p><strong>rssi</strong> – 1 字节带符号?（<em>信号强度指示器</em>）</p></li>
<li><p><strong>seat</strong> – 5 位（<em>锚点占用的座位号</em>）</p></li>
<li><p><strong>neighbor_network</strong> – 1 位（<em>状态标志，表示锚点是来自当前网络，还是来自邻居网络</em>）。</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C代码示例</strong></p>
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
<p><strong>SPI/UART 示例 1</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV 请求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度</p></td>
<td><p>价值</p></td>
</tr>
<tr class="row-odd"><td><p>0x0B</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>类型 0x0B 表示命令 dwm_an_list_get</p>
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
<tr class="row-odd"><th class="head" colspan="11"><p>TLV 响应</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="3"><p>类型</p></td>
<td rowspan="3"><p>长度</p></td>
<td><p>价值</p></td>
<td rowspan="3"><p>类型</p></td>
<td rowspan="3"><p>长度</p></td>
<td colspan="6"><p>价值</p></td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>uint8 - 错误代码</p></td>
<td rowspan="2"><p>uint8 - 编码元素的数量</p></td>
<td rowspan="2"><p>uint16 - UWB 地址，小端序</p></td>
<td colspan="3"><p>锚点 nr.1</p></td>
<td><p>锚点nr. 2 … nr.15</p></td>
</tr>
<tr class="row-even"><td><p>3 x int32 - 位置坐标 x, y, z (小端序)</p></td>
<td><p>int8 -
RSSI</p></td>
<td><div class="line-block">
<div class="line">uint8 - 标志</div>
</div>
<div class="line-block">
<div class="line">(0-4 位)座位号</div>
<div class="line">(第 5 位)邻居网络</div>
<div class="line">(6-7位) 保留</div>
</div>
</td>
<td><p>…</p></td>
</tr>
<tr class="row-odd"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x56</p></td>
<td><p>0xE1</p></td>
<td><p>0x0F</p></td>
<td colspan="4"><p>0xAB 0x1E …</p></td>
<td><p>…</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">类型0x40表示 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a> 上一条命令的状态码</div>
<div class="line">类型 0x56 表示锚点列表</div>
</div>
<p><strong>SPI/UART 示例 2</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV 请求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度</p></td>
<td><p>价值</p></td>
</tr>
<tr class="row-odd"><td><p>0x0B</p></td>
<td><p>0x01</p></td>
<td><p>0x01</p></td>
</tr>
</tbody>
</table>
<p>类型 0x0B 表示命令 dwm_an_list_get</p>
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
<tr class="row-odd"><th class="head" colspan="6"><p>TLV 响应(锚点列表为空）</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度</p></td>
<td><p>价值</p></td>
<td><p>类型</p></td>
<td><p>长度</p></td>
<td><p>价值</p></td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>0x40</p></td>
<td rowspan="2"><p>0x01</p></td>
<td rowspan="2"><p>0x00</p></td>
<td rowspan="2"><p>0x56</p></td>
<td rowspan="2"><p>0x01</p></td>
<td><p>uint8 - 值中编码的元素个数</p></td>
</tr>
<tr class="row-even"><td><p>0x00</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">类型0x40表示 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a> 上一条命令的状态码</div>
<div class="line">类型 0x56 表示锚点列表</div>
</div>
</div>


           </div>
