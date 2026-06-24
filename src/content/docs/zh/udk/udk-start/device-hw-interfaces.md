---
title: "硬件接口"
lang: zh
slug: "udk/udk-start/device-hw-interfaces"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/zh-cn/udk/udk-start/device-hw-interfaces/"
order: 35
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="hardware-interfaces">
<span id="hardware-interface"></span><h1>硬件接口</h1>
<p>在进行演示之前，熟悉硬件接口是非常重要的，尤其是 <span class="red-text">A, B 和 C 按钮</span>, <span class="red-text">2 个 USB-C 端口</span>, <span class="red-text">正面 RGB LED 灯</span> 和 <span class="green-text">两侧 GREEN LED 灯</span>. 了解这些元素将极大地帮助您有效地设置每个演示。</p>
<hr class="docutils">
<blockquote id="uihwinterfaces">
<div><a class="reference internal image-reference" href="../../../_images/for-buttons.png"><img alt="../../../_images/for-buttons.png" class="align-right" src="/docs-assets/zh-cn/_images/for-buttons.png" style="width: 260.0px; height: 226.3px;"></a>
</div></blockquote>
<p><strong>按钮, LED 和用户交互</strong></p>
<blockquote>
<div><ul class="simple">
<li><p>按钮 A:电源开启/关闭按钮（长按）。</p>
<ul>
<li><p><span class="green-text">GREEN LED</span>: 电源状态</p></li>
</ul>
</li>
<li><p>Button B:在 Qorvo NI / UCI 和 LEAPS UWBS 模式之间切换（长按）。</p>
<ul>
<li><p><span class="green-text">GREEN LED</span>: UWB状态</p></li>
</ul>
</li>
<li><p>Button C: 不适用 (未来使用)。</p>
<ul>
<li><p>RGB LEDs: 表示开机时的设备模式。</p>
<ul>
<li><p><span class="red-text">RED</span> 是 LEAPS UWBS</p></li>
<li><p><span class="blue-text">BLUE</span> 是 Qorvo NI</p></li>
<li><p><span class="green-text">GREEN</span> 是 Qorvo NI</p></li>
</ul>
</li>
</ul>
</li>
<li><p>A buzzer: 用于报警。</p></li>
<li><p>A haptic motor:用于报警。</p></li>
</ul>
</div></blockquote>
<hr class="docutils">
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/for-usb-type-c.png"><img alt="../../../_images/for-usb-type-c.png" class="align-right" src="/docs-assets/zh-cn/_images/for-usb-type-c.png" style="width: 275.44px; height: 259.16px;"></a>
</div></blockquote>
<p><strong>数据接口</strong></p>
<blockquote>
<div><ul class="simple">
<li><p>USB-C Data Port 1: USB 命令行和二进制 API。</p></li>
<li><p>USB-C Data Port 2: DAPLink + USB/UART 命令行和二进制 API。</p></li>
<li><p>集成 UWB 天线。</p></li>
<li><p>集成Bluetooth天线。</p></li>
</ul>
</div></blockquote>
<hr class="docutils">
<p><strong>开发接口</strong></p>
<blockquote>
<div><ul class="simple">
<li><p>集成DAPLink与SWD调试器和USB/UART转换器：用于编程、调试和设备配置。</p></li>
<li><p>用于外部 J-Link 调试器的 6 针 Tag Connect 兼容连接器。</p></li>
<li><p>PCB jumper pads: swd_rst, swd_dio, swd_clk, dbg_txd, dbg_rxd.</p></li>
<li><p>GPIOs: J11 (P0.21, P0.24, DW_GP0, DW_GP1, DW_GP2, DW_GP3, DW_GP4, DW_GP5, DW_GP6), J12 (P0.11, P0.12, P0.13, P0.14, P0.29, P0.31, P1.14, P1.07).</p></li>
<li><p>NFC antenna pads: P0.09/NFC1, P0.10/NFC2.</p></li>
<li><p>3.7V电池连接器。</p></li>
</ul>
<a class="reference internal image-reference" href="../../../_images/lc14_b2-top-view.png"><img alt="../../../_images/lc14_b2-top-view.png" class="align-center" src="/docs-assets/zh-cn/_images/lc14_b2-top-view.png" style="width: 452.5px; height: 561.5px;"></a>
</div></blockquote>
<hr class="docutils">
<p><strong>端口引脚映射</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 51%">
<col style="width: 24%">
<col style="width: 24%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>替代功能</p></th>
<th class="head"><p><a class="reference internal" href="/docs/zh/leaps-rtls#leaps-rtls"><span class="std std-ref">LEAPS RTLS</span></a></p></th>
<th class="head"><p><a class="reference internal" href="/docs/zh/pans-pro-rtls#pans-pro-rtls"><span class="std std-ref">PANS PRO RTLS</span></a></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>UART TX</p></td>
<td><p>P1.13</p></td>
<td><p>P1.13</p></td>
</tr>
<tr class="row-odd"><td><p>UART RX</p></td>
<td><p>P1.15</p></td>
<td><p>P1.15</p></td>
</tr>
<tr class="row-even"><td><p>UWB SPI CS</p></td>
<td><p>P0.20</p></td>
<td><p>P0.20</p></td>
</tr>
<tr class="row-odd"><td><p>UWB SPI CLK</p></td>
<td><p>P0.16</p></td>
<td><p>P0.16</p></td>
</tr>
<tr class="row-even"><td><p>UWB SPI SDO</p></td>
<td><p>P0.17</p></td>
<td><p>P0.17</p></td>
</tr>
<tr class="row-odd"><td><p>UWB SPI SDI</p></td>
<td><p>P0.23</p></td>
<td><p>P0.23</p></td>
</tr>
<tr class="row-even"><td><p>UWB IRQ</p></td>
<td><p>P0.25</p></td>
<td><p>P0.25</p></td>
</tr>
<tr class="row-odd"><td><p>UWB 复位</p></td>
<td><p>P0.15</p></td>
<td><p>P0.15</p></td>
</tr>
<tr class="row-even"><td><p>LED RED</p></td>
<td><p>P0.27</p></td>
<td><p>P0.27</p></td>
</tr>
<tr class="row-odd"><td><p>LED BLUE</p></td>
<td><p>P0.4</p></td>
<td><p>P0.4</p></td>
</tr>
<tr class="row-even"><td><p>LED GREEN</p></td>
<td><p>P0.5</p></td>
<td><p>P0.5</p></td>
</tr>
<tr class="row-odd"><td><p>LED 外部 0</p></td>
<td><p>P1.12</p></td>
<td><p>P1.12</p></td>
</tr>
<tr class="row-even"><td><p>LED 外部 1</p></td>
<td><p>P0.30</p></td>
<td><p>P0.30</p></td>
</tr>
<tr class="row-odd"><td><p>主按钮</p></td>
<td><p>P0.26</p></td>
<td><p>P0.26</p></td>
</tr>
<tr class="row-even"><td><p>按钮外部 0</p></td>
<td><p>P1.11</p></td>
<td><p>P1.11</p></td>
</tr>
<tr class="row-odd"><td><p>按钮外部 1</p></td>
<td><p>P0.28</p></td>
<td><p>P0.28</p></td>
</tr>
<tr class="row-even"><td><p>ACC I2C SDA</p></td>
<td><p>P0.22</p></td>
<td><p>P0.22</p></td>
</tr>
<tr class="row-odd"><td><p>ACC I2C SCL</p></td>
<td><p>P0.19</p></td>
<td><p>P0.19</p></td>
</tr>
<tr class="row-even"><td><p>ACC IRQ</p></td>
<td><p>P1.1</p></td>
<td><p>P1.1</p></td>
</tr>
<tr class="row-odd"><td><p>蜂鸣器</p></td>
<td><p>P0.2</p></td>
<td><p>P0.2</p></td>
</tr>
<tr class="row-even"><td><p>发动机</p></td>
<td><p>P1.10</p></td>
<td><p>P1.10</p></td>
</tr>
<tr class="row-odd"><td><p>电池 ADC 管脚</p></td>
<td><p>P0.3</p></td>
<td><p>P0.3</p></td>
</tr>
<tr class="row-even"><td><p>DCDC3V3 控制引脚</p></td>
<td><p>不适用</p></td>
<td><p>不适用</p></td>
</tr>
<tr class="row-odd"><td><p>充电器状态引脚</p></td>
<td><p>不适用</p></td>
<td><p>不适用</p></td>
</tr>
<tr class="row-even"><td><p>USB 检测器引脚</p></td>
<td><p>P1.9</p></td>
<td><p>不适用</p></td>
</tr>
<tr class="row-odd"><td><p>API SPI CS</p></td>
<td><p>P0.29</p></td>
<td><p>P0.12</p></td>
</tr>
<tr class="row-even"><td><p>API SPI CLK</p></td>
<td><p>P0.12</p></td>
<td><p>P0.11</p></td>
</tr>
<tr class="row-odd"><td><p>API SPI SDO</p></td>
<td><p>P0.11</p></td>
<td><p>P0.14</p></td>
</tr>
<tr class="row-even"><td><p>API SPI SDI</p></td>
<td><p>P0.14</p></td>
<td><p>P0.31</p></td>
</tr>
<tr class="row-odd"><td><p>API IRQ</p></td>
<td><p>P0.31</p></td>
<td><p>P0.29</p></td>
</tr>
</tbody>
</table>
</div>


           </div>
