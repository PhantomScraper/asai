---
title: "dwm_boot_cfg_set"
lang: zh
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-boot-cfg-set"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/api-commands/dwm-boot-cfg-set/"
order: 170
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-boot-cfg-set">
<span id="id1"></span><h1>dwm_boot_cfg_set</h1>
<p>此调用仅适用于以太网网关。 它设置设备复位后停留在引导加载器模式的时间。 引导加载器模式用于使用串行接口进行固件更新。 时间结束后，模块将跳转到正常运行模式。 固件更新可在跳转前启动，时间可设置为 0 至 4294967295 毫秒。 不过，需要重置后才能生效。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_boot_cfg_set">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_boot_cfg_set</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">参数</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> – boot_delay</p></li>
<li><p><strong>boot_delay</strong> – 32 位无符号整数 (<em>以毫秒为单位的延迟</em>)</p></li>
<li><p><strong>output</strong> – status_code</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>SPI/UART 示例</strong></p>
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
<td><p>值 1000 毫秒</p></td>
</tr>
<tr class="row-odd"><td><p>0x26</p></td>
<td><p>0x04</p></td>
<td><p>0xE8 0x03 0x00 0x00</p></td>
</tr>
</tbody>
</table>
<p>类型 0x26（38 dec）表示命令 <a class="reference internal" href="#dwm-boot-cfg-set"><span class="std std-ref">dwm_boot_cfg_set</span></a></p>
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
<td><p>价值</p></td>
</tr>
<tr class="row-odd"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>类型 0x40 表示状态代码</p>
</div>


           </div>
