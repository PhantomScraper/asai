---
title: "dwm_dev_info_get"
lang: zh
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-dev-info-get"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/api-commands/dwm-dev-info-get/"
order: 176
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-dev-info-get">
<span id="id1"></span><h1>dwm_dev_info_get</h1>
<p>获取模块的固件 ID, 固件版本, 配置版本和硬件版本。 固件 ID 在网关上的默认值为 1，在 DWM1001 上的默认值为 2。 网关上 ID 为 0 的固件和 DWM1001 上 ID 为 1 的固件可用作备份。 备份固件会在固件更新时使用。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_dev_info_get">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_dev_info_get</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">dwm_dev_info_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">info</span></span><span class="sig-paren">)</span><span class="p"><span class="pre">;</span></span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">参数</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a>, fw_id, fw_bckp_version, fw_version, fw_bckp_cksum, fw_cksum, cfg_version, hw_version</p></li>
<li><p><strong>fw_id</strong> – 32 位整数 (<em>当前活动固件的 ID</em>)</p></li>
<li><p><strong>fw_bckp_version</strong> – 32 位整数 (<em>maj, min, patch, res, var</em>)</p></li>
<li><p><strong>fw_version</strong> – 32 位整数 (<em>maj, min, patch, res, var</em>)</p></li>
<li><p><strong>fw_bckp_cksum</strong> – 32 位整数</p></li>
<li><p><strong>fw_cksum</strong> – 32 位整数</p></li>
<li><p><strong>cfg_version</strong> – 32 位整数</p></li>
<li><p><strong>hw_version</strong> – 32 位整数</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C代码示例</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_dev_info_t</span><span class="w"> </span><span class="n">info</span><span class="p">;</span>
<span class="n">dwm_dev_info_get</span><span class="p">(</span><span class="o">&amp;</span><span class="n">info</span><span class="p">);</span>
<span class="n">printf</span><span class="p">(</span><span class="s">"FW ID=%d</span><span class="se">\n</span><span class="s">”, info.fw_id);</span>
<span class="n">printf</span><span class="p">(</span><span class="s">"FW version: maj(%d) min(%d) patch(%d) res(%d) var(%d)</span><span class="se">\n</span><span class="s">”, info.fw_ver[1].maj, info.fw_ver[1].min, info.fw_ver[1].patch, info.fw_ver[1].res, info .fw_ver[1].var);</span>
<span class="n">printf</span><span class="p">(</span><span class="s">"CFG version: x%08x</span><span class="se">\n</span><span class="s">”, info.cfg_ver);</span>
<span class="n">printf</span><span class="p">(</span><span class="s">"HW version: x%08x</span><span class="se">\n</span><span class="s">”, info.hw_ver);</span>
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
<tr class="row-odd"><td><p>0x15</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>类型 0x15 表示命令 <a class="reference internal" href="#dwm-dev-info-get"><span class="std std-ref">dwm_dev_info_get</span></a></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 12%">
<col style="width: 12%">
<col style="width: 12%">
<col style="width: 12%">
<col style="width: 12%">
<col style="width: 41%">
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
<td rowspan="2"><p>0x50</p></td>
<td rowspan="2"><p>0x1C</p></td>
<td><p>设备信息</p></td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line">0x07 0x01 0x00 0x02 0x11 0x01 0x00</div>
<div class="line">0x9d 0x59 0x9b 0x52 0x90 0x81 0x00</div>
<div class="line">0x01 0x01 0x01 0x03 0x01 0xd2 0x81</div>
<div class="line">0x01 0x00 0x00 0x00 0x01 0x01 0x03</div>
</div>
</td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">类型0x40表示 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a> 上一条命令的状态码</div>
<div class="line">类型0x50表示设备信息</div>
</div>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 11%">
<col style="width: 27%">
<col style="width: 27%">
<col style="width: 21%">
<col style="width: 14%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="5"><p><strong>设备信息TLV编码</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>fw_id</p></td>
<td><div class="line-block">
<div class="line">fw_bckp_version</div>
<div class="line">fw_version</div>
</div>
</td>
<td><div class="line-block">
<div class="line">fw_bckp_cksum</div>
<div class="line">fw_cksum</div>
</div>
</td>
<td><p>cfg_version</p></td>
<td><p>hw</p></td>
</tr>
<tr class="row-odd"><td><p>字节 0-3</p></td>
<td><div class="line-block">
<div class="line">字节4-7</div>
<div class="line">字节8-11</div>
</div>
</td>
<td><div class="line-block">
<div class="line">字节12-15</div>
<div class="line">字节16-19</div>
</div>
</td>
<td><p>字节20-23</p></td>
<td><p>字节24-27</p></td>
</tr>
</tbody>
</table>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 20%">
<col style="width: 20%">
<col style="width: 20%">
<col style="width: 20%">
<col style="width: 20%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="5"><p><strong>fw0_version 和fw1_version TLV编码</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><strong>maj</strong></p></td>
<td><p><strong>分</strong></p></td>
<td><p><strong>patch</strong></p></td>
<td><p><strong>res</strong></p></td>
<td><p><strong>var</strong></p></td>
</tr>
<tr class="row-odd"><td><p>24 - 31 位</p></td>
<td><p>16 - 23 位</p></td>
<td><p>8 - 15位</p></td>
<td><p>4 - 7 位</p></td>
<td><p>0- 3 位</p></td>
</tr>
</tbody>
</table>
</div>


           </div>
