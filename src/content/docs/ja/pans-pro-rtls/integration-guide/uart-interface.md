---
title: "UART インターフェース"
lang: ja
slug: "pans-pro-rtls/integration-guide/uart-interface"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/uart-interface/"
order: 95
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="uart-interface">
<span id="pans-uart-interface"></span><h1>UART インターフェース</h1>
<p>ユーザーは、外部ホスト デバイスを使用して、ボー レート 115200 で UART インターフェースを介して DWM モジュールに接続できます。次の図は、DWM1001 UART インターフェースのワークフローを示しています。UART 汎用モード通信では、ホスト デバイスがイニシエーターとして機能し、DWM モジュールがレスポンダーとして機能します。DWM1001 UART には、UART 汎用モードと UART シェル モードの 2 つのモードがあります。DWM1001 UART のデフォルト モードは汎用モードです。ただし、2 つのモードは移行可能です。</p>
<p>ジェネリック モードからシェル モードへ: ”Enter” を 2 回押すか、1 秒以内に 2 バイト [0x0D, 0x0D] を入力します。</p>
<p><em>低電力モードのウェイクアップ メカニズム</em> で紹介されているように、モジュールが低電力モードで “スリープ“ 状態にある場合、2 回の “Enter“ の前に追加のバイトが必要になります。たとえば、“Enter“ を 3 回押すとモジュールが起動し、シェル モードに移行します。シェル モードから汎用モードへ: ユーザーは “quit“ コマンドを入力する必要があります。</p>
<blockquote>
<div><div class="figure align-default" id="id1">
<a class="reference internal image-reference" href="../../../_images/image91.png"><img alt="../../../_images/image91.png" src="/docs-assets/ja/_images/image91.png" style="width: 5.70833in; height: 2.29167in;"></a>
<p class="caption"><span class="caption-text">UART ワークフロー</span></p>
</div>
</div></blockquote>
<hr class="docutils">
<div class="section" id="uart-tlv-mode">
<h2>UART TLV モード</h2>
<p>UART TLV モードは TLV 形式のデータを使用します。このモードでは、ホスト デバイスと DWM モジュールは TLV 要求/応答を使用して通信します。完全な TLV リクエスト通信フローには、次の手順が含まれます。</p>
<ol class="arabic simple">
<li><p>ホストデバイスは TLV リクエストを送信します。</p></li>
<li><p>DWM1001 は TLV データで応答します。</p></li>
</ol>
<p>データを受信すると、UART は次のデータの遅延タイマーを開始します。遅延期間、具体的には 25 クロック サイクル (25/32768 秒 ≈ 763 μs) 内に新しいデータが到着すると、UART は遅延タイマーを開始し、新しいデータを待機します。遅延期間内に新しいデータが到着しない場合、遅延タイマーは期限切れになります。次に、UART は受信したデータを汎用 API スレッドに送信し、応答データまたはエラー メッセージが返されるのを待機します。</p>
<p>DWM1001 UART TLV モード スレッドは、<code class="docutils literal notranslate"><span class="pre">UART:</span> <span class="pre">アイドル</span></code>、<code class="docutils literal notranslate"><span class="pre">UART:</span> <span class="pre">アイドル</span></code> の 3 つの状態間をシリアルで転送します。 <code class="docutils literal notranslate"><span class="pre">受信中</span></code> および <code class="docutils literal notranslate"><span class="pre">UART:</span> <span class="pre">終了</span></code>。各状態は特定のイベントで次の対応する状態に移行します。</p>
<ul class="simple">
<li><p>UART: Idle: は、初期化後および各 TLV 応答が成功した後の状態です。この状態では、UART は TLV リクエストまたは 2 回の <code class="docutils literal notranslate"><span class="pre">Enter</span></code> コマンドの開始として 1 バイトのみを期待します。</p>
<ul>
<li><p>イベントを待機しています: TLV リクエストを受信して​​います。</p></li>
<li><p>イベントに対するアクション:</p>
<ul>
<li><p>遅延タイマーを開始します。</p></li>
<li><p>UART に転送: 受信中。</p></li>
</ul>
</li>
</ul>
</li>
<li><p>UART: Receiving: は、受信リクエストの終了を待っている状態です。この状態でデータを受信すると、UART は遅延タイマーをリフレッシュします。ホストデバイスがバイトの送信を完了すると、遅延タイマーが期限切れになります。</p>
<ul>
<li><p>イベントを待機中: 遅延期間がタイムアウトしました。</p></li>
<li><p>イベントに対するアクション - 受信したリクエストがダブル <code class="docutils literal notranslate"><span class="pre">Enter</span></code> の場合:</p>
<ul>
<li><p>UART シェル モードに移行します。</p></li>
</ul>
</li>
<li><p>イベントに対するアクション - 受信したリクエストがダブル <code class="docutils literal notranslate"><span class="pre">Enter</span></code> でない場合:</p>
<ul>
<li><p>受信したリクエストを汎用 API スレッドに送信します。</p></li>
<li><p>UART への転送: 完了しました。</p></li>
</ul>
</li>
</ul>
</li>
<li><p>UART: Finished: 汎用 API スレッドが受信リクエストを解析し、応答データまたはエラー メッセージを UART スレッドに送り返すのを待機している状態です。</p>
<ul>
<li><p>イベントを待機しています: 汎用 API スレッドによって呼び出される call_back() 関数。</p></li>
<li><p>イベントに対するアクション:</p>
<ul>
<li><p>応答データまたはエラー メッセージをホスト デバイスに送信します。</p></li>
<li><p>UART に転送: アイドル。</p></li>
</ul>
</li>
</ul>
</li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="uart-tlv-mode-communication">
<h2>UART TLV モード通信</h2>
<p>TLV モードでの UART 通信を次の図に示します。</p>
<ol class="arabic">
<li><p>ホストデバイスは TLV 形式でリクエストを送信します。</p></li>
<li><p>DWM モジュールは TLV 形式のメッセージで応答します。</p>
<div class="figure align-default" id="id2">
<a class="reference internal image-reference" href="../../../_images/image10.png"><img alt="../../../_images/image10.png" src="/docs-assets/ja/_images/image10.png" style="width: 4.875in; height: 3.03194in;"></a>
<p class="caption"><span class="caption-text">UART TLV通信</span></p>
</div>
</li>
</ol>
</div>
<hr class="docutils">
<div class="section" id="uart-tlv-mode-communication-example">
<h2>UART TLVモード通信の例</h2>
<p>以下の図は、ホスト デバイスが <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/api-commands/dwm-gpio-cfg-output#dwm-gpio-cfg-output"><span class="std std-ref">dwm_gpio_cfg_output</span></a> コマンドを送信してバイト配列のピン 13 レベルを HIGH ([0x28, 0x02, 0x0D, 0x01]) に設定し、TLV モードで UART API を使用して DWM モジュールから応答を受信する例を示しています。通信フローの手順は次のとおりです。</p>
<ol class="arabic simple">
<li><p>ホスト デバイスは、<a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/api-commands/dwm-gpio-cfg-output#dwm-gpio-cfg-output"><span class="std std-ref">dwm_gpio_cfg_output</span></a> コマンドを TLV 形式で送信します: Type = 0x28、Length = 0x02、Value = 0x0D 0x01。</p></li>
<li><p>DWM モジュールTLV 形式で応答します: タイプ = 0x40、長さ = 0x01、値 = 0x00、</p></li>
</ol>
<p>タイプ=0x40はリターンメッセージであることを示し、長さ=0x01はデータとして続く1バイトがあることを示し、値=0x00はTLV Requestが正しく解析されたことを示す。</p>
<div class="figure align-default" id="id3">
<a class="reference internal image-reference" href="../../../_images/image11.png"><img alt="../../../_images/image11.png" src="/docs-assets/ja/_images/image11.png" style="width: 3.90694in; height: 2.71806in;"></a>
<p class="caption"><span class="caption-text">UART TLV 通信の例</span></p>
</div>
</div>
<hr class="docutils">
<div class="section" id="uart-shell-mode-communication">
<h2>UART シェルモード通信</h2>
<p>UART シェル モードではプロンプトが表示され、シェル コマンドが使用されます。UART シェル モードは、人間が判読できる形式で API にアクセスできるようにするためのものです。したがって、すべてのシェル コマンドは文字列で、その後に文字リターン (つまり “Enter“) が続きます。ユーザーはキーボードから直接文字列を入力し、“Enter“ を押してシェル コマンドを送信できます。DWM1001 UART は、 “quit“ コマンドを除き、各シェル コマンドの後もシェル モードのままです。</p>
<p>以下の図に示すように、完全なシェル コマンド通信フローには次の手順が含まれます:</p>
<ol class="arabic simple">
<li><p>ホスト デバイスは、シェル コマンド + “Enter“ を DWM1001 に送信します。</p></li>
<li><p>応答するメッセージがある場合、DWM1001 はそのメッセージをホスト デバイスに送信します。</p></li>
<li><p>応答するものが何もない場合、DWM1001 は何も送信せず、沈黙を保ちます。</p></li>
</ol>
<div class="figure align-default" id="id4">
<a class="reference internal image-reference" href="../../../_images/image12.png"><img alt="../../../_images/image12.png" src="/docs-assets/ja/_images/image12.png" style="width: 3.88472in; height: 2.32222in;"></a>
<p class="caption"><span class="caption-text">UART シェルモード通信</span></p>
</div>
</div>
<hr class="docutils">
<div class="section" id="uart-shell-mode-communication-example">
<h2>UART シェルモード通信の例</h2>
<p>以下の図は、ホスト デバイスが UART シェルを使用して <code class="docutils literal notranslate"><span class="pre">GPIO</span> <span class="pre">set</span></code> コマンドを送信し、ピン 13 レベルを HIGH に設定する例を示しています (バイト配列の <code class="docutils literal notranslate"><span class="pre">gs</span> <span class="pre">13</span></code> の後に <code class="docutils literal notranslate"><span class="pre">Enter</span></code> キーが続きます。<em>gs</em> で詳しく説明します)。通信フローの手順は次のとおりです。</p>
<ol class="arabic simple">
<li><p>ホスト デバイスはシェル モードで <code class="docutils literal notranslate"><span class="pre">GPIO</span> <span class="pre">set</span></code> コマンドを送信します: <code class="docutils literal notranslate"><span class="pre">gs</span> <span class="pre">13</span></code> + <code class="docutils literal notranslate"><span class="pre">Enter</span></code>。</p></li>
<li><p>DWM1001 は文字列 <code class="docutils literal notranslate"><span class="pre">gpio13:</span> <span class="pre">1</span></code> でホストに応答します。</p></li>
</ol>
<div class="figure align-default" id="id5">
<a class="reference internal image-reference" href="../../../_images/image13.png"><img alt="../../../_images/image13.png" src="/docs-assets/ja/_images/image13.png" style="width: 3.5625in; height: 2.34444in;"></a>
<p class="caption"><span class="caption-text">UART シェルモード通信の例</span></p>
</div>
</div>
<hr class="docutils">
<div class="section" id="low-power-mode-wake-up-mechanism">
<h2>低電力モードのウェイクアップメカニズム</h2>
<p>PANS ライブラリで提供されているように、DWM モジュールは低電力モードで動作できます。低電力モードでは、ホストデバイスが API と通信しない場合、モジュールは API 関連のスレッドを <code class="docutils literal notranslate"><span class="pre">スリープ</span></code> 状態にします。この場合、実際の通信を開始する前に、ホスト デバイスは外部インターフェイスを通じてモジュールを起動する必要があります。</p>
<p>UART インターフェイスの場合、ホスト デバイスはモジュールをウェイクアップするために最初に 1 バイトを送信する必要があります。</p>
<p>API 送信が完了したら、<a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/api-commands/dwm-sleep#dwm-sleep"><span class="std std-ref">dwm_sleep</span></a> とシェル コマンド <em>quit</em> で紹介されているように、ホスト デバイスは電力を節約するためにモジュールを <code class="docutils literal notranslate"><span class="pre">スリープ</span></code> 状態に戻す必要があります。</p>
</div>
<hr class="docutils">
<div class="section" id="uart-wakeup">
<h2>UART ウェイクアップ</h2>
<p>DWM が (低電力モードで) スリープしている場合は、SPI/UART がコマンドの受け入れを開始する前にウェイクアップ手順を実行する必要があります。スリープから復帰するには、少なくとも 1 バイトを UART インターフェイスで送信する必要があります (低電力モードのみ)。</p>
</div>
</div>


           </div>
