---
title: "と iPhone の周辺での対話デモ"
lang: ja
slug: "udk/udk-start/nearby-interaction-demo-with-an-iphone"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/ja/udk/udk-start/nearby-interaction-demo-with-an-iphone/"
order: 107
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="nearby-interaction-demo-with-an-iphone">
<span id="anchor-ni"></span><h1>と iPhone の周辺での対話デモ</h1>
<a class="reference internal image-reference" href="../../../_images/nearby_interaction_demo_with_an_iphone.png"><img alt="../../../_images/nearby_interaction_demo_with_an_iphone.png" class="align-right" src="/docs-assets/ja/_images/nearby_interaction_demo_with_an_iphone.png" style="width: 252.00000000000003px; height: 211.26000000000002px;"></a>
<p><strong>セットアップの準備</strong></p>
<ol class="arabic simple">
<li><p>iPhone (モデル: iPhone 11、12、13) にインストールされている <a class="reference internal" href="/docs/ja/udk/udk-start/partner-application-nearby-interaction#anchor-ni-app"><span class="std std-ref">Qorvo の近くのインタラクション</span></a> (フォアグラウンド モード) または <a class="reference internal" href="/docs/ja/udk/udk-start/partner-application-nearby-interaction-background#anchor-nib-app"><span class="std std-ref">Qorvo NI の背景</span></a> アプリケーション。</p></li>
<li><p>少なくとも 1 つの LC14 (白) デバイス。</p></li>
<li><p><em>オプション:</em> <a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> <em>アプリケーションがインストールされました。</em></p></li>
<li><p><em>オプション: デバイスのバッテリー。</em></p></li>
</ol>
<p><strong>セットアップ時間:</strong> 5 分未満</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
クイックスタート</label><div class="sd-tab-content docutils">
<p><strong>概要</strong></p>
<p>この設定は、スマートフォンとの <span class="red-text">Nearby Interaction</span> と <span class="red-text">FiRa の互換性</span> を示しています。距離と角度の測定により、スマートフォンのアプリでアクセサリーの方向が表示されます。</p>
<p><strong>代表的なアプリケーション</strong>: 持ち物を探す、フォローミー、スマートリモコン、アクセス制御。</p>
<p><strong>セットアップ手順</strong></p>
<ol class="arabic simple">
<li><p>次のアプリケーションを iPhone にダウンロードしてインストールします。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p><a class="reference internal" href="/docs/ja/udk/udk-start/partner-application-nearby-interaction#anchor-ni-app"><span class="std std-ref">Qorvo の近くのインタラクション</span></a> アプリケーション（フォアグラウンドモード）。</p></li>
<li><p><a class="reference internal" href="/docs/ja/udk/udk-start/partner-application-nearby-interaction-background#anchor-nib-app"><span class="std std-ref">Qorvo NI の背景</span></a> アプリケーション (バックグラウンド モード)。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>1 つ以上の LC14 (白) デバイスの電源を入れます。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>LC14 は、QNI (Qorvo Nearby Interaction) デモのアクセサリとして機能します。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>次のオプションのいずれかを使用して、デバイスを <span class="red-text">QNI モード</span> に設定します。</p></li>
</ol>
<blockquote>
<div><ol class="upperalpha simple">
<li><p>ボタンを使用してデバイスを設定します。</p></li>
</ol>
<blockquote>
<div><p>3.1。ビープ音が鳴り、<span class="blue-text">青い LED</span> が点滅するまで、<a class="reference internal" href="/docs/ja/udk/udk-start/device-hw-interfaces#uihwinterfaces"><span class="std std-ref">ボタン B</span></a> を押し続けます。</p>
<p>3.2。 <span class="red-text">RED</span> または <span class="green-text">GREEN</span> の色が表示された場合は、手順 a を繰り返してください。</p>
<p>3.3。ビープ音の後にデバイスが <span class="blue-text">青い LED</span> で点滅すると、デバイスは <span class="red-text">QNI モード</span> に設定されています。</p>
<img alt="../../../_images/leaps-config-to-qorvo-ni-mode.gif" class="align-center" src="/docs-assets/ja/_images/leaps-config-to-qorvo-ni-mode.gif">
</div></blockquote>
<ol class="upperalpha simple" start="2">
<li><p><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a>: のデモ セレクターを使用して設定します。</p></li>
</ol>
<blockquote>
<div><p>3.1。 <a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> を開き、メイン ページから <span class="red-text">Demo Selector</span> を選択します。</p>
<p>3.2。 <span class="red-text">iPhone との近くのインタラクション</span> を選択します。</p>
<p>3.3。 Bluetooth 経由で検出されたデバイスのリストがリストに表示されます。必要に応じて、下にスワイプしてリストを更新します。</p>
<p>3.4。 QNI デモに使用するデバイスを選択します。上部の <span class="red-text">必要なデバイス</span> は、デモに必要なデバイスの数を示します。</p>
<p>3.5。 <span class="red-text">SAVE</span> を押して、デバイスを <span class="red-text">QNI モード</span> に設定します。</p>
<p>3.6。デバイスが起動すると、<span class="blue-text">青い LED</span> が点滅することを目視で確認してください。</p>
<img alt="../../../_images/qorvo-nearby-interaction.gif" class="align-center" src="/docs-assets/ja/_images/qorvo-nearby-interaction.gif">
</div></blockquote>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>iPhone で <span class="red-text">Qorvo Nearby Interaction</span> または <span class="red-text">Qorvo NI Background</span> アプリケーションを開きます。</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>Qorvo Nearby Interaction アプリケーションを開いた直後に、QNI BLE サービスを使用して近くのアクセサリをスキャンします。</p></li>
<li><p>QNI アクセサリが検出され、リストに追加されたとき。 Nearby Interaction を開始したいアクセサリを <span class="red-text">選択して接続</span> してください。複数の接続がサポートされています。</p>
<img alt="../../../_images/nearby-interaction-demo.gif" class="align-center" src="/docs-assets/ja/_images/nearby-interaction-demo.gif">
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="5">
<li><p><span class="red-text">Nearby Interaction Background モード</span> では、アクセサリを iPhone デバイスとペアリングする必要があります。</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>初めてデバイスに接続するとき、およびアプリケーションが初めて NI セッションを開始するときに、Nearby Interaction を使用するためのユーザーの承認が要求されます。</p></li>
<li><p>アクセサリが iPhone とペアリングされると、その後のアクセサリと iPhone 間の対話中に、それ以上のペアリングやアクセス許可は必要ありません。</p>
<a class="reference internal image-reference" href="../../../_images/qorvo_ni_pair_request_demo.png"><img alt="../../../_images/qorvo_ni_pair_request_demo.png" src="/docs-assets/ja/_images/qorvo_ni_pair_request_demo.png" style="width: 49%;"></a>
<a class="reference internal image-reference" href="../../../_images/qorvo_ni_background_pair_request_demo.jpg"><img alt="../../../_images/qorvo_ni_background_pair_request_demo.jpg" src="/docs-assets/ja/_images/qorvo_ni_background_pair_request_demo.jpg" style="width: 49%;"></a>
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p>iPhone はアクセサリを使用して測距を開始し、測距ラウンドごとに iPhone とアクセサリ間の測定距離を表示します。</p></li>
</ol>
<blockquote>
<div><ul>
<li><p><span class="red-text">NI バックグラウンド モード</span> を使用する <span class="red-text">Qorvo NI バックグラウンド</span> アプリケーションの場合、更新レートは低くなり、NI フォアグラウンド モードと比較して 1/3 になります。 iPhone のディスプレイがオフになっている場合でも、測距はバックグラウンドで行われます。</p></li>
<li><p><span class="red-text">NI フォアグラウンド モード</span> を使用する <span class="red-text">Qorvo Nearby Interaction</span> アプリケーションの場合、iPhone からアクセサリへの角度と方向も表示されます。測定値は iPhone の視点から取得されます。デバイスの向きを変更すると、アプリケーションは iPhone のカメラとディスプレイを使用してアクセサリの位置を示す拡張ビューも提供できます。</p>
<a class="reference internal image-reference" href="../../../_images/qorvo_nearby_interaction_application_example.png"><img alt="../../../_images/qorvo_nearby_interaction_application_example.png" src="/docs-assets/ja/_images/qorvo_nearby_interaction_application_example.png" style="width: 49%;"></a>
<a class="reference internal image-reference" href="../../../_images/qorvo_ni_backgroud_example.jpg"><img alt="../../../_images/qorvo_ni_backgroud_example.jpg" src="/docs-assets/ja/_images/qorvo_ni_backgroud_example.jpg" style="width: 49%;"></a>
</li>
</ul>
</div></blockquote>
<p>詳細については、<a class="reference internal" href="/docs/ja/udk/udk-start/partner-application-nearby-interaction#anchor-ni-app"><span class="std std-ref">Qorvo の近くのインタラクション</span></a> または <a class="reference internal" href="/docs/ja/udk/udk-start/partner-application-nearby-interaction-background#anchor-nib-app"><span class="std std-ref">Qorvo NI の背景</span></a> アプリケーションを参照してください。</p>
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
<div><img alt="../../../_images/leaps-connect-usb-port2.gif" class="align-center" src="/docs-assets/ja/_images/leaps-connect-usb-port2.gif">
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
<li><p>コマンド <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/fira#fniq"><span class="std std-ref">fniq</span></a> を使用して、Nearby Interaction モードを更新します。</p></li>
</ol>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span>Low Energy Accurate Positioning System

FOR DEMO PURPOSE ONLY, NOT FOR SALE.

Copyright :  2016-2023 LEAPS
License   :  Please visit https://www.leapslabs.com/leaps-rtls-license
Compiled  :  Jan  6 2024 09:38:07 (v0.15.0-ab84fb)

Help      :  ? or help

leaps&gt;
leaps&gt; fniq
</pre></div>
</div>
<p>このとき、デバイスの起動時に <span class="blue-text">青い LED</span> が点滅することを目視で確認してください。</p>
<img alt="../../../_images/fniq-command.gif" class="align-center" src="/docs-assets/ja/_images/fniq-command.gif">
</div></blockquote>
<ol class="arabic simple" start="5">
<li><p><span class="red-text">QNI モード</span> が正常に設定されました。<a class="reference internal" href="#anchor-ni"><span class="std std-ref">クイック スタート</span></a> の次の手順を参照してください。</p></li>
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
