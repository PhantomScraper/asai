---
title: "dwm_uwb_cfg_get"
lang: zh
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-uwb-cfg-get"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/api-commands/dwm-uwb-cfg-get/"
order: 218
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-uwb-cfg-get">
<span id="id1"></span><h1>dwm_uwb_cfg_get</h1>
<p>获取 UWB 配置参数。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_uwb_cfg_get">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_uwb_cfg_get</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">dwm_uwb_cfg_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">uwb_cfg</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">参数</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> – (<em>无</em>)</p></li>
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a>, pg_delay, tx_power</p></li>
<li><p><strong>pg_delay</strong> – 1 字节 (<em>发射机校准脉冲发生器延迟值</em>)</p></li>
<li><p><strong>tx_power</strong> – 4字节 (<em>传输功率控制单位</em>)</p></li>
<li><p><strong>pg_delay_comp</strong> – 1字节 (<em>发射机校准脉冲发生器延迟值，补偿</em>)</p></li>
<li><p><strong>tx_power_comp</strong> – 4字节 (<em>发射功率控制单位，补偿</em>)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C代码示例</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_uwb_cfg_t</span><span class="w"> </span><span class="n">uwb_cfg</span><span class="p">;</span>
<span class="n">dwm_uwb_cfg_get</span><span class="p">(</span><span class="o">&amp;</span><span class="n">uwb_cfg</span><span class="p">);</span>
<span class="n">printf</span><span class="p">(</span><span class="s">"delay=%x, power=%lx compensated(%x,%lx)</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span>
<span class="w">                     </span><span class="n">uwb_cfg</span><span class="p">.</span><span class="n">pg_delay</span><span class="p">,</span>
<span class="w">                     </span><span class="n">uwb_cfg</span><span class="p">.</span><span class="n">tx_power</span><span class="p">,</span>
<span class="w">                     </span><span class="n">uwb_cfg</span><span class="p">.</span><span class="n">compensated</span><span class="p">.</span><span class="n">pg_delay</span><span class="p">,</span>
<span class="w">                     </span><span class="n">uwb_cfg</span><span class="p">.</span><span class="n">compensated</span><span class="p">.</span><span class="n">tx_power</span><span class="p">);</span>
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
<tr class="row-odd"><td><p>0x18</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>类型 0x18 表示指令 dwm_uwb_cfg_get</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 13%">
<col style="width: 13%">
<col style="width: 13%">
<col style="width: 13%">
<col style="width: 13%">
<col style="width: 36%">
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
<td rowspan="2"><p>0x4F</p></td>
<td rowspan="2"><p>0x0A</p></td>
<td><div class="line-block">
<div class="line">1st byte: pg_delay</div>
<div class="line">2nd-5th byte: tx_power</div>
<div class="line">6th byte: pg_delay_comp</div>
<div class="line">7th-10th byte: tx_power_comp</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>hex: 0xC3
0x85 0x65 0x45
0x25 0xC4 0x85
0x65 0x45 0x25</p></td>
</tr>
</tbody>
</table>
<p>类型 0x4F 表示 UWB 配置</p>
</div>


           </div>
