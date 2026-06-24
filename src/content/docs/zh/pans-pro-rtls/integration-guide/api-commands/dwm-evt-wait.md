---
title: "dwm_evt_wait"
lang: zh
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-evt-wait"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/api-commands/dwm-evt-wait/"
order: 181
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-evt-wait">
<span id="id1"></span><h1>dwm_evt_wait</h1>
<p>用于等待来自 DWM 模块的事件. 首先，用户必须通过 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-evt-listener-register#dwm-evt-listener-register"><span class="std std-ref">dwm_evt_listener_register</span></a> 注册事件. 如果监听器已注册，且 <a class="reference internal" href="#dwm-evt-wait"><span class="std std-ref">dwm_evt_wait</span></a> 未用于消耗事件，则事件缓冲区将溢出. <a class="reference internal" href="#dwm-evt-wait"><span class="std std-ref">dwm_evt_wait</span></a> 会阻塞并休眠，直到下一个事件发生。</p>
<p>用户可以等待的事件:</p>
<ul class="simple">
<li><p>DWM_EVT_LOC_READY</p></li>
<li><p>DWM_EVT_USR_DATA_READY</p></li>
<li><p>DWM_EVT_USR_DATA_SENT</p></li>
<li><p>DWM_EVT_BH_INITIALIZED</p></li>
<li><p>DWM_EVT_UWBMAC_JOINED_CHANGED</p></li>
<li><p>DWM_EVT_UWB_SCAN_READY</p></li>
</ul>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_evt_wait">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_evt_wait</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">dwm_evt_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">evt</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">参数</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> – (<em>无</em>)</p></li>
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a>, evt</p></li>
<li><p><strong>evt</strong> – loc_ready | usr_data_ready | usr_data_sent | uwb_scan_ready | bh_initialized_changed | uwbmac_joined_changed</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C代码示例</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="kt">void</span><span class="w"> </span><span class="nf">on_dwm_evt</span><span class="p">(</span><span class="n">dwm_evt_t</span><span class="w"> </span><span class="o">*</span><span class="n">p_evt</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">     </span><span class="kt">int</span><span class="w"> </span><span class="n">i</span><span class="p">;</span>
<span class="w">     </span><span class="k">switch</span><span class="w"> </span><span class="p">(</span><span class="n">p_evt</span><span class="o">-&gt;</span><span class="n">header</span><span class="p">.</span><span class="n">id</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">     </span><span class="cm">/* New location data */</span>
<span class="w">     </span><span class="k">case</span><span class="w"> </span><span class="no">DWM_EVT_LOC_READY</span><span class="p">:</span>
<span class="w">             </span><span class="n">printf</span><span class="p">(</span><span class="s">"</span><span class="se">\n</span><span class="s">T:%lu "</span><span class="p">,</span><span class="w"> </span><span class="n">dwm_systime_us_get</span><span class="p">());</span>
<span class="w">             </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">p_evt</span><span class="o">-&gt;</span><span class="n">loc</span><span class="p">.</span><span class="n">pos_available</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">                     </span><span class="n">printf</span><span class="p">(</span><span class="s">"POS:[%ld,%ld,%ld,%u] "</span><span class="p">,</span><span class="w"> </span><span class="n">p_evt</span><span class="o">-&gt;</span><span class="n">loc</span><span class="p">.</span><span class="n">pos</span><span class="p">.</span><span class="n">x</span><span class="p">,</span>
<span class="w">                                     </span><span class="n">p_evt</span><span class="o">-&gt;</span><span class="n">loc</span><span class="p">.</span><span class="n">pos</span><span class="p">.</span><span class="n">y</span><span class="p">,</span><span class="w"> </span><span class="n">p_evt</span><span class="o">-&gt;</span><span class="n">loc</span><span class="p">.</span><span class="n">pos</span><span class="p">.</span><span class="n">z</span><span class="p">,</span>
<span class="w">                                     </span><span class="n">p_evt</span><span class="o">-&gt;</span><span class="n">loc</span><span class="p">.</span><span class="n">pos</span><span class="p">.</span><span class="n">qf</span><span class="p">);</span>
<span class="w">             </span><span class="p">}</span><span class="w"> </span><span class="k">else</span><span class="w"> </span><span class="p">{</span>
<span class="w">                     </span><span class="n">printf</span><span class="p">(</span><span class="s">"Location engine is disabled</span><span class="se">\n</span><span class="s">"</span><span class="p">);</span>
<span class="w">             </span><span class="p">}</span>

<span class="w">             </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">p_evt</span><span class="o">-&gt;</span><span class="n">loc</span><span class="p">.</span><span class="n">anchors</span><span class="p">.</span><span class="n">dist</span><span class="p">.</span><span class="n">cnt</span><span class="p">;</span><span class="w"> </span><span class="o">++</span><span class="n">i</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">                     </span><span class="n">printf</span><span class="p">(</span><span class="s">"DIST%d:"</span><span class="p">,</span><span class="w"> </span><span class="n">i</span><span class="p">);</span>

<span class="w">                     </span><span class="n">printf</span><span class="p">(</span><span class="s">"0x%04X"</span><span class="p">,</span><span class="w"> </span><span class="p">(</span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="p">)(</span><span class="n">p_evt</span><span class="o">-&gt;</span><span class="n">loc</span><span class="p">.</span><span class="n">anchors</span><span class="p">.</span><span class="n">dist</span><span class="p">.</span><span class="n">addr</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">&amp;</span><span class="w"> </span><span class="mh">0xffff</span><span class="p">));</span>
<span class="w">                     </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">p_evt</span><span class="o">-&gt;</span><span class="n">loc</span><span class="p">.</span><span class="n">anchors</span><span class="p">.</span><span class="n">an_pos</span><span class="p">.</span><span class="n">cnt</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">                             </span><span class="n">printf</span><span class="p">(</span><span class="s">"[%ld,%ld,%ld]"</span><span class="p">,</span><span class="w">                                         </span><span class="n">p_evt</span><span class="o">-&gt;</span><span class="n">loc</span><span class="p">.</span><span class="n">anchors</span><span class="p">.</span><span class="n">an_pos</span><span class="p">.</span><span class="n">pos</span><span class="p">[</span><span class="n">i</span><span class="p">].</span><span class="n">x</span><span class="p">,</span><span class="w">                                             </span><span class="n">p_evt</span><span class="o">-&gt;</span><span class="n">loc</span><span class="p">.</span><span class="n">anchors</span><span class="p">.</span><span class="n">an_pos</span><span class="p">.</span><span class="n">pos</span><span class="p">[</span><span class="n">i</span><span class="p">].</span><span class="n">y</span><span class="p">,</span><span class="w">                                             </span><span class="n">p_evt</span><span class="o">-&gt;</span><span class="n">loc</span><span class="p">.</span><span class="n">anchors</span><span class="p">.</span><span class="n">an_pos</span><span class="p">.</span><span class="n">pos</span><span class="p">[</span><span class="n">i</span><span class="p">].</span><span class="n">z</span><span class="p">);</span>
<span class="w">                     </span><span class="p">}</span>
<span class="w">                     </span><span class="n">printf</span><span class="p">(</span><span class="s">"=[%lu,%u] "</span><span class="p">,</span><span class="w"> </span><span class="n">p_evt</span><span class="o">-&gt;</span><span class="n">loc</span><span class="p">.</span><span class="n">anchors</span><span class="p">.</span><span class="n">dist</span><span class="p">.</span><span class="n">dist</span><span class="p">[</span><span class="n">i</span><span class="p">],</span>
<span class="w">                                     </span><span class="n">p_evt</span><span class="o">-&gt;</span><span class="n">loc</span><span class="p">.</span><span class="n">anchors</span><span class="p">.</span><span class="n">dist</span><span class="p">.</span><span class="n">qf</span><span class="p">[</span><span class="n">i</span><span class="p">]);</span>
<span class="w">             </span><span class="p">}</span>
<span class="w">             </span><span class="n">printf</span><span class="p">(</span><span class="s">"</span><span class="se">\n</span><span class="s">"</span><span class="p">);</span>
<span class="w">             </span><span class="k">break</span><span class="p">;</span>
<span class="w">     </span><span class="k">case</span><span class="w"> </span><span class="no">DWM_EVT_USR_DATA_READY</span><span class="p">:</span>
<span class="w">             </span><span class="n">printf</span><span class="p">(</span><span class="s">"hex:"</span><span class="p">);</span>
<span class="w">             </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">p_evt</span><span class="o">-&gt;</span><span class="n">header</span><span class="p">.</span><span class="n">len</span><span class="w"> </span><span class="o">-</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="n">dwm_evt_hdr_t</span><span class="p">);</span><span class="w"> </span><span class="o">++</span><span class="n">i</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">                     </span><span class="n">printf</span><span class="p">(</span><span class="s">"%02x "</span><span class="p">,</span><span class="w"> </span><span class="n">p_evt</span><span class="o">-&gt;</span><span class="n">usr_data</span><span class="p">[</span><span class="n">i</span><span class="p">]);</span>
<span class="w">             </span><span class="p">}</span>
<span class="w">             </span><span class="n">printf</span><span class="p">(</span><span class="s">"</span><span class="se">\n</span><span class="s">"</span><span class="p">);</span>
<span class="w">             </span><span class="k">break</span><span class="p">;</span>
<span class="w">     </span><span class="k">case</span><span class="w"> </span><span class="no">DWM_EVT_USR_DATA_SENT</span><span class="p">:</span>
<span class="w">             </span><span class="n">printf</span><span class="p">(</span><span class="s">"iot sent</span><span class="se">\n</span><span class="s">"</span><span class="p">);</span>
<span class="w">             </span><span class="k">break</span><span class="p">;</span>
<span class="w">     </span><span class="k">case</span><span class="w"> </span><span class="no">DWM_EVT_UWB_SCAN_READY</span><span class="p">:</span>
<span class="w">             </span><span class="n">printf</span><span class="p">(</span><span class="s">"[mode,rssi]: "</span><span class="p">);</span>
<span class="w">             </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">p_evt</span><span class="o">-&gt;</span><span class="n">uwb_scan</span><span class="p">.</span><span class="n">cnt</span><span class="p">;</span><span class="w"> </span><span class="o">++</span><span class="n">i</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">                     </span><span class="n">printf</span><span class="p">(</span><span class="s">"[%u, %d]"</span><span class="p">,</span><span class="w"> </span><span class="n">p_evt</span><span class="o">-&gt;</span><span class="n">uwb_scan</span><span class="p">.</span><span class="n">mode</span><span class="p">[</span><span class="n">i</span><span class="p">],</span><span class="w"> </span><span class="n">p_evt</span><span class="o">-&gt;</span><span class="n">uwb_scan</span><span class="p">.</span><span class="n">rssi</span><span class="p">[</span><span class="n">i</span><span class="p">]);</span>
<span class="w">             </span><span class="p">}</span>
<span class="w">             </span><span class="n">printf</span><span class="p">(</span><span class="s">"</span><span class="se">\n</span><span class="s">"</span><span class="p">);</span>
<span class="w">             </span><span class="k">break</span><span class="p">;</span>

<span class="w">     </span><span class="k">case</span><span class="w"> </span><span class="no">DWM_EVT_BH_INITIALIZED_CHANGED</span><span class="p">:</span>
<span class="w">             </span><span class="n">printf</span><span class="p">(</span><span class="s">"backhaul available = %d</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">p_evt</span><span class="o">-&gt;</span><span class="n">bh_initialized</span><span class="p">);</span>
<span class="w">             </span><span class="k">break</span><span class="p">;</span>
<span class="w">     </span><span class="k">case</span><span class="w"> </span><span class="no">DWM_EVT_UWBMAC_JOINED_CHANGED</span><span class="p">:</span>
<span class="w">             </span><span class="n">printf</span><span class="p">(</span><span class="s">"UWBMAC joined = %d</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">p_evt</span><span class="o">-&gt;</span><span class="n">uwbmac_joined</span><span class="p">);</span>
<span class="w">             </span><span class="k">break</span><span class="p">;</span>
<span class="w">     </span><span class="k">default</span><span class="o">:</span>
<span class="w">             </span><span class="k">break</span><span class="p">;</span>
<span class="w">     </span><span class="p">}</span>

<span class="w">     </span><span class="cm">/* Indicate the application has finished the tasks and can now */</span>
<span class="w">     </span><span class="n">dwm_sleep</span><span class="p">();</span>
<span class="p">}</span>
<span class="cm">/* … */</span>
<span class="kt">int</span><span class="w"> </span><span class="n">rv</span><span class="p">;</span>
<span class="n">dwm_evt_t</span><span class="w"> </span><span class="n">evt</span><span class="p">;</span>
<span class="n">rv</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">dwm_evt_wait</span><span class="p">(</span><span class="o">&amp;</span><span class="n">evt</span><span class="p">);</span>
<span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">rv</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="n">DWM_ERR_OVERRUN</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">     </span><span class="n">printf</span><span class="p">(</span><span class="s">"event buffer overflow</span><span class="se">\n</span><span class="s">"</span><span class="p">);</span>
<span class="p">}</span><span class="w"> </span><span class="k">else</span><span class="w"> </span><span class="p">{</span>
<span class="w">     </span><span class="n">on_dwm_evt</span><span class="p">(</span><span class="o">&amp;</span><span class="n">evt</span><span class="p">);</span>
<span class="p">}</span>
</pre></div>
</div>
<p><strong>SPI/UART 示例</strong></p>
<p>这些接口不可用</p>
</div>


           </div>
