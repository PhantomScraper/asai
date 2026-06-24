---
title: "LM8"
lang: ja
slug: "hardware/lm8"
section: "hardware"
sourceUrl: "https://docs.leapslabs.com/ja/hardware/lm8/"
order: 27
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="lm8">
<h1>LM8</h1>
<p>このページは LM8 モジュールの基本情報を提供します</p>
<div class="section" id="key-features">
<h2>主な機能</h2>
<ul class="simple">
<li><p>muRata 2AB モジュールに基づく</p></li>
<li><p><a class="reference internal" href="/docs/ja/hardware/dwm3001c#dwm3001c"><span class="std std-ref">DWM3001C</span></a> モジュールとピン互換です。</p></li>
<li><p><a class="reference internal" href="/docs/ja/hardware/dwm3001c#dwm3001c"><span class="std std-ref">DWM3001C</span></a> モジュールと同じフォームファクタです。</p></li>
<li><p>拡張レンジ用統合LNA</p></li>
<li><p>日本の UWB 規制に準拠</p></li>
</ul>
</div>
<div class="section" id="software-compatibility">
<h2>ソフトウェアの互換性</h2>
<p><a class="reference internal" href="/docs/ja/leaps-rtls#leaps-rtls"><span class="std std-ref">LEAPS RTLS</span></a> と <a class="reference internal" href="/docs/ja/pans-pro-rtls#pans-pro-rtls"><span class="std std-ref">PANS PRO RTLS</span></a> の両方と互換性があります。</p>
</div>
<hr class="docutils">
<div class="section" id="block-diagram">
<h2>ブロックダイアグラム</h2>
<blockquote>
<div><a class="reference internal image-reference" href="../../_images/lm8-block-digram.png"><img alt="../../_images/lm8-block-digram.png" class="align-center" src="/docs-assets/ja/_images/lm8-block-digram.png" style="width: 730.0999999999999px; height: 492.09999999999997px;"></a>
</div></blockquote>
</div>
<hr class="docutils">
<div class="section" id="pinouts-description">
<h2>ピン配列 説明</h2>
<p><strong>ピン番号</strong></p>
<p>LM8 モジュールのピン配置は以下の通りです（上から見て）：</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../_images/lm8-pin-numbering.png"><img alt="../../_images/lm8-pin-numbering.png" class="align-center" src="/docs-assets/ja/_images/lm8-pin-numbering.png" style="width: 611.8px; height: 633.65px;"></a>
</div></blockquote>
<hr class="docutils">
<p><strong>ピンの説明</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 22%">
<col style="width: 10%">
<col style="width: 11%">
<col style="width: 42%">
<col style="width: 16%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>信号名</strong></p></th>
<th class="head"><p><strong>ピン</strong></p></th>
<th class="head"><p><strong>I/O</strong> （デフォルト）</p></th>
<th class="head"><p><strong>説明</strong></p></th>
<th class="head"><p><strong>ICピンリファレンス</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td colspan="5"><p><strong>デジタルインターフェース</strong></p></td>
</tr>
<tr class="row-odd"><td><p>SWD_CLK</p></td>
<td><p>2</p></td>
<td><p>DI</p></td>
<td><p>Nordic Processor のデバッグおよびプログラミング用のシリアルワイヤデバッグクロック入力です。</p></td>
<td><p>SWD_CLK</p></td>
</tr>
<tr class="row-even"><td><p>SWD_DIO</p></td>
<td><p>3</p></td>
<td><p>DIO</p></td>
<td><p>Nordic Processor のデバッグおよびプログラミング用のシリアルワイヤデバッグ I/O です。</p></td>
<td><p>SWD_DIO</p></td>
</tr>
<tr class="row-odd"><td><p>GPIO_1/NFC1</p></td>
<td><p>4</p></td>
<td><p>ミックス</p></td>
<td><p>nRF52840 プロセッサの汎用入出力ピンです。NFC アンテナ接続。</p></td>
<td><p>P0.10</p></td>
</tr>
<tr class="row-even"><td><p>GPIO_2/NFC2</p></td>
<td><p>5</p></td>
<td><p>ミックス</p></td>
<td><p>nRF52840 プロセッサの汎用入出力ピンです。NFC アンテナ接続。</p></td>
<td><p>P0.09</p></td>
</tr>
<tr class="row-odd"><td><p>GPIO_3</p></td>
<td><p>6</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840プロセッサの汎用I/Oピン。</p></td>
<td><p>P0.21</p></td>
</tr>
<tr class="row-even"><td><p>GPIO_4</p></td>
<td><p>7</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840プロセッサの汎用I/Oピン。</p></td>
<td><p>P0.24</p></td>
</tr>
<tr class="row-odd"><td><p>GPIO_5</p></td>
<td><p>8</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840プロセッサの汎用I/Oピン。</p></td>
<td><p>P1.08</p></td>
</tr>
<tr class="row-even"><td><p>GPIO_6</p></td>
<td><p>9</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840プロセッサの汎用I/Oピン。</p></td>
<td><p>P0.05 (AIN)</p></td>
</tr>
<tr class="row-odd"><td><p>GPIO_7</p></td>
<td><p>10</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840プロセッサの汎用I/Oピン。</p></td>
<td><p>P0.04 (AIN)</p></td>
</tr>
<tr class="row-even"><td><p>GPIO_8</p></td>
<td><p>13</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840プロセッサの汎用I/Oピン。</p></td>
<td><p>P1.09</p></td>
</tr>
<tr class="row-odd"><td><p>I2C_SDA</p></td>
<td><p>14</p></td>
<td><p>DIO</p></td>
<td><p>I2C データライン</p></td>
<td><p>I2C_SDA</p></td>
</tr>
<tr class="row-even"><td><p>I2C_SCL</p></td>
<td><p>15</p></td>
<td><p>DO</p></td>
<td><p>I2Cクロックライン</p></td>
<td><p>I2C_SCL</p></td>
</tr>
<tr class="row-odd"><td><p>GPIO_9</p></td>
<td><p>16</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840プロセッサの汎用I/Oピン。</p></td>
<td><p>P0.08</p></td>
</tr>
<tr class="row-even"><td><p>GPIO_10</p></td>
<td><p>17</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840プロセッサの汎用I/Oピン。</p></td>
<td><p>P0.07</p></td>
</tr>
<tr class="row-odd"><td><p>VUSB</p></td>
<td><p>18</p></td>
<td><p>P</p></td>
<td><p>MCU USB 3.3Vレギュレータ用電源(4.4~5.5V)</p></td>
<td><p>VUSB</p></td>
</tr>
<tr class="row-even"><td><p>USB_N</p></td>
<td><p>19</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840 プロセッサ用 USB D- I/O。</p></td>
<td><p>USB_N</p></td>
</tr>
<tr class="row-odd"><td><p>USB_P</p></td>
<td><p>20</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840プロセッサ用USB D+ I/O。</p></td>
<td><p>USB_P</p></td>
</tr>
<tr class="row-even"><td><p>GPIO_11</p></td>
<td><p>22</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840プロセッサの汎用I/Oピン。</p></td>
<td><p>P0.12</p></td>
</tr>
<tr class="row-odd"><td><p>GPIO_12</p></td>
<td><p>23</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840プロセッサの汎用I/Oピン。</p></td>
<td><p>P0.11</p></td>
</tr>
<tr class="row-even"><td><p>GPIO_13</p></td>
<td><p>24</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840プロセッサの汎用I/Oピン。</p></td>
<td><p>P0.13</p></td>
</tr>
<tr class="row-odd"><td><p>GPIO_14</p></td>
<td><p>25</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840プロセッサの汎用I/Oピン。</p></td>
<td><p>P0.14</p></td>
</tr>
<tr class="row-even"><td><p>GPIO_15</p></td>
<td><p>26</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840プロセッサの汎用I/Oピン。</p></td>
<td><p>P0.27</p></td>
</tr>
<tr class="row-odd"><td><p>GPIO_16</p></td>
<td><p>27</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840プロセッサの汎用I/Oピン。</p></td>
<td><p>P0.26</p></td>
</tr>
<tr class="row-even"><td><p>GPIO_17</p></td>
<td><p>28</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840プロセッサの汎用I/Oピン。</p></td>
<td><p>P0.30</p></td>
</tr>
<tr class="row-odd"><td><p>GPIO_18</p></td>
<td><p>29</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840プロセッサの汎用I/Oピン。</p></td>
<td><p>P0.28</p></td>
</tr>
<tr class="row-even"><td><p>DW_GP5</p></td>
<td><p>30</p></td>
<td><p>DW</p></td>
<td><p>QM33120Wの汎用I/O</p></td>
<td><p>DW_GP5</p></td>
</tr>
<tr class="row-odd"><td><p>LNA CTRL</p></td>
<td><p>31</p></td>
<td><p>DW</p></td>
<td><p>QM33120Wの汎用I/O、低雑音アンプ制御端子</p></td>
<td><p>DW_GP6</p></td>
</tr>
<tr class="row-even"><td><p>GPIO_19</p></td>
<td><p>32</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840プロセッサの汎用I/Oピン。</p></td>
<td><p>P1.15</p></td>
</tr>
<tr class="row-odd"><td><p>GPIO_20</p></td>
<td><p>33</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840プロセッサの汎用I/Oピン。</p></td>
<td><p>P0.02 (AIN)</p></td>
</tr>
<tr class="row-even"><td><p>GPIO_21</p></td>
<td><p>34</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840プロセッサの汎用I/Oピン。</p></td>
<td><p>P1.13</p></td>
</tr>
<tr class="row-odd"><td><p>DW_GP1</p></td>
<td><p>35</p></td>
<td><p>DW</p></td>
<td><p>QM33120Wの汎用I/O</p></td>
<td><p>DW_GP1</p></td>
</tr>
<tr class="row-even"><td><p>DW_GP0</p></td>
<td><p>36</p></td>
<td><p>DW</p></td>
<td><p>QM33120Wの汎用I/O</p></td>
<td><p>DW_GP0</p></td>
</tr>
<tr class="row-odd"><td><p>GPIO_22</p></td>
<td><p>37</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840プロセッサの汎用I/Oピン。</p></td>
<td><p>P1.12</p></td>
</tr>
<tr class="row-even"><td><p>GPIO_23</p></td>
<td><p>39</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840プロセッサの汎用I/Oピン。</p></td>
<td><p>P1.14</p></td>
</tr>
<tr class="row-odd"><td><p>GPIO_24</p></td>
<td><p>40</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840プロセッサの汎用I/Oピン。</p></td>
<td><p>P1.11</p></td>
</tr>
<tr class="row-even"><td><p>GPIO_25</p></td>
<td><p>41</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840プロセッサの汎用I/Oピン。</p></td>
<td><p>P1.10</p></td>
</tr>
<tr class="row-odd"><td><p>GPIO_26</p></td>
<td><p>42</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840プロセッサの汎用I/Oピン。</p></td>
<td><p>P0.03 (AIN)</p></td>
</tr>
<tr class="row-even"><td><p>GPIO_27</p></td>
<td><p>43</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840プロセッサの汎用I/Oピン。</p></td>
<td><p>P0.29 (AIN)</p></td>
</tr>
<tr class="row-odd"><td><p>DW_GP3</p></td>
<td><p>44</p></td>
<td><p>DW</p></td>
<td><p>QM33120Wの汎用I/O</p></td>
<td><p>DW_GP3</p></td>
</tr>
<tr class="row-even"><td><p>DW_GP2</p></td>
<td><p>45</p></td>
<td><p>DW</p></td>
<td><p>QM33120Wの汎用I/O</p></td>
<td><p>DW_GP2</p></td>
</tr>
<tr class="row-odd"><td><p>GPIO_28</p></td>
<td><p>46</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840プロセッサの汎用I/Oピン。</p></td>
<td><p>P0.31 (AIN)</p></td>
</tr>
<tr class="row-even"><td><p>GPIO_29</p></td>
<td><p>47</p></td>
<td><p>DIO</p></td>
<td><p>nRF52840プロセッサの汎用I/Oピン。</p></td>
<td><p>P0.18</p></td>
</tr>
<tr class="row-odd"><td colspan="5"><p><strong>電源</strong></p></td>
</tr>
<tr class="row-even"><td><p>VCC</p></td>
<td><p>12</p></td>
<td><p>P</p></td>
<td><p>モジュールの外部電源 2.8V - 3.6V</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>GND</p></td>
<td><p>1, 11, 21
38, 48</p></td>
<td><p>G</p></td>
<td><p>共通の基盤。</p></td>
<td></td>
</tr>
</tbody>
</table>
<hr class="docutils">
<p><strong>略語の説明</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 34%">
<col style="width: 66%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>略語</strong></p></th>
<th class="head"><p><strong>説明</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>DI</p></td>
<td><p>デジタル入力</p></td>
</tr>
<tr class="row-odd"><td><p>DIO</p></td>
<td><p>デジタル入出力</p></td>
</tr>
<tr class="row-even"><td><p>DO</p></td>
<td><p>デジタル出力</p></td>
</tr>
<tr class="row-odd"><td><p>G</p></td>
<td><p>グラウンド</p></td>
</tr>
<tr class="row-even"><td><p>P</p></td>
<td><p>パワー</p></td>
</tr>
<tr class="row-odd"><td><p>DW</p></td>
<td><p>DW1000</p></td>
</tr>
</tbody>
</table>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<p>接尾辞が'n'の信号はアクティブ・ロー信号を示す。</p>
</div>
</div>
</div>


           </div>
