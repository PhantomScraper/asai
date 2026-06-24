---
title: "dwm_nvm_usr_data_get"
lang: zh
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-nvm-usr-data-get"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/api-commands/dwm-nvm-usr-data-get/"
order: 202
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-nvm-usr-data-get">
<span id="id1"></span><h1>dwm_nvm_usr_data_get</h1>
<p>从非易失性内存读取用户数据。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_nvm_usr_data_get">
<span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_nvm_usr_data_get</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">uint8_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">data</span></span>, <span class="n"><span class="pre">uint8_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">len</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">参数</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> – len (<em>缓冲区长度</em>)</p></li>
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a>, data, len</p></li>
<li><p><strong>data</strong> – 最大 250 字节 (<em>之前存储在非易失性存储器中的用户数据</em>)</p></li>
<li><p><strong>len</strong> – 1字节 (<em>数据长度，最多250字节</em>)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C代码示例</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="kt">uint8_t</span><span class="w"> </span><span class="n">buf</span><span class="p">[</span><span class="n">DWM_NVM_USR_DATA_LEN_MAX</span><span class="p">];</span>
<span class="kt">uint8_t</span><span class="w"> </span><span class="n">len</span><span class="p">;</span>
<span class="kt">int</span><span class="w"> </span><span class="n">rv</span><span class="p">;</span>
<span class="n">len</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="n">buf</span><span class="p">);</span>
<span class="n">rv</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">dwm_nvm_usr_data_get</span><span class="p">(</span><span class="n">buf</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">len</span><span class="p">);</span>
<span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">rv</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="n">DWM_ERR_OVERRUN</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">  </span><span class="n">printf</span><span class="p">(</span><span class="s">"expected length = %d</span><span class="se">\n</span><span class="s">”, len);</span>
<span class="p">}</span>
</pre></div>
</div>
<p><strong>SPI/UART 示例</strong></p>
<p>这些接口不可用</p>
</div>


           </div>
