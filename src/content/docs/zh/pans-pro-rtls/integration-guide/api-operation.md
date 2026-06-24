---
title: "API 操作"
lang: zh
slug: "pans-pro-rtls/integration-guide/api-operation"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/api-operation/"
order: 125
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="api-operation">
<h1>API 操作</h1>
<hr class="docutils">
<div class="section" id="gpio-notification-for-status-change">
<h2>状态更改的 GPIO 通知</h2>
<p>如下图所示，DWM 模块可以通过将专用 GPIO 引脚 (P0.26) 切换为高电平，来发送状态变化通知，而不是由主机设备启动 SPI/UART 通信. 要启用此功能，主机设备需要使用 dwm_int_cfg_set 命令. 在检测到高电平时，主机设备可以启动 dwm_status_get 命令来获取 DWM1001 设备的状态. dwm_int_cfg 和 dwm_status_get 命令都可以通过前面章节介绍的 SPI 或 UART 方案发送.</p>
<div class="figure align-default" id="id1">
<a class="reference internal image-reference" href="../../../_images/image14.png"><img alt="../../../_images/image14.png" src="/docs-assets/zh-cn/_images/image14.png" style="width: 3.50972in; height: 3.07361in;"></a>
<p class="caption"><span class="caption-text">DWM1001 使用数据就绪 GPIO 引脚通知主机设备状态变化</span></p>
</div>
<p>如果状态变化发生在上述的 SPI TLV 请求/响应过程中，该 GPIO 引脚的电平变化将被推迟，以避免冲突. 具体来说，当 SPI 处于状态时: “SPI:等待回调“, ”SPI:等待读取 SIZE“ 和 ”SPI:等待读取 DATA/ERR” 时，GPIO 方案将放弃对 GPIO 引脚的控制. SPI 通信结束后，当 SPI 处于 “SPI: Idle” 状态时，GPIO 方案将重新获得 GPIO 引脚的控制权.</p>
</div>
<hr class="docutils">
<div class="section" id="api-for-on-module-c-code-user-application">
<h2>模块上 C 代码用户应用程序的 API</h2>
<p>用户可以在预编译固件的板载包中提供的某些入口文件中，添加自己的代码并使用 C 代码 API 功能. 这样，用户就可以在模块固件内添加自己的功能，而无需添加外部主控制器设备.</p>
<p>在使用板载固件时，C 代码用户需要注意以下几点:</p>
<ul class="simple">
<li><p>用户应用是基于 eCos RTOS 和 DWM 库.</p></li>
<li><p>用于与用户应用程序链接的文件：</p>
<ul>
<li><p>dwm.h - 头文件 - 封装构建用户应用程序所需的所有头文件</p></li>
<li><p>libdwm.a - 静态库</p></li>
<li><p>extras.o, vectors.o, libtarget.a - eCos 静态库</p></li>
<li><p>target_s132_fw1.ld - 固件第 1 部分的链接脚本</p></li>
<li><p>target_s132_fw2.ld - 固件第 2 部分的链接脚本</p></li>
</ul>
</li>
<li><p>API 为用户应用程序提供函数和定义</p>
<ul>
<li><p>操作系统的常见功能，如线程创建, 内存分配, 访问接口（如 GPIO, SPI……）和同步（mutex, 信号）.</p></li>
<li><p>DWM 通信栈的初始化, 配置和维护</p></li>
<li><p>输入数据和测量的回调注册.</p></li>
<li><p>API将保护用户应用程序，防止错误的设置影响系统性能.</p></li>
</ul>
</li>
</ul>
<hr class="docutils">
<div class="section" id="system-specifications">
<h3>系统规格</h3>
<p>最大用户线程数: 5</p>
<blockquote>
<div><ul class="simple">
<li><p>最终用户的内存：约 KB (D12 之后待定，预计 &gt; 5KB)</p></li>
<li><p>为最终用户提供的闪存: 约 TBD kB (D12 之后待定，预计 &gt;= 40KB)</p></li>
</ul>
</div></blockquote>
</div>
</div>
<hr class="docutils">
<div class="section" id="dwm1001-threads">
<h2>DWM1001 线程</h2>
<p>在 DWM1001 固件系统中，有许多线程，包括 SPI, BLE, UART, Generic API, User App 和其他线程. 每个线程处理特定任务. SPI, BLE 和 UART 线程控制与外部设备的数据传输. 它们不会解析收到的请求. 所有收到的请求都会发送到通用 API 线程. 通用 API 线程是接收到的请求的解析器. 它判断接收到的请求是否有效. 如果有效，固件会继续准备相应的数据作为响应；如果无效，固件会使用错误信息作为响应. 然后，通用应用程序接口线程运行call_back()函数，将准备好的响应信息发送回发出请求的线程. 板载用户应用程序线程是一个独立的线程，供用户添加自己的功能. DWM1001 板载软件包中的 dwmexamplesolder 文件夹提供了入口. dwmexamplesdwm-simple 文件夹中提供了一个示例项目.</p>
</div>
<hr class="docutils">
<div class="section" id="position-representation">
<h2>位置表示</h2>
<p>在实时定位系统中显示位置和距离时，有两件事需要考虑:</p>
<blockquote>
<div><ul class="simple">
<li><p>准确性</p></li>
<li><p>精度</p></li>
</ul>
</div></blockquote>
<p>精度是指节点报告的位置与实际位置之间的误差. 目前，本设计中使用的 DW1000 可提供约 10 厘米的精度. 精度是一个最小有效位（LSB）所代表的值. 在本系统的板载固件中，精度为 1 毫米，即 0.001 米. 位置以三维坐标（X, Y, Z）表示，其中 X, Y 和 Z 为 32 位整数（4 字节）. 每个 LSB 代表 1 毫米. 这样更容易解释数值，也更容易对报告的数值进行数学计算.</p>
<p>在决定精度时，重要的是要根据精度来选择，这样才能得到有意义的结果. 如果精度很低，向用户显示精确的数值是没有用的. 与当前的 10 厘米精度相比，1 毫米的精度过于精细. 因此，在显示位置时，使用了 1 厘米的精度，即 0.01 米. 只有当坐标/距离变化超过 1 厘米时，才会显示更新值. 这类似于将浮点数/二进制数值舍入到有意义的小数位数.</p>
</div>
</div>


           </div>
