---
title: "dwm_baddr_get"
lang: zh
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-baddr-get"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/api-commands/dwm-baddr-get/"
order: 168
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-baddr-get">
<span id="id1"></span><h1>dwm_baddr_get</h1>
<p>获取设备当前使用的 BLE 地址。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_baddr_get">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_baddr_get</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">dwm_baddr_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">baddr</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">参数</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a>, ble_addr</p></li>
<li><p><strong>ble_addr</strong> – 6 字节（BLE 地址）</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C代码示例</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_baddr_t</span><span class="w"> </span><span class="n">baddr</span><span class="p">;</span>
<span class="kt">int</span><span class="w"> </span><span class="n">i</span><span class="p">;</span>
<span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">DWM_OK</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="n">dwm_baddr_get</span><span class="p">(</span><span class="o">&amp;</span><span class="n">baddr</span><span class="p">))</span><span class="w"> </span><span class="p">{</span>
<span class="w">      </span><span class="n">printf</span><span class="p">(</span><span class="s">"addr="</span><span class="p">);</span>
<span class="w">      </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="n">i</span><span class="o">:</span><span class="w"> </span><span class="n">DWM_BLE_ADDR_LEN</span><span class="w"> </span><span class="o">-</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&gt;=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="o">--</span><span class="n">i</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">              </span><span class="n">printf</span><span class="p">(</span><span class="s">"%02x%s"</span><span class="p">,</span><span class="w"> </span><span class="n">baddr</span><span class="p">.</span><span class="n">byte</span><span class="p">[</span><span class="n">i</span><span class="p">],</span><span class="w"> </span><span class="p">(</span><span class="n">i</span><span class="w"> </span><span class="o">&gt;</span><span class="w"> </span><span class="mi">0</span><span class="p">)</span><span class="w"> </span><span class="o">?</span><span class="w"> </span><span class="s">":"</span><span class="w"> </span><span class="o">:</span><span class="w"> </span><span class="s">""</span><span class="p">);</span>
<span class="w">      </span><span class="p">}</span>
<span class="w">      </span><span class="n">printf</span><span class="p">(</span><span class="s">"</span><span class="se">\n</span><span class="s">"</span><span class="p">);</span>
<span class="p">}</span><span class="w"> </span><span class="k">else</span><span class="w"> </span><span class="p">{</span>
<span class="w">      </span><span class="n">printf</span><span class="p">(</span><span class="s">"FAILED"</span><span class="p">);</span>
<span class="p">}</span>
</pre></div>
</div>
<p><strong>SPI/UART 示例</strong></p>
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
<tr class="row-odd"><td><p>0x10</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>类型0x10 表示指令 <a class="reference internal" href="#dwm-baddr-get"><span class="std std-ref">dwm_baddr_get</span></a>。</p>
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
<tr class="row-odd"><th class="head" colspan="6"><p>TLV 响应</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度</p></td>
<td><p>价值（参见错误代码）</p></td>
<td><p>类型</p></td>
<td><p>长度</p></td>
<td><p>价值</p></td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>0x40</p></td>
<td rowspan="2"><p>0x01</p></td>
<td rowspan="2"><p>0x00</p></td>
<td rowspan="2"><p>0x5F</p></td>
<td rowspan="2"><p>0x06</p></td>
<td><p>6 个字节，小端序</p></td>
</tr>
<tr class="row-even"><td><p>0x01
0x02
0x03
0x04
0x05
0x06</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">类型0x40表示 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a> 上一条命令的状态码</div>
<div class="line">类型0x5F表示BLE地址</div>
</div>
</div>


           </div>
