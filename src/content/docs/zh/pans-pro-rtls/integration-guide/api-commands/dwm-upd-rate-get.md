---
title: "dwm_upd_rate_get"
lang: zh
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-upd-rate-get"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/api-commands/dwm-upd-rate-get/"
order: 214
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-upd-rate-get">
<span id="id1"></span><h1>dwm_upd_rate_get</h1>
<p>获取位置更新率。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_upd_rate_get">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_upd_rate_get</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">uint16_t</span></span><span class="p"><span class="pre">*</span></span>, <span class="n"><span class="pre">uint16_t</span></span><span class="p"><span class="pre">*</span></span><span class="sig-paren">)</span><span class="p"><span class="pre">;</span></span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">参数</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a>, update_rate, update_rate_stationary</p></li>
<li><p><strong>update_rate</strong> – 16 位整数（<em>以 100 毫秒的倍数表示位置发布率，最大为 1 分钟，最小为 100 毫秒</em>）</p></li>
<li><p><strong>update_rate_stationary</strong> – 16 位整数（<em>节点不动时的位置发布率，以 100 毫秒的倍数表示，最大为 1 分钟，最小为 100 毫秒</em>）。</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C代码示例</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="kt">uint16_t</span><span class="w"> </span><span class="n">ur</span><span class="p">,</span><span class="w"> </span><span class="n">urs</span><span class="p">;</span>
<span class="n">dwm_upd_rate_get</span><span class="p">(</span><span class="o">&amp;</span><span class="n">ur</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">urs</span><span class="p">);</span>
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
<tr class="row-odd"><td><p>0x04</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>类型 0x04 表示命令 dwm_upd_rate_get</p>
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
<td rowspan="2"><p>0x45</p></td>
<td rowspan="2"><p>0x04</p></td>
<td><p>前 2 字节表示 16 位小端序，更新速率为 100 毫秒的倍数（例如，0x0A 0x00 表示 1 秒）；后 2 个字节表示 16 位小端序，固定更新速率为 100 毫秒的倍数（例如，0x16 0x00 表示 2.2 秒）。</p></td>
</tr>
<tr class="row-even"><td><p>0x0A 0x00
0x16 0x00</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">类型 0x45 表示更新率（正常和静止）</div>
<div class="line">类型0x40表示 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a> 上一条命令的状态码</div>
</div>
</div>


           </div>
