---
title: "LEAPS RTLS功能"
lang: zh
slug: "udk/specification/leaps-rtls-features"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/zh-cn/udk/specification/leaps-rtls-features/"
order: 52
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-rtls-features">
<h1>LEAPS RTLS功能</h1>
<p>除了UDK套件的特定功能外，本节还从更广泛的角度概述了LEAPS RTLS系统。</p>
<hr class="docutils">
<div class="section" id="key-features">
<h2>主要功能</h2>
<p>LEAPS RTLS 系统利用超宽带无线技术为实时精确定位和数据遥测提供了先进而全面的解决方案。 该解决方案的核心是名为 LEAPS UWBS（超宽带子系统）的高度复杂的嵌入式软件堆栈，可提供许多先进功能，包括</p>
<ul class="simple">
<li><p>体积小, 功能多，使 LEAPS 成为一把独特的瑞士军刀，可实时进行精确定位和数据遥测。 UWB子系统以一个固件为基础，可配置为不同的模式和网络配置文件。</p></li>
<li><p>高度嵌入, 高效, 优化的堆栈，注重多功能, 高性能, 低内存和低功耗。</p></li>
<li><p>经过验证的系统可扩展性，部署于各种大型工厂和建筑，运行范围达 50,000 平方米以上。</p></li>
<li><p>模块化结构便于添加新功能和支持新硬件，目前支持超过 15 种不同的板卡类型和变体。</p></li>
<li><p>目前，它可用于各种硬件平台，包括村田 2AB, DWM3001C, DWM1001C 和 Ambiq Micro MCU。</p></li>
<li><p>广泛的应用程序接口允许用户根据自己的特定需求轻松配置和定制系统，为实时位置跟踪提供了一个适应性强, 用途广泛的解决方案。 该应用程序可通过 UART, USB, SPI, BLE 等各种接口使用二进制类型-长度-值（TLV）帧格式，或通过 UART, USB 和 BLE 接口使用人类可读的 shell 命令行。</p></li>
<li><p>LEAPS RTLS 系统还提供了大量免费的软件工具，让系统的配置和管理变得更容易。</p></li>
<li><p>LEAPS RTLS 的持续发展将提供更多的功能，以涵盖未来更广泛的应用。 这让用户和产品制造商可以学习一个概念，并在许多应用中部署。</p></li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="performance">
<h2>性能</h2>
<ul class="simple">
<li><p>网络堆栈的设计方式，是利用有效的机制，让锚点和标签都能重复使用通话时间。 这样，就可以在扩散区域内部署几乎无限量的节点。 所有这些都是通过主播自动集群和标签漫游的有效机制自动实现的。</p></li>
<li><p>根据标签的测量模式，最大密度可以是 TWR 的 320 Hz, UL-TDoA 的 600 Hz，或使用 DL-TDoA 时的无限量标签。 最大密度是在特定条件下实现的，当所有标签都在彼此的量程范围内时，可以有 3200 个标签，更新率为</p></li>
<li><p>最大标签定位率： 取决于网络配置文件和测量模式。 TWR, DL-TDoA 和UL-TDoA通常为 10 Hz。 DL-TDoA可以为每个标签提供高达 50 Hz 的更新率。</p></li>
<li><p>X-Y定位精度:优于50公分，通常为10公分。</p></li>
<li><p>点对点范围:在视距条件下（CH5/CH9）最远可达50米，使用PA时最远可达150米。</p></li>
<li><p>基础设施部署网格尺寸:通常为 20 x 20 米，最大可达 40 x 40 米。</p></li>
<li><p>卓越的电源管理为TWR和TDoA模式提供了较长的电池寿命。</p></li>
<li><p>利用运动传感器活动的自适应定位率，可延长电池寿命并增加标签总数。</p></li>
</ul>
</div>
</div>


           </div>
