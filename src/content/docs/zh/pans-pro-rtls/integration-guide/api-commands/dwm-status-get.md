---
title: "dwm_status_get"
lang: zh
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-status-get"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/api-commands/dwm-status-get/"
order: 210
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-status-get">
<span id="id1"></span><h1>dwm_status_get</h1>
<p>获取系统状态. 可使用以下标志:</p>
<ul class="simple">
<li><p>位置数据就绪</p></li>
<li><p>节点加入 UWB 网络</p></li>
<li><p>新的回程数据准备就绪</p></li>
<li><p>回程状态已更改</p></li>
<li><p>回程路由已初始化</p></li>
<li><p>UWB 扫描结果已准备就绪</p></li>
<li><p>通过 UWB 接收到用户数据</p></li>
<li><p>通过 UWB 发送用户数据</p></li>
<li><p>固件更新中</p></li>
</ul>
<p>调用后清除标志，以下情况除外:</p>
<ul class="simple">
<li><p>节点加入 UWB 网络</p></li>
<li><p>回程路由已初始化</p></li>
<li><p>固件更新中</p></li>
</ul>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_status_get">
<span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_status_get</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">dwm_status_t</span></span><span class="p"><span class="pre">*</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">参数</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> – (<em>无</em>)</p></li>
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a>, 状态</p></li>
<li><p><strong>status</strong> – loc_ready, uwbmac_joined, bh_data_ready, bh_initialized, bh_status_changed, uwb_scan_ready, usr_data_ready</p></li>
<li><p><strong>loc_ready</strong> – ‘0’ | ‘1’ (<em>新的位置数据已准备就绪</em>)</p></li>
<li><p><strong>uwbmac_joined</strong> – ‘0’ | ‘1’ (<em>节点已连接到 UWB 网络</em>)</p></li>
<li><p><strong>bh_data_ready</strong> – ‘0’ | ‘1’ (<em>UWB MAC 回程数据准备就绪</em>)</p></li>
<li><p><strong>bh_status_changed</strong> – ‘0’ | ‘1’ (<em>UWB MAC状态已改变，用于回程</em>)</p></li>
<li><p><strong>bh_initialized</strong> – ‘0’ | ‘1’ (<em>节点已通过 UWB 回程初始化路由</em>)</p></li>
<li><p><strong>uwb_scan_ready</strong> – ‘0’ | ‘1’ (<em>UWB扫描结果已准备就绪</em>)</p></li>
<li><p><strong>usr_data_ready</strong> – ‘0’ | ‘1’ (<em>UWB用户数据已收到</em>)</p></li>
<li><p><strong>usr_data_sent</strong> – ‘0’ | ‘1’ (<em>通过 UWB 发送用户数据</em>)</p></li>
<li><p><strong>fwup_in_progress</strong> – ‘0’ | ‘1’ (<em>固件更新中</em>)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C代码示例</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_status_t</span><span class="w"> </span><span class="n">status</span><span class="p">;</span>
<span class="kt">int</span><span class="w"> </span><span class="n">rv</span><span class="p">;</span>
<span class="n">rv</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">dwm_status_get</span><span class="p">(</span><span class="o">&amp;</span><span class="n">status</span><span class="p">);</span>
<span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">rv</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="n">DWM_OK</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="n">printf</span><span class="p">(</span><span class="s">"loc_data: %d</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">status</span><span class="p">.</span><span class="n">loc_dat1</span><span class="p">);</span>
<span class="w">    </span><span class="n">printf</span><span class="p">(</span><span class="s">"uwbmac_joined: %d</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">status</span><span class="p">.</span><span class="n">uwbmac_joined</span><span class="p">);</span>
<span class="w">    </span><span class="n">printf</span><span class="p">(</span><span class="s">"bh_data_ready: %d</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">status</span><span class="p">.</span><span class="n">bh_data_ready</span><span class="p">);</span>
<span class="w">    </span><span class="n">printf</span><span class="p">(</span><span class="s">"bh_status_changed: %d</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">status</span><span class="p">.</span><span class="n">bh_status_changed</span><span class="p">);</span>
<span class="w">    </span><span class="n">printf</span><span class="p">(</span><span class="s">"bh_initialized: %d</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">status</span><span class="p">.</span><span class="n">bh_initialized</span><span class="p">);</span>
<span class="w">    </span><span class="n">printf</span><span class="p">(</span><span class="s">"uwb_scan_ready: %d</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">status</span><span class="p">.</span><span class="n">uwb_scan_ready</span><span class="p">);</span>
<span class="w">    </span><span class="n">printf</span><span class="p">(</span><span class="s">"usr_data_ready: %d</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">status</span><span class="p">.</span><span class="n">usr_data_ready</span><span class="p">);</span>
<span class="w">    </span><span class="n">printf</span><span class="p">(</span><span class="s">"usr_data_sent: %d</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">status</span><span class="p">.</span><span class="n">usr_data_sent</span><span class="p">);</span>
<span class="w">    </span><span class="n">printf</span><span class="p">(</span><span class="s">"fwup_in_progress: %d</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">status</span><span class="p">.</span><span class="n">fwup_in_progress</span><span class="p">);</span>
<span class="p">}</span>
<span class="k">else</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="n">printf</span><span class="p">(</span><span class="s">"error</span><span class="se">\n</span><span class="s">"</span><span class="p">);</span>
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
<tr class="row-odd"><td><p>0x32</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>0x32 表示指令 dwm_status_get</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 32%">
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
<td rowspan="2"><p>0x5A</p></td>
<td rowspan="2"><p>0x02</p></td>
<td><p>loc_ready (bit 0)
uwbmac_joined (bit 1)
bh_status_changed (bit 2)
bh_data_ready (bit 3)
bh_initialized (bit 4)
uwb_scan_ready (bit 5)
usr_data_ready(bit 6)
usr_data_sent(bit 7)
fwup_in_progress(bit 8)
reserved (bits 9-15)</p></td>
</tr>
<tr class="row-even"><td><p>0x01 0x00</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">类型0x5A表示状态</div>
<div class="line">类型0x40表示 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a> 上一条命令的状态码</div>
</div>
</div>


           </div>
