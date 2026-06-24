---
title: "dwm_gpio_irq_cfg"
lang: zh
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-gpio-irq-cfg"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/api-commands/dwm-gpio-irq-cfg/"
order: 186
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-gpio-irq-cfg">
<span id="id1"></span><h1>dwm_gpio_irq_cfg</h1>
<p>配置GPIO引脚的中断。 GPIO引脚可以注册的最大中断数为8。 用户最多只能注册3个中断，因为DWM已经将5个GPIO引脚用于内部目的。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_gpio_irq_cfg">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_gpio_irq_cfg</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">uint8_t</span></span><span class="w"> </span><span class="n"><span class="pre">gpio_idx</span></span>, <span class="n"><span class="pre">uint8_t</span></span><span class="w"> </span><span class="n"><span class="pre">irq_type</span></span>, <span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">(</span></span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">callback</span></span><span class="p"><span class="pre">)</span></span><span class="p"><span class="pre">(</span></span><span class="kt"><span class="pre">void</span></span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">)</span></span>, <span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">user_data</span></span><span class="sig-paren">)</span><span class="p"><span class="pre">;</span></span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">参数</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>irq_type</strong> – ‘1’ | ’2’ | ’3’ (中断类型, 1=上升, 2=下降, 3=两个都有)</p></li>
<li><p><strong>callback</strong> – : (中断回调)</p></li>
<li><p><strong>user_data</strong> – : (用户希望在回调中修改的数据)</p></li>
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C代码示例</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="kt">void</span><span class="w"> </span><span class="nf">gpio_cb</span><span class="p">(</span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">p_data</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">     </span><span class="cm">/* callback routine */</span>
<span class="p">}</span>
<span class="err">…</span>
<span class="n">dwm_gpio_irq_cfg</span><span class="p">(</span><span class="n">DWM_GPIO_IDX_13</span><span class="p">,</span><span class="w"> </span><span class="n">DWM_IRQ_TYPE_EDGE_RISING</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">gpio_cb</span><span class="p">,</span><span class="w"> </span><span class="nb">NULL</span><span class="p">);</span>
</pre></div>
</div>
<p><strong>SPI/UART 示例</strong></p>
<p>这些接口不可用</p>
</div>


           </div>
