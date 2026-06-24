---
title: "dwm_nvm_usr_data_set"
lang: en
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-nvm-usr-data-set"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/api-commands/dwm-nvm-usr-data-set/"
order: 204
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-nvm-usr-data-set">
<span id="id1"></span><h1>dwm_nvm_usr_data_set</h1>
<p>Stores user data to non-volatile memory and writes internal non-volatile memory,
which must be used carefully. Old data is rewritten.</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_nvm_usr_data_set">
<span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_nvm_usr_data_set</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">uint8_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">data</span></span>, <span class="n"><span class="pre">uint8_t</span></span><span class="w"> </span><span class="n"><span class="pre">len</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> – data, len</p></li>
<li><p><strong>data</strong> – 250 bytes max (<em>the user data to be written</em>)</p></li>
<li><p><strong>len</strong> – 1 byte (<em>data length, 250 bytes max</em>)</p></li>
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">Status code</span></a></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C code example</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="kt">uint8_t</span><span class="w"> </span><span class="n">buf</span><span class="p">[</span><span class="n">DWM_NVM_USR_DATA_LEN_MAX</span><span class="p">];</span>
<span class="kt">uint8_t</span><span class="w"> </span><span class="n">len</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">DWM_NVM_USR_DATA_LEN_MAX</span><span class="p">;</span>
<span class="kt">int</span><span class="w"> </span><span class="n">rv</span><span class="p">;</span>
<span class="n">rv</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">dwm_nvm_usr_data_set</span><span class="p">(</span><span class="n">buf</span><span class="p">,</span><span class="w"> </span><span class="n">len</span><span class="p">);</span>
<span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">DWM_OK</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="n">rv</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">   </span><span class="n">printf</span><span class="p">(</span><span class="s">"ok</span><span class="se">\n</span><span class="s">”);</span>
<span class="p">}</span>
<span class="k">else</span>
<span class="p">{</span>
<span class="w">   </span><span class="n">printf</span><span class="p">(</span><span class="s">"error, %d”, rv);</span>
<span class="p">}</span>
</pre></div>
</div>
<p><strong>SPI/UART example</strong></p>
<blockquote>
<div><p>Not available on these interfaces.</p>
</div></blockquote>
</div>


           </div>
