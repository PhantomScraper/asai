---
title: "dwm_upd_rate_set"
lang: zh
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-upd-rate-set"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/api-commands/dwm-upd-rate-set/"
order: 215
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-upd-rate-set">
<span id="id1"></span><h1>dwm_upd_rate_set</h1>
<p>以百毫秒为单位设置位置更新率和静态更新率。 在设置新值时，该调用通常会写入内部闪存。 因此，不应频繁调用。 在最坏的情况下，响应时间可能长达数百毫秒。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_upd_rate_set">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_upd_rate_set</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">uint8_t</span></span><span class="w"> </span><span class="n"><span class="pre">update_rate</span></span>, <span class="n"><span class="pre">uint8_t</span></span><span class="w"> </span><span class="n"><span class="pre">update_rate_stationary</span></span><span class="sig-paren">)</span><span class="p"><span class="pre">;</span></span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">参数</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>update_rate</strong> – 16 位整数（<em>以 100 毫秒的倍数表示位置发布率，最大为 1 分钟，最小为 100 毫秒</em>）</p></li>
<li><p><strong>update_rate_stationary</strong> – 16 位整数（<em>节点不动时的位置发布率，以 100 毫秒的倍数表示，最大为 1 分钟，最小为 100 毫秒</em>）。</p></li>
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C代码示例</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_upd_rate_set</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span><span class="w"> </span><span class="mi">50</span><span class="p">);</span><span class="w"> </span><span class="cm">/* update rate 1 second. 5 seconds stationary */</span>
<span class="n">dwm_upd_rate_set</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">);</span><span class="w"> </span><span class="cm">/* ERROR - must not be a zero */</span>
</pre></div>
</div>
<p><strong>SPI/UART 示例</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 32%">
<col style="width: 32%">
<col style="width: 37%">
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
<tr class="row-odd"><td><p>0x03</p></td>
<td><p>0x04</p></td>
<td><p>前 2 字节表示 16 位小端序，更新速率为 100 毫秒的倍数（例如 0x0A 0x00 表示 10）；后 2 字节表示 16 位小端序，静态更新速率为 100 毫秒的倍数。</p></td>
</tr>
<tr class="row-even"><td></td>
<td></td>
<td><p>0x0A 0x00 0x014 0x00</p></td>
</tr>
</tbody>
</table>
<p>类型 0x03 表示命令 dwm_upd_rate_set</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV 响应</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度</p></td>
<td><p>价值（参见错误代码）</p></td>
</tr>
<tr class="row-odd"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>类型0x40表示 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a> 上一条命令的状态码</p>
</div>


           </div>
