---
title: "dwm_nvm_usr_data_set"
lang: ja
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-nvm-usr-data-set"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/api-commands/dwm-nvm-usr-data-set/"
order: 203
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-nvm-usr-data-set">
<span id="id1"></span><h1>dwm_nvm_usr_data_set</h1>
<p>ユーザーデータを不揮発性メモリに保存し、内部の不揮発性メモリに書き込みます。このメモリは慎重に使用する必要があります。古いデータは書き換えられます。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_nvm_usr_data_set">
<span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_nvm_usr_data_set</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">uint8_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">data</span></span>, <span class="n"><span class="pre">uint8_t</span></span><span class="w"> </span><span class="n"><span class="pre">len</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">パラメータ</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> -- データ、長さ</p></li>
<li><p><strong>data</strong> -- 最大 250 バイト (<em>書き込まれるユーザーデータ</em>)</p></li>
<li><p><strong>len</strong> -- 1 バイト (<em>データ長、最大 250 バイト</em>)</p></li>
<li><p><strong>output</strong> -- <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">ステータスコード</span></a></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>Cコード例</strong></p>
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
<p><strong>SPI/UART 例</strong></p>
<blockquote>
<div><p>これらのインターフェースでは使用できません。</p>
</div></blockquote>
</div>


           </div>
