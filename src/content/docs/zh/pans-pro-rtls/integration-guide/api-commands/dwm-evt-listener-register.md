---
title: "dwm_evt_listener_register"
lang: zh
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-evt-listener-register"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/api-commands/dwm-evt-listener-register/"
order: 180
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-evt-listener-register">
<span id="id1"></span><h1>dwm_evt_listener_register</h1>
<p>在用户应用程序中，该命令用于注册以监听来自固件的事件。 例如，可以在 LE 完成位置计算和距离计算时触发事件。 该调用仅适用于最终用户应用，不能与 SPI 或 UART 一起使用。 在低功耗模式下，必须注册事件监听器才能从休眠状态唤醒。 否则，用户应用程序将一直处于休眠状态。</p>
<p>用户可以监听的事件:</p>
<ul class="simple">
<li><p>DWM_EVT_LOC_READY</p></li>
<li><p>DWM_EVT_USR_DATA_READY</p></li>
<li><p>DWM_EVT_USR_DATA_SENT</p></li>
<li><p>DWM_EVT_BH_INITIALIZED</p></li>
<li><p>DWM_EVT_UWBMAC_JOINED_CHANGED</p></li>
<li><p>DWM_EVT_UWB_SCAN_READY</p></li>
</ul>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_evt_listener_register">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_evt_listener_register</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">uint32_t</span></span><span class="w"> </span><span class="n"><span class="pre">evt_id_map</span></span>, <span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">context</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">参数</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> – event_id_map, context</p></li>
<li><p><strong>event_id_map</strong> – 32 位宽的位图（用户希望/不希望监听的事件的标志必须分别设置/清除，参见 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-evt-wait#dwm-evt-wait"><span class="std std-ref">dwm_evt_wait</span></a>)</p></li>
<li><p><strong>context</strong> – 用户想要传递给回调上下文的数据</p></li>
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C代码示例</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_evt_listener_register</span><span class="p">(</span><span class="n">DWM_EVT_LOC_READY</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="n">DWM_EVT_USR_DATA_READY</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="n">DWM_EVT_USR_DATA_SENT</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="n">DWM_EVT_UWB_SCAN_READY</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="n">DWM_EVT_BH_INITIALIZED</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="n">DWM_EVT_UWBMAC_JOINED_CHANGED</span><span class="p">,</span><span class="w"> </span><span class="nb">NULL</span><span class="p">);</span>
</pre></div>
</div>
<p><strong>SPI/UART 示例</strong></p>
<p>这些接口不可用</p>
</div>


           </div>
