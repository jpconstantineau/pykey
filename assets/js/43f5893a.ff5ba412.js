"use strict";(self.webpackChunkdocumentation=self.webpackChunkdocumentation||[]).push([[584],{3905:function(n,e,o){o.d(e,{Zo:function(){return l},kt:function(){return m}});var t=o(7294);function r(n,e,o){return e in n?Object.defineProperty(n,e,{value:o,enumerable:!0,configurable:!0,writable:!0}):n[e]=o,n}function i(n,e){var o=Object.keys(n);if(Object.getOwnPropertySymbols){var t=Object.getOwnPropertySymbols(n);e&&(t=t.filter((function(e){return Object.getOwnPropertyDescriptor(n,e).enumerable}))),o.push.apply(o,t)}return o}function a(n){for(var e=1;e<arguments.length;e++){var o=null!=arguments[e]?arguments[e]:{};e%2?i(Object(o),!0).forEach((function(e){r(n,e,o[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(n,Object.getOwnPropertyDescriptors(o)):i(Object(o)).forEach((function(e){Object.defineProperty(n,e,Object.getOwnPropertyDescriptor(o,e))}))}return n}function s(n,e){if(null==n)return{};var o,t,r=function(n,e){if(null==n)return{};var o,t,r={},i=Object.keys(n);for(t=0;t<i.length;t++)o=i[t],e.indexOf(o)>=0||(r[o]=n[o]);return r}(n,e);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(n);for(t=0;t<i.length;t++)o=i[t],e.indexOf(o)>=0||Object.prototype.propertyIsEnumerable.call(n,o)&&(r[o]=n[o])}return r}var p=t.createContext({}),c=function(n){var e=t.useContext(p),o=e;return n&&(o="function"==typeof n?n(e):a(a({},e),n)),o},l=function(n){var e=c(n.components);return t.createElement(p.Provider,{value:e},n.children)},d={inlineCode:"code",wrapper:function(n){var e=n.children;return t.createElement(t.Fragment,{},e)}},u=t.forwardRef((function(n,e){var o=n.components,r=n.mdxType,i=n.originalType,p=n.parentName,l=s(n,["components","mdxType","originalType","parentName"]),u=c(o),m=r,f=u["".concat(p,".").concat(m)]||u[m]||d[m]||i;return o?t.createElement(f,a(a({ref:e},l),{},{components:o})):t.createElement(f,a({ref:e},l))}));function m(n,e){var o=arguments,r=e&&e.mdxType;if("string"==typeof n||r){var i=o.length,a=new Array(i);a[0]=u;var s={};for(var p in e)hasOwnProperty.call(e,p)&&(s[p]=e[p]);s.originalType=n,s.mdxType="string"==typeof n?n:r,a[1]=s;for(var c=2;c<i;c++)a[c]=o[c];return t.createElement.apply(null,a)}return t.createElement.apply(null,o)}u.displayName="MDXCreateElement"},5435:function(n,e,o){o.r(e),o.d(e,{frontMatter:function(){return s},contentTitle:function(){return p},metadata:function(){return c},toc:function(){return l},default:function(){return u}});var t=o(7462),r=o(3366),i=(o(7294),o(3905)),a=["components"],s={id:"encoders",title:"Rotary Encoders",sidebar_label:"Rotary Encoders"},p=void 0,c={unversionedId:"testing_hardware/encoders",id:"testing_hardware/encoders",title:"Rotary Encoders",description:"Rotary Encoder",source:"@site/docs/testing_hardware/encoder.md",sourceDirName:"testing_hardware",slug:"/testing_hardware/encoders",permalink:"/docs/testing_hardware/encoders",editUrl:"https://github.com/jpconstantineau/pykey/tree/main/documentation/docs/testing_hardware/encoder.md",tags:[],version:"current",frontMatter:{id:"encoders",title:"Rotary Encoders",sidebar_label:"Rotary Encoders"},sidebar:"someSidebar",previous:{title:"Basic GPIOs",permalink:"/docs/testing_hardware/basic"},next:{title:"Analog I/O",permalink:"/docs/testing_hardware/analog"}},l=[{value:"Rotary Encoder",id:"rotary-encoder",children:[],level:2},{value:"Basic Test",id:"basic-test",children:[],level:2},{value:"miniMacro5 - 5 Encoders Test",id:"minimacro5---5-encoders-test",children:[],level:2}],d={toc:l};function u(n){var e=n.components,o=(0,r.Z)(n,a);return(0,i.kt)("wrapper",(0,t.Z)({},d,o,{components:e,mdxType:"MDXLayout"}),(0,i.kt)("h2",{id:"rotary-encoder"},"Rotary Encoder"),(0,i.kt)("p",null,"For basic information on rotary encoders, refer to this great tutorial from ",(0,i.kt)("a",{parentName:"p",href:"https://learn.adafruit.com/rotary-encoder"},"Adafruit")),(0,i.kt)("h2",{id:"basic-test"},"Basic Test"),(0,i.kt)("p",null,"Try the example below by changing the pin definition"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"},"import board\nimport rotaryio\n\n# Encoder Setup\nencoder = rotaryio.IncrementalEncoder(board.P0_26, board.P0_06)\nlast_position = None\nwhile True:\n    position = encoder.position\n    if last_position is None or position != last_position:\n        print(position)\n    last_position = position\n\n")),(0,i.kt)("p",null,"If you want to see an example of how to read a rotary encoder, see this ",(0,i.kt)("a",{parentName:"p",href:"https://youtu.be/4BNkuLonIVM?list=PLjF7R1fz_OOWFqZfqW9jlvQSIUmwn9lWr"},"video")),(0,i.kt)("h2",{id:"minimacro5---5-encoders-test"},"miniMacro5 - 5 Encoders Test"),(0,i.kt)("p",null,"Note: CircuitPython seems to only support up to 4 rotary encoders for the nRF52.\nInternally, it uses 2 GPIOTE channels to monitor the encoder and trigger updates when rotation is happening.  Since the nRF52840 has 8 GPIOTE channels, up to 4 rotary encoders are available.\nOther features may use GPIOTE channels and as such, the maximum number of rotary encoders which can be initialized may be less.  If you want to see more information on how it's implemented, go see the updated files for this ",(0,i.kt)("a",{parentName:"p",href:"https://github.com/adafruit/circuitpython/pull/5253"},"Pull request")),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"},"import board\nimport rotaryio\n\n# Encoder Setup\nencoder1 = rotaryio.IncrementalEncoder(board.P0_26, board.P0_06)\nencoder2 = rotaryio.IncrementalEncoder(board.P0_08, board.P0_29)\nencoder3 = rotaryio.IncrementalEncoder(board.P0_15, board.P0_02)\nencoder4 = rotaryio.IncrementalEncoder(board.P0_17, board.P0_20)\nencoder5 = rotaryio.IncrementalEncoder(board.P0_09, board.P0_13)\n\nlast_position1 = None\nlast_position2 = None\nlast_position3 = None\nlast_position4 = None\nlast_position5 = None\nwhile True:\n    position1 = encoder1.position\n    position2 = encoder2.position\n    position3 = encoder3.position\n    position4 = encoder4.position\n    position5 = encoder5.position\n    if last_position1 is None or position1 != last_position1:\n        print(position1, position2, position3, position4, position5)\n    if last_position2 is None or position2 != last_position2:\n        print(position1, position2, position3, position4, position5)\n    if last_position3 is None or position3 != last_position3:\n        print(position1, position2, position3, position4, position5)\n    if last_position4 is None or position4 != last_position4:\n        print(position1, position2, position3, position4, position5)\n    if last_position5 is None or position5 != last_position5:\n        print(position1, position2, position3, position4, position5)\n    last_position1 = position1\n    last_position2 = position2\n    last_position3 = position3\n    last_position4 = position4\n    last_position5 = position5\n")))}u.isMDXComponent=!0}}]);