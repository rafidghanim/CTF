"use strict";
var _0x5189c8 = _0x4e6b;
(function (_0x3238b4, _0xbe8f80) {
  var _0x3115fd = _0x4e6b,
    _0x49a905 = _0x3238b4();
  while (!![]) {
    try {
      var _0x593798 =
        (parseInt(_0x3115fd(0xc9)) / 0x1) * (-parseInt(_0x3115fd(0xc8)) / 0x2) +
        (-parseInt(_0x3115fd(0xc0)) / 0x3) * (-parseInt(_0x3115fd(0xc2)) / 0x4) +
        -parseInt(_0x3115fd(0xd0)) / 0x5 +
        (-parseInt(_0x3115fd(0xb7)) / 0x6) * (parseInt(_0x3115fd(0xac)) / 0x7) +
        -parseInt(_0x3115fd(0xd1)) / 0x8 +
        (-parseInt(_0x3115fd(0xc5)) / 0x9) * (parseInt(_0x3115fd(0xbc)) / 0xa) +
        parseInt(_0x3115fd(0xce)) / 0xb;
      if (_0x593798 === _0xbe8f80) break;
      else _0x49a905["push"](_0x49a905["shift"]());
    } catch (_0x18b830) {
      _0x49a905["push"](_0x49a905["shift"]());
    }
  }
})(_0x2506, 0xdb2ea);
var gameStart = {},
  gameSpeed = {},
  gameArea = {},
  gameAreaContext = {},
  snake = [],
  gameAreaWidth = 0x0,
  gameAreaHeight = 0x0,
  cellWidth = 0x0,
  playerScore = 0x0,
  integrityCheck = 0x0,
  snakeFood = {},
  snakeDirection = "",
  speedSize = 0x0,
  timer = {};
function initElement() {
  var _0x47f99e = _0x4e6b;
  (gameStart = document[_0x47f99e(0xc7)]("#gameStart")),
    (gameSpeed = document[_0x47f99e(0xc7)](_0x47f99e(0xbf))),
    (gameArea = document[_0x47f99e(0xc7)](_0x47f99e(0xbd))),
    (gameAreaContext = gameArea[_0x47f99e(0xaf)]("2d")),
    (gameAreaWidth = 0x190),
    (gameAreaHeight = 0x258),
    (cellWidth = 0x14),
    (gameArea[_0x47f99e(0xb8)] = gameAreaWidth),
    (gameArea[_0x47f99e(0xb1)] = gameAreaHeight);
}
function createFood() {
  var _0x21112e = _0x4e6b;
  snakeFood = { x: Math[_0x21112e(0xca)]((Math[_0x21112e(0xcd)]() * (gameAreaWidth - cellWidth)) / cellWidth), y: Math[_0x21112e(0xca)]((Math[_0x21112e(0xcd)]() * (gameAreaHeight - cellWidth)) / cellWidth) };
}
function control(_0x4fd151, _0x34f85c, _0x2dd344) {
  var _0x375260 = _0x4e6b;
  for (var _0xd3b162 = 0x0, _0x3fec8e = _0x2dd344[_0x375260(0xb9)]; _0xd3b162 < _0x3fec8e; _0xd3b162++) {
    if (_0x2dd344[_0xd3b162]["x"] == _0x4fd151 && _0x2dd344[_0xd3b162]["y"] == _0x34f85c) return !![];
  }
  return ![];
}
function writeScore() {
  var _0x1207dc = _0x4e6b;
  (gameAreaContext[_0x1207dc(0xad)] = "50px\x20sans-serif"),
    (gameAreaContext[_0x1207dc(0xc1)] = _0x1207dc(0xba)),
    gameAreaContext["fillText"](_0x1207dc(0xc6) + playerScore, gameAreaWidth / 0x2 - 0x64, gameAreaHeight / 0x2),
    playerScore == 0xf423f && win(gameAreaContext[_0x1207dc(0xad)], integrityCheck);
}
function win(_0x48c8c1, _0x3943ad) {
  var _0x27da25 = _0x4e6b;
  const _0x51e815 = [0x8c, 0x84, 0xb4, 0x94, 0xc8, 0xaa, 0xb3, 0x8b, 0xa3, 0xff, 0xa3, 0xb1, 0xab, 0xbf, 0xb4, 0xd0, 0xe6, 0x93, 0xea, 0xce];
  var _0x340862 = "";
  for (var _0x34cf9b = 0x0; _0x34cf9b < _0x51e815["length"]; _0x34cf9b++) {
    (_0x51e815[_0x34cf9b] ^= _0x48c8c1[_0x27da25(0xb5)](_0x34cf9b % _0x48c8c1[_0x27da25(0xb9)])), (_0x51e815[_0x34cf9b] += _0x3943ad), (_0x51e815[_0x34cf9b] &= 0xff), (_0x340862 += String["fromCharCode"](_0x51e815[_0x34cf9b]));
  }
  (gameAreaContext[_0x27da25(0xad)] = _0x27da25(0xb3)), (gameAreaContext["fillStyle"] = _0x27da25(0xae)), gameAreaContext["fillText"](_0x340862, gameAreaWidth / 0x2 - 0x64, gameAreaHeight / 0x2 + 0x3c);
}
function _0x2506() {
  var _0x3e2a5d = [
    "push",
    "height",
    "addEventListener",
    "10px\x20sans-serif",
    "#000000",
    "charCodeAt",
    "fillRect",
    "3001812emgroP",
    "width",
    "length",
    "#FF0000",
    "pop",
    "10aieOSn",
    "#gameArea",
    "down",
    "#gameSpeed",
    "6iLMmlR",
    "fillStyle",
    "1995692ItMdtK",
    "left",
    "#FFFFFF",
    "5778441OhlzLH",
    "Score:\x20",
    "querySelector",
    "2KGvmsr",
    "1523300JpaBjU",
    "round",
    "unshift",
    "click",
    "random",
    "61821254upnBKa",
    "value",
    "3911275pJJjVu",
    "14175856QncyBN",
    "right",
    "keydown",
    "disabled",
    "14bEDtvL",
    "font",
    "#ff0000",
    "getContext",
  ];
  _0x2506 = function () {
    return _0x3e2a5d;
  };
  return _0x2506();
}
function createSquare(_0x59d6f0, _0x16b59d) {
  var _0x2dc406 = _0x4e6b;
  (gameAreaContext[_0x2dc406(0xc1)] = _0x2dc406(0xb4)), gameAreaContext[_0x2dc406(0xb6)](_0x59d6f0 * cellWidth, _0x16b59d * cellWidth, cellWidth, cellWidth);
}
function createGameArea() {
  var _0x197c51 = _0x4e6b,
    _0x32f945 = snake[0x0]["x"],
    _0x502a53 = snake[0x0]["y"];
  (gameAreaContext[_0x197c51(0xc1)] = _0x197c51(0xc4)),
    gameAreaContext["fillRect"](0x0, 0x0, gameAreaWidth, gameAreaHeight),
    (gameAreaContext["strokeStyle"] = "#000000"),
    gameAreaContext["strokeRect"](0x0, 0x0, gameAreaWidth, gameAreaHeight);
  if (snakeDirection == _0x197c51(0xd2)) _0x32f945++;
  else {
    if (snakeDirection == "left") _0x32f945--;
    else {
      if (snakeDirection == _0x197c51(0xbe)) _0x502a53++;
      else snakeDirection == "up" && _0x502a53--;
    }
  }
  if (_0x32f945 == -0x1 || _0x32f945 == gameAreaWidth / cellWidth || _0x502a53 == -0x1 || _0x502a53 == gameAreaHeight / cellWidth || control(_0x32f945, _0x502a53, snake)) {
    writeScore(), clearInterval(timer), (gameStart[_0x197c51(0xd4)] = ![]);
    return;
  }
  if (_0x32f945 == snakeFood["x"] && _0x502a53 == snakeFood["y"]) {
    var _0x37fa19 = { x: _0x32f945, y: _0x502a53 };
    (playerScore += speedSize), (integrityCheck += 0x539), createFood();
  } else {
    var _0x37fa19 = snake[_0x197c51(0xbb)]();
    (_0x37fa19["x"] = _0x32f945), (_0x37fa19["y"] = _0x502a53);
  }
  snake[_0x197c51(0xcb)](_0x37fa19);
  for (var _0x30ef51 = 0x0, _0xc7cca9 = snake[_0x197c51(0xb9)]; _0x30ef51 < _0xc7cca9; _0x30ef51++) {
    createSquare(snake[_0x30ef51]["x"], snake[_0x30ef51]["y"]);
  }
  createSquare(snakeFood["x"], snakeFood["y"]);
}
function startGame() {
  var _0x4250b8 = _0x4e6b;
  (snake = []), snake[_0x4250b8(0xb0)]({ x: 0x0, y: cellWidth }), createFood(), clearInterval(timer), (timer = setInterval(createGameArea, 0x1f4 / speedSize));
}
function onStartGame() {
  var _0x31e7ae = _0x4e6b;
  (this["disabled"] = !![]), (playerScore = 0x0), (snakeDirection = _0x31e7ae(0xd2)), (speedSize = parseInt(gameSpeed[_0x31e7ae(0xcf)]));
  if (speedSize > 0x9) speedSize = 0x9;
  else speedSize < 0x0 && (speedSize = 0x1);
  startGame();
}
function _0x4e6b(_0x21aa27, _0x3a082d) {
  var _0x25068c = _0x2506();
  return (
    (_0x4e6b = function (_0x4e6b70, _0x2c51cd) {
      _0x4e6b70 = _0x4e6b70 - 0xac;
      var _0x5b389d = _0x25068c[_0x4e6b70];
      return _0x5b389d;
    }),
    _0x4e6b(_0x21aa27, _0x3a082d)
  );
}
function changeDirection(_0x14a1b1) {
  var _0x4f6af5 = _0x4e6b,
    _0x585845 = _0x14a1b1["which"];
  if (_0x585845 == "40" && snakeDirection != "up") snakeDirection = _0x4f6af5(0xbe);
  else {
    if (_0x585845 == "39" && snakeDirection != _0x4f6af5(0xc3)) snakeDirection = _0x4f6af5(0xd2);
    else {
      if (_0x585845 == "38" && snakeDirection != _0x4f6af5(0xbe)) snakeDirection = "up";
      else {
        if (_0x585845 == "37" && snakeDirection != _0x4f6af5(0xd2)) snakeDirection = _0x4f6af5(0xc3);
      }
    }
  }
}
function initEvent() {
  var _0x258ffa = _0x4e6b;
  gameStart[_0x258ffa(0xb2)](_0x258ffa(0xcc), onStartGame), window[_0x258ffa(0xb2)](_0x258ffa(0xd3), changeDirection);
}
function init() {
  initElement(), initEvent();
}
window[_0x5189c8(0xb2)]("DOMContentLoaded", init);
