/* ============================================================
   deck.js — მინიმალისტური სასლაიდე ძრავი (0 დამოკიდებულება)
   ლიცენზია: MIT
   --------------------------------------------------------
   კლავიშები:
     → ← Space PgUp PgDn Home End  — ნავიგაცია
     O — სლაიდების სია (outline)      N — ლექტორის ჩანაწერები
     D — ღია/მუქი თემა               F — სრული ეკრანი
     L — ენა (ქართული / English)     P — ბეჭდვა (PDF)
     S — ლექტორის ხედი მეორე ფანჯარაში (მიმდინარე + შემდეგი + ჩანაწერი + ტაიმერი)
   URL-ში #7 პირდაპირ მე-7 სლაიდზე გადადის; #7p იმავე სლაიდს ლექტორის ხედში ხსნის.
   ============================================================ */
(function () {
  "use strict";

  /* ---------- 1. Python-ის სინტაქსის მინი-ხაზგასმა ---------- */
  var KW = "False|None|True|and|as|assert|async|await|break|class|continue|def|del|" +
           "elif|else|except|finally|for|from|global|if|import|in|is|lambda|nonlocal|" +
           "not|or|pass|raise|return|try|while|with|yield|match|case";
  var BI = "abs|all|any|bin|bool|chr|dict|dir|divmod|enumerate|eval|filter|float|format|" +
           "frozenset|getattr|hex|id|input|int|isinstance|iter|len|list|map|max|min|next|" +
           "object|oct|open|ord|pow|print|range|repr|reversed|round|set|setattr|slice|" +
           "sorted|str|sum|super|tuple|type|zip";

  var RULES = [
    ["t-com", /^#[^\n]*/],
    ["t-str", /^(?:[rbfuRBFU]{0,2})(?:'''[\s\S]*?'''|"""[\s\S]*?"""|'(?:\\.|[^'\\\n])*'|"(?:\\.|[^"\\\n])*")/],
    ["t-num", /^\d[\d_]*(?:\.\d+)?(?:[eE][+-]?\d+)?/],
    ["t-fn",  /^@[A-Za-z_]\w*/],
    ["t-kw",  new RegExp("^(?:" + KW + ")\\b")],
    ["t-bi",  new RegExp("^(?:" + BI + ")\\b(?=\\s*\\()")],
    ["t-fn",  /^[A-Za-z_]\w*(?=\s*\()/],
    ["",      /^[A-Za-z_]\w*/],
    ["",      /^\s+/],
    ["",      /^[\s\S]/]
  ];

  function esc(s) {
    return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  }

  function highlight(src) {
    var out = "", i = 0;
    while (i < src.length) {
      var rest = src.slice(i), hit = null;
      for (var r = 0; r < RULES.length; r++) {
        var m = RULES[r][1].exec(rest);
        if (m && m[0].length) { hit = [RULES[r][0], m[0]]; break; }
      }
      if (!hit) { hit = ["", rest.charAt(0)]; }
      out += hit[0] ? '<span class="' + hit[0] + '">' + esc(hit[1]) + "</span>" : esc(hit[1]);
      i += hit[1].length;
    }
    return out;
  }

  /* ---------- 2. კოდის ბლოკები + კოპირების ღილაკი ---------- */
  function prepCode() {
    var blocks = document.querySelectorAll("pre.code > code");
    for (var i = 0; i < blocks.length; i++) {
      var code = blocks[i];
      var raw = code.textContent.replace(/^\n/, "").replace(/\s+$/, "");
      code.dataset.raw = raw;
      if (!code.classList.contains("nohl")) code.innerHTML = highlight(raw);
      else code.textContent = raw;

      var btn = document.createElement("button");
      btn.className = "cp";
      btn.type = "button";
      btn.textContent = "კოპირება";
      (function (b, txt) {
        b.addEventListener("click", function (e) {
          e.stopPropagation();
          navigator.clipboard.writeText(txt).then(function () {
            b.textContent = "დაკოპირდა ✓";
            setTimeout(function () { b.textContent = "კოპირება"; }, 1400);
          });
        });
      })(btn, raw);
      code.parentNode.appendChild(btn);
    }
  }

  /* ---------- 3. სლაიდები ---------- */
  var slides = [].slice.call(document.querySelectorAll(".slide"));
  var cur = 0;

  /* ლექტორის ხედი: hash-ის ბოლოს "p" — მაგ. #5p. peer — მეორე ფანჯარა. */
  var PRES = /p$/i.test(location.hash.slice(1));
  var peer = null;

  function show(n, push, quiet) {
    cur = Math.max(0, Math.min(slides.length - 1, n));
    for (var i = 0; i < slides.length; i++) slides[i].classList.toggle("active", i === cur);
    slides[cur].scrollTop = 0;
    document.getElementById("bar").style.width =
      ((cur + 1) / slides.length * 100) + "%";
    document.getElementById("num").textContent = (cur + 1) + " / " + slides.length;
    var lis = document.querySelectorAll("#outline li");
    for (var j = 0; j < lis.length; j++) lis[j].classList.toggle("cur", j === cur);
    if (push !== false) history.replaceState(null, "", "#" + (cur + 1) + (PRES ? "p" : ""));
    if (PRES) paint();
    if (!quiet) send();
  }

  var go = function (d) { show(cur + d); };

  /* ---------- 4. ინტერფეისის აწყობა ---------- */
  function buildUI() {
    var bar = document.createElement("div"); bar.id = "bar";

    var hud = document.createElement("div"); hud.id = "hud";
    hud.innerHTML =
      '<button type="button" data-act="prev" title="წინა">←</button>' +
      '<span id="num"></span>' +
      '<button type="button" data-act="next" title="შემდეგი">→</button>' +
      '<button type="button" data-act="outline" title="სლაიდების სია · Outline (O)">☰</button>' +
      (PRES ? "" :
        '<button type="button" data-act="pres" ' +
        'title="ლექტორის ხედი · Presenter view (S)">🎤</button>') +
      '<button type="button" data-act="lang" title="ენა · Language (L)"><span id="langlbl"></span></button>' +
      '<button type="button" data-act="theme" title="ღია / მუქი · Theme (D)">◐</button>';

    var hint = document.createElement("div"); hint.id = "hint";
    hint.innerHTML =
      '<span lang="ka"><b>←/→</b> ნავიგაცია · <b>O</b> სია · <b>N</b> ჩანაწერები · ' +
      '<b>S</b> ლექტორის ხედი · <b>D</b> თემა · <b>L</b> ენა · <b>F</b> ეკრანი · <b>P</b> PDF</span>' +
      '<span lang="en"><b>←/→</b> navigate · <b>O</b> outline · <b>N</b> notes · ' +
      '<b>S</b> presenter · <b>D</b> theme · <b>L</b> language · <b>F</b> fullscreen · <b>P</b> PDF</span>';

    var ol = document.createElement("div"); ol.id = "outline";

    document.body.appendChild(bar);
    document.body.appendChild(hud);
    document.body.appendChild(hint);
    document.body.appendChild(ol);

    hud.addEventListener("click", function (e) {
      var btn = e.target.closest ? e.target.closest("[data-act]") : null;
      var a = btn && btn.dataset.act;
      if (a === "prev") go(-1);
      else if (a === "next") go(1);
      else if (a === "outline") ol.classList.toggle("on");
      else if (a === "theme") theme();
      else if (a === "lang") lang();
      else if (a === "pres") openPresenter();
    });
    ol.addEventListener("click", function (e) {
      if (e.target.dataset && e.target.dataset.i !== undefined) {
        show(+e.target.dataset.i); ol.classList.remove("on");
      }
    });
  }

  function theme() {
    var d = document.documentElement.getAttribute("data-theme") === "dark";
    document.documentElement.setAttribute("data-theme", d ? "light" : "dark");
    try { localStorage.setItem("deck-theme", d ? "light" : "dark"); } catch (e) {}
    send();
  }

  /* ---------- ენა ---------- */
  function curLang() {
    return document.documentElement.getAttribute("lang") === "en" ? "en" : "ka";
  }

  function setLang(l, quiet) {
    document.documentElement.setAttribute("lang", l);
    var lbl = document.getElementById("langlbl");
    if (lbl) lbl.textContent = l === "en" ? "ქარ" : "EN";
    buildOutline();
    if (PRES) paint();
    try { localStorage.setItem("deck-lang", l); } catch (e) {}
    if (!quiet) send();
  }

  function lang() { setLang(curLang() === "en" ? "ka" : "en"); }

  /* სათაურიდან მხოლოდ მიმდინარე ენის ტექსტს იღებს */
  function headText(h) {
    if (!h) return "—";
    var pick = h.querySelector('[lang="' + curLang() + '"]') || h;
    /* <br>-ს ჰარით ვცვლით ასლში: არააქტიურ სლაიდზე innerText არ გამოდგება,
       რადგან ის display:none-ის დროს textContent-ივით იქცევა */
    var c = pick.cloneNode(true);
    var brs = c.querySelectorAll("br");
    for (var i = 0; i < brs.length; i++) {
      brs[i].parentNode.replaceChild(document.createTextNode(" "), brs[i]);
    }
    return c.textContent.replace(/\s+/g, " ").trim() || "—";
  }

  function buildOutline() {
    var ol = document.getElementById("outline");
    if (!ol) return;
    var items = "";
    for (var i = 0; i < slides.length; i++) {
      items += "<li data-i=" + i + ">" +
               esc(headText(slides[i].querySelector("h1, h2, h3"))) + "</li>";
    }
    ol.innerHTML =
      '<h2><span lang="ka">სლაიდები</span><span lang="en">Slides</span></h2>' +
      "<ol>" + items + "</ol>";
    var lis = ol.querySelectorAll("li");
    for (var j = 0; j < lis.length; j++) lis[j].classList.toggle("cur", j === cur);
  }

  /* ---------- 5. მოვლენები ---------- */
  function keys(e) {
    if (e.ctrlKey || e.altKey || e.metaKey) return;
    var k = e.key;
    if (k === "ArrowRight" || k === "PageDown" || k === " " || k === "Enter") { go(1); e.preventDefault(); }
    else if (k === "ArrowLeft" || k === "PageUp" || k === "Backspace") { go(-1); e.preventDefault(); }
    else if (k === "Home") show(0);
    else if (k === "End") show(slides.length - 1);
    else if (k === "Escape") document.getElementById("outline").classList.remove("on");
    else {
      var c = k.toLowerCase();
      if (c === "o") document.getElementById("outline").classList.toggle("on");
      else if (c === "n") document.body.classList.toggle("notes");
      else if (c === "d") theme();
      else if (c === "l") lang();
      else if (c === "f") {
        if (document.fullscreenElement) document.exitFullscreen();
        else document.documentElement.requestFullscreen();
      }
      else if (c === "p") { e.preventDefault(); window.print(); }
      else if (c === "s" && !PRES) openPresenter();
    }
  }

  function swipe() {
    var x0 = null;
    document.addEventListener("touchstart", function (e) { x0 = e.touches[0].clientX; }, { passive: true });
    document.addEventListener("touchend", function (e) {
      if (x0 === null) return;
      var dx = e.changedTouches[0].clientX - x0;
      if (Math.abs(dx) > 60) go(dx < 0 ? 1 : -1);
      x0 = null;
    }, { passive: true });
  }

  /* ---------- 6. ლექტორის ხედი (მეორე ფანჯარა) ----------
     ორივე ფანჯარაში ერთი და იგივე ფაილია გახსნილი; განსხვავება მხოლოდ
     hash-ის ბოლოს "p"-ია. სინქრონიზაცია — postMessage პირდაპირი ფანჯრის
     მიმართვით, ამიტომ file://-იდანაც მუშაობს (localStorage იქ არ გამოდგება). */

  function openPresenter() {
    if (peer && !peer.closed) { try { peer.focus(); } catch (e) {} return; }
    var url = location.href.split("#")[0] + "#" + (cur + 1) + "p";
    peer = window.open(url, "deckPresenter",
      "popup=yes,width=1280,height=820,menubar=no,toolbar=no,location=no");
    if (!peer) {
      alert(curLang() === "en"
        ? "The browser blocked the pop-up window. Allow pop-ups for this page."
        : "ბრაუზერმა ახალი ფანჯარა დაბლოკა. დაუშვი pop-up ამ გვერდისთვის.");
    }
  }

  function send(t) {
    if (!peer) return;
    try {
      if (peer.closed) { peer = null; return; }
      peer.postMessage({
        deck: 1, t: t || "state", n: cur, lang: curLang(),
        theme: document.documentElement.getAttribute("data-theme") || "light"
      }, "*");
    } catch (e) { peer = null; }
  }

  function onMessage(e) {
    var d = e.data;
    if (!d || d.deck !== 1) return;
    if (!peer || peer.closed) peer = e.source;
    if (d.lang && d.lang !== curLang()) setLang(d.lang, true);
    if (d.theme && d.theme !== document.documentElement.getAttribute("data-theme"))
      document.documentElement.setAttribute("data-theme", d.theme);
    if (typeof d.n === "number" && d.n !== cur) show(d.n, true, true);
    if (d.t === "hello") send();          /* პასუხად მდგომარეობას ვუბრუნებთ */
  }

  function buildPresenter() {
    document.title = "🎤 " + document.title;
    document.body.classList.add("pmode");

    var pv = document.createElement("div");
    pv.id = "pv";
    pv.innerHTML =
      '<div id="pv-top">' +
        '<div id="pv-timer">00:00</div>' +
        '<button type="button" data-p="tog" id="pv-tog" ' +
          'title="დაწყება / პაუზა · Start / pause">❚❚</button>' +
        '<button type="button" data-p="rst" title="განულება · Reset">⟲</button>' +
        '<div id="pv-clock"></div>' +
        '<div id="pv-title">' +
          '<span lang="ka">ლექტორის ხედი</span><span lang="en">Presenter view</span>' +
        '</div>' +
      '</div>' +
      '<div id="pv-body">' +
        '<div id="pv-left">' +
          '<div class="plab"><span lang="ka">ეკრანზე</span><span lang="en">On screen</span></div>' +
          '<div class="pstage" id="pv-cur"></div>' +
        '</div>' +
        '<div id="pv-right">' +
          '<div class="plab"><span lang="ka">შემდეგი</span><span lang="en">Next</span></div>' +
          '<div class="pstage" id="pv-next"></div>' +
          '<div class="plab"><span lang="ka">ჩანაწერი</span><span lang="en">Note</span></div>' +
          '<div id="pv-notes"></div>' +
        '</div>' +
      '</div>';
    document.body.appendChild(pv);

    pv.addEventListener("click", function (e) {
      var b = e.target.closest ? e.target.closest("[data-p]") : null;
      if (!b) return;
      if (b.dataset.p === "tog") timerToggle();
      else if (b.dataset.p === "rst") timerReset();
    });

    var rt;
    window.addEventListener("resize", function () {
      clearTimeout(rt); rt = setTimeout(paint, 150);
    });

    timerRun(true);
    setInterval(tick, 1000);
  }

  /* სლაიდის ასლი მინიატურაში. კადრს ამ ფანჯრის ზომას ვაძლევთ, რომ
     clamp(...vw...) იმავე სიგანეზე გამოითვალოს, მერე კი ვამცირებთ. */
  function stage(id, i) {
    var el = document.getElementById(id);
    if (!el) return;
    el.innerHTML = "";
    if (i < 0 || i >= slides.length) {
      el.innerHTML = '<div class="pend"><span lang="ka">დასასრული</span>' +
                     '<span lang="en">The end</span></div>';
      return;
    }
    var c = slides[i].cloneNode(true);
    c.classList.add("active");
    var junk = c.querySelectorAll(".cp, .note");
    for (var j = 0; j < junk.length; j++) junk[j].parentNode.removeChild(junk[j]);

    var w = window.innerWidth, h = window.innerHeight;
    var f = document.createElement("div");
    f.className = "pframe";
    f.style.width = w + "px";
    f.style.height = h + "px";
    f.appendChild(c);
    el.appendChild(f);

    var k = Math.min(el.clientWidth / w, el.clientHeight / h);
    f.style.transform = "scale(" + k + ")";
    f.style.left = Math.max(0, (el.clientWidth - w * k) / 2) + "px";
    f.style.top = Math.max(0, (el.clientHeight - h * k) / 2) + "px";
  }

  function paint() {
    if (!document.getElementById("pv")) return;
    stage("pv-cur", cur);
    stage("pv-next", cur + 1);

    var notes = slides[cur].querySelectorAll(".note"), html = "";
    for (var i = 0; i < notes.length; i++)
      html += '<div class="pnote">' + notes[i].innerHTML + "</div>";
    document.getElementById("pv-notes").innerHTML = html ||
      '<p class="pnone"><span lang="ka">ამ სლაიდზე ჩანაწერი არ არის.</span>' +
      '<span lang="en">No note on this slide.</span></p>';
  }

  /* ---------- ტაიმერი ---------- */
  var tAcc = 0, tFrom = 0, tOn = false;

  function pad(n) { return (n < 10 ? "0" : "") + n; }

  function timerRun(on) {
    if (on && !tOn) { tFrom = Date.now(); tOn = true; }
    else if (!on && tOn) { tAcc += Date.now() - tFrom; tOn = false; }
    var b = document.getElementById("pv-tog");
    if (b) b.textContent = tOn ? "❚❚" : "▶";
    tick();
  }

  function timerToggle() { timerRun(!tOn); }
  function timerReset() { tAcc = 0; tFrom = Date.now(); tick(); }

  function tick() {
    var el = document.getElementById("pv-timer");
    if (!el) return;
    var sec = Math.floor((tAcc + (tOn ? Date.now() - tFrom : 0)) / 1000);
    el.textContent = pad(Math.floor(sec / 60)) + ":" + pad(sec % 60);
    var d = new Date();
    document.getElementById("pv-clock").textContent = pad(d.getHours()) + ":" + pad(d.getMinutes());
  }

  /* ---------- 7. გაშვება ---------- */
  try {
    var saved = localStorage.getItem("deck-theme");
    if (saved) document.documentElement.setAttribute("data-theme", saved);
    else if (window.matchMedia && matchMedia("(prefers-color-scheme: dark)").matches)
      document.documentElement.setAttribute("data-theme", "dark");
  } catch (e) {}

  prepCode();
  buildUI();
  if (PRES) buildPresenter();

  var savedLang = "ka";
  try { savedLang = localStorage.getItem("deck-lang") || "ka"; } catch (e) {}
  setLang(savedLang);          /* outline-საც აწყობს */

  document.addEventListener("keydown", keys);
  window.addEventListener("message", onMessage);
  window.addEventListener("hashchange", function () {
    var n = parseInt(location.hash.slice(1), 10);
    if (n && n - 1 !== cur) show(n - 1, false);
  });
  swipe();

  var start = parseInt(location.hash.slice(1), 10);
  show(start ? start - 1 : 0, false, true);

  /* ლექტორის ფანჯარა თავად ეცნობა მთავარს — ასე მთავარი იგებს, ვის მისწეროს */
  if (PRES && window.opener && !window.opener.closed) {
    peer = window.opener;
    send("hello");
  }
})();
