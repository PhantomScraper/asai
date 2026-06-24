---
title: "比較"
lang: ja
slug: "leaps-solutions/comparison"
section: "leaps-solutions"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-solutions/comparison/"
order: 8
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="comparison">
<span id="comparision"></span><h1>比較</h1>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 19%">
<col style="width: 32%">
<col style="width: 25%">
<col style="width: 24%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>アイテム</p></th>
<th class="head"><p><a class="reference internal" href="/docs/ja/leaps-rtls#leaps-rtls"><span class="std std-ref">LEAPS RTLS</span></a></p></th>
<th class="head"><p><a class="reference internal" href="/docs/ja/pans-pro-rtls#pans-pro-rtls"><span class="std std-ref">PANS PRO RTLS</span></a></p></th>
<th class="head"><p>PANS RTLS</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>サポートされているプロファイル</p></td>
<td><p>プロファイル 2、3、4、5</p></td>
<td><p>プロファイル 0</p></td>
<td><p>プロファイル 0</p></td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">ファームウェアのアップデート</div>
<div class="line">およびメンテナンス</div>
</div>
</td>
<td><p>はい</p></td>
<td><p>限定的</p></td>
<td><p>いいえ</p></td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line">本番環境で使用</div>
<div class="line">デプロイメント</div>
</div>
</td>
<td><p>はい</p></td>
<td><p>はい</p></td>
<td><p>限定的</p></td>
</tr>
<tr class="row-odd"><td><p>スケーラビリティ</p></td>
<td><p>完全にスケーラブル</p></td>
<td><p>完全にスケーラブル <a class="footnote-reference brackets" href="#note-0" id="id1">1</a></p></td>
<td><p>完全にスケーラブル <a class="footnote-reference brackets" href="#note-1" id="id2">2</a></p></td>
</tr>
<tr class="row-even"><td><p>位置情報機能</p></td>
<td><div class="line-block">
<div class="line">TWR <a class="footnote-reference brackets" href="#note-2" id="id3">3</a>,</div>
<div class="line">UL-TDoA <a class="footnote-reference brackets" href="#note-3" id="id4">4</a>,</div>
<div class="line">DL-TDoA <a class="footnote-reference brackets" href="#note-4" id="id5">5</a></div>
</div>
</td>
<td><p>TWRのみ</p></td>
<td><p>TWRのみ</p></td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">最大。更新速度</div>
<div class="line">per tag <a class="footnote-reference brackets" href="#note-5" id="id6">6</a></div>
</div>
</td>
<td><div class="line-block">
<div class="line">TWR の場合は最大 10 Hz</div>
<div class="line">UL-TDoA の場合は最大 50 Hz</div>
<div class="line">DL-TDoA の場合は最大 50 Hz</div>
</div>
</td>
<td><p>TWR の場合は最大 10 Hz</p></td>
<td><p>TWR の場合は最大 10 Hz</p></td>
</tr>
<tr class="row-even"><td><p>合計更新容量 <a class="footnote-reference brackets" href="#note-5" id="id7">6</a></p></td>
<td><div class="line-block">
<div class="line">TWR の場合は最大 320 Hz</div>
<div class="line">UL-TDoA の場合は最大 700 Hz</div>
<div class="line">DL-TDoA の場合は無制限</div>
</div>
</td>
<td><p>TWR の場合は最大 150 Hz</p></td>
<td><p>TWR の場合は最大 150 Hz</p></td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">最大。測定値</div>
<div class="line">アップデートごと</div>
</div>
</td>
<td><p>最大 30 <a class="footnote-reference brackets" href="#note-5" id="id8">6</a></p></td>
<td><p>4</p></td>
<td><p>4</p></td>
</tr>
<tr class="row-even"><td><p>データサーバー</p></td>
<td><p>詳細</p></td>
<td><p>詳細</p></td>
<td><p>基本 (二重性フィルタリング)</p></td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">基本 (二重性フィルタリング)</div>
<div class="line">サーバー上</div>
</div>
</td>
<td><p>50 ms <a class="footnote-reference brackets" href="#note-5" id="id9">6</a></p></td>
<td><p>更新レート + 50 ミリ秒</p></td>
<td><p>更新レート + 50 ミリ秒</p></td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line">基本 (二重性フィルタリング)</div>
<div class="line">デバイス上</div>
</div>
</td>
<td><p>&lt; 10ms</p></td>
<td><p>&lt; 10ms</p></td>
<td><p>&lt; 10ms</p></td>
</tr>
<tr class="row-odd"><td><p>サーバーAPI</p></td>
<td><p>MQTT</p></td>
<td><p>MQTT</p></td>
<td><p>MQTT</p></td>
</tr>
<tr class="row-even"><td><p>デバイス API</p></td>
<td><p>UART, SPI, USB, Bluetooth</p></td>
<td><p>UART, SPI, Bluetooth</p></td>
<td><p>UART, SPI, Bluetooth</p></td>
</tr>
<tr class="row-odd"><td><p>Bluetooth API</p></td>
<td><p>アドバンスト (統合 API)</p></td>
<td><p>レガシー</p></td>
<td><p>レガシー</p></td>
</tr>
<tr class="row-even"><td><p>Bluetooth セキュリティ</p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><p>いいえ</p></td>
</tr>
<tr class="row-odd"><td><p>ツール</p></td>
<td><p>Android および iOS 用の LEAPS Manager。 <a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> Windows/Linux/macOS 用 Web アプリ。</p></td>
<td><p>Android 用 PANS PRO Manager。 Windows/Linux/macOS 用 LEAPS Center Web アプリ。</p></td>
<td><p>Android 用の DRTLS Manager。 Windows/Linux/macOS 用の基本的な Web アプリ。</p></td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line">と互換性があります</div>
<div class="line">PANS RTLS</div>
</div>
</td>
<td><p>いいえ</p></td>
<td><p>はい</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p>システムのアップデート</p></td>
<td><p>はい</p></td>
<td><p>バグ修正</p></td>
<td><p>いいえ</p></td>
</tr>
<tr class="row-even"><td><p>長期サポート</p></td>
<td><p>はい</p></td>
<td><p>バグ修正</p></td>
<td><p>いいえ</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
<dl class="footnote brackets">
<dt class="label" id="note-0"><span class="brackets"><a class="fn-backref" href="#id1">1</a></span></dt>
<dd><p>LC5A 産業用ゲートウェイを使用する場合</p>
</dd>
<dt class="label" id="note-1"><span class="brackets"><a class="fn-backref" href="#id2">2</a></span></dt>
<dd><p>ユーザーは Raspberry Pi 3B をゲートウェイ デバイスとして使用する必要があります</p>
</dd>
<dt class="label" id="note-2"><span class="brackets"><a class="fn-backref" href="#id3">3</a></span></dt>
<dd><p>双方向レンジング</p>
</dd>
<dt class="label" id="note-3"><span class="brackets"><a class="fn-backref" href="#id4">4</a></span></dt>
<dd><p>アップリンク時間差到着</p>
</dd>
<dt class="label" id="note-4"><span class="brackets"><a class="fn-backref" href="#id5">5</a></span></dt>
<dd><p>ダウンリンクの到着時間差</p>
</dd>
<dt class="label" id="note-5"><span class="brackets">6</span><span class="fn-backref">(<a href="#id6">1</a>,<a href="#id7">2</a>,<a href="#id8">3</a>,<a href="#id9">4</a>)</span></dt>
<dd><p>ネットワークプロファイルと測定モードに応じて</p>
</dd>
</dl>
<hr class="docutils">
</div>


           </div>
