(window.webpackJsonp=window.webpackJsonp||[]).push([[22],{78:function(n,e,t){"use strict";t.r(e),t.d(e,"frontMatter",(function(){return a})),t.d(e,"metadata",(function(){return u})),t.d(e,"rightToc",(function(){return c})),t.d(e,"default",(function(){return s}));var r=t(2),i=t(6),o=(t(0),t(92)),a={id:"findingbuttons",title:"Finding Buttons",sidebar_label:"Finding Buttons"},u={unversionedId:"testing_hardware/findingbuttons",id:"testing_hardware/findingbuttons",isDocsHomePage:!1,title:"Finding Buttons",description:"The following program will list the button GPIO names when you press the buttons.",source:"@site/docs/testing_hardware/findingbuttons.md",slug:"/testing_hardware/findingbuttons",permalink:"/docs/testing_hardware/findingbuttons",editUrl:"https://github.com/jpconstantineau/pykey/tree/main/documentation/docs/testing_hardware/findingbuttons.md",version:"current",sidebar_label:"Finding Buttons",sidebar:"someSidebar",previous:{title:"Key Matrix",permalink:"/docs/testing_hardware/keymatrix"},next:{title:"Finding Key Matrix",permalink:"/docs/testing_hardware/findingmatrix"}},c=[],p={rightToc:c};function s(n){var e=n.components,t=Object(i.a)(n,["components"]);return Object(o.b)("wrapper",Object(r.a)({},p,t,{components:e,mdxType:"MDXLayout"}),Object(o.b)("p",null,"The following program will list the button GPIO names when you press the buttons.\nThis assumes that the buttons have one side grounded and the other connected to the controller."),Object(o.b)("p",null,"With this list you will have a starting point on how to configure the key scanning routines."),Object(o.b)("pre",null,Object(o.b)("code",Object(r.a)({parentName:"pre"},{className:"language-python"}),"import board\nimport time\nfrom microcontroller import Pin\nfrom digitalio import DigitalInOut, Direction, Pull\n\ndef get_unique_pins():\n    exclude = ['NEOPIXEL', 'APA102_MOSI', 'APA102_SCK']\n    pins = [pin for pin in [\n        getattr(board, p) for p in dir(board) if p not in exclude]\n            if isinstance(pin, Pin)]\n    unique = []\n    for p in pins:\n        if p not in unique:\n            unique.append(p)\n    return unique\n\npins = []\n\nfor scl_pin in get_unique_pins():\n        pin = DigitalInOut(scl_pin)\n        pin.direction = Direction.INPUT\n        pin.pull = Pull.UP\n        if pin not in pins:\n            pins.append([scl_pin, pin])\n\nwhile True:\n    for item in pins:\n        if not item[1].value :\n            print(item[0])\n    time.sleep(0.2)\n")))}s.isMDXComponent=!0},92:function(n,e,t){"use strict";t.d(e,"a",(function(){return l})),t.d(e,"b",(function(){return b}));var r=t(0),i=t.n(r);function o(n,e,t){return e in n?Object.defineProperty(n,e,{value:t,enumerable:!0,configurable:!0,writable:!0}):n[e]=t,n}function a(n,e){var t=Object.keys(n);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(n);e&&(r=r.filter((function(e){return Object.getOwnPropertyDescriptor(n,e).enumerable}))),t.push.apply(t,r)}return t}function u(n){for(var e=1;e<arguments.length;e++){var t=null!=arguments[e]?arguments[e]:{};e%2?a(Object(t),!0).forEach((function(e){o(n,e,t[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(n,Object.getOwnPropertyDescriptors(t)):a(Object(t)).forEach((function(e){Object.defineProperty(n,e,Object.getOwnPropertyDescriptor(t,e))}))}return n}function c(n,e){if(null==n)return{};var t,r,i=function(n,e){if(null==n)return{};var t,r,i={},o=Object.keys(n);for(r=0;r<o.length;r++)t=o[r],e.indexOf(t)>=0||(i[t]=n[t]);return i}(n,e);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(n);for(r=0;r<o.length;r++)t=o[r],e.indexOf(t)>=0||Object.prototype.propertyIsEnumerable.call(n,t)&&(i[t]=n[t])}return i}var p=i.a.createContext({}),s=function(n){var e=i.a.useContext(p),t=e;return n&&(t="function"==typeof n?n(e):u(u({},e),n)),t},l=function(n){var e=s(n.components);return i.a.createElement(p.Provider,{value:e},n.children)},d={inlineCode:"code",wrapper:function(n){var e=n.children;return i.a.createElement(i.a.Fragment,{},e)}},f=i.a.forwardRef((function(n,e){var t=n.components,r=n.mdxType,o=n.originalType,a=n.parentName,p=c(n,["components","mdxType","originalType","parentName"]),l=s(t),f=r,b=l["".concat(a,".").concat(f)]||l[f]||d[f]||o;return t?i.a.createElement(b,u(u({ref:e},p),{},{components:t})):i.a.createElement(b,u({ref:e},p))}));function b(n,e){var t=arguments,r=e&&e.mdxType;if("string"==typeof n||r){var o=t.length,a=new Array(o);a[0]=f;var u={};for(var c in e)hasOwnProperty.call(e,c)&&(u[c]=e[c]);u.originalType=n,u.mdxType="string"==typeof n?n:r,a[1]=u;for(var p=2;p<o;p++)a[p]=t[p];return i.a.createElement.apply(null,a)}return i.a.createElement.apply(null,t)}f.displayName="MDXCreateElement"}}]);