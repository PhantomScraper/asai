---
title: "UART接口"
lang: zh
slug: "pans-pro-rtls/integration-guide/uart-interface"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/uart-interface/"
order: 95
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="uart-interface">
<span id="pans-uart-interface"></span><h1>UART接口</h1>
<p>用户可以使用外部主机设备，以 115200 的波特率通过 UART 接口连接 DWM 模块。 下图显示了 DWM1001 UART 接口的工作流程。 在 UART 通用模式通信中，主机设备是启动器，而 DWM 模块是响应器。 DWM1001 UART 提供两种模式：UART 通用模式和 UART Shell模式。 DWM1001 UART 的默认模式是通用模式。 不过，这两种模式是可以转换的。</p>
<p>通用模式转换为外壳模式:按两次 “Enter” 键，或在一秒钟内输入两个字节 [0x0D, 0x0D]。</p>
<p>如果模块在低功耗模式下处于 “sleep” 状态，如 <em>低功耗模式唤醒机制</em> 中介绍的那样，在双击“Enter”之前需要额外的字节。 例如，按三次 “Enter” 将唤醒模块并将其转入 Shell 模式。 Shell 模式转为通用模式：用户需要输入 “quit” 命令。</p>
<blockquote>
<div><div class="figure align-default" id="id1">
<a class="reference internal image-reference" href="../../../_images/image91.png"><img alt="../../../_images/image91.png" src="/docs-assets/zh-cn/_images/image91.png" style="width: 5.70833in; height: 2.29167in;"></a>
<p class="caption"><span class="caption-text">UART 工作流程</span></p>
</div>
</div></blockquote>
<hr class="docutils">
<div class="section" id="uart-tlv-mode">
<h2>UART TLV 模式</h2>
<p>UART TLV 模式使用 TLV 格式数据. 在这种模式下，主机设备和 DWM 模块使用 TLV 请求/响应进行通信. 完整的 TLV 请求通信流程包括以下步骤:</p>
<ol class="arabic simple">
<li><p>主机设备发送 TLV 请求；</p></li>
<li><p>DWM1001 回应 TLV 数据。</p></li>
</ol>
<p>在接收到任何数据时，UART 会为后续数据启动延迟计时器。 如果在延迟时间内（具体为 25 个时钟周期（25/32768 秒≈ 763 μs））有新数据输入，UART 就会启动延迟计时器，等待新数据。 如果在延迟时间内没有新数据进来，延迟计时器就会过期。 然后，UART 会将接收到的数据发送到通用 API 线程，并等待它返回响应数据或错误信息。</p>
<p>DWM1001 UART TLV 模式线程在串行的三种状态之间传输： “UART: Idle”, “UART: 接收 “和” UART: 完成”。 每个状态都会在特定事件发生时转移到下一个相应的状态。</p>
<ul class="simple">
<li><p>UART: Idle:是初始化后和每次成功的 TLV 响应后的状态. 在此状态下，UART 只期待一个字节作为 TLV 请求或双 “Enter ”命令的开始。</p>
<ul>
<li><p>等待事件：接收 TLV 请求。</p></li>
<li><p>事件的操作：</p>
<ul>
<li><p>启动延迟计时器。</p></li>
<li><p>传输到 UART:接收。</p></li>
</ul>
</li>
</ul>
</li>
<li><p>UART: Receiving:是等待接收请求结束的状态。 在此状态下接收任何数据时，UART 将刷新延迟计时器。 如果主机设备已经发送完字节，延迟计时器将失效。</p>
<ul>
<li><p>等待事件：延迟时间已过。</p></li>
<li><p>对事件的操作 - 如果收到的请求是双 “Enter”：</p>
<ul>
<li><p>转到 UART Shell 模式。</p></li>
</ul>
</li>
<li><p>对事件采取行动 - 如果收到的请求不是双 “Enter”：</p>
<ul>
<li><p>将收到的请求发送到通用 API 线程。</p></li>
<li><p>传输到 UART：完成。</p></li>
</ul>
</li>
</ul>
</li>
<li><p>UART：完成：是等待通用 API 线程解析传入请求，并将响应数据或错误信息发回 UART 线程的状态。</p>
<ul>
<li><p>等待事件：通用 API 线程调用 call_back()函数。</p></li>
<li><p>事件的操作：</p>
<ul>
<li><p>向主机设备发送响应数据或错误信息。</p></li>
<li><p>传输到 UART: Idle。</p></li>
</ul>
</li>
</ul>
</li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="uart-tlv-mode-communication">
<h2>UART TLV 模式通信</h2>
<p>下图说明了 TLV 模式下的 UART 通信：</p>
<ol class="arabic">
<li><p>主机设备以 TLV 格式发送请求；</p></li>
<li><p>DWM 模块回应一个 TLV 格式的信息。</p>
<div class="figure align-default" id="id2">
<a class="reference internal image-reference" href="../../../_images/image10.png"><img alt="../../../_images/image10.png" src="/docs-assets/zh-cn/_images/image10.png" style="width: 4.875in; height: 3.03194in;"></a>
<p class="caption"><span class="caption-text">UART TLV 通信</span></p>
</div>
</li>
</ol>
</div>
<hr class="docutils">
<div class="section" id="uart-tlv-mode-communication-example">
<h2>UART TLV 模式通信示例</h2>
<p>下图举例说明了主机设备发送 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-gpio-cfg-output#dwm-gpio-cfg-output"><span class="std std-ref">dwm_gpio_cfg_output</span></a> 命令，将引脚 13 设置为高电平（字节数组中的[0x28, 0x02, 0x0D, 0x01]），并在 TLV 模式下使用 UART API 接收 DWM 模块的响应. 通信流程的步骤如下:</p>
<ol class="arabic simple">
<li><p>主机设备以 TLV 格式发送 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-gpio-cfg-output#dwm-gpio-cfg-output"><span class="std std-ref">dwm_gpio_cfg_output</span></a> TLV格式的命令： 类型 = 0x28，长度 = 0x02，值 = 0x0D 0x01。</p></li>
<li><p>DWM 模块以 TLV 格式响应： 类型 = 0x40，长度 = 0x01，值 = 0x00,</p></li>
</ol>
<p>其中 类型= 0x40 表示这是一条返回消息，长度= 0x01 表示后面有一个字节作为数据，值= 0x00 表示 TLV 请求被正确解析。</p>
<div class="figure align-default" id="id3">
<a class="reference internal image-reference" href="../../../_images/image11.png"><img alt="../../../_images/image11.png" src="/docs-assets/zh-cn/_images/image11.png" style="width: 3.90694in; height: 2.71806in;"></a>
<p class="caption"><span class="caption-text">UART TLV 通信示例</span></p>
</div>
</div>
<hr class="docutils">
<div class="section" id="uart-shell-mode-communication">
<h2>UART Shell模式通信</h2>
<p>UART Shell 模式提供提示并使用 Shell command. UART Shell 模式旨在为用户提供人工可读的 API 访问. 因此，所有 Shell command都是字母字符串，后面跟一个字符回车，即 “Enter”. 用户可以直接通过键盘输入字符串，然后按 “Enter” 键发送 Shell command. 除 “退出” 命令外，DWM1001 UART 在执行完每条 Shell 命令后都会保持 Shell 模式。</p>
<p>如下图所示，完整的 Shell command通信流程包括以下步骤：</p>
<ol class="arabic simple">
<li><p>主机设备发送 Shell command + “Enter” 到 DWM1001。</p></li>
<li><p>如果有任何要回应的信息，DWM1001 会将信息发送给主机设备。</p></li>
<li><p>如果没有任何回应，DWM1001 不会发送任何信息，并保持安静。</p></li>
</ol>
<div class="figure align-default" id="id4">
<a class="reference internal image-reference" href="../../../_images/image12.png"><img alt="../../../_images/image12.png" src="/docs-assets/zh-cn/_images/image12.png" style="width: 3.88472in; height: 2.32222in;"></a>
<p class="caption"><span class="caption-text">UART Shell模式通信</span></p>
</div>
</div>
<hr class="docutils">
<div class="section" id="uart-shell-mode-communication-example">
<h2>UART Shell模式通信示例</h2>
<p>下图举例说明了主机设备使用 UART Shell 发送 “GPIO 设置” 命令，将引脚 13 设置为高电平（字节数组中的 “gs 13”，之后是 “回车 ”键，详见 <em>gs</em>）。 通信流程的步骤如下:</p>
<ol class="arabic simple">
<li><p>主机设备在 Shell 模式下发送 “GPIO 设置” 命令： “gs 13“ + ”Enter”。</p></li>
<li><p>DWM1001 会以字符串 “gpio13: 1” 回应主机。</p></li>
</ol>
<div class="figure align-default" id="id5">
<a class="reference internal image-reference" href="../../../_images/image13.png"><img alt="../../../_images/image13.png" src="/docs-assets/zh-cn/_images/image13.png" style="width: 3.5625in; height: 2.34444in;"></a>
<p class="caption"><span class="caption-text">UART Shell模式通信示例</span></p>
</div>
</div>
<hr class="docutils">
<div class="section" id="low-power-mode-wake-up-mechanism">
<h2>低功耗模式唤醒机制</h2>
<p>正如 PANS 库所提供的，DWM 模块可以在低功耗模式下工作。 在低功耗模式下，当主机设备不与 API 通信时，模块会让与 API 相关的线程进入 “休眠” 状态。 在这种情况下，主机设备需要通过外部接口唤醒模块，然后才能开始真正的通信。</p>
<p>对于 UART 接口，主机设备需要先发送一个字节来唤醒模块。</p>
<p>在 API 传输完成后，主机设备需要让模块回到 “睡眠” 状态，以节省电源，如 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-sleep#dwm-sleep"><span class="std std-ref">dwm_sleep</span></a> 和 shell 命令 <em>quit</em> 所介绍。</p>
</div>
<hr class="docutils">
<div class="section" id="uart-wakeup">
<h2>UART 唤醒</h2>
<p>如果 DWM 休眠（低功耗模式），在 SPI/UART 开始接受指令之前，必须执行唤醒程序。 要从休眠状态唤醒，必须在 UART 接口上发送至少一个字节（仅在低功耗模式下）。</p>
</div>
</div>


           </div>
