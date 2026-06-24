---
title: "dwm_gpio_irq_cfg"
lang: ja
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-gpio-irq-cfg"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/api-commands/dwm-gpio-irq-cfg/"
order: 186
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-gpio-irq-cfg">
<span id="id1"></span><h1>dwm_gpio_irq_cfg</h1>
<p>GPIO ピンの割り込みを設定します。 GPIO ピンに登録できる割り込みの最大数は 8 です。DWM はすでに 5 つの GPIO ピンを内部目的で使用しているため、ユーザーは最大 3 つの割り込みのみを登録する必要があります。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_gpio_irq_cfg">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_gpio_irq_cfg</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">uint8_t</span></span><span class="w"> </span><span class="n"><span class="pre">gpio_idx</span></span>, <span class="n"><span class="pre">uint8_t</span></span><span class="w"> </span><span class="n"><span class="pre">irq_type</span></span>, <span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">(</span></span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">callback</span></span><span class="p"><span class="pre">)</span></span><span class="p"><span class="pre">(</span></span><span class="kt"><span class="pre">void</span></span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">)</span></span>, <span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">user_data</span></span><span class="sig-paren">)</span><span class="p"><span class="pre">;</span></span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">パラメータ</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>irq_type</strong> -- '1' | '2' | '3' (割り込みタイプ、1=立ち上がり、2=立ち下がり、3=両方)</p></li>
<li><p><strong>callback</strong> -- : (割り込みコールバック)</p></li>
<li><p><strong>user_data</strong> -- : (ユーザーがコールバックで変更したいデータ)</p></li>
<li><p><strong>output</strong> -- <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">ステータスコード</span></a></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>Cコード例</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="kt">void</span><span class="w"> </span><span class="nf">gpio_cb</span><span class="p">(</span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">p_data</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">     </span><span class="cm">/* callback routine */</span>
<span class="p">}</span>
<span class="err">…</span>
<span class="n">dwm_gpio_irq_cfg</span><span class="p">(</span><span class="n">DWM_GPIO_IDX_13</span><span class="p">,</span><span class="w"> </span><span class="n">DWM_IRQ_TYPE_EDGE_RISING</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">gpio_cb</span><span class="p">,</span><span class="w"> </span><span class="nb">NULL</span><span class="p">);</span>
</pre></div>
</div>
<p><strong>SPI/UART 例</strong></p>
<p>これらのインターフェースでは使用できません</p>
</div>


           </div>
