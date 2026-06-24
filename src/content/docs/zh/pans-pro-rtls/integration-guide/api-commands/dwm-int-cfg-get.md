---
title: "dwm_int_cfg_get"
lang: zh
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-int-cfg-get"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/api-commands/dwm-int-cfg-get/"
order: 193
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-int-cfg-get">
<span id="id1"></span><h1>dwm_int_cfg_get</h1>
<p>读取配置标志，如果设置了这些标志，就能在 DWM 模块发生内部事件时设置专用 GPIO 引脚 (CORE_INT)。</p>
<p>此调用仅适用于 UART/SPI 接口。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_int_cfg_get">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_int_cfg_get</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">参数</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> – (<em>无</em>)</p></li>
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a>, spi_data_ready, loc_ready, bh_status_changed, bh_data_ready bh_initialized_changed, uwb_scan_ready, usr_data_ready,    :param uwbmac_joined_changed</p></li>
<li><p><strong>spi_data_ready</strong> – ‘0’ | ‘1’ (<em>新的 SPI 数据会在专用的 GPIO 引脚上产生中断，0=禁用，1=启用</em>)</p></li>
<li><p><strong>loc_ready</strong> – ‘0’ | ‘1’ (<em>位置数据就绪时产生中断，0=禁用，1=启用</em>)</p></li>
<li><p><strong>bh_status_changed</strong> – ‘0’ | ‘1’ (<em>UWBMAC 状态改变, 0=禁用，1=启用</em>)</p></li>
<li><p><strong>bh_data_ready</strong> – ‘0’ | ‘1’ (<em>UWBMAC 回程数据就绪，0=禁用，1=启用</em>)</p></li>
<li><p><strong>bh_initialized_changed</strong> – ‘0’ | ‘1’ (<em>UWBMAC 路由已配置，0=禁用，1=启用</em>)</p></li>
<li><p><strong>usr_data_ready</strong> – ‘0’ | ‘1’ (<em>通过 UWBMAC 收到用户数据</em>)</p></li>
<li><p><strong>uwb_scan_ready</strong> – ‘0’ | ‘1’ (<em>UWB 扫描结果可用</em>)</p></li>
<li><p><strong>uwbmac_joined_changed</strong> – ‘0’ | ‘1’ (<em>UWBMAC 已加入，0= 禁用，1= 启用</em>)</p></li>
<li><p><strong>usr_data_sent</strong> – ‘0’ | ‘1’ (<em>通过 UWBMAC 完成用户数据 TX</em>)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C代码示例</strong></p>
<p>模块内用户应用程序不可用。 仅在外部接口（SPI, UART）上可用</p>
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
<tr class="row-odd"><td><p>0x35</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>类型0x35 表示指令 <a class="reference internal" href="#dwm-int-cfg-get"><span class="std std-ref">dwm_int_cfg_get</span></a></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 12%">
<col style="width: 12%">
<col style="width: 12%">
<col style="width: 12%">
<col style="width: 12%">
<col style="width: 39%">
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
<td rowspan="2"><p>0x47</p></td>
<td rowspan="2"><p>0x02</p></td>
<td><div class="line-block">
<div class="line">中断配置标志:</div>
<div class="line">保留（位 9-15）</div>
<div class="line">usr_data_sent (位8)</div>
<div class="line">uwbmac_joined_changed (位7)</div>
<div class="line">usr_data_ready (位6)</div>
<div class="line">uwb_scan_ready (位5)</div>
<div class="line">bh_initialized_changed (位4)</div>
<div class="line">bh_data_ready (位3)</div>
<div class="line">bh_status_changed (位2)</div>
<div class="line">spi_data_ready (位 1)</div>
<div class="line">loc_ready (位0)</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x0E 0x00</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">类型0x47 表示中断配置</div>
</div>
</div>


           </div>
