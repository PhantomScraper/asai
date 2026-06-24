---
title: "SPI インターフェイス"
lang: ja
slug: "pans-pro-rtls/integration-guide/spi-interface"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/spi-interface/"
order: 96
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="spi-interface">
<span id="pans-spi-interface"></span><h1>SPI インターフェイス</h1>
<p>DWM1001 SPI インターフェイスは TLV 形式のデータを使用します。ユーザーは、SPI マスター モードの外部ホスト デバイスを使用して、スレーブ モードで動作する DWM モジュール SPI インターフェイスに接続できます。最大 SPI クロック周波数は 8 MHz です (これは MCU でサポートされている最大値です)。DWM1001 SPI スキームでは、ホスト デバイスは TLV 要求を通じて DWM1001 と通信します。完全な TLV リクエスト通信フローには、次の手順が含まれます。</p>
<ol class="arabic simple">
<li><p>ホストデバイスは TLV リクエストを送信します。</p></li>
<li><p>DWM1001 は応答を準備します。</p></li>
<li><p>ホストデバイスは、SIZE (各応答の長さ) と NUM (転送数) を読み取ります。</p></li>
<li><p>ホストデバイスはデータ応答を読み取ります。</p></li>
</ol>
<p>SPI は全二重通信を使用するため、ホスト デバイス (SPI マスターとして) が x バイトを書き込むと、x バイトを DWM モジュール (スレーブとして) に送信し、同時に x バイトのダミーを受信します。読み取りと同様に、ホスト デバイスは x バイトのダミーを送信し、応答として x バイトのデータを受信します。 DWM1001 SPI スキームでは、ダミー バイトは値 0xFF のオクテットです。</p>
<blockquote>
<div><div class="figure align-default" id="id1">
<a class="reference internal image-reference" href="../../../_images/image41.png"><img alt="../../../_images/image41.png" src="/docs-assets/ja/_images/image41.png" style="width: 5.66667in; height: 2.84444in;"></a>
<p class="caption"><span class="caption-text">SPI ワークフロー</span></p>
</div>
</div></blockquote>
<p>上の図に示すように、DWM1001 SPI スレッドは 4 つの状態間をシリアルに転送します。</p>
<p>各状態は、特定のイベントが発生すると、次の対応する状態に移行します。</p>
<ul>
<li><p>SPI: アイドル: 初期化後、およびデータ送信/応答が成功した後の状態。この状態では、受信したデータはすべて TLV リクエストであると見なされます。したがって、データを受信すると、ファームウェアの SPI スレッドは受信したデータを汎用 API に渡します。汎用 API は TLV リクエストを解析し、戻りデータを準備します。</p>
<blockquote>
<div><ul class="simple">
<li><p>イベントを待機しています: TLV リクエストを受信して​​います。</p></li>
<li><p>イベントに対するアクション – Type == 0xFF の場合:</p></li>
</ul>
</div></blockquote>
</li>
</ul>
<ul>
<li><p>SPI: call_back を待機: DWM1001 SPI は、汎用 API が TLV 要求を解析し、応答を準備するのを待ちます。ホスト側からのデータはすべて無視され、次のように返されます。</p>
<blockquote>
<div><ul>
<li><p>イベントを待機しています: call_back() 関数が汎用 API によって呼び出されます。</p></li>
<li><p>イベントに対するアクション:</p>
<blockquote>
<div><ul class="simple">
<li><p>データレディ GPIO ピンを HIGH に切り替えます – 詳細については、<em>SPI スキーム: データレディ GPIO ピンを使用した TLV 通信</em> を参照してください。</p></li>
<li><p>“SPI: READ SIZE/NUM を待機“ に転送します。</p></li>
</ul>
</div></blockquote>
</li>
</ul>
</div></blockquote>
</li>
<li><p>SPI: 読み取り SIZE/NUM を待機: DWM1001 SPI は応答として SIZE バイトを準備しており、転送は NUM 回行われます。 SIZE と NUM は合計 2 バイトの非ゼロ データ、つまり SIZE/NUM です。 これらは応答するデータまたはエラー メッセージの合計数 (つまり SIZE*NUM バイト) を示します。 DWM1001 SPI はスレーブとして、ホスト デバイスが SIZE/NUM バイトを読み取るのを待機しています。</p>
<blockquote>
<div><ul>
<li><p>イベントを待機中: ホストデバイスは 2 バイトを読み取ります。</p></li>
<li><p>イベントに対するアクション:</p>
<blockquote>
<div><ul class="simple">
<li><p>SIZE/NUM バイトを応答します。</p></li>
<li><p>”SPI: READ DATA/ERR を待機” に転送します。</p></li>
</ul>
</div></blockquote>
</li>
</ul>
</div></blockquote>
</li>
</ul>
<ul>
<li><p>SPI: 読み取りデータ/エラーの待機: DWM1001 SPI は、TLV 要求への応答として NUM 転送ごとに SIZE バイトのデータまたはエラー メッセージを準備し、ホスト デバイスがそれを読み取るのを待機しています。</p>
<blockquote>
<div><ul class="simple">
<li><p>イベントを待機しています: ホストデバイスは NUM 回の転送を実行します。各転送は SIZE バイトである必要があります。そうしないと、データが失われる可能性があります。</p></li>
<li><p>イベントに対するアクション:</p>
<ul>
<li><p>DATA/ERR で応答します。</p></li>
<li><p>データレディ GPIO ピンを LOW に切り替えます – 詳細については、 <em>SPI スキーム: データレディ GPIO ピンを使用した TLV 通信</em> を参照してください。 “SPI:アイドル“ に移行します。</p></li>
</ul>
</li>
</ul>
</div></blockquote>
</li>
</ul>
<p>DWM1001 では、 “SPI: アイドル“ から始まり、上記の 4 つの状態をすべて通過して “SPI: アイドル“ に戻ると、完全な TLV 要求通信フローが示されます。ユーザーは、通信フローの終了までに応答データまたはエラー メッセージを受信して​​いるはずです。</p>
<p>以下のサブセクションでは、いくつかの異なる使用法と例を示します。</p>
<hr class="docutils">
<div class="section" id="spi-tlv-communication-using-polling">
<h2>ポーリングを使用した SPI TLV 通信</h2>
<p>以下の図は、ホスト デバイスが DWM に情報を書き込む、または DWM から情報を読み取る通常の通信フローを示しています。モジュール:</p>
<ol class="arabic simple">
<li><p>ホスト デバイスはリクエストを TLV 形式で送信します。</p></li>
<li><p>ホスト デバイスは、実行される転送の数と各転送で読み取る準備ができているバイト数を示す SIZE/NUM バイトを読み取ります。</p></li>
</ol>
<ol class="arabic simple" start="3">
<li><p>ホスト デバイスは、TLV 形式で SIZE バイトのデータ応答を読み取ります。</p></li>
</ol>
<div class="figure align-default" id="id2">
<a class="reference internal image-reference" href="../../../_images/image51.png"><img alt="../../../_images/image51.png" src="/docs-assets/ja/_images/image51.png" style="width: 5.70833in; height: 3.29167in;"></a>
<p class="caption"><span class="caption-text">ポーリングを使用した SPI TLV 通信</span></p>
</div>
<div class="line-block">
<div class="line">下の図は、ホスト デバイスが <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/api-commands/dwm-gpio-cfg-output#dwm-gpio-cfg-output"><span class="std std-ref">dwm_gpio_cfg_output</span></a> TLV 要求を書き込み、ピン 13 のレベルを HIGH ([0x28, 0x02, 0x0D, 0x01]) に設定し、DWM モジュールから応答を読み取る例を示しています。</div>
<div class="line">送信と応答の通信フローには次のものが含まれます。</div>
</div>
<blockquote>
<div><ol class="arabic simple">
<li><p>ホスト デバイスは、<a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/api-commands/dwm-gpio-cfg-output#dwm-gpio-cfg-output"><span class="std std-ref">dwm_gpio_cfg_output</span></a> コマンドを書き込み、TLV 形式でピン 13 レベルを HIGH に設定します。合計 4 バイト: タイプ = 0x28、長さ = 0x02、値 = 0x0D 0x01。</p></li>
</ol>
</div></blockquote>
</div>
<hr class="docutils">
<div class="section" id="spi-tlv-communication-using-data-ready-gpio-pin">
<h2>データレディ GPIO ピンを使用した SPI TLV 通信</h2>
<p>ユーザーは、マスターが複数回ポーリングして応答ステータスをチェックする代わりに、DWM1001 から割り込みデータレディ GPIO ピン (GPIO P0.26) を設定して、データの準備ができたことを示すことができます。データレディ機能が設定されている場合、読み取られるデータがない場合、データレディ GPIO ピンは LOW レベルに設定されます。応答 SIZE/NUM とデータの読み取り準備が整うと、状態 “SPI: 読み取り SIZE/NUM を待機“ および “SPI: 読み取り DATA/ERR を待機“ の間、データ準備 GPIO ピンは HIGH レベルに設定されます。したがって、ユーザーはデータ準備 GPIO ピンを割り込みまたはステータス ピンとして使用できます。</p>
<p>SPI スキームのデータレディ GPIO ピンをセットアップするには、ユーザーは dwm_int_cfg SPI スキームを介した TLV リクエストを使用する必要があります: 通常の TLV 通信</p>
<p>この方式の通信フローを次の図に示します。</p>
<ol class="arabic">
<li><p>SPI 割り込みを設定します。</p></li>
<li><p>ホスト デバイスはリクエストを TLV 形式で書き込みます。</p></li>
<li><p>ホスト デバイスは、DWM1001 のデータレディ GPIO ピンが HIGH になるまで待機します。</p></li>
<li><p>ホストデバイスは SIZE/NUM バイトを読み取ります。</p></li>
<li><p>ホスト デバイスは、NUM 回の各転送で SIZE バイトのデータ応答を TLV 形式で読み取ります。</p>
<div class="figure align-default" id="id3">
<a class="reference internal image-reference" href="../../../_images/image71.png"><img alt="../../../_images/image71.png" src="/docs-assets/ja/_images/image71.png" style="width: 5.70833in; height: 4.34444in;"></a>
<p class="caption"><span class="caption-text">データレディ GPIO ピンを使用した SPI TLV 通信</span></p>
</div>
</li>
</ol>
<p>手順からわかるように、このスキームは DWM1001 のデータレディ GPIO ピンを使用して、応答データの準備ができたことをホスト デバイスに示します。これにより、ホストデバイスの SIZE バイトの読み取りの負荷が軽減されます。</p>
</div>
<hr class="docutils">
<div class="section" id="spi-partial-transmission">
<h2>SPI 部分送信</h2>
<p>DWM モジュールからデータを読み取るときに、ホスト デバイスが 1 回の送信でデータの全バイトを読み取らなくても、読み取り操作は完了したとみなされます。残りの応答は破棄されます。たとえば、 “SPI: Wait for Read DATA/ERR“ 状態では、DWM モジュールは SIZE バイトの応答データを準備しており、ホスト デバイスが応答のすべての SIZE バイトを読み取ることを期待しています。ただし、ホスト デバイスがデータの一部のみを読み取る場合、DWM モジュールは残りのデータをドロップし、次の状態 “SPI: IDLE“ に移行します。</p>
</div>
<hr class="docutils">
<div class="section" id="spi-error-recovery-mechanism">
<h2>SPI エラーの回復メカニズム</h2>
<p>DWM1001 SPI には、type_nop と呼ばれる特殊なタイプ値 0xFF があります。type_nop の TLV データ メッセージは、操作がないことを意味します。 “SPI: IDLE“ 状態では、DWM1001 SPI がメッセージを受信し、タイプ バイトが 0xFF であることがわかった場合、TLV データ メッセージを汎用 API スレッドに送信することを含め、いかなる操作も実行しません。</p>
<p>type_nop はエラー回復用に設計されています。ホスト デバイスが DWM1001 SPI の状態が不明な場合は、SPI 応答と非部分送信メカニズムを利用し、1 回の送信で 3 つの 0xFF ダミー バイトを送信することで DWM1001 SPI を “SPI: IDLE“ 状態にリセットできます。 3 回の送信後、DWM1001 SPI からの応答データはすべて値 0xFF のダミー バイトになり、DWM1001 SPI が “SPI: IDLE“ 状態にあることを示します。</p>
</div>
<hr class="docutils">
<div class="section" id="low-power-mode-wake-up-mechanism">
<h2>低電力モードのウェイクアップメカニズム</h2>
<p>PANS ライブラリで提供されているように、DWM モジュールは低電力モードで動作できます。低電力モードでは、ホストデバイスが API と通信しない場合、モジュールは API 関連のスレッドを``スリープ``状態にします。この場合、実際の通信を開始する前に、ホスト デバイスは外部インターフェイスを通じてモジュールを起動する必要があります。</p>
<p>SPI インターフェイスの場合、チップ選択ピンをローレベルにするとモジュールがウェイクアップします。つまり、追加の送信は必要ありません。</p>
<p>API 送信が完了したら、<a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/api-commands/dwm-sleep#dwm-sleep"><span class="std std-ref">dwm_sleep</span></a> とシェル コマンド <em>quit</em> で紹介されているように、ホスト デバイスは電力を節約するためにモジュールを``スリープ``状態に戻す必要があります。</p>
</div>
<hr class="docutils">
<div class="section" id="spi-wakeup">
<h2>SPI ウェイクアップ</h2>
<p>DWM がスリープ状態 (低電力モード) の場合、SPI がコマンドの受け入れを開始する前にウェイクアップ手順を実行する必要があります。スリープから復帰するには、SPI の CS ピンで少なくとも 35 マイクロ秒幅のパルスを生成する必要があります (低電力モードのみ)。</p>
</div>
</div>


           </div>
