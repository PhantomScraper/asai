---
title: "SPI 接口"
lang: zh
slug: "pans-pro-rtls/integration-guide/spi-interface"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/spi-interface/"
order: 96
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="spi-interface">
<span id="pans-spi-interface"></span><h1>SPI 接口</h1>
<p>DWM1001 SPI 接口使用 TLV 格式的数据. 用户可以使用 SPI 主模式的外部主机设备连接到 DWM 模块 SPI 接口，该接口以从模式运行. 最大 SPI 时钟频率为 8 MHz. (在 DWM1001 SPI 方案中，主机设备通过 TLV 请求与 DWM1001 通信. 完整的 TLV 请求通信流程包括以下步骤：</p>
<ol class="arabic simple">
<li><p>主机设备发送 TLV 请求；</p></li>
<li><p>DWM1001 准备响应；</p></li>
<li><p>主机设备读取 SIZE（每个响应的长度）和 NUM（传输次数）；</p></li>
<li><p>主机设备读取数据响应；</p></li>
</ol>
<p>由于 SPI 采用全双工通信，当主机设备（作为 SPI 主设备）写入 x 字节时，它会向 DWM 模块（作为从设备）发送 x 字节，并同时接收 x 字节的假数据. 与读取类似，主机设备发送 x 个字节的假数据，并接收 x 个字节的数据作为响应. 在 DWM1001 SPI 方案中，虚字节是值为 0xFF 的八位字节.</p>
<blockquote>
<div><div class="figure align-default" id="id1">
<a class="reference internal image-reference" href="../../../_images/image41.png"><img alt="../../../_images/image41.png" src="/docs-assets/zh-cn/_images/image41.png" style="width: 5.66667in; height: 2.84444in;"></a>
<p class="caption"><span class="caption-text">SPI 工作流程</span></p>
</div>
</div></blockquote>
<p>如上图所示，DWM1001 SPI 线程在四个状态之间串行传输.</p>
<p>每个状态都会在特定事件发生时转移到下一个相应的状态.</p>
<ul>
<li><p>SPI: Idle: 初始化后和每次成功数据传输/响应后的状态. 在此状态下，任何接收到的数据都被假定为 TLV 请求. 因此，在接收到任何数据时，固件中的 SPI 线程会将接收到的数据传递给通用 API. 通用 API 会解析 TLV 请求，并准备返回数据.</p>
<blockquote>
<div><ul class="simple">
<li><p>等待事件：接收 TLV 请求.</p></li>
<li><p>对事件采取行动 - 如果类型 == 0xFF：</p></li>
</ul>
</div></blockquote>
</li>
</ul>
<ul>
<li><p>SPI: 等待回调：DWM1001 SPI 等待通用 API 解析 TLV 请求并准备响应. 在此状态下，来自主机端的任何数据都将被忽略，并以 0x00 返回.</p>
<blockquote>
<div><ul>
<li><p>等待事件：通用 API 调用 call_back()函数.</p></li>
<li><p>事件的操作：</p>
<blockquote>
<div><ul class="simple">
<li><p>将数据就绪 GPIO 引脚切换为高电平 - 详见 <em>SPI 方案: 使用数据就绪 GPIO 引脚进行 TLV 通信</em>.</p></li>
<li><p>转到 “SPI:等待 READ SIZE/NUM”</p></li>
</ul>
</div></blockquote>
</li>
</ul>
</div></blockquote>
</li>
<li><p>SPI: 等待读取 SIZE/NUM：DWM1001 SPI 已准备好 SIZE 字节作为响应，将有 NUM 次传输. SIZE 和 NUM 共为 2 字节非零数据，即 SIZE/NUM. 它们表示要响应的数据或错误信息的总数（即 SIZE*NUM 字节）. DWM1001 SPI 作为从设备，正在等待主机设备读取 SIZE/NUM 字节.</p>
<blockquote>
<div><ul>
<li><p>等待事件：主机设备读取两个字节.</p></li>
<li><p>事件的操作：</p>
<blockquote>
<div><ul class="simple">
<li><p>回应 SIZE/NUM 字节.</p></li>
<li><p>转到 ” SPI:  等待 READ DATA/ERR”.</p></li>
</ul>
</div></blockquote>
</li>
</ul>
</div></blockquote>
</li>
</ul>
<ul>
<li><p>SPI: 等待读取 DATA/ERR：DWM1001 SPI 已为 NUM 传输中的每次传输准备了 SIZE 字节的数据或错误信息，作为对 TLV 请求的响应，并正在等待主机设备读取.</p>
<blockquote>
<div><ul class="simple">
<li><p>等待事件：主机设备进行 NUM 传输. 每次传输应为 SIZE 字节. 否则，数据可能会丢失.</p></li>
<li><p>事件的操作：</p>
<ul>
<li><p>回应 DATA/ERR.</p></li>
<li><p>将数据就绪 GPIO 引脚切换为低电平 - 详见 <em>SPI 方案： 使用数据就绪 GPIO 引脚进行 TLV 通信</em>. 转到 ” SPI: Idle “.</p></li>
</ul>
</li>
</ul>
</div></blockquote>
</li>
</ul>
<p>在 DWM1001 中，从 “SPI:在 DWM1001 中，从 “SPI: Idle”开始，遍历上述所有四种状态，然后返回 “SPI: Idle”表示完整的 TLV 请求通信流程. 在通信流程结束时，用户应该已经收到响应数据或错误信息.</p>
<p>下面的小节将举例说明几种不同的用法.</p>
<hr class="docutils">
<div class="section" id="spi-tlv-communication-using-polling">
<h2>使用轮询进行 SPI TLV 通信</h2>
<p>下图显示了主机设备向DWM模块写入/从DWM模块读取信息的正常通信流程:</p>
<ol class="arabic simple">
<li><p>主机设备以 TLV 格式发送请求.</p></li>
<li><p>主机设备读取 SIZE/NUM 字节，表示要完成的传输次数，以及每次传输中准备读取的字节数.</p></li>
</ol>
<ol class="arabic simple" start="3">
<li><p>主机设备以 TLV 格式读取 SIZE 字节的数据响应.</p></li>
</ol>
<div class="figure align-default" id="id2">
<a class="reference internal image-reference" href="../../../_images/image51.png"><img alt="../../../_images/image51.png" src="/docs-assets/zh-cn/_images/image51.png" style="width: 5.70833in; height: 3.29167in;"></a>
<p class="caption"><span class="caption-text">使用轮询进行 SPI TLV 通信</span></p>
</div>
<div class="line-block">
<div class="line">下图举例说明了主机设备写入 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-gpio-cfg-output#dwm-gpio-cfg-output"><span class="std std-ref">dwm_gpio_cfg_output</span></a> TLV 请求，将引脚 13 设置为高电平（字节数组中的[0x28, 0x02, 0x0D, 0x01]），并从 DWM 模块读取响应.</div>
<div class="line">传输和响应的通信流程包括</div>
</div>
<blockquote>
<div><ol class="arabic simple">
<li><p>主机设备写入 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-gpio-cfg-output#dwm-gpio-cfg-output"><span class="std std-ref">dwm_gpio_cfg_output</span></a> 命令，以 TLV 格式设置引脚 13 level HIGH，共 4 个字节：类型 = 0x28，长度 = 0x02，值 = 0x0D 0x01.</p></li>
</ol>
</div></blockquote>
</div>
<hr class="docutils">
<div class="section" id="spi-tlv-communication-using-data-ready-gpio-pin">
<h2>使用数据就绪 GPIO 引脚进行 SPI TLV 通信</h2>
<p>用户可以设置 DWM1001 的中断 Data-Ready GPIO 引脚 (GPIO P0.26)，以指示数据何时就绪，而无需主控器多次轮询检查响应状态. 设置数据就绪功能后，当没有数据要读取时，数据就绪 GPIO 引脚将被设置为低电平；当响应 SIZE/NUM 和数据就绪时，数据就绪 GPIO 引脚将在 “SPI.等待读取 SIZE/NUM” 和 “SPI.等待读取 SIZE/NUM” 状态下被设置为高电平： 等待读取 SIZE/NUM“ 和 ”SPI：等待读取数据/ERR” 状态时，数据就绪 GPIO 引脚将被设置为高电平. 因此，用户可以将数据就绪 GPIO 引脚用作中断或状态引脚.</p>
<p>要为 SPI 方案设置 Data-Ready GPIO 引脚，用户需要使用 dwm_int_cfg 通过 SPI 方案进行 TLV 请求： <em>SPI TLV 通信使用轮询</em> 中引入的普通 TLV 通信.</p>
<p>该方案的通信流程如下图所示.</p>
<ol class="arabic">
<li><p>设置SPI中断.</p></li>
<li><p>主机设备以 TLV 格式写入请求.</p></li>
<li><p>主机设备等待 DWM1001 上的数据就绪 GPIO 引脚变为高电平.</p></li>
<li><p>主机设备读取 SIZE/NUM 字节.</p></li>
<li><p>主机设备在每次传输中读取 NUM 次 TLV 格式的 SIZE 字节数据响应.</p>
<div class="figure align-default" id="id3">
<a class="reference internal image-reference" href="../../../_images/image71.png"><img alt="../../../_images/image71.png" src="/docs-assets/zh-cn/_images/image71.png" style="width: 5.70833in; height: 4.34444in;"></a>
<p class="caption"><span class="caption-text">使用数据就绪 GPIO 引脚进行 SPI TLV 通信</span></p>
</div>
</li>
</ol>
<p>从步骤中可以看出，该方案使用 DWM1001 上的数据就绪 GPIO 引脚在响应数据就绪时指示主机设备. 这样，主机设备在读取 SIZE 字节时就不会那么忙了.</p>
</div>
<hr class="docutils">
<div class="section" id="spi-partial-transmission">
<h2>SPI 部分传输</h2>
<p>从 DWM 模块读取数据时，如果主机设备没有在一次传输中读取所有字节的数据，读取操作仍将被视为完成. 其余的响应将被放弃. 例如，在 ” SPI:等待读取数据/ERR “状态下，DWM 模块已准备好 SIZE 字节的响应数据，并希望主机设备读取所有 SIZE 字节的响应数据. 但是，如果主机设备只读取了部分数据，DWM 模块将放弃其余数据并转入下一状态： “SPI: IDLE “.</p>
</div>
<hr class="docutils">
<div class="section" id="spi-error-recovery-mechanism">
<h2>SPI 错误恢复机制</h2>
<p>DWM1001 SPI 有一个特殊的类型值 0xFF，称为 type_nop. 带有 type_nop 的 TLV 数据报文表示无操作. 在 ” SPI: IDLE “状态下，当 DWM1001 SPI 接收到消息并发现类型字节为 0xFF 时，它将不会执行任何操作，包括向通用 API 线程发送 TLV 数据消息.</p>
<p>type_nop 是为错误恢复而设计的. 如果主机设备不确定 DWM1001 SPI 处于何种状态，可以利用 SPI 响应和非部分传输机制，通过发送三个 0xFF 假字节，将 DWM1001 SPI 重置为 “SPI.IDLE” 状态： 它可以利用 SPI 响应和非部分传输机制，将 DWM1001 SPI 复位到 “SPI：IDLE” 状态，方法是发送三个 0xFF 虚字节，每个虚字节进行一次传输. 三次传输后，DWM1001 SPI 的响应数据将全部变为值为 0xFF 的哑字节，表明 DWM1001 SPI 处于 “SPI.IDLE” 状态.</p>
</div>
<hr class="docutils">
<div class="section" id="low-power-mode-wake-up-mechanism">
<h2>低功耗模式唤醒机制</h2>
<p>正如 PANS 库所提供的，DWM 模块可以在低功耗模式下工作. 在低功耗模式下，当主机设备不与 API 通信时，模块会让与 API 相关的线程进入 “休眠” 状态. 在这种情况下，主机设备需要通过外部接口唤醒模块，然后才能开始真正的通信.</p>
<p>对于 SPI 接口，将芯片选择引脚置低电平唤醒模块，即不需要额外的传输.</p>
<p>在 API 传输完成后，主机设备需要让模块回到 “睡眠” 状态，以节省电源，如 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-sleep#dwm-sleep"><span class="std std-ref">dwm_sleep</span></a> 和 shell 命令 <em>quit</em> 所介绍.</p>
</div>
<hr class="docutils">
<div class="section" id="spi-wakeup">
<h2>SPI 唤醒</h2>
<p>如果 DWM 休眠（在低功耗模式下），则必须在 SPI 开始接受命令之前执行唤醒程序. 必须在 SPI 的 CS 引脚上产生至少 35 微秒宽的脉冲，才能从休眠状态唤醒（仅在低功耗模式下）.</p>
</div>
</div>


           </div>
