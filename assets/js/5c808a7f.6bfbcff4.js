"use strict";(self.webpackChunkdocumentation=self.webpackChunkdocumentation||[]).push([[662],{3905:function(e,t,r){r.d(t,{Zo:function(){return p},kt:function(){return m}});var n=r(7294);function i(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function o(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function a(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?o(Object(r),!0).forEach((function(t){i(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):o(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function c(e,t){if(null==e)return{};var r,n,i=function(e,t){if(null==e)return{};var r,n,i={},o=Object.keys(e);for(n=0;n<o.length;n++)r=o[n],t.indexOf(r)>=0||(i[r]=e[r]);return i}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(n=0;n<o.length;n++)r=o[n],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(i[r]=e[r])}return i}var l=n.createContext({}),d=function(e){var t=n.useContext(l),r=t;return e&&(r="function"==typeof e?e(t):a(a({},t),e)),r},p=function(e){var t=d(e.components);return n.createElement(l.Provider,{value:t},e.children)},u={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},s=n.forwardRef((function(e,t){var r=e.components,i=e.mdxType,o=e.originalType,l=e.parentName,p=c(e,["components","mdxType","originalType","parentName"]),s=d(r),m=i,h=s["".concat(l,".").concat(m)]||s[m]||u[m]||o;return r?n.createElement(h,a(a({ref:t},p),{},{components:r})):n.createElement(h,a({ref:t},p))}));function m(e,t){var r=arguments,i=t&&t.mdxType;if("string"==typeof e||i){var o=r.length,a=new Array(o);a[0]=s;var c={};for(var l in t)hasOwnProperty.call(t,l)&&(c[l]=t[l]);c.originalType=e,c.mdxType="string"==typeof e?e:i,a[1]=c;for(var d=2;d<o;d++)a[d]=r[d];return n.createElement.apply(null,a)}return n.createElement.apply(null,r)}s.displayName="MDXCreateElement"},9476:function(e,t,r){r.r(t),r.d(t,{frontMatter:function(){return c},contentTitle:function(){return l},metadata:function(){return d},toc:function(){return p},default:function(){return s}});var n=r(7462),i=r(3366),o=(r(7294),r(3905)),a=["components"],c={id:"gridmx47",title:"Raspberry Pi Pico 47-keys Ortholinear Keyboard",sidebar_label:"4x12 Ortholinear keyboard"},l=void 0,d={unversionedId:"hardware/gridmx47",id:"hardware/gridmx47",title:"Raspberry Pi Pico 47-keys Ortholinear Keyboard",description:"Coming Soon!",source:"@site/docs/hardware/gridmx47.md",sourceDirName:"hardware",slug:"/hardware/gridmx47",permalink:"/docs/hardware/gridmx47",editUrl:"https://github.com/jpconstantineau/pykey/tree/main/documentation/docs/hardware/gridmx47.md",tags:[],version:"current",frontMatter:{id:"gridmx47",title:"Raspberry Pi Pico 47-keys Ortholinear Keyboard",sidebar_label:"4x12 Ortholinear keyboard"},sidebar:"someSidebar",previous:{title:"5x5 Macropad",permalink:"/docs/hardware/5x5macropad"},next:{title:"4x12 Staggered Keyboard",permalink:"/docs/hardware/offsetmx43"}},p=[{value:"Description",id:"description",children:[],level:2},{value:"Entering the Bootloader &amp; flashing CircuitPython",id:"entering-the-bootloader--flashing-circuitpython",children:[],level:2},{value:"Firmware",id:"firmware",children:[],level:2},{value:"Pinout",id:"pinout",children:[],level:2},{value:"PCB",id:"pcb",children:[{value:"Top of PCB",id:"top-of-pcb",children:[],level:3},{value:"Bottom of PCB",id:"bottom-of-pcb",children:[],level:3}],level:2},{value:"Schematic",id:"schematic",children:[],level:2},{value:"Build Guide",id:"build-guide",children:[],level:2}],u={toc:p};function s(e){var t=e.components,r=(0,i.Z)(e,a);return(0,o.kt)("wrapper",(0,n.Z)({},u,r,{components:t,mdxType:"MDXLayout"}),(0,o.kt)("p",null,"Coming Soon!"),(0,o.kt)("p",null,"Buy it on ",(0,o.kt)("a",{parentName:"p",href:"https://www.tindie.com/products/jpconstantineau/raspberry-pi-pico-4x12-ortho-keyboard/"},"Tindie")),(0,o.kt)("h2",{id:"description"},"Description"),(0,o.kt)("h2",{id:"entering-the-bootloader--flashing-circuitpython"},"Entering the Bootloader & flashing CircuitPython"),(0,o.kt)("ul",null,(0,o.kt)("li",{parentName:"ul"},(0,o.kt)("a",{parentName:"li",href:"https://circuitpython.org/board/raspberry_pi_pico/"},"Download CircuitPython UF2 file")),(0,o.kt)("li",{parentName:"ul"},"Enter the bootloader by pressing the reset switch while holding Boot switch pressed"),(0,o.kt)("li",{parentName:"ul"},"Copy the UF2 file to the RPI drive.")),(0,o.kt)("h2",{id:"firmware"},"Firmware"),(0,o.kt)("h2",{id:"pinout"},"Pinout"),(0,o.kt)("h2",{id:"pcb"},"PCB"),(0,o.kt)("h3",{id:"top-of-pcb"},"Top of PCB"),(0,o.kt)("img",{src:"http://pykey.jpconstantineau.com/img/mx47top.svg",width:"700"}),(0,o.kt)("h3",{id:"bottom-of-pcb"},"Bottom of PCB"),(0,o.kt)("img",{src:"http://pykey.jpconstantineau.com/img/mx47bottom.svg",width:"700"}),(0,o.kt)("h2",{id:"schematic"},"Schematic"),(0,o.kt)("h2",{id:"build-guide"},"Build Guide"),(0,o.kt)("p",null,(0,o.kt)("a",{parentName:"p",href:"https://www.tindie.com/stores/jpconstantineau/?ref=offsite_badges&utm_source=sellers_jpconstantineau&utm_medium=badges&utm_campaign=badge_medium"},(0,o.kt)("img",{parentName:"a",src:"https://d2ss6ovg47m0r5.cloudfront.net/badges/tindie-mediums.png",alt:"I sell on Tindie"}))))}s.isMDXComponent=!0}}]);