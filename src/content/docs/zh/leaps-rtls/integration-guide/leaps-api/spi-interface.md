---
title: "SPI 接口"
lang: zh
slug: "leaps-rtls/integration-guide/leaps-api/spi-interface"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/leaps-api/spi-interface/"
order: 131
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="spi-interface">
<h1>SPI 接口</h1>
<hr class="docutils">
<p>模块在空闲状态下以0xFF响应。SPI事务之间的最小延迟必须至少为5毫秒。该模块充当SPI总线上的SPI从站。从属设备在一次传输中支持的最大字节数为255。在使用SPI API接口之前，用户应在重置后等待至少1秒。</p>
<hr class="docutils">
<div class="section" id="using-polling">
<h2>使用轮询</h2>
<a class="reference internal image-reference" href="../../../../_images/image3.png"><img alt="../../../../_images/image3.png" class="align-center" src="/docs-assets/zh-cn/_images/image3.png" style="width: 615.0px; height: 352.0px;"></a>
</div>
<hr class="docutils">
<div class="section" id="example-polling-leaps-gpio-cfg-output">
<h2>轮询示例 leaps_gpio_cfg_output</h2>
<a class="reference internal image-reference" href="../../../../_images/image4.png"><img alt="../../../../_images/image4.png" class="align-center" src="/docs-assets/zh-cn/_images/image4.png" style="width: 614.0px; height: 312.0px;"></a>
</div>
<hr class="docutils">
<div class="section" id="using-interrupt-gpio-when-command-is-issued-from-the-master">
<h2>从主机发出命令时使用中断（GPIO）</h2>
<a class="reference internal image-reference" href="../../../../_images/image5.png"><img alt="../../../../_images/image5.png" class="align-center" src="/docs-assets/zh-cn/_images/image5.png" style="width: 615.0px; height: 464.0px;"></a>
</div>
<hr class="docutils">
<div class="section" id="using-core-int-gpio-pin-to-notify-master-about-the-status-change">
<h2>使用CORE_INT GPIO引脚通知主机状态更改</h2>
<p>如果此中断发生在上述TLV请求响应过程中，则会被推迟。</p>
<a class="reference internal image-reference" href="../../../../_images/image6.png"><img alt="../../../../_images/image6.png" class="align-center" src="/docs-assets/zh-cn/_images/image6.png" style="width: 614.0px; height: 291.0px;"></a>
</div>
<hr class="docutils">
<div class="section" id="example-interrupt-leaps-bh-xfer">
<h2>中断leaps_bh_xfer示例</h2>
<p>单个TLV帧的最大有效载荷大小为253个字节（从属TLV报头支持的最大TLV帧=255-2=253）。主设备希望使用leaps_bh_xfer命令传输到从设备（下行链路）的字节数在命令的参数中编码。从属设备获取准备传输到主设备的下行链路数据和上行链路数据的数量，并决定在SPI传输序列中传输下行链路和上行链路的事务的大小和数量。</p>
<p>假设主设备想要传输299字节的下行链路数据，而从设备已经准备好1124字节的上行链路数据。</p>
<ul class="simple">
<li><p>下行链路字节数：299（至少2个TLV帧）</p></li>
<li><p>上行字节数:1124（至少5个TLV帧）</p></li>
</ul>
<p>主机执行leaps_bh_xfer命令，参数为==299。从属服务器的响应大小为255，事务数为5（5*253=1265）。下行链路和上行链路TLV数据块都使用保留的TLV类型进行编码，这些TLV类型可用于序列化在多个TLV帧中编码的数据。目前最多支持5个TLV帧。TLV类型100-104（0x64-0x68）保留用于上行链路数据块。TLV类型110-114（0x6E-0x72）被保留用于下行链路数据块。</p>
<a class="reference internal image-reference" href="../../../../_images/image7.png"><img alt="../../../../_images/image7.png" class="align-center" src="/docs-assets/zh-cn/_images/image7.png" style="width: 615.0px; height: 440.0px;"></a>
<hr class="docutils">
<div class="section" id="wakeup-via-spi">
<h3>通过SPI唤醒</h3>
<p>如果模块处于休眠状态（低功耗模式），则必须在SPI/UART开始接受命令之前执行唤醒过程。至少，必须在SPI的CS引脚上产生35微秒宽的脉冲，或者必须在UART接口上发送至少一个字节才能从睡眠中唤醒（仅在低功耗模式下）。</p>
</div>
</div>
</div>


           </div>
