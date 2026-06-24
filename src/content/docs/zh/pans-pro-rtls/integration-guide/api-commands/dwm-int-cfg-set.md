---
title: "dwm_int_cfg_set"
lang: zh
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-int-cfg-set"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/api-commands/dwm-int-cfg-set/"
order: 194
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-int-cfg-set">
<span id="id1"></span><h1>dwm_int_cfg_set</h1>
<p>在发生中断时，它可启用或禁用专用 GPIO 引脚的设置。 此外，中断或事件可通过设置 GPIO 引脚 CORE_INT1 传达给用户。 用户可将该引脚用作外部中断源。 可以通过使用 dwm_status_get 读取状态来处理中断，并对新状态做出相应的反应。 读取状态后，状态将被清零。 该调用仅适用于 UART/SPI 接口。 通常，在设置新值时，该调用会写入内部闪存，因此不应频繁使用，因为在最坏情况下可能需要数百毫秒！</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_int_cfg_set">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_int_cfg_set</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">参数</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> – spi_data_ready, loc_ready, bh_status_changed, bh_data_ready, bh_initialized_changed, uwb_scan_ready, usr_data_ready,    :param uwbmac_joined_changed</p></li>
<li><p><strong>spi_data_ready</strong> – ‘0’ | ‘1’ (<em>新的 SPI 数据会在专用的 GPIO 引脚上产生中断，0=禁用，1=启用</em>)</p></li>
<li><p><strong>loc_ready</strong> – ‘0’ | ‘1’ (<em>位置数据就绪时产生中断，0=禁用，1=启用</em>)</p></li>
<li><p><strong>bh_status_changed</strong> – ‘0’ | ‘1’ (<em>UWBMAC 状态改变, 0=禁用，1=启用</em>)</p></li>
<li><p><strong>bh_data_ready</strong> – ‘0’ | ‘1’ (<em>UWBMAC 回程数据就绪，0=禁用，1=启用</em>)</p></li>
<li><p><strong>bh_initialized_changed</strong> – ‘0’ | ‘1’ (<em>UWBMAC 路由已配置，0=禁用，1=启用</em>)</p></li>
<li><p><strong>uwb_scan_ready</strong> – ‘0’ | ‘1’ (<em>UWB 扫描结果可用</em>)</p></li>
<li><p><strong>usr_data_ready</strong> – ‘0’ | ‘1’ (<em>通过 UWBMAC 收到用户数据</em>)</p></li>
<li><p><strong>uwbmac_joined_changed</strong> – ‘0’ | ‘1’ (<em>UWBMAC 已加入，0=禁用，1=启用</em>)</p></li>
<li><p><strong>usr_data_sent</strong> – ‘0’ | ‘1’ (<em>通过 UWBMAC 完成用户数据 TX</em>)</p></li>
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C代码示例</strong></p>
<p>模块内用户应用程序不可用。 仅在外部接口（SPI, UART）上可用</p>
<p><strong>SPI/UART 示例</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 21%">
<col style="width: 21%">
<col style="width: 57%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>类型</p></th>
<th class="head"><p>长度</p></th>
<th class="head"><p>价值</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>0x34</p></td>
<td><p>0x02</p></td>
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
<tr class="row-odd"><td></td>
<td></td>
<td><p>0x0F 0x01</p></td>
</tr>
</tbody>
</table>
<p>类型0x34 表示命令 dwm_int_cfg_set</p>
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
<div class="line-block">
<div class="line">类型0x40表示 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a> 上一条命令的状态码</div>
</div>
</div>


           </div>
