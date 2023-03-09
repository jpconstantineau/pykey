"use strict";(self.webpackChunkdocumentation=self.webpackChunkdocumentation||[]).push([[275],{3905:function(e,t,r){r.d(t,{Zo:function(){return c},kt:function(){return h}});var n=r(7294);function i(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function o(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function a(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?o(Object(r),!0).forEach((function(t){i(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):o(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function l(e,t){if(null==e)return{};var r,n,i=function(e,t){if(null==e)return{};var r,n,i={},o=Object.keys(e);for(n=0;n<o.length;n++)r=o[n],t.indexOf(r)>=0||(i[r]=e[r]);return i}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(n=0;n<o.length;n++)r=o[n],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(i[r]=e[r])}return i}var u=n.createContext({}),p=function(e){var t=n.useContext(u),r=t;return e&&(r="function"==typeof e?e(t):a(a({},t),e)),r},c=function(e){var t=p(e.components);return n.createElement(u.Provider,{value:t},e.children)},s={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},d=n.forwardRef((function(e,t){var r=e.components,i=e.mdxType,o=e.originalType,u=e.parentName,c=l(e,["components","mdxType","originalType","parentName"]),d=p(r),h=i,m=d["".concat(u,".").concat(h)]||d[h]||s[h]||o;return r?n.createElement(m,a(a({ref:t},c),{},{components:r})):n.createElement(m,a({ref:t},c))}));function h(e,t){var r=arguments,i=t&&t.mdxType;if("string"==typeof e||i){var o=r.length,a=new Array(o);a[0]=d;var l={};for(var u in t)hasOwnProperty.call(t,u)&&(l[u]=t[u]);l.originalType=e,l.mdxType="string"==typeof e?e:i,a[1]=l;for(var p=2;p<o;p++)a[p]=r[p];return n.createElement.apply(null,a)}return n.createElement.apply(null,r)}d.displayName="MDXCreateElement"},9810:function(e,t,r){r.r(t),r.d(t,{frontMatter:function(){return l},contentTitle:function(){return u},metadata:function(){return p},toc:function(){return c},default:function(){return d}});var n=r(7462),i=r(3366),o=(r(7294),r(3905)),a=["components"],l={id:"wl_setting_up",title:"Setting up Wireless Encoderpad",sidebar_label:"Setting up Wireless Encoderpad"},u=void 0,p={unversionedId:"encoderpad/wl_setting_up",id:"encoderpad/wl_setting_up",title:"Setting up Wireless Encoderpad",description:"The following assumes you have a BlueMicro840 controller.  If yours uses a Xiao or a RP2040, see the other guides.",source:"@site/docs/encoderpad/wl_setting_up.md",sourceDirName:"encoderpad",slug:"/encoderpad/wl_setting_up",permalink:"/docs/encoderpad/wl_setting_up",editUrl:"https://github.com/jpconstantineau/pykey/tree/main/documentation/docs/encoderpad/wl_setting_up.md",tags:[],version:"current",frontMatter:{id:"wl_setting_up",title:"Setting up Wireless Encoderpad",sidebar_label:"Setting up Wireless Encoderpad"},sidebar:"someSidebar",previous:{title:"Setting up Xiao/QT Py Encoderpad",permalink:"/docs/encoderpad/basic_setting_up"},next:{title:"Sleep and Power",permalink:"/docs/testing_hardware/sleep"}},c=[{value:"With CircuitPython and PyKey firmware",id:"with-circuitpython-and-pykey-firmware",children:[{value:"Install CircuitPython",id:"install-circuitpython",children:[],level:3},{value:"Install Core Libraries",id:"install-core-libraries",children:[],level:3},{value:"Install PyKey Library",id:"install-pykey-library",children:[],level:3}],level:2},{value:"Copy the example firmware",id:"copy-the-example-firmware",children:[],level:2},{value:"With KMK",id:"with-kmk",children:[],level:2},{value:"With Arduino",id:"with-arduino",children:[],level:2},{value:"With BlueMicro_BLE",id:"with-bluemicro_ble",children:[],level:2}],s={toc:c};function d(e){var t=e.components,r=(0,i.Z)(e,a);return(0,o.kt)("wrapper",(0,n.Z)({},s,r,{components:t,mdxType:"MDXLayout"}),(0,o.kt)("p",null,"The following assumes you have a BlueMicro840 controller.  If yours uses a Xiao or a RP2040, see the other guides."),(0,o.kt)("h2",{id:"with-circuitpython-and-pykey-firmware"},"With CircuitPython and PyKey firmware"),(0,o.kt)("h3",{id:"install-circuitpython"},"Install CircuitPython"),(0,o.kt)("ul",null,(0,o.kt)("li",{parentName:"ul"},"Go to ",(0,o.kt)("a",{parentName:"li",href:"https://circuitpython.org/board/bluemicro840/"},"CircuitPython.Org Download page")," of the BlueMicro840."),(0,o.kt)("li",{parentName:"ul"},"Download the latest stable release (more recent ones are OK)"),(0,o.kt)("li",{parentName:"ul"},"Put the Blurmicro840 in bootloader mode by double-pressing reset"),(0,o.kt)("li",{parentName:"ul"},'A new drive called "BLUEMICRO" should show up on your computer'),(0,o.kt)("li",{parentName:"ul"},"Copy CircuitPython UF2 file you just downloaded to that drive."),(0,o.kt)("li",{parentName:"ul"},'Once copied, the BlueMicro840 should reset itself and a new drive called "CIRCUITPY" should show up'),(0,o.kt)("li",{parentName:"ul"},"CircuitPython is now installed.  ")),(0,o.kt)("h3",{id:"install-core-libraries"},"Install Core Libraries"),(0,o.kt)("ul",null,(0,o.kt)("li",{parentName:"ul"},"Go to ",(0,o.kt)("a",{parentName:"li",href:"https://circuitpython.org/libraries"},"CircuitPython.Org Libraries page"),"."),(0,o.kt)("li",{parentName:"ul"},"Download the Bundle for Version 7.x"),(0,o.kt)("li",{parentName:"ul"},"Uncompress the bundle"),(0,o.kt)("li",{parentName:"ul"},'Copy the following libraries into the lib folder of the "CIRCUITPY" drive',(0,o.kt)("ul",{parentName:"li"},(0,o.kt)("li",{parentName:"ul"},"adafruit_hid"),(0,o.kt)("li",{parentName:"ul"},"adafruit_ble"),(0,o.kt)("li",{parentName:"ul"},"adafruit_ble_adafruit"),(0,o.kt)("li",{parentName:"ul"},"neopixel.mpy")))),(0,o.kt)("h3",{id:"install-pykey-library"},"Install PyKey Library"),(0,o.kt)("ul",null,(0,o.kt)("li",{parentName:"ul"},"Copy the whole pykey folder from the PyKey ",(0,o.kt)("a",{parentName:"li",href:"https://github.com/jpconstantineau/pykey/tree/main/pykey"},"repo"),' into the root of the "CIRCUITPY" drive')),(0,o.kt)("h2",{id:"copy-the-example-firmware"},"Copy the example firmware"),(0,o.kt)("ul",null,(0,o.kt)("li",{parentName:"ul"},"Go to the example folder of the Pykey ",(0,o.kt)("a",{parentName:"li",href:"https://github.com/jpconstantineau/pykey/tree/main/examples/CNCEncoderPad"},"repo")),(0,o.kt)("li",{parentName:"ul"},"Copy the whole layers folder from the PyKey ",(0,o.kt)("a",{parentName:"li",href:"https://github.com/jpconstantineau/pykey/tree/main/examples/CNCEncoderPad"},"repo"),' into the root of the "CIRCUITPY" drive'),(0,o.kt)("li",{parentName:"ul"},'Copy code.py to the root of the "CIRCUITPY" drive (overwrite the existing one)')),(0,o.kt)("h2",{id:"with-kmk"},"With KMK"),(0,o.kt)("p",null,(0,o.kt)("strong",{parentName:"p"},"Notes:  KMK does not support speaker or the back-lit LEDs of the CNCEncoderpad")),(0,o.kt)("ul",null,(0,o.kt)("li",{parentName:"ul"},"Install CircuitPython as per instructions for PyKey firmware"),(0,o.kt)("li",{parentName:"ul"},"Install core libraries as per instructions for PyKey firmware"),(0,o.kt)("li",{parentName:"ul"},"Copy the whole KMK folder from the KMK_Firmware ",(0,o.kt)("a",{parentName:"li",href:"https://github.com/KMKfw/kmk_firmware/tree/master/kmk"},"repo"),' into the root of the "CIRCUITPY" drive'),(0,o.kt)("li",{parentName:"ul"},'Copy the kb.py from the boards folder into the root of the "CIRCUITPY" drive (not available yet)'),(0,o.kt)("li",{parentName:"ul"},'Copy/rename the CNCEncoperPad.py from the user_keymaps folder to code.py into the root of the "CIRCUITPY" drive (not available yet)')),(0,o.kt)("h2",{id:"with-arduino"},"With Arduino"),(0,o.kt)("h2",{id:"with-bluemicro_ble"},"With BlueMicro_BLE"))}d.isMDXComponent=!0}}]);