---
title: "dwm_mac_addr_set"
lang: zh
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-mac-addr-set"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/api-commands/dwm-mac-addr-set/"
order: 200
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-mac-addr-set">
<span id="id1"></span><h1>dwm_mac_addr_set</h1>
<p>设置 BLE, UWB, 以太网或 Wi-Fi 接口的 MAC 地址，需要重置后才能生效. 由于会写入内部非易失性存储器，因此不应频繁使用. 要使用默认 MAC 地址，需要进行出厂重置 (<em>dwm_factory_reset</em>). UWB MAC 地址的两个最小有效字节不得等于 0x0000 或 0xFFFF. BLE 地址可以是随机地址或公共 BLE 地址. 以太网和 Wi-Fi 地址必须遵守 EUI-48 格式，U/I 位必须相应设置。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_mac_addr_set">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_mac_addr_set</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">dwm_mac_addr_type_t</span></span><span class="w"> </span><span class="n"><span class="pre">type</span></span>, <span class="n"><span class="pre">dwm_mac_addr_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">addr</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">参数</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> – addr_type, addr_value</p></li>
<li><p><strong>addr_type</strong> – 8位整数(<em>0=UWB 地址, 1=BLE 随机地址, 2=BLE 公共地址, 3=ETH 地址, 4=WIFI 地址, ETH 和 WIFI 仅在网关上支持</em>)</p></li>
<li><p><strong>addr_value</strong> – 6 字节 (<em>6 字节长的 MAC 地址</em>)</p></li>
<li><p><strong>output:</strong> – <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C代码示例</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_mac_addr_t</span><span class="w"> </span><span class="n">addr</span><span class="p">;</span>
<span class="n">addr</span><span class="p">.</span><span class="n">bytes</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">:</span><span class="w"> </span><span class="mh">0xAA</span><span class="p">;</span>
<span class="n">addr</span><span class="p">.</span><span class="n">bytes</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">:</span><span class="w"> </span><span class="mh">0xBB</span><span class="p">;</span>
<span class="n">addr</span><span class="p">.</span><span class="n">bytes</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span><span class="o">:</span><span class="w"> </span><span class="mh">0xCC</span><span class="p">;</span>
<span class="n">addr</span><span class="p">.</span><span class="n">bytes</span><span class="p">[</span><span class="mi">3</span><span class="p">]</span><span class="o">:</span><span class="w"> </span><span class="mh">0xDD</span><span class="p">;</span>
<span class="n">addr</span><span class="p">.</span><span class="n">bytes</span><span class="p">[</span><span class="mi">4</span><span class="p">]</span><span class="o">:</span><span class="w"> </span><span class="mh">0xEE</span><span class="p">;</span>
<span class="n">addr</span><span class="p">.</span><span class="n">bytes</span><span class="p">[</span><span class="mi">5</span><span class="p">]</span><span class="o">:</span><span class="w"> </span><span class="mh">0xFF</span><span class="p">;</span>
<span class="kt">int</span><span class="w"> </span><span class="n">rv</span><span class="o">:</span><span class="w"> </span><span class="n">dwm_mac_addr_set</span><span class="p">(</span><span class="n">NODE_ADDR_TYPE_UWB</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">addr</span><span class="p">);</span>
<span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">rv</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="n">DWM_OK</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">  </span><span class="n">printf</span><span class="p">(</span><span class="s">"can't set node address, error %d</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">rv</span><span class="p">);</span>
<span class="p">}</span>
</pre></div>
</div>
<p><strong>SPI/UART 示例</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 26%">
<col style="width: 26%">
<col style="width: 48%">
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
<tr class="row-odd"><td rowspan="2"><p>0x2D</p></td>
<td rowspan="2"><p>0x07</p></td>
<td><div class="line-block">
<div class="line">0字节 :MAC 地址类型</div>
<div class="line">1-6字节:  小端 MAC 地址</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x00 0xEF 0xCD 0xAB
0x56 0x34 0x12</p></td>
</tr>
</tbody>
</table>
<p>类型 0x2D (45 dec)表示命令 dwm_mac_addr_set</p>
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
