---
title: "dwm_mac_addr_set_once"
lang: zh
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-mac-addr-set-once"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/api-commands/dwm-mac-addr-set-once/"
order: 199
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-mac-addr-set-once">
<span id="id1"></span><h1>dwm_mac_addr_set_once</h1>
<p>将 MAC 地址列表写入 OTP 内存，必须小心使用！写入后的值将无法修改！它的目的是在生产阶段为 UWB, BLE, 以太网或 Wi-Fi 接口使用的设备提供一个 MAC 地址池。 目前，MAC 地址列表分配给不同接口的情况如下：</p>
<ul class="simple">
<li><p>MAC 地址0分配给UWB 接口. 两个最小有效字节必须不等于 0x0000 或 0xFFFF。</p></li>
<li><p>MAC 地址 1 已分配给 BLE 接口. 该地址将用作公共 BLE 地址。</p></li>
<li><p>MAC 地址 2 和 MAC 地址 3 分别分配给以太网和 Wi-Fi 接口. 地址应采用 EUI-48 格式，并尊重 LAA/UAA 和 U/I 位。</p></li>
</ul>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_mac_addr_set_once">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_mac_addr_set_once</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">dwm_mac_addr_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">addr</span></span>, <span class="n"><span class="pre">uint8_t</span></span><span class="w"> </span><span class="n"><span class="pre">count</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">参数</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> – mac_addr_0, [mac_addr_1], [mac_addr_2], [mac_addr_3]</p></li>
<li><p><strong>mac_addr_0</strong> – 48 位值 (<em>UWB MAC 地址，小端序</em>)</p></li>
<li><p><strong>mac_addr_1</strong> – 48 位值 (<em>BLE MAC 地址，小端序</em>)</p></li>
<li><p><strong>mac_addr_2</strong> – 48 位值 (<em>以太网 MAC 地址，小端序</em>)</p></li>
<li><p><strong>mac_addr_3</strong> – 48 位值 (<em>WIFI MAC 地址，小端序</em>)</p></li>
<li><p><strong>output:</strong> – <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C代码示例</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_mac_addr_list_t</span><span class="w"> </span><span class="n">mac_addr_list</span><span class="p">;</span>
<span class="n">dwm_mac_addr_get</span><span class="p">(</span><span class="o">&amp;</span><span class="n">mac_addr_list</span><span class="p">);</span>
<span class="n">memcpy</span><span class="p">(</span><span class="n">mac_addr_list</span><span class="p">.</span><span class="n">mac</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span><span class="w"> </span><span class="p">(</span><span class="kt">uint8_t</span><span class="p">[</span><span class="n">DWM_MAC_ADDR_LEN</span><span class="p">]){</span><span class="mh">0xaa</span><span class="p">,</span><span class="w"> </span><span class="mh">0xbb</span><span class="p">,</span><span class="w"> </span><span class="mh">0xcc</span><span class="p">,</span><span class="w"> </span><span class="mh">0xdd</span><span class="p">,</span><span class="w"> </span><span class="mh">0xee</span><span class="p">,</span><span class="w"> </span><span class="mh">0xff</span><span class="p">},</span><span class="w"> </span><span class="n">DWM_MAC_ADDR_LEN</span><span class="p">);</span>
<span class="nl">rv</span><span class="p">:</span><span class="w"> </span><span class="n">dwm_mac_addr_set</span><span class="p">(</span><span class="o">&amp;</span><span class="n">mac_addr_list</span><span class="p">);</span>
<span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">rv</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="n">DWM_OK</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">  </span><span class="n">printf</span><span class="p">(</span><span class="s">"can't set MAC address list, error %d</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">rv</span><span class="p">);</span>
<span class="p">}</span>
</pre></div>
</div>
<p><strong>SPI/UART 示例</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 22%">
<col style="width: 22%">
<col style="width: 56%">
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
<tr class="row-odd"><td rowspan="2"><p>0x82</p></td>
<td rowspan="2"><p>0x18</p></td>
<td><div class="line-block">
<div class="line">(字节0-5) MAC 地址 0，小端序</div>
<div class="line">(字节6-11) MAC 地址 1，小端序</div>
<div class="line">(字节12-17) MAC 地址 2，小端序</div>
<div class="line">(字节18-23) MAC 地址 3，小端序</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>…</p></td>
</tr>
</tbody>
</table>
<p>类型 0x82 (130 dec) 表示命令 dwm_mac_addr_set_once</p>
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
