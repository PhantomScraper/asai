---
title: "PANS PRO API"
lang: zh
slug: "pans-pro-rtls/integration-guide/pans-pro-api"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/pans-pro-api/"
order: 93
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="pans-pro-api">
<span id="id1"></span><h1>PANS PRO API</h1>
<p>本指南规定了基于 Decawave DW1000 IC 的 DWM 模块的公共应用程序接口。 该 API 本质上是一组函数，提供了一种与 MCU 通信的方法，以便在应用层通过库驱动模块，而无需处理直接通过其 SPI/I2C 接口寄存器集访问 DW1000 IC 部件和其他外设的细节。 DW1000 IC 部件具有 IEEE 802.15.4-2011 标准中定义的 UWB 物理层，可作为 UWB 无线电模块，由模块的 MCU 控制。 该模块提供多个接口供用户与系统交互。 这些接口包括 UART 和 SPI 硬件接口，以及可通过智能手机应用程序使用的 BLE 接口。</p>
<p><strong>API及其指南</strong></p>
<p>一套 API 功能可以通过不同的通信接口访问，让开发人员可以灵活地使用模块，并将其集成到系统中。 API 访问主要有两种类型：</p>
<blockquote>
<div><ol class="arabic simple">
<li><p>外部访问 API：通过 UART, SPI 和 BLE。</p></li>
<li><p>集成访问 API：通过板载用户应用程序（C 代码）。</p></li>
</ol>
</div></blockquote>
<p>在上述 API 接口中：</p>
<blockquote>
<div><ol class="arabic simple">
<li><p>UART (通用), SPI 和板载 API 介绍在 <em>API</em> <em>命令</em> 部分。</p></li>
<li><p>UART（Shell）API 在 <em>Shell 命令</em> 部分介绍。</p></li>
<li><p>在 <em>TLV 类型列表</em> 部分介绍了 BLE API。</p></li>
</ol>
</div></blockquote>
<p>接下来的页面将说明 PANS API 功能本身，详细描述每个 API 功能的参数, 功能和用途。</p>
<p>用户可以使用 API 配置每个单独的模块。</p>
<hr class="docutils">
<p>下面的小节将显示每种支持的 API</p>
<div class="toctree-wrapper compound">
<ul>
<li class="toctree-l1"><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/tlv-api">TLV API</a></li>
<li class="toctree-l1"><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api">壳牌API</a></li>
<li class="toctree-l1"><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/mqtt-api">MQTT API</a></li>
<li class="toctree-l1"><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/supported-intefaces">支持的接口</a></li>
<li class="toctree-l1"><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-limitation">API 限制</a></li>
<li class="toctree-l1"><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-operation">API 操作</a></li>
</ul>
</div>
</div>


           </div>
