"use strict";(self.webpackChunkdocumentation=self.webpackChunkdocumentation||[]).push([[881],{3905:function(e,t,n){n.d(t,{Zo:function(){return u},kt:function(){return m}});var r=n(7294);function a(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function o(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function i(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?o(Object(n),!0).forEach((function(t){a(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):o(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function c(e,t){if(null==e)return{};var n,r,a=function(e,t){if(null==e)return{};var n,r,a={},o=Object.keys(e);for(r=0;r<o.length;r++)n=o[r],t.indexOf(n)>=0||(a[n]=e[n]);return a}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(r=0;r<o.length;r++)n=o[r],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(a[n]=e[n])}return a}var s=r.createContext({}),l=function(e){var t=r.useContext(s),n=t;return e&&(n="function"==typeof e?e(t):i(i({},t),e)),n},u=function(e){var t=l(e.components);return r.createElement(s.Provider,{value:t},e.children)},d={inlineCode:"code",wrapper:function(e){var t=e.children;return r.createElement(r.Fragment,{},t)}},p=r.forwardRef((function(e,t){var n=e.components,a=e.mdxType,o=e.originalType,s=e.parentName,u=c(e,["components","mdxType","originalType","parentName"]),p=l(n),m=a,f=p["".concat(s,".").concat(m)]||p[m]||d[m]||o;return n?r.createElement(f,i(i({ref:t},u),{},{components:n})):r.createElement(f,i({ref:t},u))}));function m(e,t){var n=arguments,a=t&&t.mdxType;if("string"==typeof e||a){var o=n.length,i=new Array(o);i[0]=p;var c={};for(var s in t)hasOwnProperty.call(t,s)&&(c[s]=t[s]);c.originalType=e,c.mdxType="string"==typeof e?e:a,i[1]=c;for(var l=2;l<o;l++)i[l]=n[l];return r.createElement.apply(null,i)}return r.createElement.apply(null,n)}p.displayName="MDXCreateElement"},7896:function(e,t,n){n.r(t),n.d(t,{frontMatter:function(){return c},contentTitle:function(){return s},metadata:function(){return l},toc:function(){return u},default:function(){return p}});var r=n(7462),a=n(3366),o=(n(7294),n(3905)),i=["components"],c={id:"keymatrix",title:"Key Matrix",sidebar_label:"Key Matrix"},s=void 0,l={unversionedId:"testing_hardware/keymatrix",id:"testing_hardware/keymatrix",title:"Key Matrix",description:"Matrix Definition",source:"@site/docs/testing_hardware/keymatrix.md",sourceDirName:"testing_hardware",slug:"/testing_hardware/keymatrix",permalink:"/docs/testing_hardware/keymatrix",editUrl:"https://github.com/jpconstantineau/pykey/tree/main/documentation/docs/testing_hardware/keymatrix.md",tags:[],version:"current",frontMatter:{id:"keymatrix",title:"Key Matrix",sidebar_label:"Key Matrix"},sidebar:"someSidebar",previous:{title:"Analog I/O",permalink:"/docs/testing_hardware/analog"},next:{title:"Finding Buttons",permalink:"/docs/testing_hardware/findingbuttons"}},u=[{value:"Matrix Definition",id:"matrix-definition",children:[],level:2},{value:"Test Program",id:"test-program",children:[],level:2}],d={toc:u};function p(e){var t=e.components,c=(0,a.Z)(e,i);return(0,o.kt)("wrapper",(0,r.Z)({},d,c,{components:t,mdxType:"MDXLayout"}),(0,o.kt)("h2",{id:"matrix-definition"},"Matrix Definition"),(0,o.kt)("p",null,"Most keyboards use a matrix of columns and rows to scan each key.  You will need to refer to the keyboard schematic to identify how many columns and rows your keyboard uses for it's scanning matrix.  The scanning matrix may differ from the keyboard layout.  For example, a 4x12 matrix uses 16 GPIOs and allows for 48 keys to be scanned.  A 8x8 matrix also uses 16 GPIOs but will allow 64 keys to be scanned."),(0,o.kt)("p",null,(0,o.kt)("img",{alt:"keyboard matrix",src:n(5178).Z})),(0,o.kt)("p",null,"Next, we need to identify how each row and column are mapped to the microntroller on board of the nRF52 module you use.  Since most DIY keyboards use the Arduino Pro Micro as its controller, we are using such an example."),(0,o.kt)("p",null,(0,o.kt)("img",{alt:"GPIO Mapping",src:n(6981).Z})),(0,o.kt)("p",null,"With the information from both the keyboard and controller schamatics, we can map each row and column to the GPIO and define the configuration needed."),(0,o.kt)("h2",{id:"test-program"},"Test Program"),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre",className:"language-python"},"import board\nimport keypad\n\n# Switch Matrix Setup.\nkeys = keypad.KeyMatrix(\n    row_pins=(board.P1_11, board.P0_03, board.P0_28, board.P1_13),\n    column_pins=(board.P0_02, board.P0_29, board.P0_30, board.P0_26),\n    columns_to_anodes=True,\n)\n\n\nwhile True:\n    key_event = keys.events.get()\n    if key_event:\n        print(key_event)\n\n")),(0,o.kt)("p",null,"Make sure you are connected via a serial connection to the controller. (Connect to REPL)\nBy pressing and releasing each key, you will see the press and release events as well as which key number generated the event."),(0,o.kt)("p",null,"Test each key and validate that they each work.  If none work, change ",(0,o.kt)("inlineCode",{parentName:"p"},"columns_to_anodes")," and test again. If a specific row or column do not work, verify if the GPIO configured is correct."))}p.isMDXComponent=!0},6981:function(e,t,n){t.Z=n.p+"assets/images/gpiomapping-1af4eb50266b518383edb2b41c9aa66f.png"},5178:function(e,t,n){t.Z=n.p+"assets/images/keyboardmatrix-d03a4672fcf57289bf914c6e16df4929.png"}}]);