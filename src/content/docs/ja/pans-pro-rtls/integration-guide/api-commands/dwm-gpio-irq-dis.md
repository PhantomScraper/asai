---
title: "dwm_gpio_irq_dis"
lang: ja
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-gpio-irq-dis"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/api-commands/dwm-gpio-irq-dis/"
order: 187
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-gpio-irq-dis">
<span id="id1"></span><h1>dwm_gpio_irq_dis</h1>
<p>GPIO ピンの割り込みを無効にします。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_gpio_irq_dis">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_gpio_irq_dis</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">uint8_t</span></span><span class="w"> </span><span class="n"><span class="pre">gpio_idx</span></span><span class="sig-paren">)</span><span class="p"><span class="pre">;</span></span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">パラメータ</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>gpio_idx</strong> -- 8 ビット整数 (許可される値については gpio_idx セクションを参照してください)</p></li>
<li><p><strong>output</strong> -- <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">ステータスコード</span></a></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>Cコード例</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_gpio_irq_dis</span><span class="p">(</span><span class="n">DWM_GPIO_IDX_13</span><span class="p">);</span>
</pre></div>
</div>
<p><strong>SPI/UART 例</strong></p>
<p>これらのインターフェースでは使用できません。</p>
</div>


           </div>
