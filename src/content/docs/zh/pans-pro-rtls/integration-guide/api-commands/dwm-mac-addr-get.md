---
title: "dwm_mac_addr_get"
lang: zh
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-mac-addr-get"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/api-commands/dwm-mac-addr-get/"
order: 198
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-mac-addr-get">
<span id="id1"></span><h1>dwm_mac_addr_get</h1>
<p>获取设备使用的 MAC 地址列表. 设备会使用用户指定的地址或默认地址. 每个接口的默认 MAC 地址只能更改一次，方法是调用 <em>dwm_mac_addr_set_once</em> 将其写入 OTP 内存，并成为新的默认 MAC 地址. 用户可通过调用 <em>dwm_mac_addr_set</em> 设置自定义 MAC 地址. 默认 MAC 地址在被用户修改后可通过出厂重置恢复 (参见 <em>dwm_factory_reset</em>). 设备使用列表中的 MAC 地址与特定接口的固定映射，如下所示：</p>
<ol class="arabic simple">
<li><p>UWB</p></li>
<li><p>BLE</p></li>
<li><p>以太网</p></li>
<li><p>无线网络</p></li>
</ol>
<p>BLE 地址可以是随机 BLE 地址或公共 BLE 地址. 如果不支持特定接口，列表中相应的 MAC 地址将为空。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_mac_addr_get">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_mac_addr_get</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">dwm_mac_addr_list_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">mac_addr_list</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">参数</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a>, type_0, type_1, type_2, type_3, mac_addr_0, mac_addr_1, mac_addr_2, mac_addr_3</p></li>
<li><p><strong>type_N</strong> – 状态，标志（<em>描述列表中索引 0 的 MAC 地址的类型</em>）。</p></li>
<li><p><strong>status</strong> – 2 bits (* status of the MAC address: MAC_ADDR_EMPTY = 0, MAC_ADDR_DEFAULT = 1, MAC_ADDR_USER_SPECIFIED = 2, MAC_ADDR_MUTABLE_DEFAULT = 3*)</p></li>
<li><p><strong>flags</strong> – 6 bits（<em>如果地址为 PUBLIC_BLE_ADDR，则设置第 0 位，其余位保留供将来使用</em>）。</p></li>
<li><p><strong>mac_addr_N</strong> – 48 位数值 (<em>小端序</em>)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C代码示例</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_mac_addr_list_t</span><span class="w"> </span><span class="n">mac_addr_list</span><span class="p">;</span>
<span class="nl">rv</span><span class="p">:</span><span class="w"> </span><span class="n">dwm_mac_addr_get</span><span class="p">(</span><span class="o">&amp;</span><span class="n">mac_addr_list</span><span class="p">);</span>
<span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">rv</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="n">DWM_OK</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">  </span><span class="n">printf</span><span class="p">(</span><span class="s">"UWB MAC 0x%02x%02x%02x%02x%02x%02x status=x%02x</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span>
<span class="w">  </span><span class="n">mac_addr_list</span><span class="p">.</span><span class="n">mac</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">0</span><span class="p">],</span>
<span class="w">  </span><span class="n">mac_addr_list</span><span class="p">.</span><span class="n">mac</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">1</span><span class="p">],</span>
<span class="w">  </span><span class="n">mac_addr_list</span><span class="p">.</span><span class="n">mac</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">2</span><span class="p">],</span>
<span class="w">  </span><span class="n">mac_addr_list</span><span class="p">.</span><span class="n">mac</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">3</span><span class="p">],</span>
<span class="w">  </span><span class="n">mac_addr_list</span><span class="p">.</span><span class="n">mac</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">4</span><span class="p">],</span>
<span class="w">  </span><span class="n">mac_addr_list</span><span class="p">.</span><span class="n">mac</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">5</span><span class="p">],</span>
<span class="w">  </span><span class="n">mac_addr_list</span><span class="p">.</span><span class="n">type</span><span class="p">[</span><span class="mi">0</span><span class="p">].</span><span class="n">status</span><span class="p">);</span>
<span class="p">}</span><span class="w"> </span><span class="k">else</span><span class="w"> </span><span class="p">{</span>
<span class="w">  </span><span class="n">printf</span><span class="p">(</span><span class="s">"can't get MAC address list, error %d</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">rv</span><span class="p">);</span>
<span class="p">}</span>
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
<tr class="row-odd"><td><p>0x83</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>类型0x83 (131 dec) 表示指令 dwm_mac_addr_get</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 51%">
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
<td rowspan="2"><p>0xC1</p></td>
<td rowspan="2"><p>0x18</p></td>
<td><div class="line-block">
<div class="line">(字节 0-4）列表中 MAC 地址的类型</div>
</div>
<div class="line-block">
<div class="line">(字节 5-10) MAC 地址 0，小端序</div>
<div class="line">(字节 11-16) MAC 地址 1，小端序</div>
<div class="line">(字节 17-22) MAC 地址 2，小端序</div>
<div class="line">(字节 23-28) MAC 地址 3，小端序</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>…</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">类型0x40表示 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a> 上一条命令的状态码</div>
<div class="line">类型 0xC1(193 dec) 表示 MAC 地址列表</div>
</div>
<p><strong>MAC地址标志编码</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 11%">
<col style="width: 11%">
<col style="width: 11%">
<col style="width: 11%">
<col style="width: 11%">
<col style="width: 11%">
<col style="width: 11%">
<col style="width: 11%">
<col style="width: 11%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="9"><p>MAC 地址列表的标志</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td colspan="2"><p>字节 0</p></td>
<td colspan="3"><p>字节1</p></td>
<td colspan="2"><p>字节2</p></td>
<td colspan="2"><p>字节3</p></td>
</tr>
<tr class="row-odd"><td><p>2-7 位</p></td>
<td><p>0-1位</p></td>
<td><p>11-15位</p></td>
<td><p>10位</p></td>
<td><p>8-9位</p></td>
<td><p>18-23位</p></td>
<td><p>16-17 位</p></td>
<td><p>26-31位</p></td>
<td><p>24-25位</p></td>
</tr>
<tr class="row-even"><td><p>R</p></td>
<td><p>S_0</p></td>
<td><p>R</p></td>
<td><p>P_1</p></td>
<td><p>S_1</p></td>
<td><p>R</p></td>
<td><p>S_2</p></td>
<td><p>R</p></td>
<td><p>S_3</p></td>
</tr>
</tbody>
</table>
<p>R 表示保留供将来使用. S_0, S_1, S_2, S_3 表示 MAC 地址状态. 状态可以有以下值:</p>
<blockquote>
<div><ul class="simple">
<li><p>0 - 空 MAC 地址</p></li>
<li><p>1 - OTP 内存中的默认 MAC 地址。</p></li>
<li><p>2 - 用户指定的 MAC 地址</p></li>
<li><p>3 - 可变的默认 MAC 地址，只能使用 <em>dwm_mac_addr_set_once</em> 重写一次。</p></li>
</ul>
</div></blockquote>
<p>如果 BLE 地址是公共 BLE 地址，则设置 P_1。 如果 BLE MAC 地址是随机的，则清除该标志。 有关 BLE 地址类型的更多信息，请参阅 BLE 规范。</p>
</div>


           </div>
