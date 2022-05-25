const { fstat } = require('fs');
const pg = require('pg');
const {Client} = require('pg');
const fs = require('fs');



/* 현재 like만 x30으로 처리해 놓음 */

var db = new Client({
    user : 'jwbae',
    host : 'localhost',
    database : 'rs',
    password : '',
    port : 5433
}); 

tot_l = 0; // 333
tot_d = 0; // 173


db.connect();

//해산물 658 34 27
let fish_l = [
    5,  7, 11, 12, 14, 17, 19, 21, 22,
    23, 26, 27, 29, 30, 32, 36, 39, 40,
    46,  1, 67, 75, 50, 54, 56, 60, 55,
    82, 86, 72, 73, 78, 79, 95
]
// console.log(fish_l.length)

let fish_d = [
    2,   4, 10, 15, 16, 28, 31, 34,
    35,  37, 38, 41, 48, 43, 51, 52,
    53,  57, 58, 59, 63, 64, 91, 69,
    80, 100, 45
]
// console.log(fish_d.length)

// 소고기 321 48 27
let cow_l = [
    4,   5, 12, 14, 15, 16, 20, 21, 22, 23, 28,
    34,  37, 38, 41, 46, 47, 43, 65, 66, 68, 76,
    49,  50, 53, 56, 57, 58, 60, 63, 64, 81, 83,
    85,  86, 88, 90, 69, 70, 72, 73, 74, 79, 92,
    98, 100, 94, 96
]
// console.log(cow_l.length)

let cow_d = [
    2,   4, 10, 15, 16, 28, 31, 34,
    35,  37, 38, 41, 48, 43, 51, 52,
    53,  57, 58, 59, 63, 64, 91, 69,
    80, 100, 45
]
// console.log(cow_d.length)

// 돼지고기 480 16 8
let fork_l = [
    42, 48, 64, 68, 69, 70,
    71, 72, 73, 81, 84, 85,
    86, 93, 94, 97
]
// console.log(fork_l.length)

let fork_d = [
    62, 66, 75, 79,
    88, 92, 96, 98
]
// console.log(fork_d.length)

// 닭고기 274 40 18
let chicken_l = [
    2,  4,  5, 12, 13, 14, 15, 17, 21, 22,
    23, 28, 34, 37, 38, 41, 42, 43, 46, 47,
    48, 55, 56, 57, 58, 60, 66, 68, 69, 72,
    73, 78, 81, 84, 85, 86, 90, 93, 94, 97
]
// console.log(chicken_l.length)

let chicken_d = [
    3, 16, 19, 20, 26, 29, 32,
    33, 39, 40, 44, 49, 59, 62,
    64, 74, 75, 79
]
// console.log(chicken_d.length)

// 육류 92 29 15
let meat_l = [
    2,  4,  6, 10, 12, 14, 15, 16, 18,
    21, 22, 23, 25, 28, 34, 37, 38, 41,
    43, 47, 49, 56, 57, 68, 72, 73, 78,
    81, 86
]
// console.log(meat_l.length)

let meat_d = [
    19, 24, 26, 29, 32, 33,
    39, 40, 44, 59, 62, 75,
    77, 88, 91
]
// console.log(meat_d.length)

// 쌀 242 30 6
let rice_l = [
    1,  3,   4,  8,  9, 12, 13, 16, 17,
    18, 23,  30, 31, 33, 35, 37, 39, 41,
    50, 59,  62, 65, 66, 67, 74, 80, 83,
    92, 98, 100
]
// console.log(rice_l.length)

let rice_d = [
    25, 70, 71, 72, 78, 99
]
// console.log(rice_d.length)

// 곡류 58 17 11
let gok_l = [
    4,  8, 12, 21, 22, 23, 31,
    33, 35, 53, 62, 73, 75, 84,
    87, 88, 92
]
// console.log(gok_l.length)

let gok_d = [
    5,  6, 27, 30, 36,
    61, 70, 72, 76, 78,
    81
]
// console.log(gok_d.length)

//과일류 93 11 14
let fruit_l = [
    5,  6, 27, 30, 36,
    61, 70, 72, 76, 78,
    81
]
// console.log(fruit_l.length)

let fruit_d = [
    1,  8, 16, 18, 42, 61,
    63, 65, 66, 68, 72, 81,
    95, 98
]
// console.log(fruit_d.length)



// 채소류 1753 31 13
let veg_l = [
    3,  8,  9, 11, 12, 16, 21, 22, 23,
    31, 33, 35, 39, 45, 52, 57, 58, 59,
    62, 63, 69, 70, 73, 75, 77, 80, 82,
    84, 87, 88, 97
]
// console.log(veg_l.length)

let veg_d = [
    2, 18, 27, 30, 36, 47,
    56, 67, 68, 72, 74, 93,
    98
]
// console.log(veg_d.length)

//달걀/유제품 297 26 10
let egg_l = [
    3,   9, 13, 16, 17, 19, 20, 23,
    24,  25, 44, 45, 46, 51, 53, 54,
    57,  63, 68, 69, 73, 75, 87, 88,
    95, 100
]
// console.log(egg_l.length)

let egg_d = [
    4, 12, 21, 55, 59,
    60, 64, 80, 93, 99
]
// console.log(egg_d.length)

//밀가루 315 40 12
let wheat_l = [
    1,  2,  6, 10, 11, 12, 14, 16, 18,  19,
    20, 23, 24, 32, 38, 43, 44, 47, 48,  51,
    52, 53, 54, 55, 56, 57, 59, 61, 62,  65,
    67, 74, 80, 83, 84, 89, 90, 97, 98, 100
]
// console.log(wheat_l.length)

let wheat_d = [
    3,  4,  5,  9, 13,
    17, 50, 63, 69, 70,
    78, 99
]
// console.log(wheat_d.length)

//가공식품류 547 11 3
let gagong_l = [
    6, 30, 32, 38, 48,
    61, 71, 88, 89, 90,
    92
]
// console.log(gagong_l.length)

let gagong_d = [ 65, 67, 84 ]
// console.log(gagong_d.length);

var res;
var list = [];

db.query(`select rcp_sno from recipe order by random() limit 1000;`, (err, res2) => {
    if (err) { throw err; }
    // console.log(res2.rows)
    res = res2.rows
    for (let i = 0 ; i < res.length ; i++){
        list.push(res[i].rcp_sno);
    }
    // console.log(list);
    fs.writeFileSync('./test.txt', list.toString());
    db.end();
});