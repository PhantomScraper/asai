---
title: "dwm_gpio_cfg_input"
lang: en
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-gpio-cfg-input"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/api-commands/dwm-gpio-cfg-input/"
order: 186
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-gpio-cfg-input">
<span id="id1"></span><h1>dwm_gpio_cfg_input</h1>
<p>Configures GPIO pin as input.</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_gpio_cfg_input">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_gpio_cfg_input</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">uint8_t</span></span><span class="w"> </span><span class="n"><span class="pre">gpio_idx</span></span>, <span class="n"><span class="pre">uint8_t</span></span><span class="w"> </span><span class="n"><span class="pre">gpio_pull</span></span><span class="sig-paren">)</span><span class="p"><span class="pre">;</span></span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>gpio_idx</strong> – 8-bit integer (see the section gpio_idx for allowed values)</p></li>
<li><p><strong>gpio_pull</strong> – 8-bit integer (0 no pull, 1 pull down, 3 pull up).</p></li>
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">Status code</span></a>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C code example</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_gpio_cfg_input</span><span class="p">(</span><span class="n">DWM_GPIO_IDX_13</span><span class="p">,</span><span class="w"> </span><span class="n">DWM_GPIO_PIN_PULLUP</span><span class="p">);</span>
<span class="n">dwm_gpio_cfg_input</span><span class="p">(</span><span class="n">DWM_GPIO_IDX_9</span><span class="p">,</span><span class="w"> </span><span class="n">DWM_GPIO_PIN_NOPULL</span><span class="p">);</span>
<span class="n">dwm_gpio_cfg_input</span><span class="p">(</span><span class="n">DWM_GPIO_IDX_31</span><span class="p">,</span><span class="w"> </span><span class="n">DWM_GPIO_PIN_PULLDOWN</span><span class="p">);</span>
</pre></div>
</div>
<p><strong>SPI/UART example</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="4"><p>TLV Request</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length</p></td>
<td colspan="2"><p>Value</p></td>
</tr>
<tr class="row-odd"><td></td>
<td></td>
<td><p>pin index</p></td>
<td><p>pull
config</p></td>
</tr>
<tr class="row-even"><td><p>0x29</p></td>
<td><p>0x02</p></td>
<td><p>0x0D</p></td>
<td><p>0x03</p></td>
</tr>
</tbody>
</table>
<p>Type 0x29 means command dwm_gpio_cfg_input</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV Response</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length</p></td>
<td><p>Value (see error
codes)</p></td>
</tr>
<tr class="row-odd"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x40 means <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">Status code</span></a> of the previous command</p>
</div>


           </div>
