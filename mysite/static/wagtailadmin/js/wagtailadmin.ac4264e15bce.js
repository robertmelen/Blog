(()=>{"use strict";var e,t={4055:(e,t,n)=>{var a=n(4530),r=n.n(a),i=n(1302),l=n(3407),o=n(5697),s=n.n(o);s().shape({live:s().bool.isRequired,status:s().string.isRequired}).isRequired;var c=n(5946),d=n.n(c);const u=({name:e,component:t,className:n,duration:a,children:i})=>r().createElement(d(),{component:t,transitionEnterTimeout:a,transitionLeaveTimeout:a,transitionName:`c-transition-${e}`,className:n},i);u.propTypes={name:s().oneOf(["push","pop"]).isRequired,component:s().string,className:s().string,duration:s().number,children:s().node},u.defaultProps={component:"div",children:null,className:null,duration:210};var m=n(7107),p=n(5781),g=n(5292),f=n(9408);const h=(e,t=!("true"===e.getAttribute("aria-expanded")))=>{const n=document.querySelector(`#${e.getAttribute("aria-controls")}`);n&&(e.setAttribute("aria-expanded",`${t}`),t?n.removeAttribute("hidden"):"onbeforematch"in document.body?n.setAttribute("hidden","until-found"):n.setAttribute("hidden",""),e.dispatchEvent(new CustomEvent("commentAnchorVisibilityChange",{bubbles:!0})),e.dispatchEvent(new CustomEvent("wagtail:panel-toggle",{bubbles:!0,cancelable:!1,detail:{expanded:t}})))};function b(e){const t=e.closest("[data-panel]"),n=document.querySelector(`#${e.getAttribute("aria-controls")}`);if(!n||!t||t.collapsibleInitialised)return;t.collapsibleInitialised=!0;const a=h.bind(null,e),r=t.classList.contains("collapsed"),i=n.querySelector('[aria-invalid="true"], .error, .w-field--error'),l=r&&!i;l&&a(!1),e.addEventListener("click",a.bind(null,void 0));const o=t.querySelector("[data-panel-heading]");o&&o.addEventListener("click",a.bind(null,void 0)),n.addEventListener("beforematch",a.bind(null,!0)),e.dispatchEvent(new CustomEvent("wagtail:panel-init",{bubbles:!0,cancelable:!1,detail:{expanded:!l}}))}var v=n(7858),E=n.n(v),y=n(9437);const w=({expanded:e,floating:t,insideMinimap:n,onClick:a})=>r().createElement("button",{type:"button","aria-expanded":e,onClick:a,className:`button button-small button-secondary w-minimap__collapse-all ${t?"w-minimap__collapse-all--floating":""} ${n?"w-minimap__collapse-all--inside":""}`},r().createElement(i.Z,{name:e?"collapse-up":"collapse-down"}),e?(0,f.ih)("Collapse all"):(0,f.ih)("Expand all")),S=r().createElement("span",{className:"w-required-mark"},"*"),x=({item:e,intersects:t,expanded:n,onClick:a})=>{const{href:l,label:o,icon:s,required:c,errorCount:d,level:u}=e,m=d>0,p=(0,f.qP)("%(num)s error","%(num)s errors",d).replace("%(num)s",`${d}`),g=o.length>22?`${o.substring(0,22)}…`:o;return r().createElement("a",{href:l,className:`w-minimap-item w-minimap-item--${u} ${t?"w-minimap-item--active":""} ${m?"w-minimap-item--error":""}`,onClick:a.bind(null,e),"aria-current":t,tabIndex:n?void 0:-1,"aria-describedby":n?void 0:"w-minimap-toggle"},m?r().createElement("div",{className:"w-minimap-item__errors","aria-label":p},d):null,r().createElement(i.Z,{name:"minus",className:"w-minimap-item__placeholder"}),"h1"!==u&&"h2"!==u?r().createElement(i.Z,{name:s,className:"w-minimap-item__icon"}):null,r().createElement("span",{className:"w-minimap-item__label"},r().createElement("span",{className:"w-minimap-item__text"},g),c?S:null))},q={root:null,rootMargin:"-50px 0px -70px 0px",threshold:.1},L=(e,{target:t,isIntersecting:n})=>(e[`#${t.closest("[data-panel]")?.id}`||""]=n,e),A=({container:e,anchorsContainer:t,links:n,onUpdate:l,toggleAllPanels:o})=>{const s=(0,a.useMemo)((()=>(()=>{let e="false";try{e=localStorage.getItem("wagtail:minimap-expanded")||e}catch{}return"true"===e})()),[]),[c,d]=(0,a.useState)(s),u=(0,a.useCallback)(((e=!c)=>{d(e),document.body.classList.toggle("minimap-open",e);try{localStorage.setItem("wagtail:minimap-expanded",e?"true":"false")}catch{}}),[c,d]),[m,p]=(0,a.useState)(!0),[g,b]=(0,a.useState)({}),v=(0,a.useRef)(null),E=(0,a.useRef)({}),S=(0,a.useRef)(null),A=(0,a.useRef)(null),C=(e,t)=>{c||t.preventDefault(),h(e.toggle,!0),u(!0)};return(0,a.useEffect)((()=>{u(s)}),[]),(0,a.useEffect)((()=>{v.current||(v.current=new IntersectionObserver((t=>{E.current=t.reduce(L,{...E.current}),S.current||(S.current=(0,y.D)((e=>{b(e),(e=>{const t=e.querySelectorAll('a[aria-current="true"]');if(0===t.length||e.scrollHeight===e.clientHeight)return;const n=t[0],a=t[t.length-1];let r=e.scrollTop;n&&n.offsetTop<e.scrollTop&&(r=n.offsetTop),a&&a.offsetTop>e.scrollTop+e.offsetHeight&&(r=a.offsetTop-e.offsetHeight+a.offsetHeight),e.scrollTop=r})(A.current)}),100)),S.current(E.current),t.forEach((({target:t})=>{t.closest(".deleted")&&l(e)}))}),q));const t=v.current;return t.disconnect(),n.forEach((({panel:e,toggle:n})=>{const a=e.matches(".w-panel--nested")&&null===e.closest("[data-field]");t.observe(a?n:e)})),()=>{t.disconnect()}}),[n,e]),(0,a.useEffect)((()=>{p(!0)}),[t,p]),r().createElement("div",null,r().createElement(w,{expanded:m,onClick:()=>{p(!m),o(!m)},floating:!0,insideMinimap:c}),r().createElement("div",{className:"w-minimap "+(c?"w-minimap--expanded":"")},r().createElement("div",{className:"w-minimap__header"},r().createElement("button",{id:"w-minimap-toggle",type:"button","aria-expanded":c,onClick:()=>u(!c),className:"w-minimap__toggle","aria-label":(0,f.ih)("Toggle side panel")},r().createElement(i.Z,{name:"expand-right"}))),r().createElement("ol",{className:"w-minimap__list",ref:A},n.map((e=>r().createElement("li",{key:e.href},r().createElement(x,{item:e,intersects:g[e.href],expanded:c,onClick:C}))))),r().createElement("div",{className:"w-minimap__footer"})))},C=e=>{const t=e.closest("[data-panel]"),n=t?.getAttribute("aria-labelledby"),a=t?.querySelector(`#${n}`),r=t?.querySelector("[data-panel-toggle]"),i=e.closest("[data-inline-panel-child].deleted");if(!t||!a||!r||i)return null;const l=a.querySelector("[data-panel-heading-text]")?.textContent||a.textContent?.replace(/\s+\*\s+$/g,"").trim(),o=null!==t.querySelector("[data-panel-required]"),s=r.querySelector("use")?.getAttribute("href")?.replace("#icon-","")||"",c=`h${a.getAttribute("aria-level")||a.tagName[1]||2}`,d=[].slice.call(t.querySelectorAll(".error-message")).filter((e=>e.closest("[data-panel]")===t)).length;return{anchor:e,toggle:r,panel:t,icon:s,label:l||"",href:e.getAttribute("href")||"",required:o,errorCount:d,level:c}},_=e=>{let t=document.body;const n=document.querySelector("[data-tabs]");if(n){const e=n.querySelector('[role="tab"][aria-selected="true"]')?.getAttribute("aria-controls");t=n.querySelector(`#${e}`)||t}const a=t.querySelectorAll("[data-panel-anchor]"),i=[].slice.call(a).map(C).filter(Boolean);E().render(r().createElement(A,{container:e,anchorsContainer:t,links:i,onUpdate:_,toggleAllPanels:e=>{i.forEach(((t,n)=>{0===n&&t.href.includes("title")||h(t.toggle,e)}))}}),e)};window.wagtail.components={Icon:i.Z,Portal:l.Z},document.addEventListener("DOMContentLoaded",(()=>{(0,m.bp)(),(0,m.zN)(),(0,p.U)(),(0,g.W)(),function(){const e=document.querySelector("[data-breadcrumb-next]");if(!e)return;const t=e.closest(e.dataset.headerSelector||"header");if(!t)return;const n=e.querySelector("[data-toggle-breadcrumbs]");if(!n)return;const a=e.querySelectorAll("[data-breadcrumb-item]"),r="w-max-w-4xl";let i=!1,l=!0,o=!1;function s(){a.forEach((e=>{e.classList.remove(r),e.hidden=!0})),n.setAttribute("aria-expanded","false"),n.querySelector("svg use").setAttribute("href","#icon-breadcrumb-expand"),i=!1,o=!1,document.dispatchEvent(new CustomEvent("wagtail:breadcrumbs-collapse"))}function c(){a.forEach((e=>{e.hidden=!1,e.classList.add(r)})),n.setAttribute("aria-expanded","true"),i=!0,document.dispatchEvent(new CustomEvent("wagtail:breadcrumbs-expand"))}n.addEventListener("keydown",(e=>{" "!==e.key&&"Enter"!==e.key||(e.preventDefault(),o||i?s():(c(),o=!0,n.querySelector("svg use").setAttribute("href","#icon-cross")))})),n.addEventListener("click",(()=>{o&&(l=!1,s()),i?(l=!1,o=!0,n.querySelector("svg use").setAttribute("href","#icon-cross")):l&&c()})),n.addEventListener("mouseenter",(()=>{!i&&l&&(i=!0,l=!1,c())})),n.addEventListener("mouseleave",(()=>{l=!0})),t.addEventListener("mouseleave",(()=>{o||s()})),document.addEventListener("keydown",(e=>{"Escape"===e.key&&s()}))}(),function(){const e=document.querySelector("[data-form-side]");if(!e)return;const t="formSideExplorer"in e.dataset,n=document.querySelector("[data-form-side-resize-grip]"),a=document.querySelector("[data-form-side-width-input]"),r=()=>{const t=getComputedStyle(e),n=parseFloat(t.minWidth),a=parseFloat(t.maxWidth),r=parseFloat(t.width),i=a-n;return{minWidth:n,maxWidth:a,width:r,range:i,percentage:(r-n)/i*100}},i=e=>"rtl"===document.documentElement.dir?e:100-e;let l;const o=n=>{clearTimeout(l);const o=document.querySelector("body"),s=document.querySelector(`[data-side-panel-toggle="${n}"]`);if((!n||s)&&(""===n?(e.classList.remove("form-side--open"),e.removeAttribute("aria-labelledby")):(e.classList.add("form-side--open"),e.setAttribute("aria-labelledby",`side-panel-${n}-title`)),document.querySelectorAll("[data-side-panel]").forEach((t=>{const a=t.dataset.sidePanel;if(a===n)t.hidden&&(t.hidden=!1,t.dispatchEvent(new CustomEvent("show")),e.classList.add(`form-side--${a}`),o.classList.add("side-panel-open"));else if(!t.hidden){const r=()=>{t.hidden=!0,t.dispatchEvent(new CustomEvent("hide")),e.classList.remove(`form-side--${a}`)};""===n?(o.classList.remove("side-panel-open"),l=setTimeout(r,500)):r()}})),document.querySelectorAll("[data-side-panel-toggle]").forEach((e=>{e.setAttribute("aria-expanded",e.dataset.sidePanelToggle===n?"true":"false")})),!t)){try{localStorage.setItem("wagtail:side-panel-open",n)}catch(e){}setTimeout((()=>{const{percentage:e}=r();a.value=i(e)}),500)}};document.querySelectorAll("[data-side-panel]").forEach((e=>{e.addEventListener("open",(()=>{o(e.dataset.sidePanel)}))})),document.querySelectorAll("[data-side-panel-toggle]").forEach((e=>{e.addEventListener("click",(()=>{(e=>{const t=!document.querySelector(`[data-side-panel="${e}"]`).hasAttribute("hidden");o(t?"":e)})(e.dataset.sidePanelToggle)}))}));const s=document.querySelector("[data-form-side-close-button]");s instanceof HTMLButtonElement&&s.addEventListener("click",(()=>{o("")}));const c=n=>{const{minWidth:l,maxWidth:o,range:s,width:c}=r(),d=parseInt(Math.max(l,Math.min(n,o)),10)||c,u=(0,f.qP)("%(num)s pixel","%(num)s pixels",d).replace("%(num)s",d);e.parentElement.style.setProperty("--side-panel-width",`${d}px`);const m=(d-l)/s*100;if(a.value=i(m),a.setAttribute("aria-valuetext",u),!t)try{localStorage.setItem("wagtail:side-panel-width",d)}catch(e){}};let d,u;const m=e=>{if(!e.screenX||!d||!u)return;const t="rtl"===document.documentElement.dir?-1:1,n=d-e.screenX;c(u+n*t)},p=e=>{n.releasePointerCapture(e.pointerId),n.removeEventListener("pointermove",m),document.removeEventListener("pointerup",p),document.body.classList.remove("side-panel-resizing")};n.addEventListener("pointerdown",(e=>{0===e.button&&(d=e.screenX,u=r().width,document.body.classList.add("side-panel-resizing"),n.setPointerCapture(e.pointerId),n.addEventListener("pointermove",m),document.addEventListener("pointerup",p))})),a.addEventListener("change",(e=>{const{minWidth:t,range:n}=r(),a=parseInt(e.target.value,10),l=i(a);c(t+n*l/100)})),setTimeout((()=>{try{const e=localStorage.getItem("wagtail:side-panel-open");!t&&e&&o(e),c(localStorage.getItem("wagtail:side-panel-width"))}catch(e){}setTimeout((()=>{e.classList.remove("form-side--initial")}))}))}(),function(e=document.querySelectorAll("[data-panel-toggle]")){e.forEach(b)}()})),window.addEventListener("load",(()=>{!function(e=document.querySelector("[data-panel]:target")){e&&e.scrollIntoView({behavior:"smooth"})}(),((e=document.querySelector("[data-minimap-container]"))=>{if(!e)return;const t=(0,y.D)(_.bind(null,e),100);document.addEventListener("wagtail:tab-changed",t),document.addEventListener("wagtail:panel-init",t);const n=()=>e.style.setProperty("--offset-top",`${e.offsetTop}px`),a=(0,y.D)(n,100);document.addEventListener("resize",a),n(),t(e)})()}))}},n={};function a(e){var r=n[e];if(void 0!==r)return r.exports;var i=n[e]={exports:{}};return t[e](i,i.exports,a),i.exports}a.m=t,e=[],a.O=(t,n,r,i)=>{if(!n){var l=1/0;for(d=0;d<e.length;d++){for(var[n,r,i]=e[d],o=!0,s=0;s<n.length;s++)(!1&i||l>=i)&&Object.keys(a.O).every((e=>a.O[e](n[s])))?n.splice(s--,1):(o=!1,i<l&&(l=i));if(o){e.splice(d--,1);var c=r();void 0!==c&&(t=c)}}return t}i=i||0;for(var d=e.length;d>0&&e[d-1][2]>i;d--)e[d]=e[d-1];e[d]=[n,r,i]},a.n=e=>{var t=e&&e.__esModule?()=>e.default:()=>e;return a.d(t,{a:t}),t},a.d=(e,t)=>{for(var n in t)a.o(t,n)&&!a.o(e,n)&&Object.defineProperty(e,n,{enumerable:!0,get:t[n]})},a.g=function(){if("object"==typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"==typeof window)return window}}(),a.o=(e,t)=>Object.prototype.hasOwnProperty.call(e,t),a.r=e=>{"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},a.j=404,(()=>{var e={404:0};a.O.j=t=>0===e[t];var t=(t,n)=>{var r,i,[l,o,s]=n,c=0;if(l.some((t=>0!==e[t]))){for(r in o)a.o(o,r)&&(a.m[r]=o[r]);if(s)var d=s(a)}for(t&&t(n);c<l.length;c++)i=l[c],a.o(e,i)&&e[i]&&e[i][0](),e[i]=0;return a.O(d)},n=globalThis.webpackChunkwagtail=globalThis.webpackChunkwagtail||[];n.forEach(t.bind(null,0)),n.push=t.bind(null,n.push.bind(n))})();var r=a.O(void 0,[751],(()=>a(4055)));r=a.O(r)})();