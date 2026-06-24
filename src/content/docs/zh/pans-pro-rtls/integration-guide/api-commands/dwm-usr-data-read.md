---
title: "dwm_usr_data_read"
lang: zh
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-usr-data-read"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/api-commands/dwm-usr-data-read/"
order: 216
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-usr-data-read">
<span id="id1"></span><h1>dwm_usr_data_read</h1>
<p>从节点读取用户数据. 在 UWB 上接收到的新数据会导致在状态（参见 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-status-get#dwm-status-get"><span class="std std-ref">dwm_status_get</span></a>）中设置一个专用标志，并导致在用户应用程序（参见 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-evt-listener-register#dwm-evt-listener-register"><span class="std std-ref">dwm_evt_listener_register</span></a>）中生成一个事件。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_usr_data_read">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_usr_data_read</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">uint8_t</span></span><span class="p"><span class="pre">*</span></span>, <span class="n"><span class="pre">uint8_t</span></span><span class="p"><span class="pre">*</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">参数</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> – (<em>无</em>)</p></li>
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a>, data, len</p></li>
<li><p><strong>data</strong> – 1-34字节 (<em>用户数据</em>)</p></li>
<li><p><strong>len</strong> – 1字节 (<em>数据长度</em>)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C代码示例</strong></p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">uint8_t data[DWM_USR_DATA_LEN_MAX];</span>
<span class="go">uint8_t len;</span>
<span class="go">len = DWM_USR_DATA_LEN_MAX;</span>
<span class="go">dwm_usr_data_read(data, &amp;len);</span>
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
<tr class="row-odd"><td><p>0x19</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>类型 0x19 表示命令 dwm_usr_data_read</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 31%">
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
<td rowspan="2"><p>0x4B</p></td>
<td rowspan="2"><p>0x22</p></td>
<td><p>字节 0 - N:用户数据（1 &lt;= N &lt;= 33）</p></td>
</tr>
<tr class="row-even"><td><p>0x01 0x02
0x03 …
0x23 0x22</p></td>
</tr>
</tbody>
</table>
<p>类型 0x4B 表示用户数据</p>
</div>


           </div>
