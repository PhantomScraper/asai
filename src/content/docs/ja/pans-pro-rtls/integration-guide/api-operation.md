---
title: "API オペレーション"
lang: ja
slug: "pans-pro-rtls/integration-guide/api-operation"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/api-operation/"
order: 125
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="api-operation">
<h1>API オペレーション</h1>
<hr class="docutils">
<div class="section" id="gpio-notification-for-status-change">
<h2>ステータス変更の GPIO 通知</h2>
<p>ホスト デバイスが SPI/UART 通信を開始するのではなく、以下に示すように、DWM モジュールは専用 GPIO ピン (P0.26) を HIGH レベルに切り替えることでステータス変更の通知を送信できます。この機能を有効にするには、ホスト デバイスで dwm_int_cfg_set コマンドを使用する必要があります。 HIGH レベルを検出すると、ホスト デバイスは dwm_status_get コマンドを開始して、DWM1001 デバイスからステータスを取得できます。dwm_int_cfg コマンドと dwm_status_get コマンドは両方とも、前のセクションで紹介した SPI または UART スキームを通じて送信できます。</p>
<div class="figure align-default" id="id1">
<a class="reference internal image-reference" href="../../../_images/image14.png"><img alt="../../../_images/image14.png" src="/docs-assets/ja/_images/image14.png" style="width: 3.50972in; height: 3.07361in;"></a>
<p class="caption"><span class="caption-text">DWM1001データ準備完了 GPIO ピンを使用して、ホスト デバイスにステータス変更を通知します</span></p>
</div>
<p>この GPIO ピン レベルの変更は、上記の SPI TLV 要求/応答手順中にステータス変更が発生した場合、競合を回避するために延期されます。詳細には、SPI が “SPI: call_back を待機“、“SPI: 読み取り SIZE を待機“、“SPI: 読み取り DATA/ERR を待機“ の状態にある場合、GPIO スキームは GPIO ピンの制御を放棄します。SPI 通信後、SPI が “SPI: アイドル“ の状態にある場合、GPIO スキームは GPIO ピンの制御を取り戻します。</p>
</div>
<hr class="docutils">
<div class="section" id="api-for-on-module-c-code-user-application">
<h2>モジュール上の C コード ユーザー アプリケーション用の API</h2>
<p>ユーザーは、ビルド済みファームウェアのオンボード パックで提供される特定のエントリ ファイルで、独自のコードを追加し、C コード API 関数を利用できます。この方法では、ユーザーはモジュール ファームウェア内に独自の関数を追加でき、外部ホスト コントローラー デバイスを追加する必要がない場合があります。</p>
<p>C コード ユーザーがオンボード ファームウェアを使用する際に注意すべき点がいくつかあります。</p>
<ul class="simple">
<li><p>ユーザー アプリケーションは eCos RTOS および DWM ライブラリに基づいています。</p></li>
<li><p>ユーザー アプリケーションとのリンクに使用されるファイル:</p>
<ul>
<li><p>dwm.h - ヘッダー ファイル - ユーザー アプリケーションの構築に必要なすべてのヘッダー ファイルのラッパー</p></li>
<li><p>libdwm.a - 静的ライブラリ</p></li>
<li><p>extras.o、vectors.o、libtarget.a - eCos 静的ライブラリ</p></li>
<li><p>target_s132_fw1.ld - ファームウェアセクション 1 のリンカースクリプト</p></li>
<li><p>target_s132_fw2.ld - ファームウェアセクション 2 のリンカースクリプト</p></li>
</ul>
</li>
<li><p>API はユーザー アプリケーションに関数と定義を提供します。</p>
<ul>
<li><p>スレッドの作成、メモリ割り当て、インターフェイス (GPIO、SPI など) へのアクセス、同期 (ミューテックス、シグナル) などのオペレーティング システム上の一般的な機能。</p></li>
<li><p>DWM 通信スタックの初期化、構成、およびメンテナンス</p></li>
<li><p>受信データと測定値のコールバックの登録。</p></li>
<li><p>API は、システムのパフォーマンスに影響を与える可能性のある誤った設定からユーザー アプリケーションを保護します。</p></li>
</ul>
</li>
</ul>
<hr class="docutils">
<div class="section" id="system-specifications">
<h3>システム仕様</h3>
<p>最大ユーザー スレッド: 5</p>
<blockquote>
<div><ul class="simple">
<li><p>エンドユーザー用の RAM: cca TBD kB (D12 以降は TBD、予想 &gt; 5KB)</p></li>
<li><p>エンドユーザー用のフラッシュ: cca TBD kB (D12 以降は未定、予想 &gt;= 40KB)</p></li>
</ul>
</div></blockquote>
</div>
</div>
<hr class="docutils">
<div class="section" id="dwm1001-threads">
<h2>DWM1001 スレッド</h2>
<p>DWM1001 ファームウェアシステムには、SPI、BLE、UART、汎用API、ユーザーアプリケーションなど、多数のスレッドが存在します。各スレッドは特定のタスクを処理します。SPI、BLE、UART スレッドは、外部デバイスとのデータ転送を制御します。これらのスレッドは、受信したリクエストを解析しません。受信したリクエストはすべて汎用APIスレッドに送信されます。汎用APIスレッドは、受信したリクエストを解析するスレッドです。受信したリクエストが有効かどうかを判断します。有効な場合、ファームウェアは対応するデータをレスポンスとして準備し、無効な場合はエラーメッセージをレスポンスとして使用します。その後、汎用APIスレッドは call_back() 関数を実行し、準備されたレスポンスメッセージをリクエストの送信元スレッドに返します。オンボード ユーザー アプリケーション スレッドは、ユーザーが独自の機能を追加するための独立したスレッドです。入り口は、DWM1001 オンボード パッケージの dwm\examples\ フォルダーにあります。サンプル プロジェクトは dwmexamplesdwm-simpleフォルダーにあります。</p>
</div>
<hr class="docutils">
<div class="section" id="position-representation">
<h2>ポジション代表</h2>
<p>リアルタイム測位システムで位置と距離を表示する場合、考慮すべき点が 2 つあります。</p>
<blockquote>
<div><ul class="simple">
<li><p>精度</p></li>
<li><p>精度</p></li>
</ul>
</div></blockquote>
<p>精度は、ノードによって報告された位置と実際の位置との間の誤差です。現在、この設計で使用されている DW1000 は約 10 cm の精度を提供します。精度は、最下位ビット (LSB) が表す値です。このシステムのオンボードファームウェアでは、精度は 1 mm、つまり 0.001 メートルです。位置は3次元座標（X、Y、Z）で表されます。X、Y、Zは32ビット整数（4バイト）です。各LSBは1mmを表します。これは、値の解釈を容易にし、報告された値に対する計算を容易にするためです。</p>
<p>精度を決定するときは、意味のある結果を得るために精度を考慮して選択することが重要です。精度が低い場合、ユーザーに正確な値を表示しても意味がありません。1mmの精度は、現在の10cmの精度に比べて細かすぎます。そのため、位置情報の表示には1cm、つまり0.01メートルの精度を使用します。更新された値は、座標/距離が1cm以上変化した場合にのみ表示されます。これは、float/double値を意味のある小数点以下の桁数に丸めるのと似ています。  精度を決めるときは、精度に応じて選択することが重要であるため、精度が非常に低い場合、ユーザーに正確な数値を表示することは役に立ちません。したがって、表示位置では、1 ピクセル/ピッチの変動がある場合に限り、0.01 ピクセルの精度が使用されます。これは、浮遊数/倍数の値を意識的な小数ビットに置き換えることに似ています。</p>
</div>
</div>


           </div>
