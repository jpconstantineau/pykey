(window.webpackJsonp=window.webpackJsonp||[]).push([[13],{103:function(e,t,n){"use strict";n.d(t,"a",(function(){return b})),n.d(t,"b",(function(){return m}));var a=n(0),r=n.n(a);function i(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function o(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);t&&(a=a.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,a)}return n}function l(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?o(Object(n),!0).forEach((function(t){i(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):o(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function s(e,t){if(null==e)return{};var n,a,r=function(e,t){if(null==e)return{};var n,a,r={},i=Object.keys(e);for(a=0;a<i.length;a++)n=i[a],t.indexOf(n)>=0||(r[n]=e[n]);return r}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(a=0;a<i.length;a++)n=i[a],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(r[n]=e[n])}return r}var c=r.a.createContext({}),p=function(e){var t=r.a.useContext(c),n=t;return e&&(n="function"==typeof e?e(t):l(l({},t),e)),n},b=function(e){var t=p(e.components);return r.a.createElement(c.Provider,{value:t},e.children)},d={inlineCode:"code",wrapper:function(e){var t=e.children;return r.a.createElement(r.a.Fragment,{},t)}},u=r.a.forwardRef((function(e,t){var n=e.components,a=e.mdxType,i=e.originalType,o=e.parentName,c=s(e,["components","mdxType","originalType","parentName"]),b=p(n),u=a,m=b["".concat(o,".").concat(u)]||b[u]||d[u]||i;return n?r.a.createElement(m,l(l({ref:t},c),{},{components:n})):r.a.createElement(m,l({ref:t},c))}));function m(e,t){var n=arguments,a=t&&t.mdxType;if("string"==typeof e||a){var i=n.length,o=new Array(i);o[0]=u;var l={};for(var s in t)hasOwnProperty.call(t,s)&&(l[s]=t[s]);l.originalType=e,l.mdxType="string"==typeof e?e:a,o[1]=l;for(var c=2;c<i;c++)o[c]=n[c];return r.a.createElement.apply(null,o)}return r.a.createElement.apply(null,n)}u.displayName="MDXCreateElement"},69:function(e,t,n){"use strict";n.r(t),n.d(t,"frontMatter",(function(){return o})),n.d(t,"metadata",(function(){return l})),n.d(t,"rightToc",(function(){return s})),n.d(t,"default",(function(){return p}));var a=n(2),r=n(6),i=(n(0),n(103)),o={id:"sleep",title:"Sleep and Power",sidebar_label:"Sleep and Power"},l={unversionedId:"testing_hardware/sleep",id:"testing_hardware/sleep",isDocsHomePage:!1,title:"Sleep and Power",description:"Current consumption on a BLE keyboard is dependent on how efficient the scanning routine is, how eficient it processes keystrokes, if/how the processor is put on hold, and BLE radio usage.",source:"@site/docs/testing_hardware/sleep.md",slug:"/testing_hardware/sleep",permalink:"/docs/testing_hardware/sleep",editUrl:"https://github.com/jpconstantineau/pykey/tree/main/documentation/docs/testing_hardware/sleep.md",version:"current",sidebar_label:"Sleep and Power",sidebar:"someSidebar",previous:{title:"Sound and Buzzers",permalink:"/docs/testing_hardware/sound"},next:{title:"Libraries Needed",permalink:"/docs/setup/libraries"}},s=[{value:"Normal Power Consumption",id:"normal-power-consumption",children:[]},{value:"Deep Sleep vs Sleeping Beauty (System OFF)",id:"deep-sleep-vs-sleeping-beauty-system-off",children:[]}],c={rightToc:s};function p(e){var t=e.components,n=Object(r.a)(e,["components"]);return Object(i.b)("wrapper",Object(a.a)({},c,n,{components:t,mdxType:"MDXLayout"}),Object(i.b)("p",null,"Current consumption on a BLE keyboard is dependent on how efficient the scanning routine is, how eficient it processes keystrokes, if/how the processor is put on hold, and BLE radio usage."),Object(i.b)("p",null,"Current consumption of the BLE radio is much higher than that of the processor. However, as BLE messages are only occurring at a specific frequency and are not continuous, their impact on a time-averaged basis is not as significant than the running average of the processor running constantly. "),Object(i.b)("p",null,"Reference:"),Object(i.b)("ul",null,Object(i.b)("li",{parentName:"ul"},Object(i.b)("a",Object(a.a)({parentName:"li"},{href:"https://learn.adafruit.com/deep-sleep-with-circuitpython/alarms-and-sleep"}),"Adafruit Learning Guide - CircuitPython Deep Sleep")),Object(i.b)("li",{parentName:"ul"},Object(i.b)("a",Object(a.a)({parentName:"li"},{href:"https://circuitpython.readthedocs.io/en/latest/shared-bindings/alarm/index.html"}),"CircuiPython ReadTheDocs")),Object(i.b)("li",{parentName:"ul"},Object(i.b)("a",Object(a.a)({parentName:"li"},{href:"https://www.youtube.com/watch?v=RGR1rowOaX4&t=795s"}),"Zephyr vs Arduino Power Consumption on the nRF52840 - Youtube Video")),Object(i.b)("li",{parentName:"ul"},Object(i.b)("a",Object(a.a)({parentName:"li"},{href:"https://github.com/adafruit/Adafruit_nRF52_Arduino/issues/600"}),"Gihub Issue: Bluefruit.begin() causes high power consumption")),Object(i.b)("li",{parentName:"ul"},Object(i.b)("a",Object(a.a)({parentName:"li"},{href:"https://github.com/jpconstantineau/BlueMicro_BLE/blob/master/firmware/sleep.cpp"}),"Sleep in Arduino - code example")),Object(i.b)("li",{parentName:"ul"},Object(i.b)("a",Object(a.a)({parentName:"li"},{href:"https://infocenter.nordicsemi.com/pdf/nRF52840_PS_v1.1.pdf"}),"nRF52840 datasheet (pdf)"))),Object(i.b)("h2",{id:"normal-power-consumption"},"Normal Power Consumption"),Object(i.b)("table",null,Object(i.b)("thead",{parentName:"table"},Object(i.b)("tr",{parentName:"thead"},Object(i.b)("th",Object(a.a)({parentName:"tr"},{align:null}),"Case"),Object(i.b)("th",Object(a.a)({parentName:"tr"},{align:null}),"ZMK"),Object(i.b)("th",Object(a.a)({parentName:"tr"},{align:null}),"BlueMicro_BLE"),Object(i.b)("th",Object(a.a)({parentName:"tr"},{align:null}),"Code Below"))),Object(i.b)("tbody",{parentName:"table"},Object(i.b)("tr",{parentName:"tbody"},Object(i.b)("td",Object(a.a)({parentName:"tr"},{align:null}),"Framework"),Object(i.b)("td",Object(a.a)({parentName:"tr"},{align:null}),"Zephyr"),Object(i.b)("td",Object(a.a)({parentName:"tr"},{align:null}),"Adafruit_nRF52_Arduino"),Object(i.b)("td",Object(a.a)({parentName:"tr"},{align:null}),"CircuitPython")),Object(i.b)("tr",{parentName:"tbody"},Object(i.b)("td",Object(a.a)({parentName:"tr"},{align:null}),"connected to BLE"),Object(i.b)("td",Object(a.a)({parentName:"tr"},{align:null}),"700-750 uA"),Object(i.b)("td",Object(a.a)({parentName:"tr"},{align:null}),"950-1000 uA"),Object(i.b)("td",Object(a.a)({parentName:"tr"},{align:null}),"6.8-7.2 mA")),Object(i.b)("tr",{parentName:"tbody"},Object(i.b)("td",Object(a.a)({parentName:"tr"},{align:null}),"Sleeping"),Object(i.b)("td",Object(a.a)({parentName:"tr"},{align:null}),"50 uA"),Object(i.b)("td",Object(a.a)({parentName:"tr"},{align:null}),"60 uA"),Object(i.b)("td",Object(a.a)({parentName:"tr"},{align:null}),"160-200uA")),Object(i.b)("tr",{parentName:"tbody"},Object(i.b)("td",Object(a.a)({parentName:"tr"},{align:null}),"measured using"),Object(i.b)("td",Object(a.a)({parentName:"tr"},{align:null}),"PPK"),Object(i.b)("td",Object(a.a)({parentName:"tr"},{align:null}),"PPK"),Object(i.b)("td",Object(a.a)({parentName:"tr"},{align:null}),"PPK2")))),Object(i.b)("p",null,"I tested the code below to see if time.sleep and alarm.light_sleep differed in power consumption and if one was better than the other.\nUnfortunately, both had the same power consumption with an average of 7mA.\nSuch a high current is similar to the issue filed on the Adafruit nRF52 arduino package when the cryptocell was implemented and power consumption jumped up significantly."),Object(i.b)("p",null,"Note that this was done on August 27th and some changes were done in the CircuitPython ",Object(i.b)("a",Object(a.a)({parentName:"p"},{href:"https://github.com/adafruit/circuitpython/pull/5273"}),"Light Sleep")," code since then."),Object(i.b)("h2",{id:"deep-sleep-vs-sleeping-beauty-system-off"},"Deep Sleep vs Sleeping Beauty (System OFF)"),Object(i.b)("p",null,"The CircuitPython implementation of deep sleep isn't the same as what was implemented for the BlueMicro_BLE firmware.  The arduino implementation is quite simple:"),Object(i.b)("ul",null,Object(i.b)("li",{parentName:"ul"},"setup the anode (+ve) side of the keyboard matrix to be outputs and put them ",Object(i.b)("inlineCode",{parentName:"li"},"HIGH"),". This will apply the necessary voltage to enable a trigger on the cathode side (-ve) when a key is pressed while sleeping "),Object(i.b)("li",{parentName:"ul"},"setup GPIOs on the cathode side of the matrix to be ",Object(i.b)("inlineCode",{parentName:"li"},"INPUT_PULLDOWN_SENSE")," "),Object(i.b)("li",{parentName:"ul"},"call ",Object(i.b)("inlineCode",{parentName:"li"},"sd_power_system_off();")," This is the softdevice call to completely power down the chip.")),Object(i.b)("p",null,"At that point the chip powers down but when a key is pressed, it wakes up as if rebooting from a reset or a power up.  The ",Object(i.b)("inlineCode",{parentName:"p"},"RESETREAS")," register would have the E bit set (see datasheet, page 75) on powerup. The bootloader does not appear to clear-out the ",Object(i.b)("inlineCode",{parentName:"p"},"RESETREAS")," Regiter but does clear the ",Object(i.b)("inlineCode",{parentName:"p"},"GPREGRET")," register if appropriate. ",Object(i.b)("a",Object(a.a)({parentName:"p"},{href:"https://github.com/adafruit/Adafruit_nRF52_Bootloader/blob/master/src/main.c#L182"}),"See code here")),Object(i.b)("p",null,"When referring to the nRF52840 Datasheet, page 149 and 150, we see that this wake-up mechanism is simple (POWER Peripheral uses the DETECT signal to exit from System OFF mode) "),Object(i.b)("pre",null,Object(i.b)("code",Object(a.a)({parentName:"pre"},{className:"language-python"}),'#pylint: disable = line-too-long\nimport time\nimport alarm\nimport board\nimport keypad\nimport pwmio\nimport adafruit_ble\nfrom adafruit_ble.advertising import Advertisement\nfrom adafruit_ble.advertising.standard import ProvideServicesAdvertisement\nfrom adafruit_ble.services.standard.hid import HIDService\nfrom adafruit_ble.services.standard.device_info import DeviceInfoService\nfrom adafruit_hid.keyboard import Keyboard\nfrom adafruit_hid.keyboard_layout_us import KeyboardLayoutUS\nfrom adafruit_hid.keycode import Keycode as KC\n\n# define audio hardware\nbuzzer = pwmio.PWMOut(board.P1_13, variable_frequency=True)\nOFF = 0\nON = 2**15\nnot_sleeping = True\n\n# define key GPIOs\nkeys = keypad.Keys(pins=(board.P0_29,board.P0_02,board.P0_28,board.P0_03,board.P0_10,board.P0_09,board.P0_24,board.P0_13),value_when_pressed=False)\n\n\nhid = HIDService()\n\ndevice_info = DeviceInfoService(software_revision=adafruit_ble.__version__,\n                                manufacturer="Adafruit Industries")\nadvertisement = ProvideServicesAdvertisement(hid)\nadvertisement.appearance = 961\nscan_response = Advertisement()\nscan_response.complete_name = "CircuitPython HID"\n\nble = adafruit_ble.BLERadio()\nif not ble.connected:\n    print("advertising")\n    ble.start_advertising(advertisement, scan_response)\nelse:\n    print("already connected")\n    print(ble.connections)\n\nkeyboard = Keyboard(hid.devices)\nkl = KeyboardLayoutUS(keyboard)\nlayer = 0\nkeymap = ((KC.A,KC.B,KC.C,KC.D,KC.E,KC.F,KC.G,KC.H),\n        (KC.A,KC.B,KC.C,KC.D,KC.E,KC.F,KC.G,KC.H))\n\n# End of Setup Music\nbuzzer.duty_cycle = ON\nbuzzer.frequency = 440\ntime.sleep(0.05)\nbuzzer.frequency = 880\ntime.sleep(0.05)\nbuzzer.frequency = 440\ntime.sleep(0.05)\nbuzzer.duty_cycle = OFF\n\nwhile True:\n    while not ble.connected:\n        pass\n    print("Start typing:")\n    while ble.connected:\n        key_event = keys.events.get()\n        if key_event:\n            key = keymap[layer][key_event.key_number]\n            if key_event.pressed:\n                keyboard.press(key)\n            else:\n                keyboard.release(key)\n        # time.sleep(0.02) # 6-7mA\n        # nothing 6-7mA\n        time_alarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 0.02) # 6-7mA too...\n        # Do a light sleep until the alarm wakes us.\n        alarm.light_sleep_until_alarms(time_alarm)\n        # Finished sleeping. Continue from here.\n    keys.deinit() # must release the pins in order to setup wake up alarm.\n    pin_alarm = alarm.pin.PinAlarm(pin=board.P0_29, value=False, pull=True)\n    alarm.exit_and_deep_sleep_until_alarms(pin_alarm)  # 160-200uA\n    ble.start_advertising(advertisement)\n')))}p.isMDXComponent=!0}}]);