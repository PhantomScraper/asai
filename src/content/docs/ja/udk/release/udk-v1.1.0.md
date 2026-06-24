---
title: "バージョンv1.1.0"
lang: ja
slug: "udk/release/udk-v1.1.0"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/ja/udk/release/udk-v1.1.0/"
order: 20
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="version-v1-1-0">
<h1>バージョンv1.1.0</h1>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<ul class="simple">
<li><p><strong>バージョン</strong>:  UDK v1.1.0</p></li>
<li><p><strong>発売日</strong>: 2025年6月16日</p></li>
</ul>
</div>
<ul>
<li><p>LEAPS UWB サブシステム</p>
<blockquote>
<div><ul class="simple">
<li><p>バグ修正</p></li>
<li><p>BLEアクティベーションを利用した電力最適化</p></li>
<li><p>UWB容量のさらなる最適化</p></li>
<li><p>異なるネットワーク間でのTWRタグのローミング能力の向上</p></li>
<li><p>スニファ機能の追加</p></li>
<li><p>DL-TDoA の測定データをユーザーが利用できるようにする</p></li>
<li><p>TWR 使用時にアップリンクおよびダウンリンクのユーザーデータの全容量を検証できるように API を追加する</p></li>
<li><p>レンジの徹底的な再検証</p></li>
<li><p>セキュア・ブート・オプションの追加</p></li>
<li><p>UWBルーチンのさらなるランタイム最適化</p></li>
<li><p>メモリ最適化の見直し</p></li>
<li><p>消費電力のさらなる見直しと最適化</p></li>
<li><p>Validate on DWM3001, DWM1001, Murata 2AB</p></li>
<li><p>自動テスト（システムテスト、APIテスト、さまざまなモードのテスト、システムの構成）のための屋外テストセットアップの使用</p></li>
<li><p>自動位置決め測定は、アンカーをどれだけ使っても確実に実行されます</p></li>
<li><p>新しいトリレーションアルゴリズムの追加、計算時間の追加</p></li>
<li><p>共存ネットワークを追加</p></li>
<li><p>Zone-IDを追加し、位置推定精度を向上</p></li>
<li><p>ネットワークマスクを追加し、タグがマスクに適合するネットワーク間をローミングできるように</p></li>
<li><p>InsightSIP ISP3080のサポートを追加し、消費電力を最適化</p></li>
<li><p>ISP3080で使用される新しい加速度センサーのサポートを追加</p></li>
<li><p>位置情報エンジンが無効な場合の距離の送信を追加</p></li>
<li><p>UL-TDOAスロットのタイミング、容量、設定をバグフィックス/改善</p></li>
<li><p>電源およびリセット・サイクル用の不揮発性カウンタを追加</p></li>
<li><p>ボード電圧固有の構成、電圧測定、およびバッテリ・ステータス表示を追加、バッテリ保護を改善</p></li>
<li><p>温度測定とデータ収集を追加</p></li>
<li><p>アンテナの遅延を再検証し、RFセットアップごとに補正を適用</p></li>
<li><p>自動Rx受信レート計算を追加</p></li>
<li><p>UARTのないデバッグプラットフォーム（InsightSIP ISP3080など）へのSWD経由のシェルデバッグサポートを追加</p></li>
<li><p>データバックホールの改善</p></li>
<li><p>TWR RTLS のアンカー選択戦略の改善</p></li>
<li><p>さまざまな API の改善</p></li>
<li><p>SPI フラッシュメモリのサポート追加</p></li>
<li><p>新しい RED / CRA 指令に備えた対策の実施</p></li>
<li><p>QPG6200 対応のための初期準備</p></li>
</ul>
</div></blockquote>
</li>
<li><p>LEAPS サーバー</p>
<blockquote>
<div><ul class="simple">
<li><p>UL-TDoA の時間同期の</p></li>
<li><p>改善 UL-TDoA および DL-TDoA のマルチレートアルゴリズムの改善</p></li>
</ul>
</div></blockquote>
</li>
<li><p>LEAPS Gateway</p>
<blockquote>
<div><ul class="simple">
<li><p>バグ修正</p></li>
<li><p>大容量に対応するためにパフォーマンスを最適化</p></li>
<li><p>UWB RFパラメータ、Txパワー設定のコンフィギュレーションを可能に</p></li>
<li><p>オーバーレイ・コンフィギュレーション・ファイルのサポートを追加</p></li>
</ul>
</div></blockquote>
</li>
<li><p>LEAPS Manager Android</p>
<blockquote>
<div><ul class="simple">
<li><p>バグ修正</p></li>
<li><p>ダークモードの追加</p></li>
<li><p>6つ以上のアンカーを使用し、すべてがBluetooth範囲内でない場合の自動ポジショニングを許可</p></li>
<li><p>デモの設定動作の改善</p></li>
<li><p>UWBプロパティの設定を許可</p></li>
<li><p>デバイス・フィルター機能の追加</p></li>
<li><p>デバイスのエクスポート機能の追加</p></li>
</ul>
</div></blockquote>
</li>
<li><p>LEAPS Manager iOS</p>
<blockquote>
<div><ul class="simple">
<li><p>バグ修正</p></li>
<li><p>バッテリー残量表示の追加</p></li>
<li><p>ツールチップの追加</p></li>
<li><p>ネットワークの改善</p></li>
<li><p>ヒートマップの改善</p></li>
<li><p>デモの設定動作の改善</p></li>
<li><p>Bluetoothのディスカバリーと通信の改善</p></li>
</ul>
</div></blockquote>
</li>
<li><p>LEAPS Center</p>
<blockquote>
<div><ul class="simple">
<li><p>お客様やチームからのフィードバックに基づくバグフィックス + 改善点</p></li>
<li><p>ヒートマップの改善</p></li>
<li><p>間取り図のフリップ機能の追加</p></li>
<li><p>グリッド設定の追加</p></li>
<li><p>周辺アンカーシグナルマップの追加</p></li>
<li><p>ゾーンアラーム機能の追加</p></li>
<li><p>さまざまな形状のジオフェンシングの追加</p></li>
<li><p>ロギング機能の追加</p></li>
<li><p>TWR使用時のアップリンク/ダウンリンクユーザーデータのフルキャパシティの検証ツールの追加</p></li>
<li><p>3Dオブジェクトを地図にインポートできるかどうかを調査</p></li>
<li><p>ツールチップの追加</p></li>
<li><p>2D/3D にズームイン/アウト・ボタンを追加</p></li>
</ul>
</div></blockquote>
</li>
<li><p>UDK SDK</p>
<blockquote>
<div><ul class="simple">
<li><p>バグ修正</p></li>
<li><p>顧客からのフィードバックに基づくドキュメントの改善</p></li>
<li><p>Githubでのリリース</p></li>
</ul>
</div></blockquote>
</li>
</ul>
<hr class="docutils">
<div class="section" id="known-limitations">
<h2>既知の制限</h2>
<table class="colwidths-given docutils align-default">
<colgroup>
<col style="width: 7%">
<col style="width: 53%">
<col style="width: 40%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>いいえ。</p></th>
<th class="head"><p>要約</p></th>
<th class="head"><p>影響を受ける</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>1</p></td>
<td><p><a class="reference internal" href="/docs/ja/udk/known-limitation/limit-001#limitation-1"><span class="std std-ref">UWB デバイスのキャリブレーションはサポートされていません。</span></a></p></td>
<td><p><a class="reference internal" href="/docs/ja/udk/udk-start/locate-device-using-angle-of-arrival-demo#anchor-lc"><span class="std std-ref">到着角度(AoA)を使ったデバイスの位置特定デモ</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>2</p></td>
<td><p><a class="reference internal" href="/docs/ja/udk/known-limitation/limit-002#limitation-2"><span class="std std-ref">一部のデバイスパラメータの設定はサポートされていません</span></a></p></td>
<td><p><a class="reference internal" href="/docs/ja/udk/udk-start/locate-device-using-angle-of-arrival-demo#anchor-lc"><span class="std std-ref">到着角度(AoA)を使ったデバイスの位置特定デモ</span></a></p></td>
</tr>
</tbody>
</table>
<div class="toctree-wrapper compound">
</div>
</div>
<hr class="docutils">
<div class="section" id="known-issues">
<h2>既知の問題</h2>
<table class="colwidths-given docutils align-default">
<colgroup>
<col style="width: 7%">
<col style="width: 53%">
<col style="width: 40%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>いいえ。</p></th>
<th class="head"><p>要約</p></th>
<th class="head"><p>影響を受ける</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>1</p></td>
<td><p>: <a class="reference internal" href="/docs/ja/udk/known-issue/issue-004#issue-1"><span class="std std-ref">FiRaパラメータの設定が正しく動作しません。</span></a></p></td>
<td><p><a class="reference internal" href="/docs/ja/udk/udk-start/locate-device-using-angle-of-arrival-demo#anchor-lc"><span class="std std-ref">到着角度(AoA)を使ったデバイスの位置特定デモ</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>2</p></td>
<td><p><a class="reference internal" href="/docs/ja/udk/known-issue/issue-005#issue-2"><span class="std std-ref">測距開始時または測距停止時にデバイスが予期せずリセットされることがあります。</span></a></p></td>
<td><p><a class="reference internal" href="/docs/ja/udk/udk-start/locate-device-using-angle-of-arrival-demo#anchor-lc"><span class="std std-ref">到着角度(AoA)を使ったデバイスの位置特定デモ</span></a></p></td>
</tr>
</tbody>
</table>
<div class="toctree-wrapper compound">
</div>
<hr class="docutils">
</div>
</div>


           </div>
