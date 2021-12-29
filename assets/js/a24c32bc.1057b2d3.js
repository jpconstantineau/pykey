"use strict";(self.webpackChunkdocumentation=self.webpackChunkdocumentation||[]).push([[538],{3905:function(t,e,a){a.d(e,{Zo:function(){return k},kt:function(){return f}});var r=a(7294);function n(t,e,a){return e in t?Object.defineProperty(t,e,{value:a,enumerable:!0,configurable:!0,writable:!0}):t[e]=a,t}function l(t,e){var a=Object.keys(t);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(t);e&&(r=r.filter((function(e){return Object.getOwnPropertyDescriptor(t,e).enumerable}))),a.push.apply(a,r)}return a}function i(t){for(var e=1;e<arguments.length;e++){var a=null!=arguments[e]?arguments[e]:{};e%2?l(Object(a),!0).forEach((function(e){n(t,e,a[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(a)):l(Object(a)).forEach((function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(a,e))}))}return t}function p(t,e){if(null==t)return{};var a,r,n=function(t,e){if(null==t)return{};var a,r,n={},l=Object.keys(t);for(r=0;r<l.length;r++)a=l[r],e.indexOf(a)>=0||(n[a]=t[a]);return n}(t,e);if(Object.getOwnPropertySymbols){var l=Object.getOwnPropertySymbols(t);for(r=0;r<l.length;r++)a=l[r],e.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(t,a)&&(n[a]=t[a])}return n}var d=r.createContext({}),m=function(t){var e=r.useContext(d),a=e;return t&&(a="function"==typeof t?t(e):i(i({},e),t)),a},k=function(t){var e=m(t.components);return r.createElement(d.Provider,{value:e},t.children)},o={inlineCode:"code",wrapper:function(t){var e=t.children;return r.createElement(r.Fragment,{},e)}},N=r.forwardRef((function(t,e){var a=t.components,n=t.mdxType,l=t.originalType,d=t.parentName,k=p(t,["components","mdxType","originalType","parentName"]),N=m(a),f=n,g=N["".concat(d,".").concat(f)]||N[f]||o[f]||l;return a?r.createElement(g,i(i({ref:e},k),{},{components:a})):r.createElement(g,i({ref:e},k))}));function f(t,e){var a=arguments,n=e&&e.mdxType;if("string"==typeof t||n){var l=a.length,i=new Array(l);i[0]=N;var p={};for(var d in e)hasOwnProperty.call(e,d)&&(p[d]=e[d]);p.originalType=t,p.mdxType="string"==typeof t?t:n,i[1]=p;for(var m=2;m<l;m++)i[m]=a[m];return r.createElement.apply(null,i)}return r.createElement.apply(null,a)}N.displayName="MDXCreateElement"},4234:function(t,e,a){a.r(e),a.d(e,{frontMatter:function(){return p},contentTitle:function(){return d},metadata:function(){return m},toc:function(){return k},default:function(){return N}});var r=a(7462),n=a(3366),l=(a(7294),a(3905)),i=["components"],p={id:"hardware",title:"Choosing Hardware Platform",sidebar_label:"Choosing Hardware Platform"},d=void 0,m={unversionedId:"hardware",id:"hardware",title:"Choosing Hardware Platform",description:"Here is a comparative table to help choose the processor and base hardware to build your keyboard.",source:"@site/docs/hardware.md",sourceDirName:".",slug:"/hardware",permalink:"/docs/hardware",editUrl:"https://github.com/jpconstantineau/pykey/tree/main/documentation/docs/hardware.md",tags:[],version:"current",frontMatter:{id:"hardware",title:"Choosing Hardware Platform",sidebar_label:"Choosing Hardware Platform"},sidebar:"someSidebar",previous:{title:"Getting Started",permalink:"/docs/"},next:{title:"Choosing Firmware Platform",permalink:"/docs/features"}},k=[],o={toc:k};function N(t){var e=t.components,a=(0,n.Z)(t,i);return(0,l.kt)("wrapper",(0,r.Z)({},o,a,{components:e,mdxType:"MDXLayout"}),(0,l.kt)("p",null,"Here is a comparative table to help choose the processor and base hardware to build your keyboard.\nNote that not all features and not all hardware form factors are shown."),(0,l.kt)("table",null,(0,l.kt)("thead",{parentName:"table"},(0,l.kt)("tr",{parentName:"thead"},(0,l.kt)("th",{parentName:"tr",align:null},(0,l.kt)("strong",{parentName:"th"},"Feature")),(0,l.kt)("th",{parentName:"tr",align:"left"},"SAMD21"),(0,l.kt)("th",{parentName:"tr",align:"left"},"SAMD51"),(0,l.kt)("th",{parentName:"tr",align:"left"},"RP2040"),(0,l.kt)("th",{parentName:"tr",align:"left"},"nRF52840"),(0,l.kt)("th",{parentName:"tr",align:"left"},"STM32F4"),(0,l.kt)("th",{parentName:"tr",align:"left"},"ESP32-S2"))),(0,l.kt)("tbody",{parentName:"table"},(0,l.kt)("tr",{parentName:"tbody"},(0,l.kt)("td",{parentName:"tr",align:null},(0,l.kt)("strong",{parentName:"td"},"Processor")),(0,l.kt)("td",{parentName:"tr",align:"left"},"Cortex M0+"),(0,l.kt)("td",{parentName:"tr",align:"left"},"Cortex M4F"),(0,l.kt)("td",{parentName:"tr",align:"left"},"Cortex M0+"),(0,l.kt)("td",{parentName:"tr",align:"left"},"Cortex M4F"),(0,l.kt)("td",{parentName:"tr",align:"left"},"Cortex M4F"),(0,l.kt)("td",{parentName:"tr",align:"left"},"Xtensa LX7")),(0,l.kt)("tr",{parentName:"tbody"},(0,l.kt)("td",{parentName:"tr",align:null},"Speed"),(0,l.kt)("td",{parentName:"tr",align:"left"},"48 MhZ"),(0,l.kt)("td",{parentName:"tr",align:"left"},"120 Mhz"),(0,l.kt)("td",{parentName:"tr",align:"left"},"133MHz"),(0,l.kt)("td",{parentName:"tr",align:"left"},"64 MHz"),(0,l.kt)("td",{parentName:"tr",align:"left"},"168 MHz"),(0,l.kt)("td",{parentName:"tr",align:"left"},"240MHz")),(0,l.kt)("tr",{parentName:"tbody"},(0,l.kt)("td",{parentName:"tr",align:null},"Ram"),(0,l.kt)("td",{parentName:"tr",align:"left"},"32KB"),(0,l.kt)("td",{parentName:"tr",align:"left"},"192KB"),(0,l.kt)("td",{parentName:"tr",align:"left"},"264KB"),(0,l.kt)("td",{parentName:"tr",align:"left"},"256KB"),(0,l.kt)("td",{parentName:"tr",align:"left"},"192KB"),(0,l.kt)("td",{parentName:"tr",align:"left"},"320KB + External")),(0,l.kt)("tr",{parentName:"tbody"},(0,l.kt)("td",{parentName:"tr",align:null},"Base Flash"),(0,l.kt)("td",{parentName:"tr",align:"left"},"256KB"),(0,l.kt)("td",{parentName:"tr",align:"left"},"512KB"),(0,l.kt)("td",{parentName:"tr",align:"left"},"External 2MB"),(0,l.kt)("td",{parentName:"tr",align:"left"},"1MB"),(0,l.kt)("td",{parentName:"tr",align:"left"},"1MB"),(0,l.kt)("td",{parentName:"tr",align:"left"},"External")),(0,l.kt)("tr",{parentName:"tbody"},(0,l.kt)("td",{parentName:"tr",align:null},"Hardware Features"),(0,l.kt)("td",{parentName:"tr",align:"left"}),(0,l.kt)("td",{parentName:"tr",align:"left"}),(0,l.kt)("td",{parentName:"tr",align:"left"},"2 cores, PIO"),(0,l.kt)("td",{parentName:"tr",align:"left"},"BLE"),(0,l.kt)("td",{parentName:"tr",align:"left"}),(0,l.kt)("td",{parentName:"tr",align:"left"},"WiFi")),(0,l.kt)("tr",{parentName:"tbody"},(0,l.kt)("td",{parentName:"tr",align:null},(0,l.kt)("strong",{parentName:"td"},"CircuitPython Core Modules")),(0,l.kt)("td",{parentName:"tr",align:"left"}),(0,l.kt)("td",{parentName:"tr",align:"left"}),(0,l.kt)("td",{parentName:"tr",align:"left"}),(0,l.kt)("td",{parentName:"tr",align:"left"}),(0,l.kt)("td",{parentName:"tr",align:"left"}),(0,l.kt)("td",{parentName:"tr",align:"left"})),(0,l.kt)("tr",{parentName:"tbody"},(0,l.kt)("td",{parentName:"tr",align:null},"_bleio"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u274c"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705")),(0,l.kt)("tr",{parentName:"tbody"},(0,l.kt)("td",{parentName:"tr",align:null},"alarm:"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u274c"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u274c"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705")),(0,l.kt)("tr",{parentName:"tbody"},(0,l.kt)("td",{parentName:"tr",align:null},"analogio:"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705")),(0,l.kt)("tr",{parentName:"tbody"},(0,l.kt)("td",{parentName:"tr",align:null},"board:"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705")),(0,l.kt)("tr",{parentName:"tbody"},(0,l.kt)("td",{parentName:"tr",align:null},"digitalio:"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705")),(0,l.kt)("tr",{parentName:"tbody"},(0,l.kt)("td",{parentName:"tr",align:null},"displayio:"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u274c"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705")),(0,l.kt)("tr",{parentName:"tbody"},(0,l.kt)("td",{parentName:"tr",align:null},"keypad:"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u274c"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705")),(0,l.kt)("tr",{parentName:"tbody"},(0,l.kt)("td",{parentName:"tr",align:null},"neopixel_write:"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705")),(0,l.kt)("tr",{parentName:"tbody"},(0,l.kt)("td",{parentName:"tr",align:null},"pwmio:"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705")),(0,l.kt)("tr",{parentName:"tbody"},(0,l.kt)("td",{parentName:"tr",align:null},"rotaryio:"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u274c"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705")),(0,l.kt)("tr",{parentName:"tbody"},(0,l.kt)("td",{parentName:"tr",align:null},"time:"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705")),(0,l.kt)("tr",{parentName:"tbody"},(0,l.kt)("td",{parentName:"tr",align:null},"touchio:"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705")),(0,l.kt)("tr",{parentName:"tbody"},(0,l.kt)("td",{parentName:"tr",align:null},"usb_hid:"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705"),(0,l.kt)("td",{parentName:"tr",align:"left"},"\u2705")),(0,l.kt)("tr",{parentName:"tbody"},(0,l.kt)("td",{parentName:"tr",align:null},(0,l.kt)("strong",{parentName:"td"},"Hardware Form Factors")),(0,l.kt)("td",{parentName:"tr",align:"left"}),(0,l.kt)("td",{parentName:"tr",align:"left"}),(0,l.kt)("td",{parentName:"tr",align:"left"}),(0,l.kt)("td",{parentName:"tr",align:"left"}),(0,l.kt)("td",{parentName:"tr",align:"left"}),(0,l.kt)("td",{parentName:"tr",align:"left"})),(0,l.kt)("tr",{parentName:"tbody"},(0,l.kt)("td",{parentName:"tr",align:null},"Dongle Form"),(0,l.kt)("td",{parentName:"tr",align:"left"},"Trinkey SAMD21"),(0,l.kt)("td",{parentName:"tr",align:"left"}),(0,l.kt)("td",{parentName:"tr",align:"left"}),(0,l.kt)("td",{parentName:"tr",align:"left"},"nRF52840 Dongle"),(0,l.kt)("td",{parentName:"tr",align:"left"}),(0,l.kt)("td",{parentName:"tr",align:"left"})),(0,l.kt)("tr",{parentName:"tbody"},(0,l.kt)("td",{parentName:"tr",align:null},"5 GPIOs"),(0,l.kt)("td",{parentName:"tr",align:"left"},"Trinket M0"),(0,l.kt)("td",{parentName:"tr",align:"left"}),(0,l.kt)("td",{parentName:"tr",align:"left"}),(0,l.kt)("td",{parentName:"tr",align:"left"}),(0,l.kt)("td",{parentName:"tr",align:"left"}),(0,l.kt)("td",{parentName:"tr",align:"left"})),(0,l.kt)("tr",{parentName:"tbody"},(0,l.kt)("td",{parentName:"tr",align:null},"11 GPIOs"),(0,l.kt)("td",{parentName:"tr",align:"left"},"QT Py, Seeeduino XIAO"),(0,l.kt)("td",{parentName:"tr",align:"left"}),(0,l.kt)("td",{parentName:"tr",align:"left"},"QT Py RP2040"),(0,l.kt)("td",{parentName:"tr",align:"left"}),(0,l.kt)("td",{parentName:"tr",align:"left"}),(0,l.kt)("td",{parentName:"tr",align:"left"})),(0,l.kt)("tr",{parentName:"tbody"},(0,l.kt)("td",{parentName:"tr",align:null},"18 GPIOs"),(0,l.kt)("td",{parentName:"tr",align:"left"}),(0,l.kt)("td",{parentName:"tr",align:"left"}),(0,l.kt)("td",{parentName:"tr",align:"left"},"Pro Micro RP2040"),(0,l.kt)("td",{parentName:"tr",align:"left"},"BlueMicro840, Nice!Nano"),(0,l.kt)("td",{parentName:"tr",align:"left"}),(0,l.kt)("td",{parentName:"tr",align:"left"})),(0,l.kt)("tr",{parentName:"tbody"},(0,l.kt)("td",{parentName:"tr",align:null},"21 GPIOs"),(0,l.kt)("td",{parentName:"tr",align:"left"},"Feather M0 Express"),(0,l.kt)("td",{parentName:"tr",align:"left"},"Feather M4 Express"),(0,l.kt)("td",{parentName:"tr",align:"left"},"Feather RP2040"),(0,l.kt)("td",{parentName:"tr",align:"left"},"Feather nRF52840 Express"),(0,l.kt)("td",{parentName:"tr",align:"left"},"Feather STM32F405 Express"),(0,l.kt)("td",{parentName:"tr",align:"left"})),(0,l.kt)("tr",{parentName:"tbody"},(0,l.kt)("td",{parentName:"tr",align:null},"21-23 GPIOs"),(0,l.kt)("td",{parentName:"tr",align:"left"},"ItsyBitsy M0 Express"),(0,l.kt)("td",{parentName:"tr",align:"left"},"ItsyBitsy M4 Express"),(0,l.kt)("td",{parentName:"tr",align:"left"},"ItsyBitsy RP2040"),(0,l.kt)("td",{parentName:"tr",align:"left"},"ItsyBitsy nRF52840 Express"),(0,l.kt)("td",{parentName:"tr",align:"left"}),(0,l.kt)("td",{parentName:"tr",align:"left"})),(0,l.kt)("tr",{parentName:"tbody"},(0,l.kt)("td",{parentName:"tr",align:null},"26 GPIOs"),(0,l.kt)("td",{parentName:"tr",align:"left"}),(0,l.kt)("td",{parentName:"tr",align:"left"}),(0,l.kt)("td",{parentName:"tr",align:"left"},"Pi Pico"),(0,l.kt)("td",{parentName:"tr",align:"left"}),(0,l.kt)("td",{parentName:"tr",align:"left"}),(0,l.kt)("td",{parentName:"tr",align:"left"})),(0,l.kt)("tr",{parentName:"tbody"},(0,l.kt)("td",{parentName:"tr",align:null},"Finished Products"),(0,l.kt)("td",{parentName:"tr",align:"left"}),(0,l.kt)("td",{parentName:"tr",align:"left"},"NeoTrellis M4"),(0,l.kt)("td",{parentName:"tr",align:"left"},"MacroPad RP2040, Keybow 2040, PyKey60, EncoderPad RP2040"),(0,l.kt)("td",{parentName:"tr",align:"left"},"M60 Mechanical Keyboard"),(0,l.kt)("td",{parentName:"tr",align:"left"}),(0,l.kt)("td",{parentName:"tr",align:"left"})))),(0,l.kt)("p",null,"Comments:"),(0,l.kt)("ul",null,(0,l.kt)("li",{parentName:"ul"},"STM boards do not have rotaryio implemented yet."),(0,l.kt)("li",{parentName:"ul"},"Due to limited RAM and flash size, CircuitPython builds for SAMD21 boards only include the bare minimum core modules."),(0,l.kt)("li",{parentName:"ul"},"Low clock speeds for nRF52840 allows for lower power usage and longer battery life for BLE applications.")))}N.isMDXComponent=!0}}]);