---
title: "LM8"
lang: zh
slug: "hardware/lm8"
section: "hardware"
sourceUrl: "https://docs.leapslabs.com/zh-cn/hardware/lm8/"
order: 27
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="lm8">
<h1>LM8</h1>
<p>本页提供有关 LM8 模块的基本信息</p>
<div class="section" id="key-features">
<h2>主要功能</h2>
<ul class="simple">
<li><p>基于muRata 2AB模块</p></li>
<li><p>与 <a class="reference internal" href="/docs/zh/hardware/dwm3001c#dwm3001c"><span class="std std-ref">DWM3001C</span></a> 模块引脚兼容</p></li>
<li><p>与 <a class="reference internal" href="/docs/zh/hardware/dwm3001c#dwm3001c"><span class="std std-ref">DWM3001C</span></a> 模块具有相同的外形尺寸</p></li>
<li><p>用于扩展范围的集成LNA</p></li>
<li><p>符合日本UWB法规</p></li>
</ul>
</div>
<div class="section" id="software-compatibility">
<h2>软件兼容性</h2>
<p>它与 <a class="reference internal" href="/docs/zh/leaps-rtls#leaps-rtls"><span class="std std-ref">LEAPS RTLS</span></a> 和 <a class="reference internal" href="/docs/zh/pans-pro-rtls#pans-pro-rtls"><span class="std std-ref">PANS PRO RTLS</span></a> 都兼容。</p>
</div>
<hr class="docutils">
<div class="section" id="block-diagram">
<h2>方框图</h2>
<blockquote>
<div><a class="reference internal image-reference" href="../../_images/lm8-block-digram.png"><img alt="../../_images/lm8-block-digram.png" class="align-center" src="/docs-assets/zh-cn/_images/lm8-block-digram.png" style="width: 730.0999999999999px; height: 492.09999999999997px;"></a>
</div></blockquote>
</div>
<hr class="docutils">
<div class="section" id="pinouts-description">
<h2>引脚说明</h2>
<p><strong>引脚编号</strong></p>
<p>LM8模块的引脚分配如下（从上往下看）:</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../_images/lm8-pin-numbering.png"><img alt="../../_images/lm8-pin-numbering.png" class="align-center" src="/docs-assets/zh-cn/_images/lm8-pin-numbering.png" style="width: 611.8px; height: 633.65px;"></a>
</div></blockquote>
<hr class="docutils">
<p><em>针脚说明*</em></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 22%">
<col style="width: 10%">
<col style="width: 11%">
<col style="width: 42%">
<col style="width: 16%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>信号名称</strong></p></th>
<th class="head"><p><strong>引脚</strong></p></th>
<th class="head"><p><strong>输入/输出</strong> (默认)</p></th>
<th class="head"><p><strong>描述</strong></p></th>
<th class="head"><p><strong>集成电路引脚参考</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td colspan="5"><p><strong>数字接口</strong></p></td>
</tr>
<tr class="row-odd"><td><p>SWD_CLK</p></td>
<td><p>2</p></td>
<td><p>DI</p></td>
<td><p>串行线调试时钟输入，用于Nordic处理器的调试和编程。</p></td>
<td><p>SWD_CLK</p></td>
</tr>
<tr class="row-even"><td><p>SWD_DIO</p></td>
<td><p>3</p></td>
<td><p>DIO</p></td>
<td><p>串行线调试输入/输出，用于 Nordic 处理器的调试和编程。</p></td>
<td><p>SWD_DIO</p></td>
</tr>
<tr class="row-odd"><td><p>GPIO_1/NFC1</p></td>
<td><p>4</p></td>
<td><p>混合</p></td>
<td><p>nRF52840 处理器的通用输入/输出引脚. NFC 天线连接。</p></td>
<td><p>P0.10</p></td>
</tr>
<tr class="row-even"><td><p>GPIO_2/NFC2</p></td>
<td><p>5</p></td>
<td><p>混合</p></td>
<td><p>nRF52840 处理器的通用输入/输出引脚. NFC 天线连接。</p></td>
<td><p>P0.09</p></td>
</tr>
<tr class="row-odd"><td><p>GPIO_3</p></td>
<td><p>6</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840 处理器的通用输入/输出引脚。</p></td>
<td><p>P0.21</p></td>
</tr>
<tr class="row-even"><td><p>GPIO_4</p></td>
<td><p>7</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840 处理器的通用输入/输出引脚。</p></td>
<td><p>P0.24</p></td>
</tr>
<tr class="row-odd"><td><p>GPIO_5</p></td>
<td><p>8</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840 处理器的通用输入/输出引脚。</p></td>
<td><p>P1.08</p></td>
</tr>
<tr class="row-even"><td><p>GPIO_6</p></td>
<td><p>9</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840 处理器的通用输入/输出引脚。</p></td>
<td><p>P0.05 (AIN)</p></td>
</tr>
<tr class="row-odd"><td><p>GPIO_7</p></td>
<td><p>10</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840 处理器的通用输入/输出引脚。</p></td>
<td><p>P0.04 (AIN)</p></td>
</tr>
<tr class="row-even"><td><p>GPIO_8</p></td>
<td><p>13</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840 处理器的通用输入/输出引脚。</p></td>
<td><p>P1.09</p></td>
</tr>
<tr class="row-odd"><td><p>I2C_SDA</p></td>
<td><p>14</p></td>
<td><p>DIO</p></td>
<td><p>I2C 数据线</p></td>
<td><p>I2C_SDA</p></td>
</tr>
<tr class="row-even"><td><p>I2C_SCL</p></td>
<td><p>15</p></td>
<td><p>DO</p></td>
<td><p>I2C时钟线</p></td>
<td><p>I2C_SCL</p></td>
</tr>
<tr class="row-odd"><td><p>GPIO_9</p></td>
<td><p>16</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840 处理器的通用输入/输出引脚。</p></td>
<td><p>P0.08</p></td>
</tr>
<tr class="row-even"><td><p>GPIO_10</p></td>
<td><p>17</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840 处理器的通用输入/输出引脚。</p></td>
<td><p>P0.07</p></td>
</tr>
<tr class="row-odd"><td><p>VUSB</p></td>
<td><p>18</p></td>
<td><p>P</p></td>
<td><p>用于MCU的电源(4.4~5.5V) USB 3.3V 稳压器</p></td>
<td><p>VUSB</p></td>
</tr>
<tr class="row-even"><td><p>USB_N</p></td>
<td><p>19</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840处理器的USB D-输入/输出。</p></td>
<td><p>USB_N</p></td>
</tr>
<tr class="row-odd"><td><p>USB_P</p></td>
<td><p>20</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840处理器的USB D+输入/输出。</p></td>
<td><p>USB_P</p></td>
</tr>
<tr class="row-even"><td><p>GPIO_11</p></td>
<td><p>22</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840 处理器的通用输入/输出引脚。</p></td>
<td><p>P0.12</p></td>
</tr>
<tr class="row-odd"><td><p>GPIO_12</p></td>
<td><p>23</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840 处理器的通用输入/输出引脚。</p></td>
<td><p>P0.11</p></td>
</tr>
<tr class="row-even"><td><p>GPIO_13</p></td>
<td><p>24</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840 处理器的通用输入/输出引脚。</p></td>
<td><p>P0.13</p></td>
</tr>
<tr class="row-odd"><td><p>GPIO_14</p></td>
<td><p>25</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840 处理器的通用输入/输出引脚。</p></td>
<td><p>P0.14</p></td>
</tr>
<tr class="row-even"><td><p>GPIO_15</p></td>
<td><p>26</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840 处理器的通用输入/输出引脚。</p></td>
<td><p>P0.27</p></td>
</tr>
<tr class="row-odd"><td><p>GPIO_16</p></td>
<td><p>27</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840 处理器的通用输入/输出引脚。</p></td>
<td><p>P0.26</p></td>
</tr>
<tr class="row-even"><td><p>GPIO_17</p></td>
<td><p>28</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840 处理器的通用输入/输出引脚。</p></td>
<td><p>P0.30</p></td>
</tr>
<tr class="row-odd"><td><p>GPIO_18</p></td>
<td><p>29</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840 处理器的通用输入/输出引脚。</p></td>
<td><p>P0.28</p></td>
</tr>
<tr class="row-even"><td><p>DW_GP5</p></td>
<td><p>30</p></td>
<td><p>DW</p></td>
<td><p>QM33120W 的通用输入/输出</p></td>
<td><p>DW_GP5</p></td>
</tr>
<tr class="row-odd"><td><p>LNA CTRL</p></td>
<td><p>31</p></td>
<td><p>DW</p></td>
<td><p>QM33120W低噪声放大器控制引脚的通用输入/输出</p></td>
<td><p>DW_GP6</p></td>
</tr>
<tr class="row-even"><td><p>GPIO_19</p></td>
<td><p>32</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840 处理器的通用输入/输出引脚。</p></td>
<td><p>P1.15</p></td>
</tr>
<tr class="row-odd"><td><p>GPIO_20</p></td>
<td><p>33</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840 处理器的通用输入/输出引脚。</p></td>
<td><p>P0.02 (AIN)</p></td>
</tr>
<tr class="row-even"><td><p>GPIO_21</p></td>
<td><p>34</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840 处理器的通用输入/输出引脚。</p></td>
<td><p>P1.13</p></td>
</tr>
<tr class="row-odd"><td><p>DW_GP1</p></td>
<td><p>35</p></td>
<td><p>DW</p></td>
<td><p>QM33120W 的通用输入/输出</p></td>
<td><p>DW_GP1</p></td>
</tr>
<tr class="row-even"><td><p>DW_GP0</p></td>
<td><p>36</p></td>
<td><p>DW</p></td>
<td><p>QM33120W 的通用输入/输出</p></td>
<td><p>DW_GP0</p></td>
</tr>
<tr class="row-odd"><td><p>GPIO_22</p></td>
<td><p>37</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840 处理器的通用输入/输出引脚。</p></td>
<td><p>P1.12</p></td>
</tr>
<tr class="row-even"><td><p>GPIO_23</p></td>
<td><p>39</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840 处理器的通用输入/输出引脚。</p></td>
<td><p>P1.14</p></td>
</tr>
<tr class="row-odd"><td><p>GPIO_24</p></td>
<td><p>40</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840 处理器的通用输入/输出引脚。</p></td>
<td><p>P1.11</p></td>
</tr>
<tr class="row-even"><td><p>GPIO_25</p></td>
<td><p>41</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840 处理器的通用输入/输出引脚。</p></td>
<td><p>P1.10</p></td>
</tr>
<tr class="row-odd"><td><p>GPIO_26</p></td>
<td><p>42</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840 处理器的通用输入/输出引脚。</p></td>
<td><p>P0.03 (AIN)</p></td>
</tr>
<tr class="row-even"><td><p>GPIO_27</p></td>
<td><p>43</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840 处理器的通用输入/输出引脚。</p></td>
<td><p>P0.29 (AIN)</p></td>
</tr>
<tr class="row-odd"><td><p>DW_GP3</p></td>
<td><p>44</p></td>
<td><p>DW</p></td>
<td><p>QM33120W 的通用输入/输出</p></td>
<td><p>DW_GP3</p></td>
</tr>
<tr class="row-even"><td><p>DW_GP2</p></td>
<td><p>45</p></td>
<td><p>DW</p></td>
<td><p>QM33120W 的通用输入/输出</p></td>
<td><p>DW_GP2</p></td>
</tr>
<tr class="row-odd"><td><p>GPIO_28</p></td>
<td><p>46</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840 处理器的通用输入/输出引脚。</p></td>
<td><p>P0.31 (AIN)</p></td>
</tr>
<tr class="row-even"><td><p>GPIO_29</p></td>
<td><p>47</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840 处理器的通用输入/输出引脚。</p></td>
<td><p>P0.18</p></td>
</tr>
<tr class="row-odd"><td colspan="5"><p><strong>电源供应</strong></p></td>
</tr>
<tr class="row-even"><td><p>VCC</p></td>
<td><p>12</p></td>
<td><p>P</p></td>
<td><p>模块外部电源。 2.8V - 3.6V</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>GND</p></td>
<td><p>1, 11, 21
38, 48</p></td>
<td><p>G</p></td>
<td><p>共同点。</p></td>
<td></td>
</tr>
</tbody>
</table>
<hr class="docutils">
<p><strong>缩略语解释</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 34%">
<col style="width: 66%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>缩写</strong></p></th>
<th class="head"><p><strong>解释</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>DI</p></td>
<td><p>数字输入</p></td>
</tr>
<tr class="row-odd"><td><p>DIO</p></td>
<td><p>数字输入/输出</p></td>
</tr>
<tr class="row-even"><td><p>DO</p></td>
<td><p>数字输出</p></td>
</tr>
<tr class="row-odd"><td><p>G</p></td>
<td><p>接地</p></td>
</tr>
<tr class="row-even"><td><p>P</p></td>
<td><p>电源</p></td>
</tr>
<tr class="row-odd"><td><p>DW</p></td>
<td><p>DW1000</p></td>
</tr>
</tbody>
</table>
<div class="admonition note">
<p class="admonition-title">注解</p>
<p>任何后缀为‘n’的信号都表示低电平有效信号。</p>
</div>
</div>
</div>


           </div>
