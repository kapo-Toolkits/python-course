/* ============================================================
   deck.js — მინიმალისტური სასლაიდე ძრავი (0 დამოკიდებულება)
   ლიცენზია: MIT
   --------------------------------------------------------
   კლავიშები:
     → ← Space PgUp PgDn Home End  — ნავიგაცია
     O — სლაიდების სია (outline)      N — ლექტორის ჩანაწერები
     D — ღია/მუქი თემა               F — სრული ეკრანი
     L — ენა (ქართული / English)     P — ბეჭდვა (PDF)
   URL-ში #7 პირდაპირ მე-7 სლაიდზე გადადის.
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

  function show(n, push) {
    cur = Math.max(0, Math.min(slides.length - 1, n));
    for (var i = 0; i < slides.length; i++) slides[i].classList.toggle("active", i === cur);
    slides[cur].scrollTop = 0;
    document.getElementById("bar").style.width =
      ((cur + 1) / slides.length * 100) + "%";
    document.getElementById("num").textContent = (cur + 1) + " / " + slides.length;
    var lis = document.querySelectorAll("#outline li");
    for (var j = 0; j < lis.length; j++) lis[j].classList.toggle("cur", j === cur);
    if (push !== false) history.replaceState(null, "", "#" + (cur + 1));
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
      '<button type="button" data-act="lang" title="ენა · Language (L)"><span id="langlbl"></span></button>' +
      '<button type="button" data-act="theme" title="ღია / მუქი · Theme (D)">◐</button>';

    var hint = document.createElement("div"); hint.id = "hint";
    hint.innerHTML =
      '<span lang="ka"><b>←/→</b> ნავიგაცია · <b>O</b> სია · <b>N</b> ჩანაწერები · ' +
      '<b>D</b> თემა · <b>L</b> ენა · <b>F</b> ეკრანი · <b>P</b> PDF</span>' +
      '<span lang="en"><b>←/→</b> navigate · <b>O</b> outline · <b>N</b> notes · ' +
      '<b>D</b> theme · <b>L</b> language · <b>F</b> fullscreen · <b>P</b> PDF</span>';

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
  }

  /* ---------- ენა ---------- */
  function curLang() {
    return document.documentElement.getAttribute("lang") === "en" ? "en" : "ka";
  }

  function setLang(l) {
    document.documentElement.setAttribute("lang", l);
    var lbl = document.getElementById("langlbl");
    if (lbl) lbl.textContent = l === "en" ? "ქარ" : "EN";
    buildOutline();
    try { localStorage.setItem("deck-lang", l); } catch (e) {}
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

  /* ---------- 6. გაშვება ---------- */
  try {
    var saved = localStorage.getItem("deck-theme");
    if (saved) document.documentElement.setAttribute("data-theme", saved);
    else if (window.matchMedia && matchMedia("(prefers-color-scheme: dark)").matches)
      document.documentElement.setAttribute("data-theme", "dark");
  } catch (e) {}

  prepCode();
  buildUI();

  var savedLang = "ka";
  try { savedLang = localStorage.getItem("deck-lang") || "ka"; } catch (e) {}
  setLang(savedLang);          /* outline-საც აწყობს */

  document.addEventListener("keydown", keys);
  window.addEventListener("hashchange", function () {
    var n = parseInt(location.hash.slice(1), 10);
    if (n && n - 1 !== cur) show(n - 1, false);
  });
  swipe();

  var start = parseInt(location.hash.slice(1), 10);
  show(start ? start - 1 : 0, false);
})();
