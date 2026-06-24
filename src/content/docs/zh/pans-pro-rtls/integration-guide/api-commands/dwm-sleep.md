---
title: "dwm_sleep"
lang: zh
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-sleep"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/api-commands/dwm-sleep/"
order: 129
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-sleep">
<span id="id1"></span><h1>dwm_sleep</h1>
<p>使设备进入睡眠状态（如果处于低功耗模式）。 如有必要，睡眠模式可在内部延迟。 简单地说，调用 dwm_sleep 后，设备并不能保证立即进入睡眠模式。 如果在用户应用程序中使用，则只能在线程上下文中调用该函数。 这个函数会阻塞，直到 dwm_wake_up 被调用。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_sleep">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_sleep</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">参数</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> – 无</p></li>
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C代码示例</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="cm">/* THREAD 1: sleep and block*/</span>
<span class="n">dwm_sleep</span><span class="p">();</span>
<span class="cm">/*do something*/</span>
<span class="p">...</span>
<span class="cm">/*THREAD 2: wait until event */</span>
<span class="n">dwm_evt_wait</span><span class="p">(</span><span class="o">&amp;</span><span class="n">evt</span><span class="p">);</span>
<span class="cm">/*unblock dwm_sleep()*/</span>
<span class="n">dwm_wake_up</span><span class="p">();</span>
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
<tr class="row-odd"><td><p>0x0A</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>类型0x0A 表示命令 dwm_sleep</p>
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
