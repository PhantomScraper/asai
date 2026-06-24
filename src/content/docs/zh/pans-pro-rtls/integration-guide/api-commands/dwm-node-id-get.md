---
title: "dwm_node_id_get"
lang: zh
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-node-id-get"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/api-commands/dwm-node-id-get/"
order: 201
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-node-id-get">
<span id="id1"></span><h1>dwm_node_id_get</h1>
<p>获取节点的完整 UWB 地址。 地址/ID 是一个唯一的 64 位数字。 它由固定前缀 0xDECA, MCU 唯一芯片 ID 和 DW1000 唯一部件 ID 组成，格式如下： 0xDECA + 28 位 MCU 唯一芯片 ID + 20 位 DW1000 唯一部件 ID。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_node_id_get">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_node_id_get</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">uint64_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">node_id</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">参数</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> – (<em>无</em>)</p></li>
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a>, node_id</p></li>
<li><p><strong>node_id</strong> – 64 位整数 (<em>UWB 节点地址/ID</em>)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C代码示例</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="kt">uint64_t</span><span class="w"> </span><span class="n">node_id</span><span class="p">;</span>
<span class="n">dwm_node_id_get</span><span class="p">(</span><span class="o">&amp;</span><span class="n">node_id</span><span class="p">);</span>
<span class="n">printf</span><span class="p">(</span><span class="s">"node ID = 0x%llx </span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">node_id</span><span class="p">);</span>
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
<tr class="row-odd"><td><p>0x30</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>类型0x30 表示指令 dwm_node_id_get</p>
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
<td rowspan="2"><p>0x4E</p></td>
<td rowspan="2"><p>0x08</p></td>
<td><p>8 字节，小端序</p></td>
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
<div class="line">类型0x40表示 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a> 上一条命令的状态码</div>
<div class="line">类型0x4E表示节点ID</div>
</div>
</div>


           </div>
