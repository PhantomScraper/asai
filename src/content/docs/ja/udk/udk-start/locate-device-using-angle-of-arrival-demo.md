---
title: "到着角度(AoA)を使ったデバイスの位置特定デモ"
lang: ja
slug: "udk/udk-start/locate-device-using-angle-of-arrival-demo"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/ja/udk/udk-start/locate-device-using-angle-of-arrival-demo/"
order: 84
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="locate-device-using-angle-of-arrival-aoa-demo">
<span id="anchor-lc"></span><h1>到着角度(AoA)を使ったデバイスの位置特定デモ</h1>
<a class="reference internal image-reference" href="../../../_images/locate_device_using_angle-of-arrival_demo.png"><img alt="../../../_images/locate_device_using_angle-of-arrival_demo.png" class="align-right" src="/docs-assets/ja/_images/locate_device_using_angle-of-arrival_demo.png" style="width: 216.0px; height: 245.88px;"></a>
<p><strong>セットアップの準備</strong></p>
<ol class="arabic simple">
<li><p><a class="reference internal" href="/docs/ja/udk/udk-start/partner-application-aoa-app#anchor-ranging-aoa"><span class="std std-ref">UWB レンジングおよび AoA デモ アプリ</span></a> デスクトッププログラムがコンピュータにインストールされています。</p></li>
<li><p>LC13 (灰色) デバイスが1台、LC14 (白) デバイスが少なくとも1台必要です。</p></li>
<li><p>接続デバイス用の USB-C データケーブル。</p></li>
<li><p><em>オプション:</em> <a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> <em>アプリケーションがインストールされました。</em></p></li>
<li><p><em>オプション: レスポンダデバイス用のバッテリー</em></p></li>
</ol>
<p><strong>セットアップ時間:</strong> 5 分未満</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
クイックスタート</label><div class="sd-tab-content docutils">
<p><strong>概要</strong></p>
<p>このセットアップは、デバイス間の <span class="red-text">FiRa compatibility</span> を示す。距離と角度の測定は、デスクトップアプリケーションの Initiator と Responder デバイス間の方向を示す。</p>
<p><strong>典型的なアプリケーション</strong>：入退室管理、フォローミー、屋内環境内のオブジェクトやデバ イスの検索と追跡。</p>
<p><strong>セットアップ手順</strong></p>
<ol class="arabic simple">
<li><p>アプリケーションをダウンロードし、コンピュータにインストールします。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>詳細は <a class="reference internal" href="/docs/ja/udk/udk-start/partner-application-aoa-app#anchor-ranging-aoa"><span class="std std-ref">UWB レンジングおよび AoA デモ アプリ</span></a> のインストール手順を参照してください。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>LC13 と LC14 デバイスの電源を <span class="red-text">ON</span> します。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>LC13 はイニシエータとして機能し、LC14 はレスポンダとして機能する。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>以下のオプションのいずれかを使用して、デバイスを <span class="red-text">Qorvo UCI mode</span> に設定する：</p></li>
</ol>
<blockquote>
<div><ol class="upperalpha simple">
<li><p>ボタンを使用してデバイスを設定します。</p></li>
</ol>
<blockquote>
<div><p>3.1. <a class="reference internal" href="/docs/ja/udk/udk-start/device-hw-interfaces#uihwinterfaces"><span class="std std-ref">ボタン B</span></a> を、ビープ音がして <span class="green-text">GREEN LED</span> が点滅するまで押し続けます。</p>
<p>3.2. もし <span class="red-text">RED</span> または <span class="blue-text">BLUE</span> の色が表示されたら、ステップ a を繰り返してください。</p>
<p>3.3. ビープ音の後に <span class="green-text">GREEN LED</span> が点滅した場合、デバイスは <span class="red-text">Qorvo UCI mode</span> に設定されています。</p>
<img alt="../../../_images/leaps-config-to-qorvo-uci-mode.gif" class="align-center" src="/docs-assets/ja/_images/leaps-config-to-qorvo-uci-mode.gif">
</div></blockquote>
<ol class="upperalpha simple" start="2">
<li><p><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a>: のデモ セレクターを使用して設定します。</p></li>
</ol>
<blockquote>
<div><p>3.1。 <a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> を開き、メイン ページから <span class="red-text">Demo Selector</span> を選択します。</p>
<p>3.2. <span class="red-text">Locate Device Using Angle-of-Arrival</span> を選択します。</p>
<p>3.3。 Bluetooth 経由で検出されたデバイスのリストがリストに表示されます。必要に応じて、下にスワイプしてリストを更新します。</p>
<p>3.4. デモに使用するデバイスを選択してください。上側の <span class="red-text">Required devices</span> は、デモに必要なデバイスの数を示しています。</p>
<p>3.5. <span class="red-text">SAVE</span> を押して、デバイスを <span class="red-text">Qorvo UCI mode</span> に設定します。</p>
<p>3.6. デバイスが起動すると <span class="green-text">GREEN LED</span> が点滅することを目視で確認してください。</p>
<img alt="../../../_images/qorvo-uwb-ranging-aoa.gif" class="align-center" src="/docs-assets/ja/_images/qorvo-uwb-ranging-aoa.gif">
</div></blockquote>
</div></blockquote>
<ol class="arabic" start="4">
<li><p>デバイスの接続には USB-C データケーブルを使用し、PC との接続には <a class="reference internal" href="/docs/ja/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C データポート 1 を使用します。Port 1</span></a> をPCに接続する。</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/connect-uwbrangingaoa-002.jpg"><img alt="../../../_images/connect-uwbrangingaoa-002.jpg" src="/docs-assets/ja/_images/connect-uwbrangingaoa-002.jpg" style="width: 98%;"></a>
</div></blockquote>
</li>
</ol>
<blockquote>
<div><p><em>オプションです： オプション：デモを開始した後、レスポンダを PC から切り離して自由に移動させたい場合は、レスポンダにバッテリを接続してください。</em></p>
</div></blockquote>
<ol class="arabic" start="5">
<li><p>デスクトップで <span class="red-text">UWB Ranging &amp; AoA Demo App</span> を開きます。 <span class="red-text">Next</span> をクリックしてデバイスリストに入ります。</p>
<ul class="simple">
<li><p>USB接続されたデバイスがデバイスリストに表示されます。リストを確認し、使用するデバイスを特定してください。デフォルトでは、USB経由で検出されたすべてのデバイスが選択されます。</p></li>
<li><p>必要に応じて、デバイスごとの追加設定や <span class="red-text">Fira Configuration</span> を変更することができます。まずはデフォルト値で問題ないでしょう。</p></li>
</ul>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/uwb_ranging_and_aoa_demo_app_main.png"><img alt="../../../_images/uwb_ranging_and_aoa_demo_app_main.png" src="/docs-assets/ja/_images/uwb_ranging_and_aoa_demo_app_main.png" style="width: 98%;"></a>
</div></blockquote>
</li>
<li><p><span class="red-text">Save and start</span> を押してデモを開始する。次の <span class="red-text">Real Time Location</span> ウィンドウには、選択された Initiator と Responder 間の距離と角度の座標マップが表示される。</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/uwb_ranging_and_aoa_demo_app_location.png"><img alt="../../../_images/uwb_ranging_and_aoa_demo_app_location.png" src="/docs-assets/ja/_images/uwb_ranging_and_aoa_demo_app_location.png" style="width: 98%;"></a>
</div></blockquote>
</li>
<li><p>レスポンダのデバイスは、バッテリで駆動している場合は PC から取り外すことができる。これにより、評価のためにレスポンダを自由に動かすことができます。再びセッションを開始するには、<a class="reference internal" href="/docs/ja/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C Data Port 1</span></a> を使用してデバイスを PC に再接続する必要があります。</p></li>
</ol>
<blockquote>
<div><img alt="../../../_images/leaps-connect-usb-port1.gif" class="align-center" src="/docs-assets/ja/_images/leaps-connect-usb-port1.gif">
</div></blockquote>
<ol class="arabic simple" start="8">
<li><p>UWB 測距 &amp; AoA デモアプリには、評価に役立つ以下のような幅広いオプションが用意されています。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>距離、角度、X-Y 位置を表示するリアルタイムロケーション。</p></li>
<li><p>距離と角度の値をリアルタイムで表示するTrend Over Time。</p></li>
<li><p>イニシエータから選択したレスポンダまでの方向を表示するLocate My Device。</p></li>
<li><p>ジオフェンシング</p></li>
<li><p>フロアプラン</p></li>
<li><p>グリッド</p></li>
<li><p>ログ記録</p></li>
</ul>
</div></blockquote>
<p>詳細は <a class="reference internal" href="/docs/ja/udk/udk-start/partner-application-aoa-app#anchor-ranging-aoa"><span class="std std-ref">UWB レンジングおよび AoA デモ アプリ</span></a> を参照してください。</p>
</div>
<input id="sd-tab-item-1" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-1">
詳細</label><div class="sd-tab-content docutils">
<p><strong>高度なセットアップ</strong></p>
<p>高度なセットアップの準備をしてください。ターミナルの能力を活用して、プロのようにデバイスを設定できるようにお手伝いします。以下の手順に従うだけで準備は完了です。</p>
<ol class="arabic simple">
<li><p>USB-C データ ケーブルを使用して、デバイスの <a class="reference internal" href="/docs/ja/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C データ ポート 1</span></a> または <a class="reference internal" href="/docs/ja/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C データ ポート 2</span></a> を PC に接続します。</p></li>
</ol>
<blockquote>
<div><img alt="../../../_images/leaps-connect-usb-port1.gif" class="align-center" src="/docs-assets/ja/_images/leaps-connect-usb-port1.gif">
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>Putty、Teraterm、Minicom などの希望のターミナル アプリケーション、またはお気に入りのターミナル アプリケーションを使用してシリアル ポートに接続します。ボーレートを <span class="red-text">115200</span> に設定する必要があります。</p></li>
</ol>
<blockquote>
<div><p>たとえば、Ubuntu (Linux) で Minicom を使用します。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">minicom</span> <span class="o">-</span><span class="n">b</span> <span class="mi">115200</span> <span class="o">-</span><span class="n">D</span> <span class="o">/</span><span class="n">dev</span><span class="o">/</span><span class="n">ttyACM0</span>
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>シェル コンソールで <span class="red-text">ダブル Enter</span> を押して、コマンド ライン制御システムにアクセスします。</p></li>
</ol>
<blockquote>
<div><p>たとえば、Ubuntu (Linux) では、<span class="red-text">/dev/ttyACM0</span> を開き、<span class="red-text">double Enter</span> を押します。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>minicom -b 115200 -D /dev/ttyACM0

  Welcome to minicom 2.7.1

  OPTIONS: I18n
  Compiled on Dec 23 2019, 02:06:26.
  Port /dev/ttyACM0, 16:02:57

  Press CTRL-A Z for help on special keys



  Low Energy Accurate Positioning System

  FOR DEMO PURPOSE ONLY, NOT FOR SALE.

  Copyright :  2016-2023 LEAPS
  License   :  Please visit https://www.leapslabs.com/leaps-rtls-license
  Compiled  :  Jan  6 2024 09:38:07 (v0.15.0-ab84fb)

  Help      :  ? or help

  leaps&gt;
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/fira#fuci"><span class="std std-ref">fuci</span></a> コマンドを使用して、FiRa UCIモードを更新します。</p></li>
</ol>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span>Low Energy Accurate Positioning System

FOR DEMO PURPOSE ONLY, NOT FOR SALE.

Copyright :  2016-2023 LEAPS
License   :  Please visit https://www.leapslabs.com/leaps-rtls-license
Compiled  :  Jan  6 2024 09:38:07 (v0.15.0-ab84fb)

Help      :  ? or help

leaps&gt;
leaps&gt; fuci
</pre></div>
</div>
<p>デバイスの起動時に <span class="green-text">GREEN LED</span> が点滅することを目視で確認してください。</p>
<img alt="../../../_images/fuci-command.gif" class="align-center" src="/docs-assets/ja/_images/fuci-command.gif">
</div></blockquote>
<ol class="arabic simple" start="5">
<li><p>これで <span class="red-text">Qorvo UCI mode</span> が正常に設定されました。 <a class="reference internal" href="#anchor-lc"><span class="std std-ref">Quick Start</span></a> の次の手順を参照してください。</p></li>
</ol>
</div>
<input id="sd-tab-item-2" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-2">
トラブルシューティング</label><div class="sd-tab-content docutils">
<ol class="arabic">
<li><p>Bluetooth Low Energy (BLE) と LED が両方ともオフの場合、ユーザーはボードが機能していないと誤って認識する可能性があります。このシナリオでは、ユーザーの唯一の手段は、工場出荷時設定へのリセット (<a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/sys#frst"><span class="std std-ref">frst</span></a>) コマンドを開始することです。</p></li>
<li><p>インストールプロセスに関連するいくつかの問題を修正するためのヒントをいくつか紹介します。</p>
<ul class="simple">
<li><p>バージョンを確認してください。最新の正式バージョンを使用することをお勧めします。</p></li>
<li><p>デバイスの現在の状態がわからない場合は、<a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> のデモ セレクターの <span class="red-text">デバイスをデフォルトにリセット</span> 機能を使用します。次のGIF画像を参照してください。</p></li>
</ul>
<img alt="../../../_images/reset-devices-to-defaul-x2.gif" class="align-center" src="/docs-assets/ja/_images/reset-devices-to-defaul-x2.gif">
</li>
</ol>
</div>
</div>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<ul class="simple">
<li><p>弊社製品に関するご意見やご質問については、<a class="reference external" href="https://forum.leapslabs.com">LEAPS フォーラム</a> にアクセスすることをお勧めします。</p></li>
<li><p>既知の制限と問題リストの詳細については、セクション <a class="reference internal" href="/docs/ja/udk/release#udk-releases"><span class="std std-ref">リリース</span></a> を参照してください。</p></li>
</ul>
</div>
</div>


           </div>
