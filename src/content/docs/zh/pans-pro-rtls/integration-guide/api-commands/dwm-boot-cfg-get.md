---
title: "dwm_boot_cfg_get"
lang: zh
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-boot-cfg-get"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/api-commands/dwm-boot-cfg-get/"
order: 169
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-boot-cfg-get">
<span id="id1"></span><h1>dwm_boot_cfg_get</h1>
<p>此调用仅适用于以太网网关. 获取引导加载器配置. 更多信息请参阅 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-boot-cfg-set#dwm-boot-cfg-set"><span class="std std-ref">dwm_boot_cfg_set</span></a>。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_boot_cfg_get">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_boot_cfg_get</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">dwm_mac_addr_list_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">mac_addr_list</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">参数</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> – (<em>无</em>)</p></li>
<li><p><strong>output</strong> – status_code, boot_delay</p></li>
<li><p><strong>boot_delay</strong> – 32 位无符号整数 (<em>以毫秒为单位的延迟</em>)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

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
<tr class="row-odd"><td><p>0x27</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>类型 0x27 (39) 表示命令 <a class="reference internal" href="#dwm-boot-cfg-get"><span class="std std-ref">dwm_boot_cfg_get</span></a>。</p>
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
<td><p>价值</p></td>
<td><p>类型</p></td>
<td><p>长度</p></td>
<td><p>价值</p></td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>0x40</p></td>
<td rowspan="2"><p>0x01</p></td>
<td rowspan="2"><p>0x00</p></td>
<td rowspan="2"><p>0x60</p></td>
<td rowspan="2"><p>0x04</p></td>
<td><p>启动延迟，以毫秒为单位</p></td>
</tr>
<tr class="row-even"><td><p>0xB8 0x0B
0x00 0x00</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">类型 0x40 表示状态代码</div>
<div class="line">类型0x60 (96)型表示引导加载程序配置</div>
</div>
</div>


           </div>
